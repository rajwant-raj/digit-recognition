import gradio as gr
import numpy as np
import keras 
import matplotlib.pyplot as plt

model = keras.models.load_model("my_keras_model.h5")


def predict_digit(index):
    img_flat = X_test[index]
    img = img_flat.reshape(28, 28)

    input_data = np.expand_dims(img_flat, axis=0)

    prediction_probabilities = model.predict(input_data)
    prediction = np.argmax(prediction_probabilities)

    fig, ax = plt.subplots()
    ax.imshow(img, cmap='gray')
    ax.axis('off')
    ax.set_title(f"Predicted: {prediction}")

    return fig, f"✅ Predicted Digit: {prediction}"

demo = gr.Interface(
    fn=predict_digit,
    inputs=gr.Slider(0, len(X_test)-1, step=1, label="Select MNIST Test Image Index"),
    outputs=["plot", "text"],
    title="🧠 Handwritten Digit Recognition (Gradio)",
    description="Use the slider to select an image from the MNIST test dataset and predict the digit using a trained ML model."
)

if __name__ == "__main__":
    demo.launch()