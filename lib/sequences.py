#!/usr/bin/env python3

def print_fibonacci(length):   
    fibonacci = [0, 1]
    if length <= 0:
        print ([])
    elif length == 1:
        print([0])
        
    elif length == 2:
        print([0, 1])
        
    else:
        for i in range(2, length):
            fibonacci_next = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(fibonacci_next)
    return fibonacci
print(print_fibonacci(10))


