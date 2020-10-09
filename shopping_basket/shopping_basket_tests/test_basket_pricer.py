from unittest import TestCase
from basket_pricer import BasketPricer

catalogue = {
    101: {'name': 'Baked Beans', 'price': 0.99},
    150: {'name': 'Biscuits', 'price': 1.20},
    200: {'name': 'Sardines', 'price': 1.89},
    351: {'name': 'Shampoo (Small)', 'price': 2.00},
    352: {'name': 'Shampoo (Medium)', 'price': 2.50},
    353: {'name': 'Shampoo (Large)', 'price': 3.50},
}

offers = {
    101: [("buyXgetX", 2, 1),],
    200: [("percentOff", 25)],
    351: [("buyXSetGetMinFree", 1)],
    352: [("buyXSetGetMinFree", 1)],
    353: [("buyXSetGetMinFree", 1)],
}


class TestBasketPricer(TestCase):

    def test(self):
        self.assertTrue(True)

    def test_get_basket_total_no_offers(self):
        basket = [
            (101, 3),
            (150, 2)
        ]
        bpricer = BasketPricer(catalogue, basket=basket)
        self.assertEqual(5.37, bpricer.computeTotal())
        pass
