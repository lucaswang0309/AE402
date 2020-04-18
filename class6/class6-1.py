# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:05:27 2020

@author: lucas
"""

class Human:
    def __init__(self ,height ,weight):
        self.height = height
        self.weight = weight
        
    def BMI(self):
        bmi =  self.weight / (self.height*0.01)**2 
        print(bmi)
Human1 = Human(175,65)
Human1.BMI()
        