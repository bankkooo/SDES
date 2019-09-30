from operator import xor
bin8 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(8)]))
#bin10 = lambda z: ''.join(reversed([str((z >> j) & 1) for j in range(10)]))
key = []
S0 = [["01","00","11","10"],
      ["11","10","01","00"],
      ["00","10","01","11"],
      ["11","01","11","10"]]
S1 = [["00","01","10","11"],
      ["10","00","01","11"],
      ["11","00","01","00"],
      ["10","01","00","11"]]
def IP(c):
    New_c = []
    New_c.append(c[1])
    New_c.append(c[5])
    New_c.append(c[2])
    New_c.append(c[0])
    New_c.append(c[3])
    New_c.append(c[7])
    New_c.append(c[4])
    New_c.append(c[6])
    #print("IP:",New_c)
    #EP(New_c)
    return  New_c

def EP(c):
    New_c = []
    New_c.append(c[7])
    New_c.append(c[4])
    New_c.append(c[5])
    New_c.append(c[6])
    New_c.append(c[5])
    New_c.append(c[6])
    New_c.append(c[7])
    New_c.append(c[4])
    #print("EP:", New_c)
    return New_c
    #K1(New_c,c)

def K1(c,Oc,key):
    New_c = []
    All_s = []
    New_s0 = []
    New_s1 = []
    k1 = key
    for i in range(len(c)):
        New_c.append(xor(int(c[i]),int(k1[i])))

    #print("Xork1:",New_c)
    New_s0 = Find_s0(New_c[0:4])
    New_s1 = Find_s1(New_c[4:8])
    All_s = New_s0 + New_s1
    #print("s0s1:"+str(All_s))
    #P4(All_s,Oc)
    return All_s




def Find_s0(c):
    New_c = []
    row = []
    col = []
    row.append(c[0])
    row.append(c[3])
    col.append(c[1])
    col.append(c[2])
    Numrow = int("".join(str(x) for x in row), 2)
    Numcol = int("".join(str(x) for x in col), 2)
    New_c = S0[Numrow][Numcol]
    #print(New_c)
    return (str(New_c))

def Find_s1(c):
    New_c = []
    row = []
    col = []
    row.append(c[0])
    row.append(c[3])
    col.append(c[1])
    col.append(c[2])
    Numrow = int("".join(str(x) for x in row), 2)
    Numcol = int("".join(str(x) for x in col), 2)
    New_c = S1[Numrow][Numcol]
    #print(New_c)
    return(str(New_c))

def P4(c,Oc):
    New_c = []
    New_c.append(c[1])
    New_c.append(c[3])
    New_c.append(c[2])
    New_c.append(c[0])
    #print("P4:",New_c)
    #exor(New_c,Oc)
    return New_c

def exor(c,Oc):
    New_c = []
    text = []
    for i in range(len(c)):
        New_c.append(xor(int(c[i]),int(Oc[i])))

    a = ''.join(map(str, New_c))
    b = ''.join(map(str, Oc[4:8]))
    text.append(a)
    text.append(b)
    #plaintext = b+a
    #print(text)
    return text

def swap(T):
    plaintext = T[1] + T[0]
    #print(plaintext)
    return plaintext

def noswap(T):
    plaintext = T[0] + T[1]
    #print(plaintext)
    return plaintext

def K2(c,Oc,key):
    New_c = []
    All_s = []
    New_s0 = []
    New_s1 = []
    k2 = key
    for i in range(len(c)):
        New_c.append(xor(int(c[i]),int(k2[i])))

    #print("Xork2:",New_c)
    New_s0 = Find_s0(New_c[0:4])
    New_s1 = Find_s1(New_c[4:8])
    All_s = New_s0 + New_s1
    #print("s0s1:"+str(All_s))
    #P4(All_s,Oc)
    return All_s

def IPinverse(c):
    c = list(c)
    New_c = []
    New_c.append(c[3])
    New_c.append(c[0])
    New_c.append(c[2])
    New_c.append(c[4])
    New_c.append(c[6])
    New_c.append(c[1])
    New_c.append(c[7])
    New_c.append(c[5])
    #print("cP:",New_c)
    #EP(New_c)
    return  New_c

def key1(k):
    k = bin(k)
    k = str(k)
    keylist = k.split('b')
    k = keylist[1]
    k = list(k)
    #print("Key::", k)
    key = []
    if(len(k)<10):
        erase = 10-len(k)
        for i in range(erase):
            k.insert(0,0)

    k = P10(k)
    New_k = []
    New_k.append(k[1])
    New_k.append(k[2])
    New_k.append(k[3])
    New_k.append(k[4])
    New_k.append(k[0])
    New_k.append(k[6])
    New_k.append(k[7])
    New_k.append(k[8])
    New_k.append(k[9])
    New_k.append(k[5])
    #print("Newkey:",k)
    k2 = key2(New_k)
    k1 = P8(New_k)
    key.append(k1)
    key.append(k2)
    return key

