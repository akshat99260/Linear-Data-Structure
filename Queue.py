# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:27:17 2020

@author: Akshat Jain
"""


class Queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self ,  data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        data = self.queue[0]
        return data
    
    def queuesize(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.peek()
queue.dequeue()
queue.dequeue()
queue.queuesize()
        