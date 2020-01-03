

def divide_addrss(ip_address):

    new_address = ip_address.replace('/', '.')
    segments = new_address.split('.')
    mask = segments[-1]
    binary_list = []

    for index in range(len(segments) - 1):
        binary_list.append(int(segments[index]))

    # print(binary_list)
    # print(mask)

    return binary_list, int(mask)


def convert_address(network, dec_mask):

    bin_network = []

    for item in network:
        bin_value = "{0:08b}".format(item)
        bin_network.append(bin_value)

    bin_mask = []
    one_segment = int(dec_mask / 8)

    for index in range(4):
        if one_segment > 0:
            bin_mask.append('1'*8)
            one_segment -= 1
            dec_mask -= 8
        else:
            value = ''
            for index_2 in range(8):
                if dec_mask > 0:
                    value += '1'
                    dec_mask -= 1
                else:
                    value += '0'
            bin_mask.append(value)

    return bin_network, bin_mask


def add_address(bin_net, mask_net):

    # print(bin_net)
    # print(mask_net)
    binary_network_address = []
    integer_network_address = ''
    point_index = 0

    for index in range(len(bin_net)):
        new_value = ''
        for value_index in range(len(bin_net[index])):
            if bin_net[index][value_index] == mask_net[index][value_index]:
                new_value +=  bin_net[index][value_index]
            else:
                new_value += '0'
        binary_network_address.append(new_value)

        if point_index < 3:
            integer_network_address += str(int(new_value,2)) + '.'
            point_index += 1
        else:
            integer_network_address += str(int(new_value,2))


    binary_broadcast_address = []
    integer_broadcast_address = ''

    for index in range(len(binary_network_address)):
        if index < 3:
            binary_broadcast_address.append(binary_network_address[index])
        else:
            binary_broadcast_address.append('1'*8)

    for index in range(len(binary_broadcast_address)):

        if index < 3:
            integer_broadcast_address += str(int(binary_broadcast_address[index], 2)) + '.'
        else:
            integer_broadcast_address += str(int(binary_broadcast_address[index], 2))

        # print(binary_broadcast_address)


    return integer_network_address, integer_broadcast_address


ip_add = '192.168.0.15/24'
network, mask = divide_addrss(ip_add)
bin_network, bin_mask = convert_address(network, mask)
int_network_address, integer_broadcast_address = add_address(bin_network, bin_mask)
print(int_network_address)
print(integer_broadcast_address)