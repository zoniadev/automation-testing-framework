from behave import step as original_step
import traceback
import sys

def step(arg):
    def wrapper(func):
        @original_step(arg)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except AssertionError:
                # If it's already an assertion error, just re-raise it
                raise
            except Exception as e:
                # Capture the full stack trace
                tb = traceback.format_exc()
                print(f"\n!!! EXCEPTION CAUGHT IN STEP: {arg} !!!")
                print(tb)
                print("!!! --------------------------------- !!!\n")
                
                # Raise AssertionError to ensure Allure marks it as Failed (Red), not Broken
                # But include the original error message
                raise AssertionError(f"Step failed due to {type(e).__name__}: {e}") from e

        return inner

    return wrapper