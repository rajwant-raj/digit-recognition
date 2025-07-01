# 🧠 Digit Recognition using ML

This project is a simple machine learning app that recognizes handwritten digits (0–9) from images using the MNIST dataset. The trained model is deployed via both **Streamlit** and **Gradio** interfaces.

---

## 📌 Project Features

- ✔️ Train a model using `LogisticRegression` on MNIST digits
- ✔️ Save & reuse the trained model with `joblib`
- ✔️ Visualize predictions using:
  - 🟢 Streamlit Web App
  - 🔵 Gradio Interface
- ✔️ Interactive HTML + JS mockup for UI
- ✔️ Clean folder structure + Colab notebook

---

## 🛠️ Tech Stack

| Tool        | Use                          |
|-------------|-------------------------------|
| Python      | Core language                 |
| Scikit-learn| ML model & dataset            |
| Matplotlib  | Plots and visualizations      |
| Streamlit   | ML web app frontend           |
| Gradio      | Alternate ML frontend         |
| HTML/CSS/JS | Mock UI for frontend design   |

---

## 📁 Folder Structure

digit-recognition/
│ ├── my_keras_model.h5 # Trained ML model
│ └── gradio_app.py # Gradio UI app
├── Digit_Recognition_Colab.ipynb # Training notebook
├── requirements.txt
├── README.md


---

## 📈 Model Accuracy

| Metric         | Value     |
|----------------|-----------|
| Accuracy       | ~96%      |
| Algorithm Used | Logistic Regression |

---

## 🚀 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/digit-recognition.git
cd digit-recognition
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🎯 Running the Apps
▶️ Streamlit App
bash
Copy
Edit
cd backend
streamlit run streamlit_app.py
▶️ Gradio App
bash
Copy
Edit
cd backend
python gradio_app.py
🔮 Screenshots (Optional)
You can add screenshots here after running the app:

scss
Copy
Edit
📸 ![gradio-app](![Screenshot 2025-07-01 201139](https://github.com/user-attachments/assets/96ccfb58-104e-497b-89ec-a486ec5ca332)
g)
📚 Credits
scikit-learn.org
scalezix
Gradio

Streamlit

Handwritten Digits Dataset: load_digits() from sklearn.datasets
source data from kaggle
