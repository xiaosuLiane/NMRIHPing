import base64
import binascii
import re
import socket

import chardet
def deleteStr(s,start,end):
    s_ = ''
    for i in range(len(s)):
        if i >= start and i <= end:
            s_ += ''
            continue
        s_ += s[i]
    d = s[start:end][0:6]
    score = int(d[4:6]+d[2:4]+d[0:2],16)
    if d[4:6] != '00':
        print('警告:',d[4:6])
        score = int((d[4:6]+d[2:4]+d[0:2]).replace('0',''),16)
    print(score)
    print(d[4:6]+d[2:4]+d[0:2])
    print('删除:'+s[start:end])
    return s_,score

if __name__ == '__main__':
    a = bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900")
    other_addr = ('1.117.77.239', 27070)
    net = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    net.sendto(a, other_addr)
    reply, other = net.recvfrom(1024)
    # print(reply.hex())
    reply = reply.hex().split('ffffffff41')[1]
    # print(reply)
    a = bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900" + reply)
    # print(a)
    net.sendto(a, other_addr)
    reply, other = net.recvfrom(5000)
    # print(int(bytes.hex(reply).split('006477')[0][-2:],16))
    # print(str(int(bytes.hex(reply).split('006477')[0][-2:],16)))#服务器在线人数
    # print(reply)
    print(reply.decode('utf-8', 'ignore'))
    print('Header:'+bytes.hex(reply))

    # print(bytes.fromhex(bytes.hex(reply)[12:].split('00')[0]).decode('utf-8'))
    a = bytes.fromhex("ffffffff5500000000")
    net.sendto(a, other_addr)
    reply, other = net.recvfrom(3000)
    # print(reply.hex())
    reply = bytes.fromhex("ffffffff55" + reply.hex()[10:])
    # print(reply)
    net.sendto(reply, other_addr)
    reply, other = net.recvfrom(3000)
    print(reply.__str__())
    print(reply.decode('utf-8', 'ignore'))
    print(bytes.hex(reply)[12:])
    a_ = bytes.hex(reply)[12:]
    print(a_)
    i_1 = -1
    i_2 = -1
    score = []
    for i in range(len(a_)-1):
        s = a_[i:i + 2]
        if s == '00':
            if i_1 == -1:
                i_1 = i
            elif i_1 != -1 and i_2 == -1:
                i_2 = i
            if i_1 != -1 and i_2 != -1:
                a_,score_ = deleteStr(a_,i_2+2,i_2+16)
                score.append(score_)
                i_1 = -1
                i_2 = -1
        # print('to:'+s+' ',i_1,' ',i_2)
    print(score)
    a = re.findall('00(.*?)00', a_)
    print(a_)
    s = ''
    for i in range(len(a)):
        try:
            if bytes.fromhex(str(a[i])).decode('utf-8', 'ignore') == '':
                continue
            # print(bytes.fromhex(str(i)).decode('utf-8', 'ignore'))
            s += bytes.fromhex(str(a[i])).decode('utf-8', 'ignore') + ' 分数:'+str(score[i])+'\r\n'
        except:
            if len(a[i]) % 2 != 0:
                # print(bytes.fromhex(str(i)+'0').decode('utf-8', 'ignore'))
                s += bytes.fromhex(str(a[i]) + '0').decode('utf-8', 'ignore') +' 分数:'+str(score[i])+ '\r\n'
    print(s)
    # for i in reply.decode('utf-8','ignore').__str__():
    #     try:
    #         a = chardet.detect(i.encode('utf-8'))
    #         if not (a["encoding"]=='ascii') or (a["encoding"]=='ascii' and ord(i) >= 33 and ord(i) <= 122):
    #             print(i,' ',len(i),' ',a["encoding"])
    #     except:
    #         pass
    #This code is ping NMRIHserver by Pushad QQ:3261601443