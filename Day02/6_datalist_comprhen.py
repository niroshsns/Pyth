def myList():
    x = [x**2 for x in range(10)] # Loop list
    return x

if __name__ == '__main__':
    a = myList()
    print(a)
    print(a[1:4:2]) #
    del a[1:4:2] # Remove by index 2nd and 4th
    print(a)
    del a[0]
