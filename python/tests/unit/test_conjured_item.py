import unittest
from gilded_rose import Item, GildedRose

class ConjuredItemUpdateStrategyTest(unittest.TestCase):
    def test_conjured_item(self) -> None:
        test_cases = [
            (Item("Conjured product", 5, 1), [4, 0]),
            (Item("Conjured product", 0, 10), [-1, 6]),
            (Item("Conjured product", 5, 10), [4, 8])
        ]
        for item, expected in test_cases:
            with self.subTest(item=item):
                gilded_rose = GildedRose([item])
                gilded_rose.update_quality()
                self.assertEqual(expected, [item.sell_in, item.quality])

if __name__ == '__main__':
    unittest.main()
