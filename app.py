from flask import Flask,render_template,jsonify,request
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


app = Flask(__name__)

ridge_trail_model = pickle.load(open("models/ridge.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl","rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict_datapoint",methods = ["POST","GET"])
def predictdata():
    if request.method == "POST":
        try:
            data = request.form
            print(data)
            data = dict(data)
            data = {k:[v] for k,v in data.items()}
            data = pd.DataFrame(data)
            # Drop the same features as in training (BUI and DC)
            data = data.drop(['BUI', 'DC'], axis=1, errors='ignore')
            data = scaler.transform(data)
            pred = ridge_trail_model.predict(data)
            result = str(pred[0])
            return render_template("predict.html", result=result)
        except Exception as e:
            return render_template("predict.html", result=f"Error: {str(e)}")
    else:
        return render_template("predict.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",debug = True)