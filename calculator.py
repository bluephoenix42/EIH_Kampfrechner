#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#attacker=0 defender=1 undecided = 2 tie=3

"""
Created on Thu Jul  5 11:32:32 2018

@author: jan
"""
import table
class calculator:
    def __init__(self):
        self.table = table.table()
        self.outcomes = dict()
        for roun in range(1,4):
            for winner in [0, 1, 2, 3]:
                self.outcomes[(roun, winner)]=[]
        
    def calc_outcomes(self,chit,mod, mor, fac):
        tab = self.table.get_tab(chit)
        self.outcomes[(0,2)]=[(fac, mor)]
        for roun in range(1,4):
            for past in self.outcomes[(roun-1,2)]:
                for i in range(1,7):
                    for j in range(1,7):
                        x=0
                        temp=((past[0][0]-tab[(1,0,roun)][j+mod[1]]*past[0][1], past[0][1]-tab[(0,0,roun)][i+mod[0]]*past[0][0]), (past[1][0]+tab[(1,1,roun)][j+mod[1]],past[1][1]+tab[(0,1,roun)][i+mod[0]]))
                        #überprüfen ob ausgelöscht
                        if temp[0][0]<=0:
                            temp[0][0]=0
                            if temp[0][1]<=0:
                                #temp[0][1]=0
                                self.outcomes[roun,3].append(temp)
                            else:
                                self.outcomes[roun,1].append(temp)
                        elif temp[0][1]<=0:
                            #temp[0][1]=0
                            self.outcomes[roun,0].append(temp)
                        #überprüfen ob break
                        elif temp[1][0]<=0:
                            #temp[1][0]=0
                            if temp[1][1]<=0:
                                #temp[1][1]=0
                                self.outcomes[roun,3].append(temp)
                            else:
                                self.outcomes[roun,1].append(temp)
                        elif temp[1][1]<=0:
                            #temp[1][1]=0
                            self.outcomes[roun,0].append(temp)
                        #überprüfe ob letzte Runde
                        elif roun==3:
                            self.outcomes[roun,3].append(temp)
                        #sonst weiter
                        else:
                            self.outcomes[roun,2].append(temp)
                            
    def winchance(self):
        win_ch = {0:0,1:0, 3:0}
        for roun in range(1,4):
            for fighter in [0,1,3]:
                win_ch[fighter]=win_ch[fighter]+(len(self.outcomes[roun,fighter])/(36**roun))
        return win_ch
    
chit=(((3,1),(4,2),(5,1)),((2,1),(2,4),(3,3)))
mod=(1,-1)
mor=(2,3)
fac=(80,60)
ca=calculator()
ca.calc_outcomes(chit, mod, mor, fac)
print(ca.winchance())