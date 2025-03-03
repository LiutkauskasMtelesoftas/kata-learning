import unittest
from gilded_rose import Item, GildedRose

class AgedBrieUpdateStrategyTest(unittest.TestCase):
    #write a test with tests cases like in backstage passes
    def test_aged_brie(self) -> None:
        test_cases = [
            (Item("Aged Brie", 5, 50), [4, 50]),
            (Item("Aged Brie", 5, 10), [4, 11])
        ]
        
        for item, expected in test_cases:
            with self.subTest(item=item):
                gilded_rose = GildedRose([item])
                gilded_rose.update_quality()
                self.assertEqual(expected, [item.sell_in, item.quality])
        
if __name__ == '__main__':
    unittest.main()

        
