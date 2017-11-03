
import random

class ShippingContainer:

    next_serial = 1234


    @staticmethod
    def _get_next_serial_random():
        # note there is no 'self' argument
        # static methods should be used when no access to the class is required
        # i.e. a 'pure' function that depends only on its arguments...
        return random.randint(0, 9999)

    @classmethod
    def _get_next_serial_incremented(cls):
        # class methods should be used when access to the class is required
        # in this case, to maintain state across instances...
        result = cls.next_serial
        cls.next_serial += 1
        return result


    @classmethod
    def create_empty(cls, owner, *args, **kwargs):
        # this is a factory method...
        # use *args and **kwargs to forward any extra args to the subclass __init__
        return cls(owner, contents=None, *args, **kwargs)


    @classmethod
    def create_with_items(cls, owner, items, *args, **kwargs):
        # this is a factory method...
        return cls(owner, contents=list(items), *args, **kwargs)


    def __init__(self, owner, contents):
        self.owner = owner
        self.contents = contents
        # can call it directly...
        # next_serial is not in the LEGB scopes, so must be qualified...
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        #... or use the static method...
        # (to get polymophic dispatch of static methods, use the instance)
        # self.serial = ShippingContainer._get_next_serial_random()
        self.serial = self._get_next_serial_random()
        #... or use the class method...
        # self.serial = ShippingContainer._get_next_incremented()


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 3.0

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def _get_next_serial_random():
        # note there is no 'self' argument
        # static methods should be used when no access to the class is required
        # i.e. a 'pure' function that depends only on its arguments...
        return random.randint(9999, 19999)

    def __init__(self, owner, contents, celsius):
        """overriding the base class"""
        # first call the base class init to do the same work...
        super().__init__(owner, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temp):
        if temp > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("{} is too hot!".format(temp))
        self._celsius = temp

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    @staticmethod
    def _get_next_serial_random():
        return random.randint(19999, 29999)

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, temp):
        if temp < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("{} is too cold!".format(temp))
        # note: super().celsius does not work!
        # instead, we use a function from the celsius property...
        RefrigeratedShippingContainer.celsius.fset(self, temp)
