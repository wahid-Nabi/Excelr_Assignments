# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:54:44 2020

@author: patel
"""

import pandas as pd

import numpy as np 

data=pd.read_csv("C:\\Users\\patel\\Downloads\\Fraud_check (2).csv")
data2=pd.read_csv("C:\\Users\\patel\\Downloads\\Fraud_check (2).csv")

data
colnames=(data2.columns)
colnames
num=data['Taxable.Income']
data['Status']=np.where(num<=30000,'risky','good')
data.head()
data.dtypes


obj_data2=data2.select_dtypes(include=('int64','float64','object'))
#obj_data['Status']=obj_data['Status'].astype('int64')

cleanup_nums2={"Undergrad":{"YES":1,"NO":0},"Marital.Status":{"Single":1,"Married":2,"Divorced":3},"Urban":{"YES":1,"NO":0} }
obj_data2.replace(cleanup_nums2,inplace=True)
data2=obj_data2
obj_data2['Urban']=obj_data2['Urban'].astype('object')
obj_data2['Undergrad']=obj_data2['Undergrad'].astype('object')
obj_data2['Marital.Status']=obj_data2['Marital.Status'].astype('object')

data2


obj_data=data.select_dtypes(include=('int64','float64','object'))

cleanup_nums={"Status":{"good":1,"risky":0}}
obj_data.replace(cleanup_nums,inplace=True)
data=obj_data
obj_data['Status']=obj_data['Status'].astype('object')

data



#defining target and predictors
x=data2
x

y=data.Status
y

#test,train split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
y_train

x_train.shape,x_test.shape
y_train.shape,y_test.shape
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier(criterion="entropy")
model.fit(x_train,y_train)

preds = model.predict(x_train)
preds

# Accuracy = train
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_train, preds))


preds = model.predict(x_test)
preds

# Accuracy = train
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, preds))#....1


#plot
from matplotlib import pyplot as plt

tree.plot_tree(model.fit(x_train,y_train))

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import graphviz
from graphviz import Source
from pydotplus import pydotplus
#dot_data = StringIO()
help(tree.export_graphviz())
dot_data=Source(tree.export_graphviz(model , out_file=None,feature_names=colnames))
graph=graphviz.Source(dot_data)
graph







