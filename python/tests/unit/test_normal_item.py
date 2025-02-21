import unittest
from gilded_rose import Item, GildedRose

class NormalItemUpdateStrategyTest(unittest.TestCase):
    def test_quality_of_normal_product_should_decrease_to_zero(self) -> None:
        items = [Item("product", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        
    def test_quality_of_normal_product_should_degrade_twice_as_fast_after_sell_date(self) -> None:
        items = [Item("product", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
    
    def test_quality_of_normal_product_should_not_be_negative(self) -> None:
        items = [Item("product", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_and_sell_in_of_normal_product_should_decrease(self):
        items = [Item("product", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([4, 9], [items[0].sell_in, items[0].quality])

if __name__ == '__main__':
    unittest.main()
