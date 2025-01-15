import numpy as np
import matplotlib.pyplot as plt

scores = [88, 92, 76, 85, 90, 91, 95, 89, 77, 84, 86, 79, 94, 81, 80]

mean = np.mean(scores)
median = np.median(scores)
std_dev = np.std(scores)

print(f"평균 (Mean): {mean}")
print(f"중앙값 (Median): {median}")
print(f"표준편차 (Standard Deviation): {std_dev}")

plt.hist(scores, bins = 5, color='skyblue', edgecolor = 'black')
plt.title('시험 점수 분포 (Histogram)')
plt.xlabel('점수 구간')
plt.ylabel('학생 수')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'평균: {mean}')
plt.legend()
plt.show()