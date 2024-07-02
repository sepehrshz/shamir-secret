import random

def shares_generator(S, t, n, p):
    coefficients = [S] + [random.randint(0, p - 1) for _ in range(t - 1)]
    
    shares = []
    for i in range(1, n + 1):
        y = sum([coefficients[j] * (i ** j) for j in range(t)]) % p
        shares.append((i, y))

    return shares

S_value = 2797
t_threshold = 8
n_shares = 7
p_prime = 8797

shares_generated = shares_generator(S_value, t_threshold, n_shares, p_prime)
print("Shares:", shares_generated)

def lagrange(x, y, p_val):
        secret = 0
        for i in range(len(x)):
            sum = 1
            for j in range(len(x)):
                if i != j:
                    sum *= (x[j]) * pow(x[j] - x[i], -1, p_val)
            secret += y[i] * sum
        return secret % p_val