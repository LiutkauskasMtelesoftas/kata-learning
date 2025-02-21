import unittest
from gilded_rose import Item, GildedRose

class SulfurasUpdateStrategyTest(unittest.TestCase):
    def test_sulfuras_should_not_change_in_sell_in(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
    
    def test_sulfuras_should_not_change_in_quality(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
