"""clean human readable list output"""
def print_picnic(items_dict, left_width, right_width):
    """takes input and rearanges into well readable table"""
    print('PICNIP ITEMS'.center(left_width + right_width, '_'))
    for k, value in items_dict.items():
        print(k.ljust(left_width, '.') + str(value).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
