# -*- coding: utf-8 -*-
"""
Created on Fri May  7 00:38:29 2021

@author: siddh
"""
def selectionsort(a):
    size=len(a)
    print(size)
    for i in range(size-1):
        mini=i
        for j in range(mini+1,size):
            if a[j]['First Name']<a[mini]['First Name']:
                mini=j
        if i!=mini:
            a[i]['First Name'],a[mini]['First Name']=a[mini]['First Name'],a[i]['First Name']
def selectionsortL(a):
    size=len(a)
    print(size)
    for i in range(size-1):
        mini=i
        for j in range(mini+1,size):
            if a[j]['Last Name']<a[mini]['Last Name']:
                mini=j
        if i!=mini:
            a[i]['Last Name'],a[mini]['Last Name']=a[mini]['Last Name'],a[i]['Last Name']

tests = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
print(len(tests))

selectionsortL(tests)
selectionsort(tests)
for i in tests:
    print(i)