class a:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "a: {}, b: {}, c: {}".format(self.a, self.b, self.c)

    def printall(self):
        print(self.a, self.b, self.c)


def main():
    c = a(1, 2, 3)
    b = a(4, 6, 7)
    print(c)
    b.printall()

main()