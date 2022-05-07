nums = {
    '1': 'один',
    '2': 'два',
    '3': 'три'
}

# print(nums)
# print(type(nums))


myString = '1 кот, 2 кота, 3 кота'

# for k, v in nums.items():
#     print(k, v)



for k, v in nums.items():
    myString = myString.replace(k, v)


print(myString)