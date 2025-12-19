from scipy import stats

#-------------------------------------------

p = 3/75 #==> 0.04
x_value = 6

geom_prob = stats.geom.pmf(x_value, p)

print(f"The probability that the first defective bulb is selected in the sixth : {geom_prob}")