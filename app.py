import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
#Load models
h_model = pickle.load(open('model.pkl','rb'))
c_model = pickle.load(open('Cmodel.pkl','rb'))
d_model = pickle.load(open('Dmodel.pkl','rb'))
k_model = pickle.load(open('Kmodel.pkl','rb'))







#Main roots
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/home')
def homee():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/heart') #heart disease
def heart():
    return render_template('heart.html')

@app.route('/c') #for c virus
def c():
    return render_template('C.html')

@app.route('/k') #kideny disease
def k():
    return render_template('kideny.html')

@app.route('/diabetes') #diabetes disease
def diabetes():
    return render_template('diabetes.html')

#Prediction roots 
#----------------------------------------------------HEART
@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    sex = request.form.get('sex')
    #if int(sex)==1:
    #    sex ='Male'
    #else:
     #   sex = 'Female'
    Chest_pain= request.form.get('Chest Pain Type (CP)')
    trestbps = request.form.get('Resting Blood Pressure (trestbps)')
    chol= request.form.get('Serum Cholestoral (chol) mg/dl')
    fbs = request.form.get('Fasting Blood Sugar (fbs) > 120 mg/dl')
    #if int(fbs)==1:
    #    fbs ='Yes'
   # else:
    #    fbs = 'No'
    restecg= request.form.get('Resting Electrocardiographic Results (restecg)')
    thalach = request.form.get('Maximum Heart Rate Achieved (thalach)')
    exang = request.form.get('Exercise Induced Angina (exang)')
    oldpeak = request.form.get('ST depression (oldpeak)')
    slope = request.form.get('Slope of the ST Segment (slope)')
    ca = request.form.get('Number of Major Vessels (ca)')
    thal = request.form.get('Thal')
    
    
    t = [x for x in request.form.values()]
    if t[1] == 'Male':
        t[1]=1
    else:
        t[1] = 0
        
    if t[5] == 'Yes':
        t[5]=1
    else:
        t[5] = 0
        
    if t[8] == 'Yes':
        t[8]=1
    else:
        t[8] = 0
    
    
    
    float_features  = [float(y) for y in t] #load values and handle it
    final_features = [np.array(float_features)]
    prediction = h_model.predict(final_features) #prediction
    #Handle the output
    if prediction == 1:
        output ='You have heart problems \n You should take \n Angiotensin-converting enzyme (ACE) inhibitors and angiotensin II receptor blockers (ARBs) \n the dosage is: 6.25 mg TID, with a max of 450 mg.'
    else:
        output ='Your heart is okay \n You should go Gym , do some kind of sports or even walk an hour every day \n do not forget to eat healthy food \n and stop eating fast food.'
    
    return render_template('heartRes.html',prediction_text="{}".format(output)
                           ,age=age
                           ,sex =sex
                           ,Chest_pain = Chest_pain
                           ,trestbps = trestbps
                           ,chol = chol
                           ,fbs = fbs
                           ,restecg = restecg
                           ,thalach = thalach
                           ,exang = exang
                           ,oldpeak = oldpeak
                           ,slope = slope
                           ,ca = ca
                           ,thal = thal)

#----------------------------------------------------C
@app.route('/cpredict', methods=['POST'])
def cpredict():
    Age = request.form.get('Age')
    Sex = request.form.get('Sex')
    #if int(Sex)==1:
     #   Sex ='Male'
    #else:
      #  Sex = 'Female'
    #ALB = request.form.get('Albumin Blood Test (ALB) g/L')
    ALP = request.form.get('Alkaline Phosphatase Test (ALP) IU/L')
    ALT =  request.form.get('Alanine Transaminase Test (ALT) U/L')
    AST = request.form.get('Aspartate Transaminase Test (AST) U/L')
    BIL = request.form.get('Bilirubin Blood Test (BIL) µmol/L')
    CHE = request.form.get('Cholinesterase (CHE) kU/L')
    CHOL = request.form.get('Cholesterol (CHOL) mmol/L')
    CREA = request.form.get('Creatinine Blod Test (CREA) µmol/L')
    GGT = request.form.get('Gamma-Glutamyl Transpeptidase Test (GGT) U/L')
    PROT = request.form.get('Protein Blood Test (PROT) g/L')
    
    
    
    t = [x for x in request.form.values()]
    if t[1] == 'Male':
        t[1]=1
    else:
        t[1] = 0
    
    float_features  = [float(y) for y in t] #load values and handle it
    final_features = [np.array(float_features)]
    prediction = c_model.predict(final_features) #prediction
    #Handle the output
    if prediction == 1:
        output ='You have Hepatitis C disease \n \n You should take \n SOVALDI \n the dosage is: one tablet everyday at the same time. \n and VIRACURE the dosage is: 3 tablets everyday after each meal'
    else:
        output ='You are good. \n but Steer clear of actions \n that could transmit the infection,\n such as drug injections \n using non-sterile equipment. dont forget to eat healthy food' 
    
    return render_template('cRes.html',prediction_text="{}".format(output)
                           ,Age = Age
                           ,Sex = Sex
                           ,ALP = ALP
                           ,ALT = ALT
                           ,AST = AST
                           ,BIL = BIL
                           ,CHE = CHE
                           ,CHOL = CHOL
                           ,CREA = CREA
                           ,GGT = GGT
                           ,PROT = PROT)

