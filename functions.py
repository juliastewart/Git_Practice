
# Here are some functions that you can fill in to make them work.
# Replace the "raise NotImplementedError" line with the correct code!
   
def print_the_instructors_name(fn, ln):
    if type(fn) is str:
        name = str(fn+' '+ln)
        print(name)
    else:
        raise NotImplementedError
    return(name)

def print_the_number_of_this_room(num):
    print('Room number: ', num)
    return(num)

def split_this_string_at_each_space(input_string):
    raise NotImplementedError

def take_the_average_of_these_numbers(a, b):
    raise NotImplementedError

def print_the_time_now_using_astropy():
    raise NotImplementedError

def return_the_minimum_of_two_numbers(a, b):
    raise NotImplementedError

def return_the_std_of_two_numbers(a, b):
    raise NotImplementedError
