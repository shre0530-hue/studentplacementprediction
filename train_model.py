import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Training data
data = {
    "cgpa": [7.5, 8.2, 6.8, 9.0, 7.0, 8.5, 6.5, 7.8, 8.8, 7.2],
    "internships": [1,2,0,3,1,2,0,1,2,1],
    "projects": [2,3,1,4,2,3,1,2,3,2],
    "communication": [7,8,5,9,6,8,5,7,9,6],
    "technical": [7,8,5,9,6,8,5,7,9,6],
    "placed": [1,1,0,1,0,1,0,1,1,0]
}

df = pd.DataFrame(data)

X = df[["cgpa","internships","projects","communication","technical"]]
y = df["placed"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model created successfully")