#-----------------------------------------------------DIABETES
@app.route('/diabetesPrediction', methods=['POST'])
def diabetesPrediction():
    gender = request.form.get('gender')
    #if int(gender)==1:
     #   gender ='Male'
    #else:
       # gender = 'Female'
    age = request.form.get('age')
    hypertension = request.form.get('hypertension')
    #if int(hypertension)==1:
     #   hypertension ='Yes'
    #else:
      #  hypertension = 'No' 
    heart_disease  = request.form.get('heart_disease')
    #if int(heart_disease)==1:
     #   heart_disease ='Yes'
    #else:
      #  heart_disease = 'No'
    bmi  = request.form.get('bmi')
    HbA1c_level = request.form.get('HbA1c_level')
    blood_glucose_level = request.form.get('blood_glucose_level')
    
    
    t = [x for x in request.form.values()]
    if t[0] == 'Male':
        t[0]=1
    else:
        t[0] = 0
        
    if t[2] == 'Yes':
        t[2]=1
    else:
        t[2] = 0
        
    if t[3] == 'Yes':
        t[3]=1
    else:
        t[3] = 0
        
    float_features  = [float(y) for y in t] #load values and handle it
    final_features = [np.array(float_features)]
    prediction = d_model.predict(final_features) #prediction
    #Handle the output
    if prediction == 1:
        output ='You have Diabetes \n You should take ANSOLINE \n the dosage is: based on the percentage of sugar in blood. \n You must see a doctor for your safety.'
    else:
        output ='You are good \n You should go to the gym \n to lose weight, you should manage your stress \n do not forget to eat healthy food, \n especially fibre and quit smoking and alcohol.'
    
    return render_template('diabetesRes.html',prediction_text="{}".format(output),
                            age = age
                           ,gender=gender
                           ,hypertension = hypertension
                           ,heart_disease = heart_disease
                           ,bmi = bmi
                           ,HbA1c_level = HbA1c_level
                           ,blood_glucose_level = blood_glucose_level)

#----------------------------------------------------Kideny
@app.route('/kpredict', methods=['POST'])
def kpredict():
    Blood_Pressure = request.form.get('Blood_Pressure')
    Specific_Gravity = request.form.get('Specific_Gravity')
    Albumin = request.form.get('Albumin')
    Sugar = request.form.get('Sugar')
    Pus_Cell = request.form.get('Pus_Cell')
    Blood_Glucose_Random = request.form.get('Blood_Glucose_Random')
    Blood_Urea = request.form.get('Blood_Urea')
    Sodium = request.form.get('Sodium')
    Hemoglobin = request.form.get('Hemoglobin')
    Hypertension = request.form.get('Hypertension')
    #if int(Hypertension)==1:
    #    Hypertension ='Yes'
   # else:
     #   Hypertension = 'No' 
    Diabetes_Mellitus  = request.form.get('Diabetes_Mellitus')
    #if int(Diabetes_Mellitus)==1:
     #   Diabetes_Mellitus ='Yes'
    #else:
     #   Diabetes_Mellitus = 'No'
    Appetite = request.form.get('Appetite')
    #if int(Appetite)==1:
    #    Appetite ='Good'
   # else:
     #   Appetite = 'Poor'
    Pedal_Edema = request.form.get('Pedal_Edema')
    #if int(Pedal_Edema)==1:
    #    Pedal_Edema ='Yes'
   # else:
     #   Pedal_Edema = 'No'
    Anemia = request.form.get('Anemia')
    #if int(Anemia)==1:
     #   Anemia ='Yes'
    #else:
      #  Anemia = 'No' 
    t = [x for x in request.form.values()]
    if t[4] == 'Yes':
        t[4]=1
    else:
        t[4] = 0
        
    if t[9] == 'Yes':
        t[9]=1
    else:
        t[9] = 0
        
    if t[10] == 'Yes':
        t[10]=1
    else:
        t[10] = 0
        
    if t[11] == 'Good':
        t[11]=1
    else:
        t[11] = 0    
        
    if t[12] == 'Yes':
        t[12]=1
    else:
        t[12] = 0    
        
    if t[13] == 'Yes':
        t[13]=1
    else:
        t[13] = 0        
    float_features  = [float(y) for y in t] #load values and handle it
    final_features = [np.array(float_features)]
    prediction = k_model.predict(final_features) #prediction
    #Handle the output
    if prediction == 1:
        output ='You have Kideny \n \n You should do dialysis treatment to replicate some of the kidney functions, which may be necessary in stage 5.                                  '
    else:
        output ='You are good \n You should change your lifestyle to help you stay as healthy as possible \n do not forget to eat healthy food.'
    
    return render_template('kRes.html',prediction_text="{}".format(output),
                            Blood_Pressure = Blood_Pressure
                           ,Specific_Gravity=Specific_Gravity
                           ,Albumin = Albumin
                           ,Sugar = Sugar
                           ,Pus_Cell = Pus_Cell
                           ,Blood_Glucose_Random = Blood_Glucose_Random
                           ,Blood_Urea = Blood_Urea
                           ,Sodium = Sodium
                           ,Hemoglobin = Hemoglobin
                           ,Hypertension = Hypertension
                           ,Diabetes_Mellitus = Diabetes_Mellitus
                           ,Appetite = Appetite
                           ,Pedal_Edema = Pedal_Edema
                           ,Anemia = Anemia)






#run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)