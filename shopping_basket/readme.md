# Shopping Basket Pricer

This module allows computes for the subtotal, discounts, and total of a shopping basket based from a given catalogue, basket, and offers.

### Definitions

* **basket**: A collection of goods a customer wishes to buy
* **subtotal**: The undiscounted cost of items in a basket
* **discount**: The amount to subtract from subtotal to compute for the final price
* **total**: The final price of goods after applying discount
* **offers**: The pricing rules for items
* **catalogue**: Products sold currently. Mapping of item to price.
* **basket_pricer**: The class that computes for subtotal, discount, and total for a given basket, offers, and catalogue.

## BasketPricer

* The class responsible for computing the subtotal, discount, and total for a given basket, offers, and catalogue.

### Inputs

* **catalogue**: Required input. A set containing dictionaries for each product being sold.
    * **Format**:
        ```python
        {
            <item_id>: {
                "name": <product_name>,
                "price": <product_price>
            },
            ...
        }
        ```
    * **Example**:
        ```python
        {
            101: {'name': 'Baked Beans', 'price': 0.99},
            150: {'name': 'Biscuits', 'price': 1.20},
            200: {'name': 'Sardines', 'price': 1.89},
            351: {'name': 'Shampoo (Small)', 'price': 2.00},
            352: {'name': 'Shampoo (Medium)', 'price': 2.50},
            353: {'name': 'Shampoo (Large)', 'price': 3.50},
        }
        ```

* **offers**: Optional input. Mapping of offer to an item.
    * **Offer classes**: Offers that can be mapped to an item. \* To add new offer classes see [Offers Factory](#offers-factory)
        * **BuyXGetXOffer**: Get an amount free when the number of item reaches a target.
            * **Parameters**
                * **buy_amount** - Target item quantity before giving a free amount of the same item.
                * **free_amount** - Quantity of free items once target buy amount has been reached.
        * **PercentageOffer**: Subtract a percentage from the original price of an item.
            * **Parameters**
                * **percent**: Percentage amount to give as a discount
        * **BuySetXGetMinFree**: For every target quantity bought from a list of items, the cheapest item from that list is given as free.
            * **Parameters**
                * **group_id**: Identifier for items that can be grouped in the offer.
                * **buy_amount**: Quantity target before giving the cheapest item for free.
    * **Format**:
        ```python
        {
            <item_id>: [
                {
                    "offer_name": <offer_class_name>,
                    <class_parameter>: <value>,
                    ...
                }
            ]
        }
        ```
    * **Example**:
        ```python
        {
            101: [{
                "offer_name": "BuyXGetXOffer",
                "buy_amount": 2,
                "free_amount": 1
            }],
            200: [{
                "offer_name": "PercentOffOffer",
                "percent": 25
            }],
            351: [{
                "offer_name": "BuyXSetGetMinFree",
                "group_id": 1,
                "buy_amount": 3
            }],
            352: [{
                "offer_name": "BuyXSetGetMinFree",
                "group_id": 1,
                "buy_amount": 3
            }],
            353: [{
                "offer_name": "BuyXSetGetMinFree",
                "group_id": 1,
                "buy_amount": 3
            }],
        }
        ```

* **basket**: Optional input. Nothing is computed if none. A collection of item to buy and the quantity.
    * **Format**:
        ```python
        [
            (<item_id>, <quantity>),
            ...
        ]
        ```
    * **Example**:
        ```python
        [
            (101, 5),
            (352, 3),
        ]

### Methods
* **constructor**: Takes in catalogue, offers, and basket
* **compute_basket**: Returns a summary of the basket (subtotal, discount, total) in a dictionary format.
* **compute_subtotal**: Returns the total amount of the basket without any discount
* **compute_discount**: Returns the total amount to be discounted.

# Offers Factory

* Responsible for creating the offers and how they are applied to the basket.
* To add a new offer, the `Offer` class should be inherited.
* The `compute_discount` method (from base class) gets the discount for every item in the basket.
    * This calls another method `compute` which should be implemented by child classes
* The `compute` method contains the logic to get the discount for a given item.

## Sample Usage

```python
Python 3.8.2 (default, Apr 27 2020, 15:53:34)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from basket_pricer import BasketPricer
>>>
>>> catalogue = {
...     101: {'name': 'Baked Beans', 'price': 0.99},
...     150: {'name': 'Biscuits', 'price': 1.20},
...     200: {'name': 'Sardines', 'price': 1.89},
...     351: {'name': 'Shampoo (Small)', 'price': 2.00},
   352:...     352: {'name': 'Shampoo (Medium)', 'price': 2.50},
...     353: {'name': 'Shampoo (Large)', 'price': 3.50},
... }
>>> offers = {
...     101: [{"offer_name": "BuyXGetXOffer", "buy_amount": 2, "free_amount": 1}],
...     150: [{"offer_name": "BuyXGetXOffer", "buy_amount": 3, "free_amount": 2}],
...     200: [{"offer_name": "PercentOffOffer", "percent": 25}],
...     351: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
...     352: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
...     353: [{"offer_name": "BuyXSetGetMinFree", "group_id": 1, "buy_amount": 3}],
... }
>>> basket = [ (101, 4), (150, 1) ] # buying 4pcs of Baked Beans and 1pc of Biscuits"
>>> BasketPricer(catalogue, offers, basket).computeBasket()
{'subtotal': 5.16, 'discount': 0.99, 'total': 4.17}
>>> # 1pc of Baked Beans for free, 3 pcs of Baked beans at original price, and 1pc of Biscuits at original price
>>>
```