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
        pass


class BuyXGetXOffer(Offer):

    def computeDiscount(self):
        pass
