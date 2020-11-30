import math
import erwtima_1

letters_count, pdf = erwtima_1.alphabetGR_count_distribution('NEO_SYNTAGMA_AB.txt')
H = 0
for i in pdf.keys():
    if pdf[i] > 0:
        H += -pdf[i]*math.log(pdf[i],2)

print('The entropy of the text NEO_SYNTAGMA_AB for distribution p is: ',H)
