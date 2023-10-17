# def fibo(num):
#     if num <= 1:
#         return num
#     return fibo(num - 1) + fibo(num -2)

# print(fibo(7))

def to_roman(num, answer = ''):
    # write your code here!
    numerals ={
        "M" : 1000,
        "CM": 900,
        "D" : 500,
        "CD": 400,
        "C" : 100,
        "XC": 90,
        "L" : 50,
        "XL": 40,
        "X" : 10,
        "IX": 9,
        "V" : 5,
        "IV": 4,
        "I" : 1,
    }
    if num == 0:
        return answer
    for numeral, val in numerals.items():
        if num >= val:
            return to_roman(num=num%val, answer = answer + numeral*(num//val))
        
print(to_roman(699))