import joblib

#load the model
model=joblib.load('diabetes_79.pkl')
result=model.predict([[1,1,1,1,1,1,1,1]])

if result[0]==1:
    print('diabetes')
else:
    print('not diabetes')