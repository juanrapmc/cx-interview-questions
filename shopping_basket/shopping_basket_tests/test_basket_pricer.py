from unittest import TestCase

catalogue = {
    101: {'name': 'Baked Beans', 'price': 0.99},
    150: {'name': 'Biscuits', 'price': 1.20},
    200: {'name': 'Sardines', 'price': 1.89},
    351: {'name': 'Shampoo (Small)', 'price': 2.00},
    352: {'name': 'Shampoo (Medium)', 'price': 2.50},
    353: {'name': 'Shampoo (Large)', 'price': 3.50},
}


class TestBasketPricer(TestCase):

    def test(self):
        self.assertTrue(True)
