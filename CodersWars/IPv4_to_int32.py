# Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each octet is a single byte (or 8 bits).
#
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
#
# Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.
#
# Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.
#
#   ip_to_int32("128.32.10.1") => 2149583361


def to_binary(number):
    result = ''
    while number > 0:
        if number % 2 == 0:
            result += '0'
        else:
            result += '1'
        number = number // 2
    if len(result) != 8:
        add = len(range(8)) - len(result)
        result += '0' * add
    return result[::-1]


def ip_to_int32(ip):
    array = ip.split('.')
    numbers = []
    for index in array:
        i = int(index)
        numbers.append(to_binary(i))
    return '.'.join(numbers)

ip = "128.32.10.1"
print(ip_to_int32(ip))



import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]
print(ip2long(ip))