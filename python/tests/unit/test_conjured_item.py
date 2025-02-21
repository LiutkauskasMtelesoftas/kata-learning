import unittest
from gilded_rose import Item, GildedRose

class BackstagePassesUpdateStrategyTest(unittest.TestCase):
    def test_conjured_quality_should_not_be_lower_than_zero(self) -> None:
        items = [Item("conjured product", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        
    def test_conjured_should_degrade_twice_as_fast(self) -> None:
        items = [Item("Conjured product", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
    
    def test_conjured_should_degrade_twice_as_fast_after_sell_date(self) -> None:
        items = [Item("Conjured product", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
    
    def test_sell_in_of_conjured_product_should_decrease(self):
        items = [Item("Conjured product", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        
if __name__ == '__main__':
    unittest.main()
