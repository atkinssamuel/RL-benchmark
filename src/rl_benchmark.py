import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# matplotlib.use('Agg')
import datetime
import sys

from src.consts.consts import Stock, Riskless, Simulation


def stock_update(s_cur, u, sigma, dt):
    return s_cur + \
           (u - 1) * s_cur * dt + \
           (sigma - 1) * s_cur * np.sqrt(dt) * np.random.normal(0, 1, 1)


def riskless_update(b_cur, r, dt):
    return b_cur + (r - 1) * b_cur * dt


def portfolio_update(x_cur, u, a_t, r, sigma, dt):
    return (u * a_t + r * (1 - a_t)) * x_cur * dt + sigma * a_t * x_cur * np.sqrt(dt) * np.random.normal(0, 1, 1)


def dependent_portfolio_update(b_next, s_next, alpha):
    return (1 - alpha) * b_next + alpha * s_next


def alpha_analytical(u, r, sigma, p):
    return (u - r)/(np.square(sigma) * (1 - p))


def simulate_stock_history():
    s = np.zeros(shape=(Simulation.increments,))
    b = np.zeros(shape=(Simulation.increments,))
    t = np.zeros(shape=(Simulation.increments,))

    s[0] = Stock.s_0
    b[0] = Riskless.b_0

    for i in range(1, Simulation.increments):
        s[i] = stock_update(s[i-1], Stock.u, Stock.sigma, Simulation.dt)
        b[i] = riskless_update(b[i-1], Riskless.r, Simulation.dt)
        t[i] = t[i-1] + Simulation.dt

    return s, b, t


def simulate_constant_alpha(s, b, alpha):
    return (1 - alpha) * b + alpha * s


def plot_simulation(s, b, x, t):
    plt.figure()

    font = {'font.family': 'serif',
            'font.size': 14,
            'font.weight': 'normal'}
    plt.rcParams.update(font)

    plt.title("Portfolio Management Strategy Simulation")

    plt.plot(t, s, label="Risky Asset", color="orange")
    plt.plot(t, b, label="Risk-Free Asset", color="brown")
    plt.plot(t, x, label="Portfolio Value", color="green")



    plt.ylabel("USD")
    plt.xlabel("Time (Days)")
    plt.legend()
    plt.grid(True)
    plt.show()
    return

if __name__ == "__main__":
    # computing optimal alpha for p = 0.5
    p = 0.5
    alpha = alpha_analytical(Stock.u_annual, Riskless.r_annual, Stock.sigma, p)

    s, b, t = simulate_stock_history()
    x = simulate_constant_alpha(s, b, alpha)

    plot_simulation(s, b, x, t)


