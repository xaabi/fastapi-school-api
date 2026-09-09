import numpy as np

# 1. Bikin Matriks 2D (3 Siswa x 2 Mata Pelajaran: [Matematika, Bahasa])
# Baris 1: Siswa A (Nilai 80, 90)
# Baris 2: Siswa B (Nilai 70, 85)
# Baris 3: Siswa C (Nilai 60, 75)
nilai_siswa = np.array([
    [80, 90],
    [70, 85],
    [60, 75]
])

print("--- Matriks Nilai Siswa (3x2) ---")
print(nilai_siswa)

# 2. Cek Bentuk Matriks (Shape)
print("\nUkuran Matriks (Baris, Kolom):", nilai_siswa.shape)

# 3. Slicing/Mengambil Data Spesifik
# Ambil nilai Matematika saja (Kolom pertama / indeks 0 untuk semua baris)
nilai_mtk = nilai_siswa[:, 0]
print("Nilai Matematika Semua Siswa:", nilai_mtk)

# 4. Rata-rata Nilai per Mata Pelajaran (Axis 0 = Vertikal / Kolom)
rata_per_matpel = np.mean(nilai_siswa, axis=0)
print("Rata-rata [Matematika, Bahasa]:", rata_per_matpel)