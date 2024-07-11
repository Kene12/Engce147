x = int(input('Enter your number:'))
def numpat(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end=" ")
        print("")
def numpatR(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print('*', end=" ")
        print("")
def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(i+1):
            print('*', end=" ")
        print("")
def pyramidR(n):
    for i in range(n, 0, -1):
        print(" "*(n-i),end="")
        for j in range(i):
            print('*', end=" ")
        print("")
        
def numpatright(n):
    for i in range(n):
        for j in range(i, n):
            print(' ', end=" ")
        for j in range(i+1):
            print('*', end=" ")
        print("")

numpat(x)
print('-------------------------')
numpatR(x)
print('-------------------------')
pyramid(x)
print('-------------------------')
pyramidR(x)
print('-------------------------')
numpatright(x)