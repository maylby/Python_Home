# Дополнения к основным материлам занятий

''' Оператор break '''

number = 0
for number in range(10):
    number = number + 1
if number == 5: 
    print('Error')
    # break # VSCode не позволяет воспользоваться оператором "break"
print('Number is ' + str(number))
print('Out of loop')


''' Оператор continue '''

number = 0
for number in range(10):
    number = number + 1
if number == 5:
    print('Error')
    # continue # VSCode не позволяет воспользоваться оператором "continue"
print('Number is ' + str(number))
print('Out of loop')
