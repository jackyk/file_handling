from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta

    # @abstractmethod
    # def weight():pass
    #
    # @abstractmethod
    # def eat():pass

    def __iter__(self):
        while False:
            yield None
    def getiterator(self):
        return self.__iter__()

test = Animal('True')
test.getiterator()


# class Cat(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super(Cat, self).__init__
#     def weight(self):
#         return "This cat is called {} and it is {} years old".format(self.name, self.age)
#
#     def eat(self):
#         return "{} drinks milk and eats meat". format(self.name)
#
# paka = Cat("Kitty", 2)
# print paka.weight()
# print paka.eat()