def key2(k):
    #k = bin10(k)
    #k = list(k)
    New_k = []
    New_k.append(k[2])
    New_k.append(k[3])
    New_k.append(k[4])
    New_k.append(k[0])
    New_k.append(k[1])
    New_k.append(k[7])
    New_k.append(k[8])
    New_k.append(k[9])
    New_k.append(k[5])
    New_k.append(k[6])

    k2 = P8(New_k)
    return k2

def P8(k):
    #print("P8:",k)
    New_k = []
    New_k.append(k[5])
    New_k.append(k[2])
    New_k.append(k[6])
    New_k.append(k[3])
    New_k.append(k[7])
    New_k.append(k[4])
    New_k.append(k[9])
    New_k.append(k[8])
    return New_k

def P10(k):
    #print("P8:",k)
    New_k = []
    New_k.append(k[2])
    New_k.append(k[4])
    New_k.append(k[1])
    New_k.append(k[6])
    New_k.append(k[3])
    New_k.append(k[9])
    New_k.append(k[0])
    New_k.append(k[8])
    New_k.append(k[7])
    New_k.append(k[5])
    return New_k

def find(c,y1,y2,key):
    #Cipher = "01110010"
    Cipher = c
    result = []
    ret = 0
    for i in range(len(Cipher)):
        #print(Cipher[i])

        ret = 0
        res = int("".join(str(x) for x in Cipher[i]), 2)
        Cipher[i] = bin8(res)
        #print("Original:",Cipher[i])
        Ip = IP(Cipher[i])
        Ep1 = EP(Ip)
        #print("1:",y)
        k1 = K1(Ep1,Ip,y2)
        p41 = P4(k1,Ip)
        xor1 = exor(p41,Ip)
        xor1 = swap(xor1)
        text1 = xor1
        #print("----------------------------")
        Ep2 = EP(text1)
        #print("2:",y)
        k2 = K2(Ep2,text1,y1)
        p42 = P4(k2,text1)
        xor2 = exor(p42,xor1)
        xor2 = noswap(xor2)
        cpt = IPinverse(xor2)
        #print("Result::", cpt)
        cpt = int("".join(str(x) for x in cpt), 2)
        #print("::",cpt)
        cpt = str(chr(cpt))
#        if(cpt==9):
#            print("Congratulation!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        result.append(cpt)
        if (len(result) == len(c)):
#            resu = "".join(str(result))
            #print(str(result[1]))
            if(result[0]=="5" and result[1]=="9" and result[2]=="0" and result[3]=="6" and result[4]=="1" and result[5]=="0" and result[6]=="6"  and result[7]=="1"  and result[8]=="4"):
                #ret = 1
                print(result,":key::",bin(key))



    #print(c)
    if(ret):
        print("Congratulation!!!")
        #return result


#print("-------------------------------")
Ciphertext ="0b1110001,0b11110,0b10100100,0b1101111,0b110000,0b10100100,0b1101111,0b110000,0b11000001,0b11001010,0b1110001,0b10111110,0b10111110,0b11000001,0b11000001,0b1110001,0b11001111,0b10100100,0b10111110,0b1110001,0b111111,0b10111110,0b111111,0b10111110,0b11001010,0b1110001,0b111111,0b1101111,0b1110001,0b111111,0b11000001,0b1110001,0b1110001,0b1101111,0b1101111,0b11110,0b10100100,0b10111110,0b110000,0b111111,0b11001010,0b111111,0b11000001,0b1110001,0b1110001,0b1110001,0b1101111,0b1110001,0b1110001,0b11110,0b1110001,0b1110001,0b1110001,0b110000,0b11000001,0b111111,0b1110001,0b111111,0b11001111,0b111111,0b1110001,0b11001010,0b10111110,0b11001111,0b1110001,0b1110001,0b110000,0b11000001,0b11001010,0b11001111,0b11001111,0b111111,0b1110001,0b11001010,0b11110,0b1110001,0b11110"
#Ciphertext ="0b1110001,0b11110,0b10100100,0b1101111,0b110000,0b10100100,0b1101111,0b110000,0b11000001"
test = "01110001"
Cipherlist = []
Student = []
Cipherlist = Ciphertext.split(',')
#find(test,10)
#key = 298
for key in range(1024):
    kA=key1(key)
    #print("ka::",key)
    find(Cipherlist,kA[0],kA[1],key)


