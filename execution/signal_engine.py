from dataclasses import dataclass
from typing import Optional

@dataclass
class TradeSignal:
    symbol: str
    direction: str   # "long" / "short"
    entry: float
    stop_loss: float
    take_profit: float
    confidence: float

class SignalEngine:

    def generate_signal(self, layer_map) -> Optional[TradeSignal]:

        # ใช้ Layer 2-3 เป็น Entry Zone
        layer2 = layer_map.layers[1]
        layer3 = layer_map.layers[2]

        if layer2.state == "accumulating" and layer2.confidence > 0.6:

            entry = (layer2.price_low + layer2.price_high) / 2
            sl = layer2.price_low * 0.98
            tp = layer3.price_high

            return TradeSignal(
                symbol=layer_map.symbol,
                direction="long",
                entry=entry,
                stop_loss=sl,
                take_profit=tp,
                confidence=layer2.confidence
            )

        return None
