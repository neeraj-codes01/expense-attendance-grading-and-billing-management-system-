import numpy as np
# simulate the problem gap: apply a 10% increase to many prices
prices=np.array([100,23,200,45,56])
increased_prices=prices*1.1
print("original prices:",prices)
print("after 10% increase:",increased_prices)