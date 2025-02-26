import numpy as np

data = np.array([12, 15, 14, 10, 18, 20, 22, 24, 17, 19])


mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
