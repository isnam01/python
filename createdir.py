#!usr/bin/python
import os
for i in range(100) :
    os.mkdir("directory%d.txt"%i)
    s=open('file%d'%i,'w')
    s.close()
