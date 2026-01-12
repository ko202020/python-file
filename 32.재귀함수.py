def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
    
print(factorial(5))  # 120

""" 5 
* factoral(4) 
* factoral(3) 
* factoral(2) 
* 1 """