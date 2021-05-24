# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:38:41 2021

@author: siddh
"""
#implementation of linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next 
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        node=Node(data,self.head)
        self.head=node
    def printll(self):
        if self.head==None:
            print("Linked list is empty")
            return
        
        itr=self.head 
        ll=''
        while itr:
            ll+=str(itr.data)+'---->'
            itr=itr.next 
        print(ll)
    def insertatend(self,data):
        node=Node(data,None)
        if self.head==None:
            self.head=node
            return
        itr=self.head 
        while itr.next:
            
            itr=itr.next
    
        itr.next=node 
    def addlist(self,Li):
        self.head=None
        for a in Li:
            self.insertatend(a)
    def getl(self):
        c=0
        itr=self.head
        while itr:
            itr=itr.next 
            c+=1
        return c
    def removeat(self,n):
        if n<0 or n>=self.getl():
            raise Exception("invalid index")
        if n==0:
            self.head=self.head.next 
            return
        c=0
        itr=self.head 
        while itr:
            
            if c==(n-1):
                itr.next=itr.next.next 
                break
            itr=itr.next
            c+=1
    def insertat(self,n,val):
        if n<0 or n>=self.getl():
            raise Exception("invalid index")
        if n==0:
            node=Node(val)
            node.next=self.head.next 
            self.head=node
            return
        itr=self.head 
        c=0
        while itr:
            if c==(n-1):
              node=Node(val)
              node.next=itr.next 
              itr.next=node
              break
            itr=itr.next 
            c+=1
              
            
        
def main():
    Link=LinkedList()
    Link.insertatbeg(45)
    Link.insertatbeg(90)
    Link.insertatend(70)
    Link.addlist([i for i in range(2,100,2)])
    Link.removeat(3)
    Link.insertat(1, "Hello")
    print('Length',Link.getl())
    
    Link.printll()
main()
                