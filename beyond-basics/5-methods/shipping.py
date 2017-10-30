
class ShippingContainer:

    next_serial = 1234

    def __init__(self, owner, contents):
        self.owner = owner
        self.contents = contents
        # next_serial is not in the LEGB scopes, so must be qualified...
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1