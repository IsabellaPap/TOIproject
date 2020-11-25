import math

def alphabetGR_count_distribution(text_file):

    with open (text_file, 'r') as f:
        data = f.read()
    
    letters = {'α':0,'β':0,'γ':0,'δ':0,'ε':0,'ζ':0,'η':0,'θ':0,'ι':0,'κ':0,'λ':0,'μ':0,'ν':0,'ξ':0,'ο':0,'π':0,
               'ρ':0,'σ':0,'τ':0,'υ':0,'φ':0,'χ':0,'ψ':0,'ω':0}
    total = 0
    for i in data:
        if i in ['α','Α','ά','Ά']:
            total += 1
            letters['α'] += 1
        elif i in ['β','Β']:
            total += 1
            letters['β'] += 1
        elif i in ['γ','Γ']:
            total += 1
            letters['γ'] += 1
        elif i in ['δ','Δ']:
            total += 1
            letters['δ'] += 1
        elif i in ['ε','έ','Ε','Έ']:
            total += 1
            letters['ε'] += 1
        elif i in ['ζ','Ζ']:
            total += 1
            letters['ζ'] += 1
        elif i in ['η','ή','Η','Ή']:
            total += 1
            letters['η'] += 1
        elif i in ['θ','Θ']:
            total += 1
            letters['θ'] += 1
        elif i in ['ι','ί','Ι','Ί','ϊ','ΐ']:
            total += 1
            letters['ι'] += 1
        elif i in ['κ','Κ']:
            total += 1
            letters['κ'] += 1
        elif i in ['λ','Λ']:
            total += 1
            letters['λ'] += 1
        elif i in ['μ','Μ']:
            total += 1
            letters['μ'] += 1
        elif i in ['ν','Ν']:
            total += 1
            letters['ν'] += 1
        elif i in ['ξ','Ξ']:
            total += 1
            letters['ξ'] += 1
        elif i in ['ο','ό','Ο','Ό']:
            total += 1
            letters['ο'] += 1
        elif i in ['π','Π']:
            total += 1
            letters['π'] += 1
        elif i in ['ρ','Ρ']:
            total += 1
            letters['ρ'] += 1
        elif i in ['σ','Σ','ς']:
            total += 1
            letters['σ'] += 1
        elif i in ['τ','Τ']:
            total += 1
            letters['τ'] += 1
        elif i in ['υ','ύ','Υ','Ύ']:
            total += 1
            letters['υ'] += 1
        elif i in ['φ','Φ']:
            total += 1
            letters['φ'] += 1
        elif i in ['χ','Χ']:
            total += 1
            letters['χ'] += 1
        elif i in ['ψ','Ψ']:
            total += 1
            letters['ψ'] += 1
        elif i in ['ω','Ω','ώ','Ώ']:
            total += 1
            letters['ω'] += 1

    p = {'α':0,'β':0,'γ':0,'δ':0,'ε':0,'ζ':0,'η':0,'θ':0,'ι':0,'κ':0,'λ':0,'μ':0,'ν':0,'ξ':0,'ο':0,'π':0,
               'ρ':0,'σ':0,'τ':0,'υ':0,'φ':0,'χ':0,'ψ':0,'ω':0}
    num_letters = 0
    for l in letters.keys():
        num_letters += 1
        p[l] = letters[l]/total
    return letters, p

letters_count, pdf = alphabetGR_count_distribution('NEO_SYNTAGMA_AB')
H = 0
for i in pdf.keys():
    if pdf[i] > 0:
        H += -pdf[i]*math.log(pdf[i],2)

print('The entropy of the text NEO_SYNTAGMA_AB for distribution p is: ',H)
