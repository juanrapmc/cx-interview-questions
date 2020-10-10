from unittest import TestCase
from offers import BuyXGetXOffer, PercentOffOffer, BuyXSetGetMinFree
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

        basket = [ (101, 2), (150, 1), (200, 1) ]
        buyGetOffer = BuyXGetXOffer(catalogue, offers, basket)
        self.assertEqual(0, buyGetOffer.computeDiscount())

        basket = [ (101, 5), (150, 1), (200, 1) ]
        buyGetOffer = BuyXGetXOffer(catalogue, offers, basket)
        self.assertEqual(0.99, buyGetOffer.computeDiscount())

    def test_buyXSetGetMinFree(self):
        basket = [ (352, 1), (353, 3), (351, 2) ]
        buyXSetMinFreeOffer = BuyXSetGetMinFree(catalogue, offers, basket)
        self.assertEqual(5.5, buyXSetMinFreeOffer.computeDiscount())

        basket = [ (353, 3) ]
        buyXSetMinFreeOffer = BuyXSetGetMinFree(catalogue, offers, basket)
        self.assertEqual(3.5, buyXSetMinFreeOffer.computeDiscount())

        basket = [ (351, 1), (352, 1), (353, 1) ]
        buyXSetMinFreeOffer = BuyXSetGetMinFree(catalogue, offers, basket)
        self.assertEqual(2, buyXSetMinFreeOffer.computeDiscount())

        basket = [ (351, 3), (353, 3), (352, 3) ]
        buyXSetMinFreeOffer = BuyXSetGetMinFree(catalogue, offers, basket)
        self.assertEqual(8, buyXSetMinFreeOffer.computeDiscount())
