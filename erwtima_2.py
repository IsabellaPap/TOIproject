import math

#letters in greek alphabet
num_letters = 24 
x = 1/num_letters

# u = equal distribution
u = {'Α':x, 'Β':x, 'Γ':x, 'Δ':x, 'Ε':x, 'Ζ':x, 'Η':x, 'Θ':x, 'Ι':x,
     'Κ':x, 'Λ':x, 'Μ':x, 'Ν':x, 'Ξ':x, 'Ο':x, 'Π':x, 'Ρ':x, 'Σ':x,
     'Τ':x, 'Υ':x, 'Φ':x, 'Χ':x, 'Ψ':x, 'Ω':x}

h_equal = math.log(num_letters,2)

print('The entropy of the Greek alphabet (equal distribution) = ',h_equal)
      

