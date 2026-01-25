
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Sample dataset (you can replace with CSV later)
data = {
    "Experience": [0, 1, 2, 3, 4, 5],
    "Salary": [10000, 15000, 20000, 25000, 30000, 35000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

# Save model
output_dir = os.path.join(os.path.dirname(__file__), "..",'backend')
os.makedirs(output_dir, exist_ok=True)
model_path = os.path.join(output_dir, "pred_salary_model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained and saved!")