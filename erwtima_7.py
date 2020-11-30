import math
import erwtima_1
import random

# CODING PART

def code_words(a):
    # a is float
    a = a - int(a)
    # now we have only the decimal part
    r = -1
    b = []
    # limit for code word 5 bits
    while a > 10**(-5):
        if a >= 2**r:
            b.append('1')
            a = a - 2**r
        else:
            b.append('0')
        r -= 1
    return ''.join(b)


def length_words(p):
    lp = []
    for i in p:
        # L(x) = ceiling of log(1/p[i],2)+1
        m_l = math.log(1/i,2)
        if m_l == int(m_l):
            lp.append(int(m_l)+1)
        else:
            lp.append(int(m_l)+2)
    return lp

letters_count,pdf = erwtima_1.alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt') 
p = list(pdf.values())
# f keeps track of Sums so it can add the previous to the next
f = []
# fi contains all the results of F for every probability
fi = []
# s is the sum as we move (stored in f) 
s = 0
# implementation of F function calculation
for i in range(len(p)):
    s += p[i]
    f.append(s)
    if i == 0:
        fi.append(p[i]/2)
    else:
        fi.append(f[i-1] + p[i]/2)

l = []
# i will take one by one the results of F function
for i in fi:
    # code_words converts fi results to bit sequences
    l.append(code_words(i))

# finding the length of each word = 8 bits for task 7
l_w = 8
c = []
for i in range(len(p)):
    # because code_words returns joined array [:l_w[i]] indicates how many bits to use
    c.append(l[i][:8])
    
print('F = ',f,'\nFI = ',fi,'\nL = ',l,'\nLP = ',l_w,'\nCode = ',c)
print(''.join(c[3]))

h = 0
l_sfe = 0
for i in range(len(p)):
    h -= p[i] * math.log(p[i],2)
    l_sfe += p[i] * len(c[i]) 
print('H(X) = ',h,'L(X) = ',l_sfe,'Eff =',h/l_sfe)

def coding(mes,code):
    coded_mes = []
    for i in mes:
        coded_mes.append(code[i])
    return ''.join(coded_mes)

# Create code by using letters keys and c values
code = letters_count
for key, val in zip(code,c):
    code[key]= val

# Create the message
with open ("NEO_SYNTAGMA_KEF.txt","r") as f1:
    mes_in = ''.join(f1.read())

coded_mes = coding(mes_in,code)