import socketserver
import threading

class ModbusRegisterManager:
    def __init__(self):
        self.registers = {}
        self.debug = False

    def get(self, addr):
        val = self.registers.get(addr, 0)
        if self.debug:
            print(f"[MODBUS] READ addr=0x{addr:04X} -> {val}")
        return val

    def set(self, addr, value):
        self.registers[addr] = value
        if self.debug:
            print(f"[MODBUS] WRITE addr=0x{addr:04X} <- {value}")

    def set_debug(self, enabled: bool):
        self.debug = enabled
        print(f"[MODBUS] Debug logging {'enabled' if enabled else 'disabled'}")

class ModbusTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        if not data:
            return
        manager = self.server.register_manager
        function_code = data[7]
        if function_code == 0x03:
            start = int.from_bytes(data[8:10], 'big')
            count = int.from_bytes(data[10:12], 'big')
            values = []
            for i in range(count):
                val = manager.get(start + i)
                values += [(val >> 8) & 0xFF, val & 0xFF]
            response = bytearray(data[0:4]) + bytes([0, 3 + 2 * count]) + bytes([0x03, 2 * count]) + bytes(values)
            self.request.sendall(response)
        elif function_code == 0x06:
            addr = int.from_bytes(data[8:10], 'big')
            val = int.from_bytes(data[10:12], 'big')
            manager.set(addr, val)
            self.request.sendall(data[:12])
        else:
            self.request.sendall(data[:7] + bytes([function_code + 0x80, 0x01]))

class ModbusTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, handler_class, register_manager):
        super().__init__(server_address, handler_class)
        self.register_manager = register_manager

def start_modbus_server(register_manager):
    server = ModbusTCPServer(('0.0.0.0', 502), ModbusTCPHandler, register_manager)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()