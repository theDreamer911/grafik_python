import matplotlib.pyplot as plt

labels = ['Dokter', 'Guru', 'Pegawai Kantor', 'Pedagang']
quantity = [3, 10, 12, 11]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.title('Daftar Pekerjaan Siswa Kelas XII-A')
plt.pie(quantity, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()
