from scipy import stats

#-------------------------------------------

n = 10
p = 0.5
binom_prob = 0
for x_value in range(7, 11):
    binom_prob += stats.binom.pmf(x_value, n, p)

print(f"The probability win : {binom_prob}")


