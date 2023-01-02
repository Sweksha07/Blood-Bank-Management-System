import pymysql
from flask import Flask ,redirect ,render_template ,request ,url_for
db_connection=None
db_cursor=None
app = Flask(__name__)
from db import*

def db_connect():
    global db_connection,db_cursor
    try:
        db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="blood_bank_management_system",port=3307)
        print("Connected")
        db_cursor=db_connection.cursor()
        return True
    
    except:
        print("some error occurs,can't connect to database")
        return False
def db_disconnect():
    global db_connection,db_cursor
    db_connection.close()
    db_cursor.close()
def getAllPatients():
    isConnected = db_connect()
    if(isConnected):
        print("yes connected")
        getQuery = "select * from Patients;"  #writting query
        db_cursor.execute(getQuery)           #executing query
        allData = db_cursor.fetchall()        #fetching data from query
        print(allData)
        db_disconnect()
        return allData

@app.route("/")
def index():
    #return "Hello Python"
    db_connect()
    allData = getAllPatients()
    return render_template("index.html",data=allData)



@app.route("/add",methods=["GET","POST"])
def addPatient():  
    if request.method == "POST":
        data = request.form
        isInserted = insertPatients(data["Name"],data["Contact_no"],data["Age"],data["Blood_Grp"],data["Current_Disease"])
        if(isInserted):
            return redirect(url_for("index"))
    return render_template("add.html")




@app.route("/update",methods=["GET","POST"])
def update():
    id=request.args.get("ID",type=int,default=1)
    print(id)
    actual_data = getPatientsById(id)   
    #print(actual_data)
    
    if request.method=="POST":
        data=request.form
        print("data----->",data)
        isUpdated=updatePatients(data["Name"],data["Contact_no"],data["Age"],data["Blood_Grp"],data["Current_Disease"],id ) 
        if(isUpdated): 
            return redirect(url_for("index")) 
    return render_template("update.html",data=actual_data)  

@app.route("/delete")
def delete():
    id=request.args.get("ID",type=int,default=1)
    isDeleted=deletePatient(id) 
    if(isDeleted): 
        return redirect(url_for("index")) 
    return render_template("index.html")  



if __name__=="__main__":
    app.run(debug=True)