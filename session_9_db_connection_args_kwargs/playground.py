def demonstrate_args(arg1, arg2):
    """Function with regular arguments."""
    print(f"arg1: {arg1}, arg2: {arg2}")

# Demonstrating regular arguments
demonstrate_args('apple', 'banana')



def demonstrate_args_and_args(arg1, *args):
    """Function that accepts additional positional arguments."""
    print(f"arg1: {arg1}")
    print("*args:", args)

# Demonstrating *args
demonstrate_args_and_args('apple', 'banana', 'cherry', 'date')



def demonstrate_kwargs(arg1, **kwargs):
    """Function that accepts any number of keyword arguments."""
    print(f"arg1: {arg1}")
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")

# Demonstrating **kwargs
demonstrate_kwargs('fruit', first='apple', fruit2='banana', third='orange')
#
# def demonstrate_all(arg1, *args, **kwargs):
#     """Function that accepts a mix of regular, *args, and **kwargs."""
#     print(f"arg1: {arg1}")
#     print("*args:", args)
#     if kwargs:
#         print("**kwargs:")
#         for key, value in kwargs.items():
#             print(f"{key}: {value}")







# # Demonstrating all
# demonstrate_all('fruit', 'apple', 'banana', fav='cherry', hel='date')
