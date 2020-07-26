# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:10:08 2020

@author: Akshat Jain
"""

class Stack():
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self ,  data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek(self):
        data = self.stack[-1]
        return data
    
    def stacksize(self):
        return len(self.stack)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.pop()
stack.pop()
stack.stacksize()
        