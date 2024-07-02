import random

def shares_generator(S, t, n, p):
    coefficients = [S] + [random.randint(0, p - 1) for _ in range(t - 1)]

S_value = 2797
t_threshold = 8
n_shares = 7
p_prime = 8797