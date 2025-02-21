from handlers.aged_brie import AgedBrieUpdateStrategy
from handlers.sulfuras import SulfurasUpdateStrategy
from handlers.backstage_passes import BackstagePassesUpdateStrategy
from handlers.conjured_item import ConjuredUpdateStrategy
from handlers.normal_item import NormalItemUpdateStrategy

class StrategyContext:
    def get_strategy(self, item) -> object:
        concert_substrings = ["concert", "backstage", "pass"]
        if "brie" in item.name.lower():
            return AgedBrieUpdateStrategy()
        elif "sulfuras" in item.name.lower():
            return SulfurasUpdateStrategy()
        elif any(concert in item.name.lower() for concert in concert_substrings):
            return BackstagePassesUpdateStrategy()
        elif "conjured" in item.name.lower():
            return  ConjuredUpdateStrategy()
        else:
            return NormalItemUpdateStrategy()
