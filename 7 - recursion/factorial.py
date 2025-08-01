


def factorial(n):
    ans = 1
    
    if n <= 1:
        return n 
    else: 
        return n * factorial(n - 1)