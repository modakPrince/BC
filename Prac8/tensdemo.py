import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1) # Reshape for the encoder

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the feature data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# One-hot encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)

# Define the model architecture
model = tf.keras.models.Sequential([
    # Input layer with 4 features (sepal length/width, petal length/width)
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    
    # Hidden layer
    tf.keras.layers.Dense(10, activation='relu'),
    
    # Output layer with 3 units (for 3 iris species) and softmax activation
    tf.keras.layers.Dense(3, activation='softmax')
])

# Display the model summary
model.summary()

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train,
                    epochs=50,
                    batch_size=5,
                    validation_data=(X_test, y_test),
                    verbose=1) # Set verbose=0 to hide epoch logs

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'\nTest Accuracy: {accuracy*100:.2f}%')
