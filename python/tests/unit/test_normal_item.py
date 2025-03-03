import unittest
from gilded_rose import Item, GildedRose

class NormalItemUpdateStrategyTest(unittest.TestCase):
    def test_normal_item(self) -> None:
        test_cases = [
            (Item("product", 5, 10), [4, 9]),
            (Item("product", 0, 10), [-1, 8]),
            (Item("product", 5, 1), [4, 0]),
            (Item("product", 5, 0), [4, 0])
        ]
        for item, expected in test_cases:
            with self.subTest(item=item):
                gilded_rose = GildedRose([item])
                gilded_rose.update_quality()
                self.assertEqual(expected, [item.sell_in, item.quality])

if __name__ == '__main__':
    unittest.main()
