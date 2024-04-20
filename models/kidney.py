import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,  precision_score, recall_score, f1_score
from sklearn.model_selection import  RandomizedSearchCV, train_test_split , GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pickle
#To turn off warning messages.
import warnings
warnings.filterwarnings('ignore')

# Importing the dataset 
data = pd.read_csv("kidney_disease.csv")  

data['classification'] = data['classification'].map({'ckd':1,'notckd':0 , 'ckd\t':1})
data['htn'] = data['htn'].map({'yes':1,'no':0})
data['dm'] = data['dm'].map({'yes':1,'no':0})
data['cad'] = data['cad'].map({'yes':1,'no':0})
data['appet'] = data['appet'].map({'good':1,'poor':0})
data['ane'] = data['ane'].map({'yes':1,'no':0})
data['pe'] = data['pe'].map({'yes':1,'no':0})
data['ba'] = data['ba'].map({'present':1,'notpresent':0})
data['pcc'] = data['pcc'].map({'present':1,'notpresent':0})
data['pc'] = data['pc'].map({'abnormal':1,'normal':0})
data['rbc'] = data['rbc'].map({'abnormal':1,'normal':0})


data['age']=data['age'].fillna(data['age'].mean())
data=data.fillna(data.median())
data = data.drop(["pcv","wc","rc","id"], axis = 1)  

n_cols = {'bp':'Blood_Pressure',
            'sg':  'Specific_Gravity','al': 'Albumin','su' : 'Sugar','bgr': 'Blood_Glucose_Random','bu' : 'Blood_Urea' ,
            'sc' : 'Serum_Creatinine','sod' : 'Sodium','pot' : 'Potassium','hemo' : 'Hemoglobin',
            'rbc' : 'Red_Blood_Cells','pc' : 'Pus_Cell','pcc' : 'Pus_Cell_Clumps','ba' : 'Bacteria','htn' : 'Hypertension', 
            'dm' : 'Diabetes_Mellitus','cad' : 'Coronary_Artery_Disease','appet' : 'Appetite','pe' : 'Pedal_Edema',
            'ane' : 'Anemia','classification' : 'Target'}

data.rename(columns=n_cols ,inplace=True)






# Splitting the data  
X = data.drop(["Target"], axis = 1) 
y = data["Target"]


# Splitting the data  
X = X.drop(["age","Red_Blood_Cells","Pus_Cell_Clumps",
               "Serum_Creatinine","Potassium","Coronary_Artery_Disease",
               "Bacteria","Potassium","Coronary_Artery_Disease"], axis = 1) 



#Splitting the data into the training and testing set  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)  


clf = RandomForestClassifier(n_estimators=2, random_state=42)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


cm_rnf = confusion_matrix(y_test, y_pred)
print("Confution matrix for model " f'{clf} : \n',cm_rnf)
ac_rnf = accuracy_score(y_test, y_pred)
print("Accuracy score for model " f'{clf} : ',ac_rnf)
cr_rnf = classification_report(y_test, y_pred)
print("classification_report for model " f'{clf} : \n',cr_rnf)

print(clf.score(X_train,y_train))
print(clf.score(X_test,y_test))

pickle.dump(clf, open('Kmodel.pkl' , 'wb'))

model = pickle.load(open('Kmodel.pkl' , 'rb'))

print(model.predict([[70,1.025,5,5,1,22,2,5,4,1,1,1,1,1]]))
print(model.predict([[80,1.02,0,0,0,93,33,144,13.3,0,0,1,0,0]]))







