import sys
sys.path.append('Strategies')

from .brie import AgedBrieUpdateStrategy
from .sulfuras import SulfurasUpdateStrategy
from .backstage_passes import BackstagePassesUpdateStrategy
from .conjured import ConjuredUpdateStrategy
from .normal import NormalItemUpdateStrategy

class StrategyContext:
    def get_strategy(self, item):
        concert_substrings = ["concert", "backstage", "pass"]
        if "brie" in item.name.lower():
            brie = AgedBrieUpdateStrategy()
            return brie
        elif "sulfuras" in item.name.lower():
            sulfuras = SulfurasUpdateStrategy()
            return sulfuras
        elif any(concert in item.name.lower() for concert in concert_substrings):
            concert = BackstagePassesUpdateStrategy()
            return concert
        elif "conjured" in item.name.lower():
            conjured = ConjuredUpdateStrategy()
            return conjured
        else:
            normal = NormalItemUpdateStrategy()
            return normal
