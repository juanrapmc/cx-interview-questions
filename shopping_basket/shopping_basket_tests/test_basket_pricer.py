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

    def test_compute_basket_no_offers(self):
        basket = [ (101, 4), (150, 1) ]
        bPricer = BasketPricer(catalogue, basket=basket)
        expectedComputation = {
            'discount': 0,
            'subtotal': 5.16,
            'total': 5.16
        }
        self.assertEqual(expectedComputation, bPricer.computeBasket())

    def test_compute_basket_with_offers(self):
        basket = [ (101, 4), (150, 1) ]
        bPricer = BasketPricer(catalogue, offers, basket)
        expectedComputation = {
            'discount': 0.99,
            'subtotal': 5.16,
            'total': 4.17
        }
        self.assertEqual(expectedComputation, bPricer.computeBasket())

    def test_compute_basket_no_basket(self):
        bPricer = BasketPricer(catalogue)
        expectedComputation = {
            'discount': 0,
            'subtotal': 0,
            'total': 0
        }
        self.assertEqual(expectedComputation, bPricer.computeBasket())

    def test_get_basket_subtotal(self):
        basket = [ (101, 4), (150, 1) ]
        bPricer = BasketPricer(catalogue, basket=basket)
        self.assertEqual(5.16, bPricer.computeSubtotal())

    def test_get_basket_discount(self):
        basket = [ (101, 4), (150, 1) ]
        bPricer = BasketPricer(catalogue, offers, basket)
        self.assertEqual(0.99, bPricer.computeDiscount())
