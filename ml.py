import pandas as pd
import numpy as np

# ML modelleri
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Veri okuma

df = pd.read_csv(r"C:\Users\kerem\Downloads\movies_with_revenue.csv")
df.head()
# Kolon seçme
df = df[["budget", "gross", "rating", "numVotes", "year"]]

# Temizlik
df = df[(df["budget"] > 0) & (df["gross"] > 0) & (df["numVotes"] > 0)]

# LOG dönüşümleri
df["log_budget"] = np.log(df["budget"])
df["log_gross"] = np.log(df["gross"])
df["log_votes"] = np.log(df["numVotes"])

# Tahmin etmek
X = df[["log_budget", "rating", "log_votes", "year"]]
y = df["log_gross"]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

print("Linear Regression R2:", r2_score(y_test, y_pred_lr))
print("Linear Regression RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lr)))

# Non-linear

rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest R2:", r2_score(y_test, y_pred_rf))
print("Random Forest RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf)))


# Hangisi daha önemli
importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print(importance)