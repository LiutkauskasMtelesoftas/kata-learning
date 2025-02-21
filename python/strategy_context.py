from handlers.aged_brie import AgedBrieUpdateStrategy
from handlers.sulfuras import SulfurasUpdateStrategy
from handlers.backstage_passes import BackstagePassesUpdateStrategy
from handlers.conjured_item import ConjuredUpdateStrategy
from handlers.normal_item import NormalItemUpdateStrategy

class StrategyContext:
    def get_strategy(self, item) -> object:
        concert_substrings = ["concert", "backstage", "pass"]
        item_name = item.name.lower()
        if "brie" in item_name:
            return AgedBrieUpdateStrategy()
        elif "sulfuras" in item_name:
            return SulfurasUpdateStrategy()
        elif any(concert in item_name for concert in concert_substrings):
            return BackstagePassesUpdateStrategy()
        elif "conjured" in item_name:
            return  ConjuredUpdateStrategy()
        else:
            return NormalItemUpdateStrategy()
