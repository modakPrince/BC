import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

# Sample DataSet
X,y = load_wine(return_X_y = True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 67)

model = DecisionTreeClassifier(criterion = 'entropy', random_state = 67)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy}")

plt.figure(figsize = (12,8))
plot_tree(
    model,
    class_names = ['class_0','class_1','class_2'],
    filled = True,
    rounded = True
    )
plt.title("Decision tree - Wine")
plt.show();

