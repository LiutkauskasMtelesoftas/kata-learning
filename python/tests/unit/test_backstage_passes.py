import unittest
from gilded_rose import Item, GildedRose

class BackstagePassesUpdateStrategyTest(unittest.TestCase):
    
    #cahnge this method so it would only have sell in and quality and back stage passes name is passed in the loop
    def test_backstage_passes(self) -> None:
        concert = "Backstage passes to a TAFKAL80ETC concert"
        test_cases = [
            (Item(concert, 5, 48), [4, 50]),
            (Item(concert, 11, 50), [10, 50]),
            (Item(concert, 10, 49), [9, 50]),
            (Item(concert, 10, 10), [9, 12]),
            (Item(concert, 5, 10), [4, 13]),
            (Item(concert, 0, 10), [-1, 0]),
        ]
        for item, expected in test_cases:
            with self.subTest(item=item):
                gilded_rose = GildedRose([item])
                gilded_rose.update_quality()
                self.assertEqual(expected, [item.sell_in, item.quality])

if __name__ == '__main__':
    unittest.main()
