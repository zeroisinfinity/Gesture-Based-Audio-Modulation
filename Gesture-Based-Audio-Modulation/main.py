import time
from control.time_filter import TimeFilter

tf = TimeFilter()

print('running...\n')

for frm in range(10):
    g = float("nan") if frm == 5 else frm * 0.1
    t = time.time()

    g_out , dt = tf.update(g,t)
    print(f'g={g_out:.2f} | dt={dt:.6f}')
    time.sleep(0.02)
