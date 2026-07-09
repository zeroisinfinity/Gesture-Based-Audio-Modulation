import time
from control.time_filter import TimeFilter
from control.velocity import VelocityFilter
from control.acceleration import AccelerationFilter

tf = TimeFilter()
vf = VelocityFilter()
af = AccelerationFilter()

print('Running...\n')

for frm in range(10):
    g = frm * 0.1
    t = time.time()

    g_out , g_prev , dt = tf.update(g,t)

    v, v_prev = vf.update(
        g_n=g,
        g_prev=g_prev,
        dt=dt
    )

    a = af.update(
        v=v,
        v_prev=v_prev,
        dt=dt
    )

    print(
        f"g={g_out:.2f} | "
        f"g_prev={g_prev:.2f} | "
        f"dt={dt:.5f} | "
        f"v={v:.2f} | "
        f"v_prev={v_prev:.2f} | "
        f"a={a:.2f}"
    )
    time.sleep(0.02)
