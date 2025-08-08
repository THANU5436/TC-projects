from flask import Flask,jsonify,redirect,request
from pymongo import MongoClient
import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
app=Flask(__name__)
client=MongoClient('mongodg')
db=client['MRECWAI']
dat_col=db['cropDta']
metrics_col=db['modelmetrics']
predictions_col=db['predictions']
Collection=db['students']

    0:"crop":"APPLE",     "fertilizer":"UREA"
    1:"crop":"BANANA",    "fertilizer":"UREA"
    2:"crop":"BANANA",    "fertilizer":"UREA"
    3:"crop":"BANANA",    "fertilizer":"UREA"
    4:"crop":"BANANA" ,   "fertilizer":"UREA"
    5:"crop":"BANANA" ,   "fertilizer":"UREA"
    6:"crop":"BANANA",    "fertilizer":"UREA"
    7:"crop":"BANANA",    "fertilizer":"UREA"
    8:"crop":"BANANA",    "fertilizer":"UREA"
    9:"crop":"BANANA",    "fertilizer":"UREA"
    10:"crop":"BANANA",   "fertilizer":"UREA"
    11:"crop":"BANANA",   "fertilizer":"UREA"
    12:"crop":"BANANA",   "fertilizer":"UREA"
    13:"crop":"BANANA",   "fertilizer":"UREA"
    14:"crop":"BANANA",   "fertilizer":"UREA"
    15:"crop":"BANANA",   "fertilizer":"UREA"     
    16:"crop":"BANANA",   "fertilizer":"UREA"
    17:"crop":"BANANA",   "fertilizer":"UREA"
    18:"crop":"BANANA",   "fertilizer":"UREA"
    19:"crop":"BANANA",   "fertilizer":"UREA"
    20:"crop":"BANANA",   "fertilizer":"UREA"
@app.route('/')
def home():
    return jsonify({"message:"}) "welcome to MRECWAI"
@app.route('/getStudents',methods=['POST'])
def get_all_students():
    result=[]
    for stu in Collection.find()