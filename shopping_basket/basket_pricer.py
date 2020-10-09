import importlib


class BasketPricer(object):

    def __init__(self, catalogue, offers=None, basket=None):
        self.catalogue = catalogue
        self.offers = offers
        self.basket = basket

    def computeBasket(self):
        """
        Computes for the basket total (subtotal - discounts)

        Returns:
            A dictionary containing the computed subtotal, discount, and total
        """
        summary = {
            'subtotal': 0,
            'discount': 0,
            'total': 0
        }

        if not self.basket:
            return summary
        if self.offers:
            summary['discount'] = self.computeDiscount()

        summary['subtotal'] = self.computeSubtotal()
        summary['total'] = round(summary['subtotal'] - summary['discount'], 2)
        return summary

    def computeSubtotal(self):
        """
        Computes for the basket subtotal

        Returns:
            Amount for the items added in the basket
        """
        subtotal = 0
        for item, qty in self.basket:
            if item in self.catalogue:
                subtotal += self.catalogue[item]['price']*qty
        return subtotal

    def computeDiscount(self):
        """
        Computes for basket items total discount

        Returns:
            Amount to be discounted
        """
        discount = 0
        offers = set()
        for item, _ in self.basket:
            if item in self.offers:
                for offer in self.offers[item]:
                    offers.add(offer[0])

        module = importlib.import_module('offers')
        for offer in offers:
            OfferClass = getattr(module, offer)
            discount += OfferClass(self.catalogue, self.offers, self.basket).computeDiscount()
        return discount
