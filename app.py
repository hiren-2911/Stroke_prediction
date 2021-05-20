from flask import Flask,render_template,request
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

def valpredict(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,10)
    loaded_model=pickle.load(open('E:/python/web_flask/Stroke_pickle.pkl','rb'))
    result=loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods=["POST"])
def result():
    if request.method=="POST":
        to_predict_list=request.form 
        print(to_predict_list)
        to_predict_list=list(to_predict_list.values())
        to_predict_list=list(map(int,to_predict_list))
        print(to_predict_list)
        result=valpredict(to_predict_list)
        if int(result)==1:
            prediction="The person might get stroke"
        else:
            prediction="The person is stroke free"
    return render_template("result.html",prediction=prediction)

if __name__=="__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AND_RELOAD"]==True

