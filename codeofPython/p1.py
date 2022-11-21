
M = int(input())
N = int(input())


def gcd(M,N):
    if M<N:
        M,N=N,M
    if N != 0:
        gcd(N,M%N)
    return N
R=gcd(M,N)
if N==1 or M==1 or R==N:
    print("{} {}".format(M,N))
else:
    print("{} {} {}".format(M,N,R))