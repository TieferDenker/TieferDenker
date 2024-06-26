from math import log, floor

phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189
sq5 = 2.2360679774997896964091736687312762354406183596115257242708972454

def Solve_Prob(n):
    m = floor(log(sq5*n,phi))-1
    lim = floor((m+1)/3)
    a = 1
    b = 2
    summ = 0
    k = 1
    while k <= lim:
        if b%2 == 0:
            summ = summ + b
            k = k + 1
        t = a
        a = b
        b = t + b
    return summ

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)