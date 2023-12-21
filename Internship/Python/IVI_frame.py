# byte_position = 0
# bit_position = 7
# size = 3
# hex_list = ["40", "12", "6C", "AF", "05", "78", "4A", "04"]
# #hex_list = ['60', '20', '45', '6C', 'FE', '3D', '4B', 'AA']
# byte = hex_list[byte_position]
# hex_to_binary = bin(int(byte, 16))[2:].zfill(8)
# binary_list = [x for x in hex_to_binary[::-1]]
# binary_str= ''.join(binary_list[bit_position:bit_position-size:-1])
# decimal_number = int(binary_str, 2)
# print(decimal_number)

def decimal_result(hex_list: list, byte_position: int, bit_position: int, size: int):

    byte = hex_list[byte_position]
    hex_to_binary = bin(int(byte, 16))[2:].zfill(8)
    binary_list = [x for x in hex_to_binary[::-1]]
    binary_str= ''.join(binary_list[bit_position:bit_position-size:-1])
    decimal_number = int(binary_str, 2)
    return decimal_number

class PassengerSeatMemoRequest:
    def __init__(self):
        self.byte_position = 0
        self.bit_position = 7
        self.size = 3

class ClimFPrightBlowingRequest:
    def __init__(self):
        self.byte_position = 5
        self.bit_position = 7
        self.size = 4

class TimeFormatDisplay:
    def __init__(self):
        self.byte_position = 5
        self.bit_position = 3
        self.size = 1

payload = [['60', '20', '45', '6C', 'FE', '3D', '4B', 'AA'], ["40", "12", "6C", "AF", "05", "78", "4A", "04"]]
passenger = PassengerSeatMemoRequest()
clim = ClimFPrightBlowingRequest()
time = TimeFormatDisplay()


print(f"\nResults for payload : {payload[0]}\n")
print(f"Decimal result for PassengerSeatMemoRequest: {decimal_result(payload[0], passenger.byte_position, passenger.bit_position, passenger.size)}")
print(f"Decimal result for ClimFPrightBlowRequest: {decimal_result(payload[0], clim.byte_position, clim.bit_position, clim.size)}")
print(f"Decimal result for TimeFormatDisplay: {decimal_result(payload[0], time.byte_position, time.bit_position, time.size)}")

print(f"\nResults for payload : {payload[1]}\n")
print(f"Decimal result for PassengerSeatMemoRequest: {decimal_result(payload[1], passenger.byte_position, passenger.bit_position, passenger.size)}")
print(f"Decimal result for ClimFPrightBlowRequest: {decimal_result(payload[1], clim.byte_position, clim.bit_position, clim.size)}")
print(f"Decimal result for TimeFormatDisplay: {decimal_result(payload[1], time.byte_position, time.bit_position, time.size)}")


# hex_list_1 = ['60', '20', '45', '6C', 'FE', '3D', '4B', 'AA']
# hex_list_2 = ["40", "12", "6C", "AF", "05", "78", "4A", "04"]
# byte_position = 0
# bit_position = 7
# size = 3

# print(decimal_result(hex_list_1, byte_position, bit_position, size))
# print(decimal_result(hex_list_2, byte_position, bit_position, size))