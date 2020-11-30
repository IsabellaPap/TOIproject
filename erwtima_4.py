import math
import erwtima_1

num_letters = 24
distance = 0
x = 1/num_letters

u = {'Α':x, 'Β':x, 'Γ':x, 'Δ':x, 'Ε':x, 'Ζ':x, 'Η':x, 'Θ':x, 'Ι':x,
     'Κ':x, 'Λ':x, 'Μ':x, 'Ν':x, 'Ξ':x, 'Ο':x, 'Π':x, 'Ρ':x, 'Σ':x,
     'Τ':x, 'Υ':x, 'Φ':x, 'Χ':x, 'Ψ':x, 'Ω':x}

#calling function that calculates distribution p from our text
letters_count, pdf = erwtima_1.alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt')

for i in pdf.keys():
    distance += pdf[i]*math.log(pdf[i]/u[i],2)
    
print('Kullback-Leibler distance = ',distance)

