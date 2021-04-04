import joblib
import numpy as np
import logging

from flask import Flask
from flask import jsonify


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def homepage():
    return """
    <h1>Machine Learning Model</h1>
    <p>Bryam David Vega Moreno</p>
    """

@app.route('/predict',methods=['GET'])
def predict():
    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    predict = model.predict(X_test.reshape(1,-1))
    return jsonify({'predict': list(predict)})

if __name__ == '__main__':

    model = joblib.load('./models/best_model.pkl')
    app.run(debug=True, use_reloader=True)