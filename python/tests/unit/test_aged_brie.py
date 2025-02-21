import unittest
from gilded_rose import Item, GildedRose

class AgedBrieUpdateStrategyTest(unittest.TestCase):
    def test_brie_quality_should_be_less_than_50(self) -> None:
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_brie_should_increase_in_quality_as_sell_in_decreases(self) -> None:
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([4, 11], [items[0].sell_in, items[0].quality])
    
        
if __name__ == '__main__':
    unittest.main()

        
