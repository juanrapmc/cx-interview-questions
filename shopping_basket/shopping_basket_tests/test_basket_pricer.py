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
    101: [{"offer_name": "BuyXGetXOffer", "buy_amount": 2, "free_amount": 1}],
    150: [{"offer_name": "BuyXGetXOffer", "buy_amount": 3, "free_amount": 2}],
    200: [{"offer_name": "PercentOffOffer", "percent": 25}],
    351: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
    352: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
    353: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
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

        basket = [(150, 5), (101, 5)]
        bPricer = BasketPricer(catalogue, offers, basket)
        expectedComputation = {
            'discount': 3.39,
            'subtotal': 10.95,
            'total': 7.56
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
