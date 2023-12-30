# File: Student.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date: 10/8/2023
# Description of Program: Creates Student objects that contain name and grades for exam 1 and 2. Has functions to get (name and exam scores) and set (only exam scores) as well as calculate the average.

class Student:
    def __init__(self, name, exam1=None, exam2=None):
        """ Construct a Student object with name and exam scores"""
        self.__name=name
        self.__exam1=exam1
        self.__exam2=exam2
        
    def __str__(self):
        return "Student: "+ str(self.__name) + "\n  Exam1: "+ str(self.__exam1) + "\n  Exam2: "+ str(self.__exam2)

    def getName(self):
        return self.__name
    
    def getExam1Grade(self):
        return self.__exam1
    
    def getExam2Grade(self):
        return self.__exam2

    def setExam1Grade(self, exam1):
        self.__exam1=exam1
    
    def setExam2Grade(self, exam2):
        self.__exam2=exam2

    def getAverage(self):
        if(self.__exam1==None):
           print("Some exam grades not available.")
        elif(self.__exam2==None):
           print("Some exam grades not available.")
        elif(self.__exam1!=None and self.__exam2!=None):
            print((self.__exam1+self.__exam2)/2)
    
