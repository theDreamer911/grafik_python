import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2.5 * np.pi * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (V)')

plt.title('Gelombang Sinus')
plt.grid(True)

plt.show()
