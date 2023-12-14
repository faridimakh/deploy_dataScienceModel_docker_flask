import joblib
import numpy as np
import torch
from flask import Flask, render_template, request
from maclass import QualityPredictor
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form.get('var_1'))
        print(request.form.get('var_2'))
        print(request.form.get('var_3'))
        print(request.form.get('var_4'))
        print(request.form.get('var_5'))
        print(request.form.get('var_6'))
        print(request.form.get('var_7'))
        print(request.form.get('var_8'))
        try:
            var_1 = float(request.form['var_1'])
            var_2 = float(request.form['var_2'])
            var_3 = float(request.form['var_3'])
            var_4 = float(request.form['var_4'])
            var_5 = float(request.form['var_5'])
            var_6 = float(request.form['var_6'])
            var_7 = float(request.form['var_7'])
            var_8 = float(request.form['var_8'])
            pred_args = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8]
            # ----------------------------------------------------------------------------------------------------------
            # Load the model
            model = open('model.pkl', 'rb')
            lr_model = joblib.load(model)
            input_tensor = torch.from_numpy(np.array([pred_args], dtype=np.float32))

            with torch.no_grad():
                model_prediction = round(float(lr_model(input_tensor)), 3)
            # ----------------------------------------------------------------------------------------------------------
            # model_prediction = round(float(3.2544), 3)


        except ValueError:
            return "Please Enter valid values"
    return render_template('predict.html', prediction=model_prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
