import math
import erwtima_3

num_letters = 24
distance = 0
x = 1/num_letters

u = {'α':x, 'β':x, 'γ':x, 'δ':x, 'ε':x, 'ζ':x, 'η':x, 'θ':x, 'ι':x,
     'κ':x, 'λ':x, 'μ':x, 'ν':x, 'ξ':x, 'ο':x, 'π':x, 'ρ':x, 'σ':x,
     'τ':x, 'υ':x, 'φ':x, 'χ':x, 'ψ':x, 'ω':x}

#calling function that calculates distribution p from our text
letters_count, pdf = erwtima_3.alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt')

for i in pdf.keys():
    distance += pdf[i]*math.log(pdf[i]/u[i],2)
    
print('Kullback-Leibler distance = ',distance)

