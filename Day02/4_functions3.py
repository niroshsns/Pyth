def parrot (voltage, state= 'a stiff', action= 'shine', type= 'Norwegian Blue'):
    print("-- This parrot wouldn't", action, "if you put", voltage, "volts through it.")
    print ("--Nice Color..", type)
    print ("--It's",state, " !")

#Any number of args
def concat(*args, sep ='/'):
    return sep.join(args)

if __name__ == '__main__':
    parrot(3000)
    parrot('a thousand', state='push')
    #parrot(voltage=1000, 'a stiffer') //Positional argument cannot appear after keyword arguments
    #parrot('1000',voltage='10060') // got multiple values for argument 'voltage'
    #parrot() // missing 1 required positional argument

    print(concat('a', 'b', 'c'))
    print(list(range(3,6)))
    
    
    


