"""Dictionary of all birthdays."""

birthdays = {'Jack': '29.08.2002', 'Rogers': '12.12.2007'}

while True:
    name = input("Enter a name (blank to quit!): ")
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the bday of ' + name)
    else:
        print("No records available in database for " + name + " ")
        birthday = input("Enter the birthdate from " + name + " ")
        birthdays[name] = birthday
        print("Database updated succesfully")
        print(birthdays)
