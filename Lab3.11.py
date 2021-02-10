import math

print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())

Area = wall_height * wall_width
print('Wall area:',Area,'square feet')

Paint = float(Area / 350)
print('Paint needed:','{:.2}'.format(Paint),'gallons')
can = round(Paint)
print('Cans needed:',math.ceil(can),'can(s)')

Color_choice = {
    'red':35,
    'blue':25,
    'green':23
}
print('\nChoose a color to paint the wall:')
color = input()
print('Cost of purchasing',color,'paint: $'+str(can*Color_choice[color]))
