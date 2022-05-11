import re

def palindrome_checker(str_eval):
    removals = '[\W|_]'
    store = re.sub(removals, '', str_eval)
    store2 = store[::-1]
    print(store2)
    print(store)
    if store2 == store:
        print('The string entered is a palindrome!')
        return True
    else:
        print('The string entered is not a palindrome')
        return False

while True:
    value1 = input('Welcome! Do you want to check for a possible Palindrome? Y/N: ')
    value1= value1.lower()
    if value1 == 'n':
        print('Thanks for using this program! See you next time')
        break
    elif value1 == 'y':
        value2 = input('Please, enter the characters to check: ')
        palindrome_checker(value2)
    else:
        print('Please answer Y for "Yes", or N for "No"')
        continue
   
