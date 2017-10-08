import pandas as pd
from numpy import sqrt,mean,log,diff,random
from scipy import log,exp,sqrt,stats
import sys

read_data = sys.stdin.readlines()

for i in xrange(0,len(read_data)):
    # data = list(read_data[i].split(','))
    data = [int(s) for s in read_data[i].split(',')]

    if float(data[0])==1:
        S = float(data[1]);
        X = float(data[2]);
        T = float(data[3]);
        C = float(data[4]);
        
        vol = 2*(log((X+C)/S))/(sqrt(T))                  
        sys.stdout.write(str(abs(vol))+'\n')
     
    if float(data[0])==2:
        S = float(data[1]);
        X = float(data[2]);
        T = float(data[3]);
        B = float(data[4]);
        C = float(data[5]);
        
        if  ((B/S) <= 2) and (S > X):
            vol = (2*(log(1+(X+C)/S))/(sqrt(T)))*8
        elif ((B/S) > 5) and (S<=X) :
            vol = (2*(log(1+(X+C)/S))/(sqrt(T)))*6
        else:
            vol = (2*(log(1+(X+C)/S))/(sqrt(T)))*1.2
            
        sys.stdout.write(str(abs(vol))+'\n')
        
    if float(data[0])==3:
        S = float(data[1]);
        for i in xrange(0,int(data[2])):
            C = float(data[3+i]);
            X = float(data[3+int(data[2])+i]);
            T = float(data[3+2*int(data[2])+i]);
            vol = 2*(log((X+C)/S))/(sqrt(T))                  
            sys.stdout.write(str(abs(vol))+", ")
        sys.stdout.write("\n")
    
    if float(data[0])==4:
        S = float(data[1]);
        B = float(data[2]);
        for i in xrange(0,int(data[3])):
            C = float(data[4+i]);
            X = float(data[4+int(data[3])+i]);
            T = float(data[4+2*int(data[3])+i]);
            fin_vol = []
            
            if  ((B/S) <= 2) and (S > X):
                vol = ((2*(log(1+(X+C)/S))/(sqrt(T)))*8)*C
            elif ((B/S) > 5) and (S<=X) :
                vol = ((2*(log(1+(X+C)/S))/(sqrt(T)))*6)*C
            else:
                vol = ((2*(log(1+(X+C)/S))/(sqrt(T)))*1.2)*C
            fin_vol.append(abs(vol))
            
        sys.stdout.write(str(sum(fin_vol))+'\n')            
  




