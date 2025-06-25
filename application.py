from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application

ridge_model=pickle.load(open('Models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('Models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        temp=float(request.form.get('Temp'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        new_data_scale=standard_scaler.transform([[temp,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scale)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')
        

if __name__=="__main__":
    application.run(debug=True)
