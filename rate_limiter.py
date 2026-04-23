import time

def rate_limiter(max_calls, time_window):
    calls = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()

            while calls and calls[0] <= current_time - time_window:
                calls.pop(0)

            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                print("Rate limit exceeded. Try later")

        return wrapper
    return decorator


@rate_limiter(5, 10)
def my_function():
    print("Function executed at", time.strftime("%X"))


for i in range(10):
    my_function()
    time.sleep(1)