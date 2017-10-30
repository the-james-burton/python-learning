
class ShippingContainer:

    next_serial = 1234


    @staticmethod
    def _get_next_serial():
        # note there is no 'self' argument
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def _get_next_serial2(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result


    def __init__(self, owner, contents):
        self.owner = owner
        self.contents = contents
        # can call it directly...
        # next_serial is not in the LEGB scopes, so must be qualified...
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        #... or use the static method...
        self.serial = ShippingContainer._get_next_serial()
        #... or use the class method...
        self.serial = ShippingContainer._get_next_serial2()