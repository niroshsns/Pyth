i = 10
def func(arg = i):
    print(arg)

i = 20   

def func2(a, L = []):
    L.append(a)
    return L

if __name__ == '__main__':
    #func(26)
    print(func2(1))
    K = func2(2)
    print(func2(3))
    print(func2(4))
    print('K updated', K)
    
    K = func2 (2)
    print(func2(3))
    print (func2(4))
    L2 = ["A", "B", "C"]
    L3 = func2("D", L2)
    print("K has updated again ", K)
    print ("L2 = ", L2)
    print("L3 = ", L3)
    print ("L2 is updated within the function")
    L3 = func2 ("E", L3)
    print ("L2 = ", L2)
    print("L3 = ", L3)
    print ("Both L2 and L3 are updated within the function as "
    "they are refering to same mutable variable")
    L4 = list ()
    L4 = func2("New List", L4) # New reference is given
    func2 ("F", L2)
    print("L2 = ", L2)
    print ("L3 = ", L3)
    print("L4 = ", L4)

    
    
    


