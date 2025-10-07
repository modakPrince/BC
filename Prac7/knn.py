from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.datasets import load_iris
data = load_iris()
X,y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state = 67)

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test,y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test,y_pred)}")
print(f"Classification Report: \n{classification_report(y_test,y_pred)}")
