#!/usr/bin/env python
"""
Pi taken from here:
http://micronetsoftware.com/pi_day
"""
import struct

period=1E6
fpi=open("pi.txt","r")
fpib=open("pi.bin","wb")
i=0
j=0
for line in fpi:
    i+=1
    if i<20:continue
    line=line.strip("\n\r")
    if line=="":continue
    series=line.split(":")[0].strip(" ")
    blocks=series.split(" ")
    for block in blocks:
        for n in xrange(10):
            d=[int(block[n])]
            fpib.write(struct.pack('1b',*d))
    if (j%1E6)==0:print "%dM digits written"%(j/1E6)
    j+=50
fpi.close()
fpib.close()
print "Done."
