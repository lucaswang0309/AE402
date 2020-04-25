# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:39:53 2020

@author: lucas
"""

class Animal:
    def __init__(self,HP):
        self.HP = HP
    
    def hurt(self,damage):
        self.HP -= damage 
        print("剩餘血量" + str(self.HP))
        
class Dog(Animal):
    def __init__(self,HP):
        super().__init__(HP)
    
    def roar(self):
        print(" 汪汪汪")
        
class Affenpinscher(Dog):
    def __init__(self):
        super().__init__(200)
     
    def roar(self):
        print("阿阿阿")
        
class AfghanHound(Dog):
    def __init__(self):
        super().__init__(5000)
     
    def roar(self):
        print("喔喔喔")
class Cat(Animal):
    def __init__(self,HP):
        super().__init__(0.5)
        
    def meaw(self):
        print("喵喵喵")
        
class Smallcat(Animal):
    def __init__(self,HP):
        super().__init__(0.25)
        
    def meaw(self):
        print("喵喵喵")
dog1 = AfghanHound()
dog2 = Affenpinscher()
cat1 = Cat()
cat2 = Smallcat()
dog2.roar()
dog1.roar()
cat2.roar()
cat1.roar()

        
        

    