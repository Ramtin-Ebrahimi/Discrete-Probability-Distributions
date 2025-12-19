from scipy import stats

#-------------------------------------------
# الف: احتمال اینکه کامپیوتر در ۴ ماه خراب نشود

lambda_ = 1
x_value = 0
poisson_prob = stats.poisson.pmf(x_value, mu=lambda_)

print(f"The probability that the computer will not break down at all in four months : {poisson_prob}")
#-------------------------------------------
# ب: احتمال اینکه در ۴ ماه دقیقاً یک بار خراب شود

lambda_ = 1
x_value = 1
poisson_prob = stats.poisson.pmf(x_value, mu=lambda_)

print(f"The probability of a computer crashing once every four months : {poisson_prob}")
#-------------------------------------------
# ج: احتمال اینکه در ۴ ماه دقیقاً دو بار خراب شود

lambda_ = 1
x_value = 2
poisson_prob = stats.poisson.pmf(x_value, mu=lambda_)

print(f"The probability of a computer crashing twice in four months : {poisson_prob}")
#-------------------------------------------
# د: احتمال اینکه در ۴ ماه دقیقاً سه بار خراب شود

lambda_ = 1
x_value = 3
poisson_prob = stats.poisson.pmf(x_value, mu=lambda_)

print(f"The probability of a computer crashing three times in four months : {poisson_prob}")