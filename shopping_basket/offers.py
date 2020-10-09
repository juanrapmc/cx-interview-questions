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
        discount = 0
        for item, qty in self.basket:
            if item in self.offers:
                for offer in self.offers[item]:
                    if offer[0] == 'BuyXGetXOffer':
                        buy_amt = 0
                        free_amt = 0
                        free_total = 0
                        for _ in range(1, qty+1):
                            if free_amt:
                                free_total += 1
                                free_amt -= 1
                                continue
                            buy_amt += 1
                            if buy_amt % offer[1] == 0:
                                free_amt = offer[2]
                        discount += self.catalogue[item]['price'] * free_total
        return round(discount, 2)
