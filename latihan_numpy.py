import numpy as np

# 1. Membuat Array 1 Dimensi (Vektor)
data_nilai = np.array([70, 85, 90, 65, 100])
print("Array Nilai:", data_nilai)

# 2. Operasi Matematika Langsung (Bonus nilai 5 poin ke semua siswa)
nilai_plus = data_nilai + 5
print("Nilai Setelah Bonus (+5):", nilai_plus)

# 3. Statistik Dasar (Khas Pemrosesan Data AI)
print("Nilai Rata-rata:", np.mean(data_nilai))
print("Nilai Tertinggi:", np.max(data_nilai))
print("Nilai Terendah :", np.min(data_nilai))

# 4. Filter Data (Ambil yang nilainya di atas 75)
lulus = data_nilai[data_nilai > 75]
print("Nilai yang Lulus (>75):", lulus)