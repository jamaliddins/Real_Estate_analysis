import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('main_Listings.csv')

"""Hypothesis H1.1: Rental listings have a more right-skewed price distribution than sell listings, 
    driven by luxury furnished apartments pulling the mean up."""
# Step 1: Split into two groups
rental_cats = [1, 4, 5, 8, 11, 13, 14, 15, 16, 17, 18, 19, 21, 23]
df['listing_type'] = df['category'].apply(
    lambda x: 'Rental' if x in rental_cats else 'Sell'
)

rental_prices = df[df['listing_type'] == 'Rental']['price'].dropna()
sell_prices = df[df['listing_type'] == 'Sell']['price'].dropna()

# Step 2: Measure skewness
rental_skew = stats.skew(rental_prices)
sell_skew = stats.skew(sell_prices)

print(f"Rental skewness: {rental_skew:.2f}")
print(f"Sell skewness:   {sell_skew:.2f}")

# Step 3: Test if skewness is statistically significant
_, p_rental = stats.skewtest(rental_prices)
_, p_sell = stats.skewtest(sell_prices)

print(f"\nRental skew p-value: {p_rental:.4f}")
print(f"\nSell skew p-value: {p_sell:.4f}")

# Step 4: Conclusion
if rental_skew > sell_skew and p_rental < 0.05:
    print("\n✅ Hypothesis SUPPORTED")
else:
    print("\n❌ Hypothesis NOT supported")

# Step 5: Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(rental_prices.clip(upper=rental_prices.quantile(0.95)),
             bins=50, color='steelblue', edgecolor='white')
axes[0].set_title(f'Rental Prices  (skew = {rental_skew:.2f})')
axes[0].set_xlabel('Price (SAR)')

axes[1].hist(sell_prices.clip(upper=sell_prices.quantile(0.95)),
             bins=50, color='coral', edgecolor='white')
axes[1].set_title(f'Sell Prices  (skew = {sell_skew:.2f})')
axes[1].set_xlabel('Price (SAR)')

plt.tight_layout()
plt.savefig('h1_1_skewness.png', dpi=150)
plt.show()