import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,  precision_score, recall_score, f1_score
from sklearn.model_selection import  RandomizedSearchCV, train_test_split , GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import pickle
#To turn off warning messages.
import warnings
warnings.filterwarnings('ignore')


# Importing the dataset 
data = pd.read_csv("diabetes_prediction_dataset.csv")  

data['smoking_history'] = data['smoking_history'].map({'never':0,'current':1,
                                                      'former':2,'ever':3,'not current':4})
data['gender'] = data['gender'].map({'Female':1,'Male':0})

data['smoking_history'] = data['smoking_history'].fillna(1)
data['gender']=data['gender'].fillna(data['gender'].median())

print(f'Good People : {data.diabetes.value_counts()[0]}')
print(f'Infected People : {data.diabetes.value_counts()[1]}')

# Splitting the data  
X = data.drop(["diabetes","smoking_history"], axis = 1)  
y = data["diabetes"] 

 
scale=MinMaxScaler()
scale.fit(X)





  
#Splitting the data into the training and testing set  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

clf_rnf=RandomForestClassifier()
parametrs_rnf={ 
    'n_estimators': [200, 500],
    'max_features': [ 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
grid_forest=GridSearchCV(clf_rnf, parametrs_rnf, cv=6, n_jobs=-1)
grid_forest.fit(X_train,y_train)

best_model_rnf=grid_forest.best_estimator_
y_pred_rnf=best_model_rnf.predict(X_test)

cm_rnf = confusion_matrix(y_test, y_pred_rnf)
print("Confution matrix for model " f'{best_model_rnf} : \n',cm_rnf)
ac_rnf = accuracy_score(y_test, y_pred_rnf)
print("Accuracy score for model " f'{best_model_rnf} : ',ac_rnf)
cr_rnf = classification_report(y_test, y_pred_rnf)
print("classification_report for model " f'{best_model_rnf} : \n',cr_rnf)

print(best_model_rnf.score(X_train,y_train))
print(best_model_rnf.score(X_test,y_test))

pickle.dump(best_model_rnf, open('Dmodel.pkl' , 'wb'))

model = pickle.load(open('Dmodel.pkl' , 'rb'))

print(model.predict([[1,80,0,1,25,6.5,140]]))
print(model.predict([[0,50,1,0,27,5.7,260]]))

