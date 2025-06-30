####################### Q1 #######################
def sum_numbers(*args):
    sum_num = 0
    for x in args:
        sum_num += x
    return sum_num
print(sum_numbers(1, 2, 3, 4))

####################### Q2 #######################
def print_user_info(**kwargs):
    info = []
    for key, value in kwargs.items():
        info.append(f"{key}={value}")
    print(" ".join(info))

print_user_info(name="Dana", age=30, city="Tel Aviv")

####################### Q3 #######################
def combine_values(*args, **kwargs):
    result = sum(args)
    print(f"sum: {result}")

    print(type(kwargs))
    print(kwargs)
    print('your name is', kwargs['name'])

combine_values(2, 4, 6, name="Tom", job="Dev")

####################### Q4 #######################
def greet_user(**kwargs):
    if 'name' in kwargs:
        print(f'hello {kwargs["name"]}.')
    else:
        print('hello guest.')

greet_user(name="Lior")
greet_user()







