__author__ = 'Nathen'


input_str = input('Paste input nums: ')
k, m, n = map(lambda num: float(num), input_str.split(' '))

population = k + m + n

# odds when dominant first
pK = k / population

# odds when heterozygous first
pMK = (m / population) * (k / (population - 1.0))
pMM = (m / population) * ((m - 1.0) / (population - 1.0)) * 0.75
pMN = (m / population) * (n / (population - 1.0)) * 0.5

# odds when we choose recessive first
pNK = (n / population) * (k / (population - 1.0))
pNM = (n / population) * (m / (population - 1.0)) * 0.5

result = pK + pMK + pMM + pMN + pNK + pNM

print(result)
