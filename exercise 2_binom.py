from scipy import stats

#-------------------------------------------
# الف: احتمال زنده‌بودن هر پنج نفر 

n = 5
p = 2/3
x_value=5
binom_prob = stats.binom.pmf(x_value, n, p)

print(f"The probability that all five people are alive : {binom_prob}")
#-------------------------------------------
# ب: احتمال اینکه حداقل سه نفر زنده باشند

n = 5
p = 2/3
binom_prob = 0
for x_value in range(3,6):
    binom_prob += stats.binom.pmf(x_value, n, p)

print(f"The probability of at least three people being alive : {binom_prob}")
#-------------------------------------------
# ج: احتمال اینکه دقیقاً دو نفر زنده باشند

n = 5
p = 2/3
x_value = 2
binom_prob = stats.binom.pmf(x_value, n, p)

print(f"The probability that only two people are alive : {binom_prob}")

