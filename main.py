from flask import Flask,render_template, request, redirect,session
import os
from flask_pymongo import PyMongo  
from bson.objectid import ObjectId 

app=Flask(__name__)
app.secret_key=os.urandom(24)
app.config["MONGO_URI"] = "mongodb+srv://anuraksha:anuraksha@cluster0.se0lm.mongodb.net/Incident?retryWrites=true&w=majority"
mongo = PyMongo(app) 
incident_registrations = mongo.db.incident_registrations

@app.route('/')
def dashboard():
    incident=incident_registrations.find()
    return render_template('dashboard.html',incident=incident)
   

@app.route('/register_complaint')
def register_complaint():
    return render_template('register_complaint.html')

@app.route('/incident_registration', methods=['POST','GET'])
def incident_registration():
    
    cname=request.form.get('cname')
    
    cemail=request.form.get('cemail')
    
    description=request.form.get('description')
    
    res={
        'cname':cname, 
        'cemail':cemail,
        'description':description
    }
    incident_registrations.insert_one(res)
   
    return redirect('/')
    
@app.route('/contactus')
def contactus():
    
    return render_template('contactus.html')
    
@app.route('/helpline')
def helpline():
    
    return render_template('helpline.html')
    

@app.route('/view/<incident_id>')
def view(incident_id):
    
    incident = incident_registrations.find_one({'_id' : ObjectId(incident_id)}) 
    return render_template('view.html', incident=incident)
    

    
if __name__=="__main__":
    app.run(debug=True)

