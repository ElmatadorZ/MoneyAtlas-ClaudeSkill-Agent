# data/market_data_loader.py

import random

class MarketDataLoader:

    def load(self):
        # mock data
        return {
            "price": random.uniform(1800, 2000),
            "volume": random.uniform(1000, 5000)
        }
