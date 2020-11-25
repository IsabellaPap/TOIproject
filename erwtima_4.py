import math
import erwtima_3

distance = 0

u = ['α': 1/num_letters, 'β': 1/num_letters, 'γ': 1/num_letters, 'δ': 1/num_letters, 'ε': 1/num_letters, 'ζ': 1/num_letters, 'η': 1/num_letters, 'θ': 1/num_letters, 'ι': 1/num_letters,
     'κ': 1/num_letters, 'λ': 1/num_letters, 'μ': 1/num_letters, 'ν': 1/num_letters, 'ξ': 1/num_letters, 'ο': 1/num_letters, 'π': 1/num_letters, 'ρ': 1/num_letters, 'σ': 1/num_letters,
     'τ': 1/num_letters, 'υ': 1/num_letters, 'φ': 1/num_letters, 'χ': 1/num_letters, 'ψ': 1/num_letters, 'ω': 1/num_letters]

#calling function that calculates distribution p from our text
pdf = erwtima_3.alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt')

for i in pdf.keys():
    distance += pdf[i]*math.log(pdf[i]/u[i],2)
    
print('Kullback-Leibler distance = ',distance)

