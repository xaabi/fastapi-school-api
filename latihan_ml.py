import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Bikin Dataset Dummy Siswa (Data Historis buat Latihan AI)
data = {
    "Nilai_MTK": [85, 90, 50, 45, 95, 60, 40, 80, 55, 75],
    "Kehadiran": [90, 95, 60, 50, 100, 70, 40, 85, 65, 80],
    "Status": [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]  # 1 = Lulus, 0 = Tidak Lulus
}

df = pd.DataFrame(data)

# 2. Pisahkan Feature (X) dan Target/Label (y)
X = df[["Nilai_MTK", "Kehadiran"]] # Fitur yang dipelajari AI
y = df["Status"]                    # Target jawaban yang ingin diprediksi

# 3. Bagi Data jadi Data Latih (80%) dan Data Uji (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Inisialisasi dan Latih Model Machine Learning (Decision Tree)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Uji Akurasi Model AI
y_pred = model.predict(X_test)
akurasi = accuracy_score(y_test, y_pred)
print(f"--- Akurasi Model AI: {akurasi * 100}% ---")

# 6. Tes Prediksi Siswa Baru (Misal: Nilai MTK 88, Kehadiran 90%)
siswa_baru = np.array([[88, 90]])
prediksi = model.predict(siswa_baru)
hasil = "LULUS" if prediksi[0] == 1 else "TIDAK LULUS"

print(f"\nPrediksi Siswa Baru (Nilai: 88, Kehadiran: 90%): {hasil}")