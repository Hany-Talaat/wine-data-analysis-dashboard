import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv('data/Wine_data.csv')


# =========================
# Data Cleaning
# =========================

df['country'] = df['country'].fillna(df['country'].mode()[0])

df['price'] = df['price'].fillna(df['price'].mean())

columns_to_fill = [
    'province',
    'region_1',
    'region_2',
    'taster_name'
]

df[columns_to_fill] = df[columns_to_fill].fillna('Unknown')

df['taster_twitter_handle'] = (
    df['taster_twitter_handle']
    .str.replace('@', '', regex=False)
    .str.strip()
    .fillna('Unknown')
)

df['designation'] = df['designation'].fillna(
    df['designation'].mode()[0]
)

df.dropna(subset=['variety'], inplace=True)


print("Remaining missing values:")
print(df.isnull().sum())


# =========================
# Matplotlib Visualizations
# =========================

top_10 = (
    df.groupby('country')['points']
    .mean()
    .nlargest(10)
)

# Top 10 countries by average score
plt.figure(figsize=(10, 6))

plt.plot(
    top_10.index,
    top_10.values,
    marker='o',
    linewidth=2,
    markersize=8
)

plt.xlabel("Country")
plt.ylabel("Mean Points")
plt.title("Top 10 Countries by Average Wine Score")
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


# Price vs Points
sample = df.sample(50, random_state=42)

plt.figure(figsize=(8, 6))

plt.scatter(
    sample['price'],
    sample['points'],
    marker='*',
    s=30
)

plt.xlabel("Price")
plt.ylabel("Points")
plt.title("Wine Price vs. Points")
plt.tight_layout()
plt.show()


# Bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_10.index,
    top_10.values,
    edgecolor="black"
)

plt.ylim(85, 95)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Country")
plt.ylabel("Average Score")
plt.title("Top 10 Countries by Average Wine Score")
plt.tight_layout()
plt.show()


# Country frequency
country_counts = df['country'].value_counts()

print("\nWine Reviews by Country:")
print(country_counts.head(10))


# =========================
# Spain Analysis
# =========================

spain_df = df[df['country'] == 'Spain']

spain_provinces = (
    spain_df.groupby('province')['points']
    .mean()
)

plt.figure(figsize=(8, 8))

plt.pie(
    spain_provinces.values,
    labels=spain_provinces.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Spain - Province and Average Score")
plt.show()


# =========================
# Canada Analysis
# =========================

canada_df = df[df['country'] == 'Canada']

canada_provinces = (
    canada_df.groupby('province')['price']
    .mean()
)

plt.figure(figsize=(8, 8))

plt.pie(
    canada_provinces.values,
    labels=canada_provinces.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Canada - Province and Average Price")
plt.show()


# =========================
# Italy Analysis
# =========================

italy_df = df[df['country'] == 'Italy']

italy_provinces = (
    italy_df.groupby('province')['price']
    .mean()
)

plt.figure(figsize=(10, 6))

plt.plot(
    italy_provinces.index,
    italy_provinces.values
)

plt.xticks(rotation=45, ha='right')
plt.xlabel("Province")
plt.ylabel("Mean Price")
plt.title("Italy - Province and Average Price")
plt.tight_layout()
plt.show()


# =========================
# Seaborn Analysis
# =========================

top_provinces = (
    df[df['country'] == 'Italy']['province']
    .value_counts()
    .head(4)
    .index
)

df_italy = df[
    (df['country'] == 'Italy') &
    (df['province'].isin(top_provinces))
].dropna(subset=['price'])


# Price distributions
g = sns.FacetGrid(
    df_italy,
    row="province",
    height=1.7,
    aspect=4
)

g.map(
    sns.kdeplot,
    "price",
    fill=True
)

g.set(xlim=(0, 150))
g.set_titles(row_template="{row_name}")
g.fig.subplots_adjust(top=0.9)

g.fig.suptitle(
    "Price Distributions Across Top Italian Wine Provinces"
)

plt.show()


# Price vs Points for selected provinces

last_2_provinces = (
    df[df['country'] == 'Italy']['province']
    .value_counts()
    .tail(2)
    .index
)

df_italy_2 = df[
    (df['country'] == 'Italy') &
    (df['province'].isin(last_2_provinces))
].dropna(
    subset=['price', 'points']
)

g = sns.FacetGrid(
    df_italy_2,
    col="province",
    margin_titles=True,
    height=4,
    aspect=1.2
)

g.map(
    plt.scatter,
    'price',
    'points'
)

for ax in g.axes_dict.values():
    ax.axhline(
        y=90,
        linestyle="--",
        linewidth=1.5
    )

g.set(
    xlim=(0, 200),
    ylim=(80, 100)
)

g.set_axis_labels(
    "Price ($)",
    "Points (Rating)"
)

g.fig.subplots_adjust(top=0.85)

g.fig.suptitle(
    "Italian Wine Price vs. Score"
)

plt.show()
