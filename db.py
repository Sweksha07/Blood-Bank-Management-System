import pymysql
from flask import Flask, redirect,render_template,request, url_for
db_connection=None
db_cursor=None
app = Flask(__name__)
from db import *



def db_connect():
    global db_connection,db_cursor
    try:
            db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="blood_bank_management_system",port=3307)
            print("Connected")
            db_cursor=db_connection.cursor()
            return True
    except:
        print("some error occure, cant connect to database")
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
        #print(allData)
        db_disconnect()
        return allData

def insertPatients(Name,Contact_no,Age,Blood_Grp,Current_Disease):
    isConnected = db_connect()
    if(isConnected):
        insertQuery = "insert into Patients(Name,Contact_no,Age,Blood_Grp,Current_Disease) values (%s,%s,%s,%s,%s);"  #writting query
        db_cursor.execute(insertQuery,(Name,Contact_no,Age,Blood_Grp,Current_Disease)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

def getPatientsById(Id):
    isConnected = db_connect()
    if(isConnected):
        selectQuery = "select * from Patients where Id=%s;"  #writting query
        db_cursor.execute(selectQuery,(Id)) #executing query
        current_Patient=db_cursor.fetchone()
        db_connection.commit()
        db_disconnect()
        return current_Patient
    else:
        return False

def updatePatients(Id,Name,Contact_no,Age,Blood_Grp,Current_Disease):
    isConnected = db_connect()
    if(isConnected):
        updateQuery = "update Patients set Name=%s,Contact_no=%s,Age=%s,Blood_Grp=%s,Current_Disease=%s where Id=%s;"  #writting query
        db_cursor.execute(updateQuery,(Id,Name,Contact_no,Age,Blood_Grp,Current_Disease)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False


def deletePatient(Id):
    isConnected = db_connect()
    if(isConnected):
        deleteQuery = "delete from Patients where Id=%s ;"  #writting query
        db_cursor.execute(deleteQuery,(Id)) #executing query
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

