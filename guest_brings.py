"""Counts the total amount of items guests bring."""
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    """brought quantities"""
    num_brought = 0
    for _key, value in guests.items():
        num_brought = num_brought + value.get(item, 0)
    return num_brought

print('The guests have brought the following quantities')
print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
print(' - Apples ' + str(total_brought(allGuests, 'apples')))
print(' - apple pies ' + str(total_brought(allGuests, 'apple pies')))
print(' - Cups ' + str(total_brought(allGuests, 'cups')))
print(' - Pretzels ' + str(total_brought(allGuests, 'pretzels')))
