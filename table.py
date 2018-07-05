#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:34:05 2018

@author: jan
"""
class table:
    def __init__(self):
        self.damage=dict()
        self.moral=dict()
        for i in range(1, 6):
            for j in range(1,6):
                x=0
                self.damage[(i,j)]=dict()
                self.moral[(i,j)]=dict()
        tabl = open("table.txt")
        y=0
        for line in tabl:
            if y>0:
                self.moral[((x-1)//2+1,(y-1)//8+1)][(y-1)%8]=float(temp)
            y=y+1
            x=0
            temp=""
            for cha in line:
                if cha ==",":
                    x=x+1
                    if x%2:
                        self.damage[((x-1)//2+1,(y-1)//8+1)][(y-1)%8]=float(temp)
                    else:
                        self.moral[((x-1)//2+1,(y-1)//8+1)][(y-1)%8]=float(temp)
                    temp = ""
                else:
                    temp = temp + cha
            self.moral[((x-1)//2+1,(y-1)//8+1)][(y-1)%8]=float(temp)
        tabl.close()
        
            
    def get_table(pos):
        return self.table[pos]
