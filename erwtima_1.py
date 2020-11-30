import math

with open('NEO_SYNTAGMA.txt','r') as f1:
    data = f1.read()

with open('NEO_SYNTAGMA_AB.txt','w') as f2:
    
    letters = {'α':0,'Α':0,'Ά':0,'ά':0,'β':0,'Β':0,'γ':0,'Γ':0,'δ':0,'Δ':0,'ε':0,'Ε':0,'Έ':0,'έ':0,
    'ζ':0,'Ζ':0,'η':0,'Η':0,'Ή':0,'ή':0,'θ':0,'Θ':0,'ι':0,'Ι':0,'Ί':0,'ί':0,'ϊ':0,'κ':0,'Κ':0,'λ':0,'Λ':0,
    'μ':0,'Μ':0,'ν':0,'Ν':0,'ξ':0,'Ξ':0,'ο':0,'Ο':0,'Ό':0,'ό':0,'π':0,'Π':0,'ρ':0,'Ρ':0,'σ':0,'Σ':0,'ς':0,
    'τ':0,'Τ':0,'υ':0,'Υ':0,'Ύ':0,'ύ':0,'ϋ':0,'φ':0,'Φ':0,'χ':0,'Χ':0,'ψ':0,'Ψ':0,'ω':0,'Ω':0,'Ώ':0,'ώ':0}

    for i in data:
        if i in letters.keys():
            f2.write(i)

def alphabetGR_count_distribution(text_file):

    with open (text_file, 'r') as f:
        data = f.read()
    
    letters = {'Α':0,'Β':0,'Γ':0,'Δ':0,'Ε':0,'Ζ':0,'Η':0,'Θ':0,'Ι':0,'Κ':0,'Λ':0,'Μ':0,'Ν':0,'Ξ':0,'Ο':0,'Π':0,
               'Ρ':0,'Σ':0,'Τ':0,'Υ':0,'Φ':0,'Χ':0,'Ψ':0,'Ω':0}
    with open ('NEO_SYNTAGMA_KEF.txt','w') as f2:
        total = 0
        for i in data:
            if i in ['α','Α','ά','Ά']:
                total += 1
                letters['Α'] += 1
                f2.write('Α')
            elif i in ['β','Β']:
                total += 1
                letters['Β'] += 1
                f2.write('Β')
            elif i in ['γ','Γ']:
                total += 1
                letters['Γ'] += 1
                f2.write('Γ')
            elif i in ['δ','Δ']:
                total += 1
                letters['Δ'] += 1
                f2.write('Δ')
            elif i in ['ε','έ','Ε','Έ']:
                total += 1
                letters['Ε'] += 1
                f2.write('Ε')
            elif i in ['ζ','Ζ']:
                total += 1
                letters['Ζ'] += 1
                f2.write('Ζ')
            elif i in ['η','ή','Η','Ή']:
                total += 1
                letters['Η'] += 1
                f2.write('Η')
            elif i in ['θ','Θ']:
                total += 1
                letters['Θ'] += 1
                f2.write('Θ')
            elif i in ['ι','ί','Ι','Ί','ϊ','ΐ']:
                total += 1
                letters['Ι'] += 1
                f2.write('Ι')
            elif i in ['κ','Κ']:
                total += 1
                letters['Κ'] += 1
                f2.write('Κ')
            elif i in ['λ','Λ']:
                total += 1
                letters['Λ'] += 1
                f2.write('Λ')
            elif i in ['μ','Μ']:
                total += 1
                letters['Μ'] += 1
                f2.write('Μ')
            elif i in ['ν','Ν']:
                total += 1
                letters['Ν'] += 1
                f2.write('Ν')
            elif i in ['ξ','Ξ']:
                total += 1
                letters['Ξ'] += 1
                f2.write('Ξ')
            elif i in ['ο','ό','Ο','Ό']:
                total += 1
                letters['Ο'] += 1
                f2.write('Ο')
            elif i in ['π','Π']:
                total += 1
                letters['Π'] += 1
                f2.write('Π')
            elif i in ['ρ','Ρ']:
                total += 1
                letters['Ρ'] += 1
                f2.write('Ρ')
            elif i in ['σ','Σ','ς']:
                total += 1
                letters['Σ'] += 1
                f2.write('Σ')
            elif i in ['τ','Τ']:
                total += 1
                letters['Τ'] += 1
                f2.write('Τ')
            elif i in ['υ','ύ','Υ','Ύ']:
                total += 1
                letters['Υ'] += 1
                f2.write('Υ')
            elif i in ['φ','Φ']:
                total += 1
                letters['Φ'] += 1
                f2.write('Φ')
            elif i in ['χ','Χ']:
                total += 1
                letters['Χ'] += 1
                f2.write('Χ')
            elif i in ['ψ','Ψ']:
                total += 1
                letters['Ψ'] += 1
                f2.write('Ψ')
            elif i in ['ω','Ω','ώ','Ώ']:
                total += 1
                letters['Ω'] += 1
                f2.write('Ω')


        p = {'Α':0,'Β':0,'Γ':0,'Δ':0,'Ε':0,'Ζ':0,'Η':0,'Θ':0,'Ι':0,'Κ':0,'Λ':0,'Μ':0,'Ν':0,'Ξ':0,'Ο':0,'Π':0,
                'Ρ':0,'Σ':0,'Τ':0,'Υ':0,'Φ':0,'Χ':0,'Ψ':0,'Ω':0}
        num_letters = 0
        for l in letters.keys():
            num_letters += 1
            p[l] = letters[l]/total
        return letters, p
letters_count, pdf = alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt')
print(pdf)