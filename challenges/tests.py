import statistics

my_normal = statistics.NormalDist()

print(my_normal.samples(5))

print(my_normal.pdf(1))

print(my_normal.cdf(1))
