# ai_model/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from ai_model.recommendation_model import RecommendationModel

def train_model(user_podcast_data, num_users, num_podcasts, embedding_dim):
    # Split data into training and testing sets
    train_data, test_data = train_test_split(user_podcast_data, test_size=0.2, random_state=42)

    # Create the recommendation model
    model = RecommendationModel(num_users, num_podcasts, embedding_dim)

    # Compile the model
    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_data, epochs=10, batch_size=32, validation_data=test_data)

    # Evaluate the model
    loss, accuracy = model.evaluate(test_data)
    print(f'Test loss: {loss:.3f}, Test accuracy: {accuracy:.3f}')

    # Save the model
    model.save('recommendation_model.h5')
