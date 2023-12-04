"""
All the atrubutes in the object remain private until I wanna make them public

private - public - protected variables

publiv int number = 10;
private String my_str = "Mate;

Private means that - I can modify or delete the private attribute from inside, but I cant reach it trough the object

In python there is no REAL private attribute
"""

class Test:
    def __init__(self):
        """
            'private' attribute
        """
        self.__price = 10_000
        temp = [1, 2, 3]

    def __hello(self):
        """
            'private' function
        """
        print(f"Hello: {self.__price}")

class Test2:
    def __init__(self):
        self.name = "Mate"

my_test = Test()
my_test2 = Test2()

my_test.__price = 30_000
my_test._Test__price = 40_000

my_test._Test__hello()


