# def fibo(num):
#     if num <= 1:
#         return num
#     return fibo(num - 1) + fibo(num -2)

# # print(fibo(7))

# def to_roman(num, answer = ''):
#     # write your code here!
#     numerals ={
#         "M" : 1000,
#         "CM": 900,
#         "D" : 500,
#         "CD": 400,
#         "C" : 100,
#         "XC": 90,
#         "L" : 50,
#         "XL": 40,
#         "X" : 10,
#         "IX": 9,
#         "V" : 5,
#         "IV": 4,
#         "I" : 1,
#     }
#     if num == 0:
#         return answer
#     for numeral, val in numerals.items():
#         if num >= val:
#             return to_roman(num=num%val, answer = answer + numeral*(num//val))
        
# print(to_roman(699))


input_list = [1, [2, 3], 4, [[5]], 6]

# def flatten_list(input, index=0):
#     new_list = []
#     for item in input:
#         print(type(item))
#         if type(item) == list:
#             for item2 in item:
#                 new_list.append(item2)
#         else:
#             new_list.append(item)

#     return new_list

# print(flatten_list(input_list))

# def flatten_list_r(input, index=0, new_list=[]):
#     if index == len(input):
#         return new_list
    
#     if type(input[index]) == list:
#         for item in input[index]:
#             new_list.append(item)

#     else:
#         new_list.append(input[index])
    
#     return flatten_list_r(input, index = index + 1)

def flatten_list_r(input, index=0, new_list=[]):
    if index == len(input):
        return new_list
    if type(input[index]) == list:
        # new_list.append(input)
        flatten_list_r(input[index], index = index + 1)
    else:
        new_list.append(input[index])
        
        flatten_list_r(input, index = index + 1)
    return new_list
    
    

print(flatten_list_r(input_list))