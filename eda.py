import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("movies_with_revenue.csv")

# Dataseti okuma
df.head()
df.info()
df.isna().sum()
df.describe()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["gross"].dropna(), bins=40)
plt.xlabel("Revenue (Gross)")
plt.ylabel("Film sayısı")
plt.title("Revenue dağılımı")
plt.show()
# Budget dağılımı
plt.figure(figsize=(8,5))
plt.hist(df["budget"].dropna(), bins=40)
plt.xlabel("Budget")
plt.ylabel("Film sayısı")
plt.title("Budget dağılımı")
plt.show()

# Budget ve revenue arasındaki ilişki
plt.figure(figsize=(8,6))
plt.scatter(df["budget"], df["gross"], alpha=0.3)
plt.xlabel("Budget")
plt.ylabel("Revenue (Gross)")
plt.title("Budget vs Revenue")
plt.show()

# Log dönüşümü sonrası budget ve revenue ilişkisi
plt.figure(figsize=(8,6))
plt.scatter(np.log1p(df["budget"]), np.log1p(df["gross"]), alpha=0.3)
plt.xlabel("log(Budget)")
plt.ylabel("log(Revenue)")
plt.title("Log-Budget vs Log-Revenue")
plt.show()
# IMDb rating ile revenue arasındaki ilişki
plt.figure(figsize=(8,6))
plt.scatter(df["rating"], df["gross"], alpha=0.3)
plt.xlabel("IMDb Rating")
plt.ylabel("Revenue")
plt.title("Rating vs Revenue")
plt.show()

# IMDb vote count ile revenue arasındaki ilişki
plt.figure(figsize=(8,6))
plt.scatter(df["votes"], df["gross"], alpha=0.3)
plt.xscale("log")
plt.xlabel("Votes (log scale)")
plt.ylabel("Revenue")
plt.title("Votes vs Revenue")
plt.show()

# Filmlerin çıkış yılına göre revenue dağılımı
plt.figure(figsize=(10,5))
plt.scatter(df["year"], df["gross"], alpha=0.4)
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.title("Revenue by Release Year")
plt.show()

# Sayısal değişkenler arasındaki korelasyon matrisi
plt.figure(figsize=(7,5))
corr = df[["budget","gross","rating","votes","runtime"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Numerik Değişkenler Arası Korelasyon")
plt.show()