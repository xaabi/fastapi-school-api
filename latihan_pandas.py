import pandas as pd

# 1. Bikin Data Dummy Siswa (Bentuk Dictionary)
data_siswa = {
    "Nama": ["Budi", "Siti", "Joko", "Rini", "Sabiq"],
    "Nilai_MTK": [80, 95, 60, 75, 90],
    "Kota": ["Jakarta", "Bandung", "Jakarta", "Surabaya", "Jakarta"]
}

# 2. Ubah jadi DataFrame Pandas (Tabel)
df = pd.DataFrame(data_siswa)
print("--- Tabel Data Siswa ---")
print(df)

# 3. Filter Data (Hanya siswa dari Jakarta)
df_jakarta = df[df["Kota"] == "Jakarta"]
print("\n--- Siswa Asal Jakarta ---")
print(df_jakarta)

# 4. Buat Kolom Baru Berdasarkan Kondisi (Lulus jika nilai MTK >= 80)
df["Status"] = df["Nilai_MTK"].apply(lambda x: "Lulus" if x >= 80 else "Remidi")
print("\n--- Tabel Akhir dengan Status Lulus ---")
print(df)