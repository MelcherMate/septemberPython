"""

Class attributes
    - class variable
    - class method

1. I can reach the class variable trough the object
2. I can not reach the attributes of the instance

What are classmethod good for:
    - if i wanna change the class attributes or change someting on it
    - if i wanna create new object -> factory method
"""


class Test:
    test_class_val = "anything"


    def __init__(self):
        self.price = 10_000

    @classmethod
    def first_classmethod(cls):
        return cls

test = Test()

test2 = test.first_classmethod()
test3 = Test.first_classmethod()
"""
test2 = Test()

test.test_class_val = "everything"
Test.test_class_val = "nothing"

print(test.test_class_val)
print(test2.test_class_val)
print(Test.test_class_val)
"""

