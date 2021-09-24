name = ('centimeters to inches converter')
centimeters = int(input('Enter Centimeters'))

if centimeters >= 0:
    inches = (centimeters*0.393701)
    feet = (inches/12)

print(name)
print(' ')
print("centimeters:")
print(centimeters)
print(' ')
print ("inches:")
print (inches)

d=12


if inches < (d):
    print('process complete!')
else:
   print(' ')
   print("feet:")
   print(feet)
   print(' ')
   print('since the inches exceeded 12, I have automatically inputted feet for your conveninece!')
   print('process complete!')
