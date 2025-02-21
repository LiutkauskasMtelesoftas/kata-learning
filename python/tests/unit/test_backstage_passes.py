import unittest
from gilded_rose import Item, GildedRose

class BackstagePassesUpdateStrategyTest(unittest.TestCase):
    def test_quality_for_concert_should_be_less_than_50_1(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
    
    def test_quality_for_concert_should_be_less_than_50_2(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
    
    def test_quality_for_concert_should_be_less_than_50_3(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        
    def test_quality_for_concert_should_increase_by_2_when_sell_in_is_10_or_less(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        
    def test_quality_for_concert_should_increase_by_3_when_sell_in_is_5_or_less(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
    
    def test_quality_for_concert_should_be_0_when_sell_in_is_0(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
    
    def test_sell_in_for_concert_should_decrease(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
