import numpy as np

# Set Seed supaya angka acaknya konsisten setiap kali di-run
np.random.seed(42)

# 1. Bikin Data Acak 100 Nilai Ujian Siswa (Rentang 50 - 100)
nilai_ujian = np.random.randint(50, 101, size=100)
print("--- 10 Nilai Siswa Pertama dari Total 100 ---")
print(nilai_ujian[:10])

# 2. Analisis Statistik Data (Penting untuk Preprocessing Data AI)
print("\n--- Analisis Statistik Data ---")
print("Rata-rata (Mean)      :", np.mean(nilai_ujian))
print("Standar Deviasi (Std) :", np.std(nilai_ujian))

# 3. Normalisasi Data (Skala 0 sampai 1) -> Trik Wajib AI Engineer!
# Rumus Min-Max Scaling: (x - min) / (max - min)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)
nilai_normal = (nilai_ujian - nilai_min) / (nilai_max - nilai_min)

print("\n--- 5 Data Pertama Setelah Di-normalisasi (Skala 0 - 1) ---")
print(np.round(nilai_normal[:5], 3))