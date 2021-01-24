from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [24.27, 23.18, 22.39, 8.41, 7.19, 6.62]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Bahasa Pemrograman Favorit (UMSU)')
ax.set_ylabel('Pengguna')
ax.set_xlabel('Bahasa')

ax.set_xticks(x)
ax.set_xticklabels(("Python", "JavaScript", "Java",
                    "C#", "PHP", "C++"))

plt.show()
