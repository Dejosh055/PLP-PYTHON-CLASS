print('Choose operation')
print('1. ADDITION')
print('2. MULTIPLICATION')
print('3. SUBTRACTION')
print('4. DIVISION')

operation = input()
num1 = input('Enter first number:')
num2 = input('Enter Second number:')
if operation == '1':
    print('the sum is'+ " " + str(int( num1) + int(num2)) )

elif operation == '2':
    print('the product is'+ " " + str(int( num1) * int(num2)) )

elif operation == '3':
    print('the Difference is'+ " " + str(int( num1) - int(num2)) )
elif operation == '4':
    print('the Result is'+ " " + str(int( num1) / int(num2)) )

else:
    print('enter a valid number')
       