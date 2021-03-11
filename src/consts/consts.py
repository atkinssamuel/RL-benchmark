import numpy as np

# taking into account the annual vs. incremental rates of returns of stocks
def incremental(annual, N):
    daily = (annual + 1) ** (1 / 365) - 1
    return (daily + 1) ** (1 / N) - 1


class Simulation:
    num_days = 252
    increment_per_day = 1
    increments = num_days * increment_per_day
    dt = num_days / increments


class Stock:
    u_annual = 0.09
    u = incremental(u_annual, Simulation.increment_per_day)
    sigma_annual = 0.05
    sigma = 0.2 / np.sqrt(Simulation.increments)
    sigma = incremental(sigma_annual, Simulation.increment_per_day)
    s_0 = 5000

class Riskless:
    r_annual = 0.03
    r = incremental(r_annual, Simulation.increment_per_day)
    b_0 = 3000


