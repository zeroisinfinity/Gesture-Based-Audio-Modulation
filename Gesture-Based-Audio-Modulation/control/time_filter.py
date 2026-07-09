import math


class TimeFilter:

    def __init__(
        self,
        eps_t=1e-6,
        dt_safe=0.05,
        lambda_dt=0.1,
        dt_init=0.016
    ):

        # Parameters
        self.eps_t = eps_t
        self.dt_safe = dt_safe
        self.lambda_dt = lambda_dt

        # State
        self.prev_time = None
        self.dt_prev = dt_init
        self.g_prev = 0.0

    def update(self, g_n, t_n):

        # First frame
        if self.prev_time is None:
            self.prev_time = t_n
            self.g_prev = g_n
            return g_n, g_n, self.dt_prev

        # Raw timestep
        dt_raw = t_n - self.prev_time

        # Clamp timestep
        dt_raw = max(
            self.eps_t,
            min(dt_raw, self.dt_safe)
        )

        # Smooth timestep
        dt = (
            self.lambda_dt * self.dt_prev
            +
            (1 - self.lambda_dt) * dt_raw
        )

        # Reject invalid gesture values
        if not math.isfinite(g_n):
            g_n = self.g_prev

        # Save previous gesture before updating state
        g_prev = self.g_prev

        # Update state
        self.prev_time = t_n
        self.dt_prev = dt
        self.g_prev = g_n

        return g_n, g_prev, dt