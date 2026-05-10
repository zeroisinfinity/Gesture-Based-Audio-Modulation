import math

from pandas.core.array_algos.take import take_nd


class TimeFilter:

    def __init__(self,
                 eps_t = 1e-6,
                 dt_safe = 0.05,
                 lambda_dt = 0.1,
                 dt_init = 0.016
                 ):

        # parameters
        self.eps_t = eps_t # e_t
        self.dt_safe = dt_safe # t_safe
        self.lambda_dt = lambda_dt # lambda

        # state
        self.prev_time = None # tn-1
        self.dt_prev = dt_init # t-init
        self.g_prev = 0.0 # gn-1

    def update(self,g_n,t_n):
        # first frame
        if self.prev_time is None:
            self.prev_time = t_n
            self.g_prev = g_n
            return g_n , self.dt_prev

        # raw dt
        dt_raw = t_n - self.prev_time # del_t

        # clamp dt
        dt_raw = max(
            self.eps_t,
            min(dt_raw , self.dt_safe)
        )

        # smooth dt
        dt = (
            self.lambda_dt * self.dt_prev
            +
            (1 - self.lambda_dt) * dt_raw
        )

        # sanitize dt
        if not math.isfinite(g_n):
            g_n = self.g_prev

        # update state
        self.prev_time = t_n
        self.dt_prev = dt
        self.g_prev = g_n

        return g_n,dt


