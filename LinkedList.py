# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:19:04 2020

@author: Akshat Jain
"""

class Node(object):
    def __init__(self , data):
        self.data = data
        self.nextNode = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insertstart(self , data):
        self.size = self.size+1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    def size1(self):
        return self.size
    
    def insertend(self , data):
        self.size = self.size + 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            actualNode = self.head
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode
            actualNode.nextNode = newNode
    def insertafter(self , previousdata , data):
        self.size = self.size + 1
        newNode = Node(data)
        currentNode = self.head
        previousNode = currentNode
        while previousNode.data != previousdata:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        newNode.nextNode = currentNode
        previousNode.nextNode = newNode
    
    def insertbefore(self , data , afterdata):
        self.size = self.size + 1
        newNode = Node(data)
        currentNode = self.head
        previousNode = currentNode
        while previousNode.data != afterdata:
            currentNode = previousNode
            previousNode = previousNode.nextNode
            
        newNode.nextNode = previousNode
        currentNode.nextNode = newNode
    
    def remove(self , data):
        if self.head is None:
            return
        self.size = self.size - 1
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
        
        
    def traverselist(self ):
        actualNode = self.head
        while actualNode is not None:
            print(str(actualNode.data))
            actualNode = actualNode.nextNode
ll = LinkedList()            
ll.insertstart(10)
ll.insertend(20)
ll.insertend(30)
ll.insertend(40)
ll.size1()
ll.remove(30)
ll.insertafter(20 , 30)
ll.insertbefore(25 , 30)
ll.traverselist()























