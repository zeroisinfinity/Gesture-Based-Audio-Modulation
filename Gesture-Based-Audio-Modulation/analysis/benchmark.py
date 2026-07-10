import time
import pandas as pd

from config.constants import GESTURE
from config.parameters import *

from control.time_filter import TimeFilter
from control.velocity import VelocityFilter
from control.acceleration import AccelerationFilter
from control.jerk import JerkLimiter

from logs.results import results

tf = TimeFilter(
    eps_t=EPS_T,
    dt_safe=DT_SAFE,
    lambda_dt=LAMBDA_DT,
    dt_init=DT_INIT
)

vf = VelocityFilter(v_max=V_MAX)
af = AccelerationFilter()
jf = JerkLimiter(j_max=J_MAX)

for frame, g in enumerate(GESTURE):

    t = time.time()

    g, g_prev, dt = tf.update(g, t)

    v, v_prev = vf.update(
        g_n=g,
        g_prev=g_prev,
        dt=dt
    )

    a_raw = af.update(
        v=v,
        v_prev=v_prev,
        dt=dt
    )

    a, j = jf.update(
        a_raw=a_raw,
        dt=dt
    )

    results["frame"].append(frame)
    results["gesture"].append(g)
    results["gesture_prev"].append(g_prev)
    results["dt"].append(dt)
    results["velocity"].append(v)
    results["velocity_prev"].append(v_prev)
    results["acceleration_raw"].append(a_raw)
    results["acceleration"].append(a)
    results["jerk"].append(j)

    time.sleep(0.02)


df_alpha = pd.DataFrame(results)

print(df_alpha)

df_alpha.to_csv("analysis/results.csv", index=False)

print("\nSaved to analysis/results.csv")