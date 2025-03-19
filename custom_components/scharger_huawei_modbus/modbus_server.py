import socketserver
import threading
import logging

_LOGGER = logging.getLogger(__name__)

class ModbusRegisterManager:
    def __init__(self):
        self.registers = {}
        self.debug = False

    def get(self, address):
        return self.registers.get(address, 0)

    def set(self, address, value):
        self.registers[address] = value
        if self.debug:
            _LOGGER.debug("[MODBUS] Set register 0x%04X = %d", address, value)

    def set_debug(self, enabled):
        self.debug = enabled

class ModbusTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_ip, client_port = self.client_address
        _LOGGER.info("[MODBUS] New connection from %s:%s", client_ip, client_port)
        try:
            data = self.request.recv(1024)
            if len(data) < 8:
                return

            transaction_id = data[0:2]
            protocol_id = data[2:4]
            length = data[4:6]
            unit_id = data[6:7]
            function_code = data[7]

            if function_code == 3:  # Read Holding Registers
                start_addr = int.from_bytes(data[8:10], "big")
                count = int.from_bytes(data[10:12], "big")
                values = []
                for i in range(count):
                    val = self.server.register_manager.get(start_addr + i)
                    values.append(val)

                byte_count = count * 2
                response = (
                    transaction_id +
                    protocol_id +
                    bytes([0, byte_count + 3]) +
                    unit_id +
                    bytes([function_code, byte_count]) +
                    b''.join(val.to_bytes(2, "big") for val in values)
                )
                self.request.sendall(response)
                _LOGGER.debug("[MODBUS] Read Holding Registers: addr=0x%04X count=%d", start_addr, count)

            elif function_code == 6:  # Write Single Register
                addr = int.from_bytes(data[8:10], "big")
                value = int.from_bytes(data[10:12], "big")
                self.server.register_manager.set(addr, value)
                self.request.sendall(data[:12])  # Echo back
                _LOGGER.debug("[MODBUS] Write Single Register: addr=0x%04X = %d", addr, value)

        except Exception as e:
            _LOGGER.error("ModbusTCPHandler error: %s", e)

class ModbusTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

    def __init__(self, server_address, handler_class, register_manager):
        super().__init__(server_address, handler_class)
        self.register_manager = register_manager

def start_modbus_server(register_manager, port=502):
    server = ModbusTCPServer(('0.0.0.0', port), ModbusTCPHandler, register_manager)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    _LOGGER.info("[MODBUS] Server started on port %s", port)
    return server
