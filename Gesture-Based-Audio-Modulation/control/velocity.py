class VelocityFilter:

    def __init__(self, v_max=12.0):
        #max allowed vel
        self.v_max = v_max
        #prev vel (for acc)
        self.v_prev = 0.0

    def update(self , g_n , g_prev , dt):

        #prev vel
        v_prev = self.v_prev

        #raw vel
        v_raw = (g_n - g_prev) / dt

        #clamp vel
        v = max(
            -self.v_max,
            min(v_raw , self.v_max)
        )

        # save state
        self.v_prev = v

        return v , v_prev
