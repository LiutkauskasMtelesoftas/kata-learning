# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        
        brie = "brie".lower()
        concert_substrings = ["concert", "backstage", "pass"]
        sulfuras = "sulfuras".lower()
        quality_items = [brie, sulfuras] + concert_substrings
        
        for item in self.items:
            lower_name = item.name.lower()
            if lower_name.__contains__(sulfuras):
                continue
            if not any(special in lower_name for special in quality_items):
                self.decrease_quality(item)
            else:
                self.increase_quality(item,concert_substrings)
            if item.sell_in <= 0:
                if not any(special in lower_name for special in quality_items):  
                    self.decrease_quality(item)
                elif any(concert in lower_name for concert in concert_substrings):
                    item.quality = 0
                item.sell_in -= 1

    def decrease_quality(self, item):
        conjured = "conjured".lower()
        item.quality -= 1 if item.quality > 0 else 0
        item.quality -= 1 if conjured in item.name.lower() and item.quality > 0 else 0
        item.sell_in -= 1 if item.sell_in > 0 else 0

    def increase_quality(self, item, concert_substrings):
        item.quality +=1 if item.quality < 50 else 0
        if any(concert in item.name.lower() for concert in concert_substrings):
            item.quality += 1 if item.sell_in < 11 and item.quality < 50 else 0
            item.quality += 1 if item.sell_in < 6 and item.quality < 50 else 0
        item.sell_in -= 1 if item.sell_in >= 0 else 0

class Item:
    def __init__(self, name, sell_in, quality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
