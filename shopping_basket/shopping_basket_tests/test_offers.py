from unittest import TestCase
from offers import BuyXGetXOffer, PercentOffOffer
from shopping_basket_tests.test_basket_pricer import catalogue, offers


class TestOffers(TestCase):

    def test_percentOffOffer(self):
        basket = [ (101, 4), (150, 1), (200, 1) ]
        percentOffer = PercentOffOffer(catalogue, offers, basket)
        self.assertEqual(0.47, percentOffer.computeDiscount())

        basket = [ (101, 4), (150, 1), (200, 5) ]
        percentOffer = PercentOffOffer(catalogue, offers, basket)
        self.assertEqual(2.36, percentOffer.computeDiscount())

    def test_buyXGetXOffer_one_free(self):
        basket = [ (101, 3), (150, 1), (200, 1) ]
        buyGetOffer = BuyXGetXOffer(catalogue, offers, basket)
        self.assertEqual(0.99, buyGetOffer.computeDiscount())

        basket = [ (101, 4), (150, 1), (200, 1) ]
        buyGetOffer = BuyXGetXOffer(catalogue, offers, basket)
        self.assertEqual(0.99, buyGetOffer.computeDiscount())

    def test_buyXGetXOffer_multi_free(self):
        basket = [ (101, 6), (150, 1), (200, 1) ]
        buyGetOffer = BuyXGetXOffer(catalogue, offers, basket)
        self.assertEqual(1.98, buyGetOffer.computeDiscount())
