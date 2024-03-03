from functools import reduce

def multiply_list(nums):
    return reduce(lambda x, y: x * y, nums) #lambda arguments: expression

nums = [float(num) for num in input("Enter the numbers separated by comma: ").split(',')]

result = multiply_list(nums)
print("Result:", result)

#Функция для умножения всех чисел в списке