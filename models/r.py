import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))



@app.route('/')
def home():
    return render_template('main.html')

@app.route('/home')
def homee():
    return render_template('main.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/c')
def c():
    return render_template('C.html')

@app.route('/predict', methods=['POST'])
def predict():
    float_features  = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction == 1:
        output ='You have heart problems \n \n You should take \n Angiotensin-converting enzyme (ACE) inhibitors \n and angiotensin II receptor blockers (ARBs) \n and the dosage is: 6.25 mg TID, with a maximum of 450 mg. \n or ask for a replacement \n if it does not exist'
    else:
        output ='Your heart is okay \n You should go Gym , do some kind of sports or even walk an hour every day \n do not forget to eat healthy food \n and stop eating fast food.'
    
    return render_template('res.html',prediction_text="{}".format(output))





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)