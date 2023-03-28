def fibonacci(n):
    #n= 100
    a = 0
    b = 1
    results = []
    while a <= n:
        results.append(a)
        b = a + b
        a = b - a
    return results

def ask_ok(prompt, retry=4, reminder= 'Please Try Again'):
    while True:
        ok_sts = input(prompt)
        if ok_sts in ('y', 'ye', 'yes'):
            return True
        if ok_sts in ('n', 'no', 'nop','nope'):
            return False
        retry = retry -1
        if retry <0:
            #raise ValueError('Invalid Input')
            print(reminder)

if __name__ == '__main__':
    #a = 150
    #print('fibonacci seq upto ',a, ' is ',fibonacci(a))
    ask_ok('Enter Your Status: ')
    
    
    


