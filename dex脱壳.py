#!/usr/bin/python3
#必须在python3运行
fp=open('classes.dex','rb')
fp.seek(-4,2)
sz=int.from_bytes(fp.read(),byteorder='big')
fp.seek(0-4-sz,2)
wp=open('answer.apk','wb')
for i in fp.read():
    a=i^255
    a=a&0xff
    wp.write(a.to_bytes(1,'little'))