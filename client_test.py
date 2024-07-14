import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
class ClientTest(unittest.TestCase):
    def test_getDataPoint(self):
        quote = {
            'stock': 'ABC',
            'top_bid': {'price': 120.48, 'size': 10},
            'top_ask': {'price': 121.2, 'size': 10}
        }
        expected = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
        self.assertEqual(getDataPoint(quote), expected)

class ClientTest(unittest.TestCase):
    def test_getRatio(self):
        price_a = 119.2
        price_b = 120.48
        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)
        self.assertIsNone(getRatio(price_a, 0))


if __name__ == '__main__':
    unittest.main()
