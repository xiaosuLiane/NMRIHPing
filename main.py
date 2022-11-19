import base64
import binascii
import re
import socket

import chardet

a = bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900")
other_addr = ('121.5.51.123', 27015)
net = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
net.sendto(a,other_addr)
reply,other = net.recvfrom(1024)
# print(reply.hex())
reply = reply.hex().split('ffffffff41')[1]
# print(reply)
a = bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900"+reply)
# print(a)
net.sendto(a,other_addr)
reply,other = net.recvfrom(5000)
# print(reply)
print(reply.decode('utf-8','ignore'))
a = bytes.fromhex("ffffffff5500000000")
net.sendto(a,other_addr)
reply,other = net.recvfrom(3000)
# print(reply.hex())
reply = bytes.fromhex("ffffffff55"+reply.hex()[10:])
# print(reply)
net.sendto(reply,other_addr)
reply,other = net.recvfrom(3000)
print(reply.__str__())
print(reply.decode('utf-8','ignore'))
# for i in reply.decode('utf-8','ignore').__str__():
#     try:
#         a = chardet.detect(i.encode('utf-8'))
#         if not (a["encoding"]=='ascii') or (a["encoding"]=='ascii' and ord(i) >= 33 and ord(i) <= 122):
#             print(i,' ',len(i),' ',a["encoding"])
#     except:
#         pass