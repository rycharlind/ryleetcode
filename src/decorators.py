def my_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Sup")

    return wrapper

@my_decorator
def run():
    print("World")


run()