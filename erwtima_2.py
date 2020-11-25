import math

#letters in greek alphabet
num_letters = 24

# u = equal distribution
u = ['α': 1/num_letters, 'β': 1/num_letters, 'γ': 1/num_letters, 'δ': 1/num_letters, 'ε': 1/num_letters, 'ζ': 1/num_letters, 'η': 1/num_letters, 'θ': 1/num_letters, 'ι': 1/num_letters,
     'κ': 1/num_letters, 'λ': 1/num_letters, 'μ': 1/num_letters, 'ν': 1/num_letters, 'ξ': 1/num_letters, 'ο': 1/num_letters, 'π': 1/num_letters, 'ρ': 1/num_letters, 'σ': 1/num_letters,
     'τ': 1/num_letters, 'υ': 1/num_letters, 'φ': 1/num_letters, 'χ': 1/num_letters, 'ψ': 1/num_letters, 'ω': 1/2num_letters]

h_equal = math.log(num_letters,2)

print('The entropy of the Greek alphabet (equal distribution) = ',h_equal)
      

