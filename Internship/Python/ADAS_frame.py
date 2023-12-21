p1 = "00 06 02 08 80 00 00 00 00 00 00 00 00 05 D0 08 FF 60 00 00 02 00 00 00 00 06 01 08 80 00 00 00 00 00 00 00 00 00 10 C7 77 8A 70 AB AF 88 2A 8C"
payload_list1 = p1.split()


def ldw_alert_status(payload_list):

    signal_extract = payload_list[4:12]
    byte_position = 2
    bit_position = 5
    size = 2
    replacement = 2 
    replacement_binary = bin(int(replacement))[2:] #2 decimal to 10 binar (00000010)
    if str(size) != str(len(replacement_binary)):
        raise ValueError(f"Make sure replacement length (in binary) is equal with size.\n {str(size)} != {len(str(replacement_binary))}")
    hex_byte = signal_extract[byte_position] 
    hex_to_binary = bin(int(hex_byte, 16))[2:].zfill(8)
    reversed_binary_list = [x for x in hex_to_binary[::-1]]
    reversed_binary_list[bit_position:bit_position-size:-1] = replacement_binary
    new_byte_str = ''.join(reversed_binary_list[::-1])
    hexadecimal_result = (hex(int(new_byte_str, 2)))[2:]
    payload_list[6] = hexadecimal_result.upper()

    return payload_list


def follow_up_time_display(payload_list):

    signal_extract = payload_list[16:24]
    byte_position = 4
    bit_position = 7
    size = 6
    replacement = 45 
    replacement_binary = bin(int(replacement))[2:] 
    if str(size) != str(len(replacement_binary)):
        raise ValueError(f"Make sure replacement length (in binary) is equal with size.\n {str(size)} != {len(str(replacement_binary))}")
    hex_byte = signal_extract[byte_position] 
    hex_to_binary = bin(int(hex_byte, 16))[2:].zfill(8)
    reversed_binary_list = [x for x in hex_to_binary[::-1]]
    reversed_binary_list[bit_position:bit_position-size:-1] = replacement_binary
    new_byte_str = ''.join(reversed_binary_list[::-1])
    hexadecimal_result = (hex(int(new_byte_str, 2)))[2:]
    payload_list[20] = hexadecimal_result.upper()

    return payload_list


def lca_override_display(payload_list):

    signal_extract = payload_list[28:36]
    byte_position = 5
    bit_position = 2
    size = 1
    replacement = 1
    replacement_binary = bin(int(replacement))[2:] 
    if str(size) != str(len(replacement_binary)):
        raise ValueError(f"Make sure replacement length (in binary) is equal with size.\n {str(size)} != {len(str(replacement_binary))}")
    hex_byte = signal_extract[byte_position]
    hex_to_binary = bin(int(hex_byte, 16))[2:].zfill(8)
    reversed_binary_list = [x for x in hex_to_binary[::-1]]
    reversed_binary_list[bit_position:bit_position-size:-1] = replacement_binary
    new_byte_str = ''.join(reversed_binary_list[::-1])
    hexadecimal_result = (hex(int(new_byte_str, 2)))[2:]                                        
    payload_list[33] = hexadecimal_result.upper().zfill(2)   #mai trebuie verificat atunci cand am un singur digit cum ii pun 0 inainte ca sa fie formatul din payload cu dubludigit

    return payload_list


def modified_frame_result(payload_list):

    result = ldw_alert_status(payload_list)
    result = follow_up_time_display(payload_list)
    result = lca_override_display(payload_list)
    result_string = ' '.join(result)

    return result_string

try:
    print(f"\nOriginal frame:\n{p1}\nReplaced frame:\n{modified_frame_result(payload_list1)}\n")
except ValueError as e:
    print(f"Error: {e}")













