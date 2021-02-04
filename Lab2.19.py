print('Enter amount of lemon juice (in cups):')
lj = int(input())
print('Enter amount of water (in cups):')
w = int(input())
print('Enter amount of agave nectar (in cups):')
an = float(input())
print('How many servings does this make?')
s = int(input())

print('\nLemonade ingredients - yields','{:.2f}'.format(s),'servings')
print('{:.2f}'.format(lj),'cup(s) lemon juice')
print('{:.2f}'.format(w),'cup(s) water')
print('{:.2f}'.format(an),'cup(s) agave nectar')

print('\nHow many servings would you like to make?')
ser = int(input())

print('\nLemonade ingredients - yields','{:.2f}'.format(ser),'servings')
print('{:.2f}'.format(lj*8),'cup(s) lemon juice')
print('{:.2f}'.format(w*8),'cup(s) water')
print('{:.2f}'.format(an*8),'cup(s) agave nectar')

print('\nLemonade ingredients - yields','{:.2f}'.format(ser),'servings')
print('{:.2f}'.format(lj*8/16),'gallon(s) lemon juice')
print('{:.2f}'.format(w*8/16),'gallon(s) water')
print('{:.2f}'.format(an*8/16),'gallon(s) agave nectar')

