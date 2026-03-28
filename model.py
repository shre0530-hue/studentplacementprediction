import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Training data

data = {
    'cgpa':[7.5,6.2,8.1,5.4,7.8,6.9,8.5,5.9,7.0,8.2],
    'skills':[8,5,9,4,7,6,9,4,7,9],
    'projects':[3,2,4,1,3,2,4,1,3,4],
    'internship':[1,0,1,0,1,0,1,0,1,1],
    'placed':[1,0,1,0,1,0,1,0,1,1]
}


df = pd.DataFrame(data)

X = df[['cgpa','skills','projects','internship']]
y = df['placed']

model = LogisticRegression()
model.fit(X,y)

pickle.dump(model, open('model.pkl','wb'))

print("Model trained successfully")