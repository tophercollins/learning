def new_decorator(func):

    def wrap_func():
        print('Some code before executing func')
        func()
        print('Some extra code, after the original function')
    return wrap_func

@new_decorator
def func_need_decorator():
    print('Please decorate me!')

func_need_decorator()