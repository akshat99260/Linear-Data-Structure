# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:09:26 2020

@author: Akshat Jain
"""

class HashTable(object):
    def __init__(self):
        self.size = 11
        self.keys = [None]*self.size
        self.values= [None]*self.size
        
        
    def hashFunction(self , key):
        sum = 0
        for i in range(len(key)):
            sum = sum + ord(key[i])
        return sum % self.size
    
    def put(self,key,data):
        index = self.hashFunction(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] == data
                return
            index = (index+1) % self.size
        self.keys[index] = key
        self.values[index] = data
    
    def get(self , key):
        index = self.hashFunction(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index+1)%self.size
        return None
    
if __name__ == "__main__":
    h = HashTable()
    h.put('Akshat',21)
    h.put('Ayush' ,22)
    h.put('Prasham',20)
    print(h.get('Prasham'))
    print(h.get('Akshat'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    