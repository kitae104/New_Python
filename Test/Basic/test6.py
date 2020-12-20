from sklearn.datasets import fetch_openml
df = fetch_openml(name="titanic")
X_data = df.data
Y_data = df.target
print(Y_data)