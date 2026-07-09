import time
from control.time_filter import TimeFilter
from control.velocity import VelocityFilter

tf = TimeFilter()
vf = VelocityFilter()

print('Running...\n')

for frm in range(10):
    g = frm * 0.1
    t = time.time()

    g_out , g_prev , dt = tf.update(g,t)

    v = vf.update(g_n = g_out ,
                  g_prev = g_prev,
                  dt = dt)

    print(
        f"g={g_out:.2f} | "
        f"g_prev={g_prev:.2f} | "
        f"dt={dt:.5f} | "
        f"v={v:.2f}"
    )
    time.sleep(0.02)
