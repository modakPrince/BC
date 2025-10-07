import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dataset = pd.read_csv("hello.csv")
X = dataset[['Argentina','France']].values
y = dataset['Result'].values

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state=67
    )
model = GaussianNB()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)

print("\nConfusion Matrix")
print(confusion_matrix(y_test,y_pred))

print(f"\nClassification Report\n{classification_report(y_test,y_pred)}")
