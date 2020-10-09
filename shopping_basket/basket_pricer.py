

class BasketPricer(object):

    def __init__(self, catalogue, offers=None, basket=None):
        self.catalogue = catalogue
        self.offers = offers
        self.basket = basket

    def computeBasket(self):
        pass

    def computeSubtotal(self):
        pass

    def computeDiscount(self):
        pass
