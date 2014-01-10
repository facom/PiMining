"""
################################################################################
#  ___ _     __  __ _      _           
# | _ (_)___|  \/  (_)_ _ (_)_ _  __ _ 
# |  _/ |___| |\/| | | ' \| | ' \/ _` |
# |_| |_|   |_|  |_|_|_||_|_|_||_\__, |
#                                |___/ 
################################################################################
# 2014 (C) Jorge I. Zuluaga zuluagajorge@gmail.com
################################################################################
# Pi has been downloaded from:
# http://micronetsoftware.com/pi_day
################################################################################
"""

################################################################################
#PACKAGES
################################################################################
import struct

################################################################################
#LOAD PI
################################################################################
FPI=open("numbers/pi.bin","rb")

################################################################################
#CONSTANTS
################################################################################
K=1E3
M=1E6
G=1E9

################################################################################
#ROUTINES
################################################################################
def piDigits(offset,length,string=False):
    FPI.seek(offset,0)
    data=FPI.read(length)
    fmt="%db"%length
    sequence=struct.unpack(fmt,data)
    if string:
        return [str(s) for s in sequence]
    else:
        return sequence

def piSegment(offset,length):
    digits=piDigits(offset,length,string=True)
    return "".join(digits)

def piValue(ndigits):
    pi="3."+piSegment(0,ndigits)
    return pi

def piSearch(digits,maxdigits=1000):
    ndigits=len(digits)
    finds=[]
    for i in xrange(int(maxdigits)):
        query=piSegment(i,ndigits)
        if query==digits:finds+=[i]
    return finds

def piFrequency(ndigits):
    from numpy import zeros
    h=zeros(10)
    for i in xrange(ndigits):
        FPI.seek(i,0)
        data=FPI.read(1)
        fmt="%db"%1
        d=struct.unpack(fmt,data)
        h[d]+=1
    return h

if __name__=="__main__":

    #Get Digits
    digits=piDigits(0,1000)
    print digits

    #Get Value
    value=piValue(100)
    print "Value: %s"%value
    
    #Histogram digits
    h=piFrequency(1000)
    print "Frequence of digits: ",h

    #Linear search
    digits="123"
    ndigits=len(digits)
    ipos=piSearch(digits,maxdigits=10*K)
    print "Finds '%s': "%(digits),ipos
    print "Context around %d digit: %s"%(ipos[0],piSegment(ipos[0]-10,ndigits+20))
    

