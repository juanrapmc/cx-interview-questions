from abc import ABC, abstractmethod


class Offer(ABC):

    def __init__(self, catalogue, offers, basket):
        self.catalogue = catalogue
        self.offers = offers
        self.basket = basket

    @abstractmethod
    def compute(self, offer, item, qty):
        raise NotImplementedError

    def computeDiscount(self):
        discount = 0
        for item, qty in self.basket:
            if item in self.offers:
                for offer in self.offers[item]:
                    if offer[0] == type(self).__name__:
                        discount += self.compute(offer, item, qty)
        return round(discount, 2)


class PercentOffOffer(Offer):

    def compute(self, offer, item, qty):
        return self.catalogue[item]['price'] * qty * (offer[1]/100)


class BuyXGetXOffer(Offer):

    def compute(self, offer, item, qty):
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
        return self.catalogue[item]['price'] * free_total


class BuyXSetGetMinFree(Offer):

    def compute(self, offer_groups):
        discount = 0
        for group_id in offer_groups:
            offer_group = offer_groups[group_id]
            offer_group.sort(key=lambda x: x[2], reverse=True)
            buy_amt = 0
            for item in offer_group:
                for _ in range(1, item[1]+1):
                    buy_amt += 1
                    if buy_amt == item[3]:
                        discount += item[2]
                        buy_amt = 0
        return discount

    def computeDiscount(self):
        groups = {}
        for item, qty in self.basket:
            if item in self.offers:
                for offer in self.offers[item]:
                    if offer[0] == type(self).__name__:
                        if offer[1] in groups:
                            groups[offer[1]].append((
                                item, qty,
                                self.catalogue[item]['price'],
                                offer[2]))
                        else:
                            groups[offer[1]] = [(
                                item, qty,
                                self.catalogue[item]['price'],
                                offer[2])]

        return self.compute(groups)
