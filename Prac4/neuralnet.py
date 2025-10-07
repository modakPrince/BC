import numpy as np
import tensorflow as tf

# 1. The same XOR dataset is used [cite: 503, 504]
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

# 2. Define the model using Keras Sequential API
# This replaces the entire manual NeuralNetwork class [cite: 469]
model = tf.keras.Sequential([
    # Hidden layer with 4 neurons, same as the original hidden_size [cite: 506]
    tf.keras.layers.Dense(4, activation='relu', input_shape=(2,)),
    
    # Output layer with 1 neuron for binary classification
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 3. Compile the model
# This step sets up the training process, replacing the manual 'backward' method [cite: 481]
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 4. Train the model
# The .fit() method handles the entire training loop over epochs [cite: 487]
model.fit(X_train, y_train, epochs=1000) # verbose=0 hides training progress

# 5. Test the trained network
print("Testing trained network:")
predictions = model.predict(X_train)

for inputs, prediction in zip(X_train, predictions):
    # Round the prediction to get a clear 0 or 1
    predicted_class = prediction.round()
    print(f"Input: {inputs}, Predicted Output: {predicted_class[0]}")
