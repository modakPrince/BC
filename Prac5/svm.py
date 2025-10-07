import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.inspection import DecisionBoundaryDisplay

# [cite_start]Load dataset (only 2 features for visualization) [cite: 593]
cancer = load_breast_cancer()
X = cancer.data[:, :2] #take first 2 features [cite: 594]
y = cancer.target

# [cite_start]Train-test split [cite: 597]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- SCALING AND GRID SEARCH REMOVED ---

# 1. Create a default SVM model instead of grid searching
# We are manually choosing the parameters instead of finding the best ones.
svm = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)

# 2. Train the model directly on the unscaled data
svm.fit(X_train, y_train)

# --- EVALUATION AND PLOTTING (REMAINS THE SAME) ---

# Make predictions
y_pred = svm.predict(X_test)

# Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# [cite_start]Plot Decision boundary (for 2D features only) [cite: 638]
disp = DecisionBoundaryDisplay.from_estimator(
    svm,
    X_train,
    response_method="predict",
    alpha=0.5,
    cmap="coolwarm", # Changed cmap for better visibility
    xlabel=cancer.feature_names[0],
    ylabel=cancer.feature_names[1],
)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, s=20, edgecolors="k")
plt.title("SVM Decision Boundary (No Scaling or Grid Search)")
plt.show()
