import random
import erwtima_3


def huffman(p):
   
    #to parakato den xriazete, aplos elegxi ama ta stixoia pou tou exoume dosi einai 100% kai oti dipote allo to stamatai(sta test pou tou ekana merikes fores me blockare xoris logo)
    assert(sum(p.values()) == 1.0) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

   
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    
    assert(len(p) >= 2) 

    sorted_p = sorted(p.items(), key=lambda x: x[1])      
    return sorted_p[0][0], sorted_p[1][0]
#Gia na douleyi aplos prepi na baloume mesa ston huffman to alphabet apo to erwtima_3, opws huffman(example)

def coding(mes,code):
    coded_mes = []
    for i in mes:
        coded_mes.append(code[i])
    return ''.join(coded_mes)

# Create code by using letters keys and c values
#ekana antikatastasi tou Shannon me huffman
letters = huffman(erwtima_3.letters_count)
code = letters
for key, val in zip(code,c):
    code[key]= val

# Create the message
with open ("NEO_SYNTAGMA_KEF.txt","r") as f1:
    mes_in = ''.join(f1.read())

coded_mes = coding(mes_in,code)

# DECODING PART

# Decoding the message
def decoding01(mes,code):
    decoded = []
    for i in range(0,len(mes)):
        letter = ''
        # checks for every value if it matches with codeword
        # because it is a "prefix code" we will not have matches regardless of the length we check
        for key, value in code.items():  
            # for every codeword it checks if the same length matches the code
            if value == mes[i:i+len(code[key])]:
                letter = key
        i += len(letter)
     # if you uncomment the difference from the original message increases
     #   if letter == '':
      #      letter = '_'
        decoded.append(letter)
    return ''.join(decoded)

r_message = decoding01(coded_mes,code)

with open ('NEO_SYNTAGMA_CODED_SF.txt','w') as f1:
      f1.write(r_message)

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

print('Διαφορά από αρχικό μήνυμα: ',hamming_distance(mes_in,r_message))
