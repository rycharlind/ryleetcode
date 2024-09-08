
def example1():
    l = [1, 2, 3, 4]

    def getItem():
        for i in l:
            yield i

    gen = getItem()

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

def example2():
    counter = count_up_to(5)
    for number in counter:
        print(number)

# example1()
example2()