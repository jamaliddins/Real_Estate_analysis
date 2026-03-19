import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('main_Listings2.csv')

# Configure cities to major and minor
major_cities = ['الرياض', 'جدة']
min_listings = 30

"""Hypothesis H1.2: Price distributions in Riyadh and Jeddah are significantly wider (higher IQR) 
   than in smaller cities, reflecting more market segmentation."""
# Step 1: IQR per city individually
def iqr(series):
    return series.quantile(0.75) - series.quantile(0.25)

city_stats = df.groupby('city')['price'].agg(
    count='count',
    median='median',
    IQR=iqr
).reset_index()

# Filter out tiny cities
city_stats = city_stats[city_stats['count'] >= min_listings]
city_stats['city_type'] = city_stats['city'].apply(
    lambda x: 'Major' if x in major_cities else 'Small'
)
city_stats = city_stats.sort_values('IQR', ascending=False)

#print("IQR per city (top 15):")
#print(city_stats[['city', 'city_type', 'median', 'IQR', 'count']].head(15).to_string(index=False))

# Step 2: Check if major cities rank at the top
top_cities = city_stats.head(5)['city'].tolist()
major_in_top = [c for c in major_cities if c in top_cities]
print(f"\nMajor cities in top 5 widest IQ: {major_in_top}")

# Step 3: Levene's test - comparing SPREAD between major vs small cities
major_prices = df[df['city'].isin(major_cities)]['price'].dropna()
small_cities = city_stats[city_stats['city_type'] == 'Small']['city'].tolist()
small_prices = df[df['city'].isin(small_cities)]['price'].dropna()

stat, p = stats.levene(major_prices, small_prices)

print(f"\nMajor cities IQR : SAR {iqr(major_prices):,.0f}")
print(f"Small cities IQR : SAR {iqr(small_prices):,.0f}")
print(f"\nLevene's test - stat={stat:.2f}, p={p:.4f}")
print(f"Spread significantly wider in major cities: {'YES ✅' if p < 0.05 else 'NO ❌'}")

# Step 4: Visualize — boxplot per city, sorted by IQR
top10_cities = city_stats.head(10)['city'].tolist()
plot_data = [
    df[df['city'] == city]['price'].clip(
        upper=df[df['city'] == city]['price'].quantile(0.95)
    ).dropna()
    for city in top10_cities
]

colors = ['coral' if c in major_cities else 'steelblue' for c in top10_cities]

fig, ax = plt.subplots(figsize=(13, 6))
bp = ax.boxplot(plot_data, labels=top10_cities, patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_ylabel('Price (SAR)')
ax.set_title("Price Spread by City  —  Red = Major cities  (Levene p={:.4f})".format(p))
ax.tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.show()
