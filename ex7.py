import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num_throws = 10_000_000

dice_rolls_1 = np.random.randint(1, 7, size=num_throws)
dice_rolls_2 = np.random.randint(1, 7, size=num_throws)

sums = dice_rolls_1 + dice_rolls_2

sums_freq = np.bincount(sums)[2:]

probabilities = sums_freq / num_throws * 100

results_df = pd.DataFrame({
    "Сума": range(2, 13),
    "Ймовірність (%)": probabilities
})

plt.figure(figsize=(10, 6))
plt.bar(results_df["Сума"], results_df["Ймовірність (%)"], color='skyblue')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірність суми при киданні двох кубиків')
plt.grid(axis='y')

plt.show()
print(results_df)

#     Сума  Ймовірність (%)
# 0      2          2.76449
# 1      3          5.55408
# 2      4          8.33739
# 3      5         11.13127
# 4      6         13.89472
# 5      7         16.67626
# 6      8         13.88610
# 7      9         11.09805
# 8     10          8.33327
# 9     11          5.55466
# 10    12          2.76971
