from modules.Config_db import * 
from passlib.hash import sha256_crypt
from bson.objectid import ObjectId
import os
import math
import random
import smtplib

def getCredentialByUsername(username):
    cred = db.Credentials.find_one({
        "username": username
        })
    return cred

def verifyPass(user_pwd,cred_pwd):
    return sha256_crypt.verify(user_pwd,cred_pwd)


def getCredentialByEmployeeID(empID):
    cred = db.Credentials.find_one({
        "employeeID": ObjectId(empID)
        })
    return cred

def verifyEmail(email):
    record = db.Employees.find_one({
        "email" : email
    })
    if(record!=None):
        return record
    return None

def set_OTP():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP for password reset."
    msg= otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("excoticly.positive@gmail.com", "xtvy wiyt ysck yqld")
    return s,msg,OTP