def is_palindrome(my_string):
    s = my_string
    if s.upper():
        s = s.lower()
    s_clone = ''.join(reversed(s))
    if s_clone == s:
        return True
    else:
        return False

my_string = input("Enter a string: ")

if is_palindrome(my_string):
    print("The string is a palindrome..")
else:
    print("The string is not a palindrome.")

#Функция которая проверяет является ли переданная строка палиндромом или нет