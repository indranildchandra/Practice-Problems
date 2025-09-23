# Question: Imagine you’re building a real-time anomaly detector on sensor data stream (say temperature readings). You want to detect if the average in the last N readings exceeds a threshold. How would you design this system so it works efficiently for millions of events per second?

# Solution: Exact sliding-window (fixed N) — O(1) per update, O(N) memory

from collections import deque
from typing import Deque

class SlidingWindowAnomalyDetector:
    def __init__(self, window_size: int, threshold: float):
        assert window_size > 0
        self.window_size = window_size
        self.threshold = threshold
        self.buffer: Deque[float] = deque()
        self.running_sum = 0.0

    def add(self, value: float) -> bool:
        """
        Add a reading; return True if average over last up-to-N readings > threshold.
        This is exact for the current window.
        """
        self.buffer.append(value)
        self.running_sum += value

        if len(self.buffer) > self.window_size:
            oldest = self.buffer.popleft()
            self.running_sum -= oldest

        avg = self.running_sum / len(self.buffer)
        return avg > self.threshold

# Example
det = SlidingWindowAnomalyDetector(window_size=3, threshold=50.0)
print(det.add(40))  # False
print(det.add(60))  # False (avg 50)
print(det.add(70))  # True  (avg ~56.67)
print(det.add(80))  # True  (avg 70)
