"""
Date: 10.16.2024
Author: KL
Description: VaR function
"""
import numpy as np
import matplotlib.pyplot as plt


def VaR(r, alpha):
    # This function returns the left tail value
    # alpha = risk level
    # r = an array of stock returns
    # out = positively stated value of r at the 1-alpha percentile
    percentile_value = np.percentile(r, 100 * (1 - alpha))
    return abs(percentile_value)


# Example
returns = np.random.normal(0, 1, 10000)
print(np.percentile(returns, 97.72))
plt.hist(returns, bins=200, alpha=0.75)
plt.show()
