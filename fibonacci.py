def Fibonacci(n):
    if n < 3:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)
def main(len):
    for i in range(1,len+1):
        print('Fibonacci(',i,')=',Fibonacci(i))
main(200)