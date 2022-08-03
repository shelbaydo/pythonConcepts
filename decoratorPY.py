from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup()

# To create a decorator function in Python, 
# I create an outer function that takes a function as an argument.
# There is also an inner function that wraps around the decorated function.
# and then return the inner function


# To use a decorator ,
# you attach it to a function like you see in the code below.
#  We use a decorator by placing the name of the decorator 
#  directly above the function we want to use it on. 
# You prefix the decorator function with an @ symbol.

