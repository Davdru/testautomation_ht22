
def yield_demo1():
    yield 1
    yield 2
    yield 3

#
# for i in yield_demo1():
#     print(i)


def yield_demo2():
    a = 1
    r = 1
    while True:
        yield r
        r = r * a
        a += 1

i = 0
for n in yield_demo2():
    print(n)
    i+=1
    if i > 10:
        break




def min_dekorator(f):
    def inner():
        print("Hej jag är dekorerad funktion")
        f()
        print("Hejdå!")
    return inner


@min_dekorator
def foo():
    print("Hej, jag är funktionen foo")


print(type(foo))
