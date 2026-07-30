import pandas as pd
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv("sample_data.csv")
X=df[["cpu","ram","temp"]]
y=df["health"]
model = DecisionTreeClassifier()
model.fit(X,y)
import pickle
pickle.dump(model,open("model.pkl","wb"))
print("model saved")