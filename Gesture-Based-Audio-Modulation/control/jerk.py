class JerkLimiter:

    def __init__(self, j_max=800.0):
        self.j_max = j_max
        self.a_prev = 0.0

    def update(self, a_raw, dt):

        # Raw jerk
        j_raw = (a_raw - self.a_prev) / dt

        # Clamp jerk
        j = max(
            -self.j_max,
            min(j_raw, self.j_max)
        )

        # Integrate bounded jerk
        a = self.a_prev + j * dt

        # Update acceleration state
        self.a_prev = a

        return a, j