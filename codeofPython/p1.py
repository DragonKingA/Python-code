
# M = int(input())
# N = int(input())
# def gcd(M,N):
#     if M<N:
#         M,N=N,M
#     if N != 0:
#         gcd(N,M%N)
#     return N
# R=gcd(M,N)
# if N==1 or M==1 or R==N:
#     print("{} {}".format(M,N))
# else:
#     print("{} {} {}".format(M,N,R))

# def dec2bin(x):
#     bins = ''
#     while x:
#         x *= 2
#         bins=bins+str(1 if x>=1. else 0)
#         x -= int(x)
#     return bins[:8]

# print(dec2bin(0.404))

# def bin2oh(binum, oh):
#     result = ''
#     binum=int(binum,2)
#     if oh == 'o':
#         result=result+oct(binum)
#         return result[2:]
#     elif oh == 'h':
#         result=result+hex(binum)
#         result=result.upper()
#         return result[2:]
# print(bin2oh(bin(7809),'h'))
# from random import *

# def makechange(num):
#     changes = {}
#     numint = int(num)
#     numdec = round(num - numint, 2)
#     for i in [50,20,10,5,2,1]:
#         res=numint//i
#         if res>0 and numint>0:
#             if i not in changes:
#                 changes[i]=0
#             changes[i] = changes[i]+res
#             numint -= res*i
#     for i in [0.5,0.2,0.1,0.05,0.02,0.01]:
#         res=numdec//i
#         if res>0 and numdec>0. :
#             if i not in changes:
#                 changes[i]=0
#             changes[i]=changes[i]+int(res)
#             numdec=round(numdec-res*i,2)
#     return changes  


# if __name__ == '__main__':
#     seed(0)
#     for i in range(10):
#         num = round(random() * 100, 2)
#         print(sorted(makechange(num).items(), key=lambda item: item[0], reverse=True))



import math

def encryptMessage(key, message):
    res=""
    for i in range(0,key,1):
        res+=message[i::key]
    return res
    #------------End-----------

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
 
        if (col == numOfColumns) or (col == numOfColumns-1 and row>=numOfRows-numOfShadeBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
    
    #------------End-----------


if __name__ == '__main__':
    messages = ["Behind every successful man there's a lot of unsuccessful years.",
                'Common sense is not so common.',
                'There are no secrets to success.It is the result of preparation, hard work, and learning from failure.',
                'All things are difficult before they are easy.']
    for message in messages:
        for key in range(8, 10):
            encrytext = encryptMessage(key, message)
            print(encrytext)
            print(decryptMessage(key, encrytext))















