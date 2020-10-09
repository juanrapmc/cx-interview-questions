from abc import ABC, abstractmethod


class Offer(ABC):
    def __init__(self, basket):
        self.basket = basket

    @abstractmethod
    def computeDiscount(self):
        raise NotImplementedError
