class PredictionFilter:
    def __init__(self,
                 prediction_time = 0.02):
        # pred horizon(sec)
        self.prediction_time = prediction_time

    def update(self, g, v, a):

        # Const acc pred
        g_pred = (
            g +
            v * self.prediction_time +
            0.5 * a * (self.prediction_time**2)
        )

        return g_pred
        
