# Question: Imagine you’re building a real-time anomaly detector on sensor data stream (say temperature readings). You want to detect if the average in the last N readings exceeds a threshold. How would you design this system so it works efficiently for millions of events per second?

# Solution: Memory-constant approx: Exponential Moving Average (EMA) — O(1) per update, O(1) memory
# When N is large or you want minimal memory and CPU, use EMA. This is approximate but often acceptable for anomaly detection requiring quick response.
# Refer to ema_vs_sma_comparison.py and ema_vs_sma_comparison.png for more details.

class EMAAnomalyDetector:
    def __init__(self, alpha: float, threshold: float):
        """
        alpha in (0,1] controls memory: higher alpha -> reacts faster to new values.
        Common mapping: alpha = 2/(N+1) approximates window N.
        """
        assert 0 < alpha <= 1.0
        self.alpha = alpha
        self.threshold = threshold
        self.ema = None

    def add(self, value: float) -> bool:
        if self.ema is None:
            self.ema = value
        else:
            # EMA Formula: EMA_t = alpha * x_t + (1 - alpha) * EMA_{t-1}
            # This is a weighted average where recent values are given more weight.
            # It's a good approximation for a sliding window because the influence of old data decays exponentially, similar to how a sliding window drops old data points.
            # The relationship alpha = 2 / (N + 1) is a common heuristic to relate the smoothing factor 'alpha' to a window size 'N'.
            # Refer to ema_vs_sma_comparison.png for more details.
            self.ema = self.alpha * value + (1 - self.alpha) * self.ema
        return self.ema > self.threshold

# Example mapping alpha ~ 2/(N+1)
N = 100
alpha = 2.0 / (N + 1)
det = EMAAnomalyDetector(alpha=alpha, threshold=50.0)
print(det.add(40))
print(det.add(60))
