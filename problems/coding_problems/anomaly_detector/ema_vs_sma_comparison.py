import numpy as np
import matplotlib.pyplot as plt
from solution1_sliding_window_moving_avg import SlidingWindowAnomalyDetector
from solution2_exponential_moving_avg import EMAAnomalyDetector

# Generate a sample dataset
np.random.seed(42)
data = np.linspace(50, 60, 200) + np.random.normal(0, 2, 200)
data[100:120] += 10  # Anomaly

# Parameters
window_size = 10
alpha = 2 / (window_size + 1)
threshold = 60

# Calculate SMA
sma_detector = SlidingWindowAnomalyDetector(window_size=window_size, threshold=threshold)
sma_values = [sma_detector.add(value) and sma_detector.running_sum / len(sma_detector.buffer) for value in data]
# a bit of a hack to get the sma values
for i in range(len(sma_values)):
    if sma_values[i] == False:
        sma_values[i] = sma_detector.running_sum / len(sma_detector.buffer)
        
# Calculate EMA
ema_detector = EMAAnomalyDetector(alpha=alpha, threshold=threshold)
ema_values = [ema_detector.add(value) and ema_detector.ema for value in data]
for i in range(len(ema_values)):
    if ema_values[i] == False:
        ema_values[i] = ema_detector.ema


# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(data, label='Original Data', color='gray', alpha=0.5)
plt.plot(sma_values, label=f'SMA (window={window_size})', color='blue')
plt.plot(ema_values, label=f'EMA (alpha={alpha:.2f})', color='red')
plt.axhline(y=threshold, color='green', linestyle='--', label='Threshold')
plt.title('SMA vs. EMA for Anomaly Detection')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('ema_vs_sma_comparison.png')

print("Generated ema_vs_sma_comparison.png")
