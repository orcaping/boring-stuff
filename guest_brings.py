"""Counts the total amount of items guests bring."""
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    """brought quantities"""
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

def brough_items(guests, item):
    """brought items"""
    numBrought = 0
    for k, v in guests.items():
        print(v.get(item, 0))
    return numBrought

print('The guests have brought the following quantities')
print(' - Ham Sandwiches ' + str(total_brought(allGuests, 'ham sandwiches')))
print(' - Apples ' + str(total_brought(allGuests, 'apples')))
print(' - apple pies ' + str(total_brought(allGuests, 'apple pies')))
print(' - Cups ' + str(total_brought(allGuests, 'cups')))
print(' - Pretzels ' + str(total_brought(allGuests, 'pretzels')))
