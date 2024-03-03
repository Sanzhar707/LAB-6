import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000) #Задержка функции
    result = math.sqrt(number)
    return result

number = float(input("Enter a number: "))
milliseconds = int(input("Enter the delay time in milliseconds: "))

result = square_root_after_milliseconds(number, milliseconds)

print(f"The square root of {number} after {milliseconds} milliseconds is {result}")