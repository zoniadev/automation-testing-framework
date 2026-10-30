from behave import step as original_step

def step(arg):
    def wrapper(func):
        @original_step(arg)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                # Drop Playwright's full-page Aria snapshot so Allure reports stay readable
                msg = str(e).split("\nAria snapshot:")[0]
                raise AssertionError(msg) from None

        return inner

    return wrapper
