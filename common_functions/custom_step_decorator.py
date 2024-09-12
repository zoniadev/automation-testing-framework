from behave import step as original_step

def step(arg):
    def wrapper(func):
        @original_step(arg)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                raise AssertionError(e)

        return inner

    return wrapper
