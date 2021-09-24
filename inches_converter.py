name = ('inches converter')
inches = int(input('Enter Inches'))

if inches >= 0:
    centimeters = (inches*2.54)
    feet = (inches/12)

print(name)
print(' ')

print('centimeters')
print(centimeters)
print(' ')
print('feet')
print(feet)

print('process complete!')
