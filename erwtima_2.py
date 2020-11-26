import math

#letters in greek alphabet
num_letters = 24 
x = 1/num_letters

# u = equal distribution
u = {'α':x, 'β':x, 'γ':x, 'δ':x, 'ε':x, 'ζ':x, 'η':x, 'θ':x, 'ι':x,
     'κ':x, 'λ':x, 'μ':x, 'ν':x, 'ξ':x, 'ο':x, 'π':x, 'ρ':x, 'σ':x,
     'τ':x, 'υ':x, 'φ':x, 'χ':x, 'ψ':x, 'ω':x}

h_equal = math.log(num_letters,2)

print('The entropy of the Greek alphabet (equal distribution) = ',h_equal)
      

