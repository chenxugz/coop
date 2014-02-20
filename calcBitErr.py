#!/usr/bin/env python

def CntOnes(a):

    x = ord(a)
    cnt = 0
    for i in range(0,8):
        if (x & 1) ==1 :
            cnt = cnt +1
        x = (x >> 1)
    return cnt	 

def CalcBER(inData):

    bitErr = 0;
    
    for i in range(0,len(inData)):
        bitErr = bitErr + (8-CntOnes(inData[i]))

    print "BER = ", float(bitErr)/len(inData)/8
	


if __name__ == '__main__':
	try:
		CalcBER(1,1)
	except KeyboardInterrupt:
		pass

