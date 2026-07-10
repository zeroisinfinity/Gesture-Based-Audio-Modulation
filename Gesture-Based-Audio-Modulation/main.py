import time
import pandas as pd
from control.time_filter import TimeFilter
from control.velocity import VelocityFilter
from control.acceleration import AccelerationFilter
from control.jerk import JerkLimiter
from config.constants import GESTURE
from logs.results import res2
from control.prediction import PredictionFilter

tf = TimeFilter()
vf = VelocityFilter()
af = AccelerationFilter()
jf = JerkLimiter()
pf = PredictionFilter()

indx = 0

print("Running...\n")

for g in GESTURE:

    t = time.time()

    # Time
    g, g_prev, dt = tf.update(g, t)

    # Velocity
    v, v_prev = vf.update(
        g_n=g,
        g_prev=g_prev,
        dt=dt
    )

    # Raw acceleration
    a_raw = af.update(
        v=v,
        v_prev=v_prev,
        dt=dt
    )

    # Jerk limiter
    a, j = jf.update(
        a_raw=a_raw,
        dt=dt
    )

    g_pred = pf.update(
        g=g,
        v=v,
        a=a
    )

    res2["n"].append(indx)
    res2["g"].append(g)
    res2["g_prev"].append(g_prev)
    res2["dt"].append(dt)
    res2["v"].append(v)
    res2["v_prev"].append(v_prev)
    res2["a_raw"].append(a_raw)
    res2["a"].append(a)
    res2["j"].append(j)
    res2["g_pred"].append(g_pred)

    indx+=1

    time.sleep(0.02)

df = pd.DataFrame(res2)
df = df.round(4)
df.to_csv("analysis/res2.csv", index=False)
print(df)

