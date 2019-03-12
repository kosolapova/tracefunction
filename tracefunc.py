import sys


def foo():
    friends = ["Bob", "Tom"]
    for f in friends:
        print("Hi %s!" % f)
    return len(friends)


def tracefunc(frame, event, arg):
    function_name = frame.f_code.co_name
    local_vars = list(frame.f_code.co_varnames)
    print('function: %s, local vars: %s' % (function_name, local_vars))
    return


def tracefoo(function_to_trace):
    sys.settrace(tracefunc)
    function_to_trace()
    return


tracefoo(foo)


