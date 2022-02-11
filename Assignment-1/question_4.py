import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()

        print(func.__name__,' took ',str((end-start)),' sec')

        return result

    return wrapper    


@time_it
def isprime():
    try:
        no=int(input('Enter a number to check it is prime or not : '))
        if type(no)==int:
            if all(no%i !=0 for i in range(2,no//2)):
                print('True')
            else:
                print('False')
            
    except Exception as e:
        print('Please enter a integer....')
        isprime()



isprime()