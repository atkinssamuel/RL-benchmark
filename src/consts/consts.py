# taking into account the annual vs. incremental rates of returns of stocks
def incremental(annual, N):
    return annual ** (1 / N)


class Simulation:
    timeframe = 100
    increments = timeframe * 1000
    dt = timeframe / increments


class Stock:
    u_annual = 1.09
    u = incremental(u_annual, Simulation.increments)
    sigma = 1.05
    s_0 = 50


class Riskless:
    r_annual = 1.03
    r = incremental(r_annual, Simulation.increments)
    b_0 = 30



