from timeit import default_timer as timer

def fibonacci(n):
    start = timer()
    if n < 0 :
        return 0
    elif n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    print(fibonacci(n))
    print("timer: ", timer() - start)
    
fibonacci(10)