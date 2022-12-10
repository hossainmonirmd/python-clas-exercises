# Ass 2
"""
def easy_function(num):
    return lambda x: x * num


result = easy_function(20)

print(result(15))
"""
## Ass 3

lst = [10, 20, 35, 45]


E_N_lambda = filter (lambda num: num % 2 == 0,lst)
print("Totall even number is:",len(list(E_N_lambda)))

O_N_lambda = filter (lambda num: num % 2 == 1,lst)
print("Totall odd number is:",len(list(O_N_lambda)))
"""

# Ass 1
add = lambda num: num + 10
print(add(15))

multiplytwonumbers = lambda x, y: x * y

print(multiplytwonumbers(10, 10))
"""
"""
out_lst = []
for value in lst:
    if value % 2 == 1:
        out_lst.append(value)

print(out_lst)
"""






