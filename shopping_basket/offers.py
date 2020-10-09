from abc import ABC, abstractmethod


class Offer(ABC):

    def __init__(self, catalogue, offers, basket):
        self.catalogue = catalogue
        self.offers = offers
        self.basket = basket

    @abstractmethod
    def computeDiscount(self):
        raise NotImplementedError


class PercentOffOffer(Offer):

    def computeDiscount(self):
        discount = 0
        for item, qty in self.basket:
            if item in self.offers:
                for offer in self.offers[item]:
                    if offer[0] == 'PercentOffOffer':
                        discount += self.catalogue[item]['price'] * qty * (offer[1]/100)
        return round(discount, 2)

class BuyXGetXOffer(Offer):

    def computeDiscount(self):
        pass
