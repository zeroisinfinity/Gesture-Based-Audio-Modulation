class AccelerationFilter:

    def __init__(self , a_max = 50.0):
        #max alloweed acc
        self.a_max = a_max
        #prev acc (later needed for jerk)
        self.a_prev = 0.0

    def update(self, v , v_prev , dt):
        #raw acc
        a_raw = (v - v_prev) / dt
        return a_raw