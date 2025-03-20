import socketserver
import threading
import logging

_LOGGER = logging.getLogger(__name__)

PRESET_REGISTER_VALUES = {
    0x3000: 1,
    0x3001: 0,
    0x3002: 32,
    0x3003: 7400,
    0x3004: 1,
    0x3005: 1,
    0x3006: 1,
    0x3010: 0
}

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
        _LOGGER.info("[MODBUS] New connection from %s:%s", *self.client_address)
        try:
            data = self.request.recv(1024)
            if len(data) < 8:
                return
            transaction_id, protocol_id, length, unit_id = data[:2], data[2:4], data[4:6], data[6:7]
            function_code = data[7]

            if function_code == 3:
                start = int.from_bytes(data[8:10], "big")
                count = int.from_bytes(data[10:12], "big")
                values = [self.server.register_manager.get(start + i) for i in range(count)]
                response = (transaction_id + protocol_id +
                            bytes([0, len(values)*2 + 3]) +
                            unit_id +
                            bytes([function_code, len(values)*2]) +
                            b''.join(val.to_bytes(2, "big") for val in values))
                self.request.sendall(response)
            elif function_code == 6:
                addr = int.from_bytes(data[8:10], "big")
                val = int.from_bytes(data[10:12], "big")
                self.server.register_manager.set(addr, val)
                self.request.sendall(data[:12])
        except Exception as e:
            _LOGGER.error("[MODBUS] Handler error: %s", e)

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
