print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

print('\nSelect first service:')
ser1 = input()
print('Select second service:')
ser2 = input()

#print invoice

print('\nDavy\'s auto shop invoice')
total = 0
if ser1 == 'Oil change':
    print('\nService 1: Oil change, $35')
    total += 35
elif ser1 == 'Tire rotation':
    print('\nService 1: Tire rotation, $19')
    total +=19
elif ser1 == 'Car wash':
    print('\nService 1: Car wash, $7')
    total +=7
elif ser1 == 'Car wax':
    print('\nService 1: Car wax, $12')
    total += 12
elif ser1 == '-':
    print('\nService 1: No service')
else:
    print('Invalid')

if ser2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total += 35
elif ser2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total +=19
elif ser2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total +=7
elif ser2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total += 12
elif ser2 == '-':
    print('Service 2: No service')
else:
    print('Invalid')
print('\nTotal: $'+str(total))