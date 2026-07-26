from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model only once
model = joblib.load("model/house_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    stories = int(request.form["stories"])
    mainroad = int(request.form["mainroad"])
    guestroom = int(request.form["guestroom"])
    basement = int(request.form["basement"])
    hotwaterheating = int(request.form["hotwaterheating"])
    airconditioning = int(request.form["airconditioning"])
    parking = int(request.form["parking"])
    prefarea = int(request.form["prefarea"])
    furnishingstatus = int(request.form["furnishingstatus"])

    data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "stories":[stories],
        "mainroad":[mainroad],
        "guestroom":[guestroom],
        "basement":[basement],
        "hotwaterheating":[hotwaterheating],
        "airconditioning":[airconditioning],
        "parking":[parking],
        "prefarea":[prefarea],
        "furnishingstatus":[furnishingstatus]
    })

    prediction = model.predict(data)

    predicted_price = round(prediction[0],2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price : ₹ {predicted_price:,.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)