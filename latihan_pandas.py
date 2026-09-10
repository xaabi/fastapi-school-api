import pandas as pd
import numpy as np

# 1. Data Dummy Siswa dengan Data Kosong (NaN)
data_lengkap = {
    "Nama": ["Budi", "Siti", "Joko", "Rini", "Sabiq"],
    "Jurusan": ["IPA", "IPS", "IPA", "IPS", "IPA"],
    "Nilai_MTK": [80, np.nan, 60, 75, 90],  # Siti nilainya kosong
    "Kehadiran": [90, 85, np.nan, 95, 100]  # Joko kehadirannya kosong
}

df = pd.DataFrame(data_lengkap)
print("--- 1. Data Asli (Ada Data Kosong/NaN) ---")
print(df)

# 2. Mengisi Data Kosong (Imputation) dengan Rata-Rata Column
df["Nilai_MTK"] = df["Nilai_MTK"].fillna(df["Nilai_MTK"].mean())
df["Kehadiran"] = df["Kehadiran"].fillna(df["Kehadiran"].mean())
print("\n--- 2. Data Setelah Data Kosong Diisi Rata-Rata ---")
print(df)

# 3. Groupby: Hitung Rata-Rata Nilai & Kehadiran Per Jurusan
rata_jurusan = df.groupby("Jurusan")[["Nilai_MTK", "Kehadiran"]].mean()
print("\n--- 3. Analisis Rata-Rata Per Jurusan ---")
print(rata_jurusan)