from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI()

# --- 1. PREPARASI MODEL AI (MACHINE LEARNING) ---
# Data Latihan: [Nilai Ujian, Kehadiran (%)], Label: 1 (Lulus), 0 (Tidak Lulus)
X_train = np.array([
    [85, 90],
    [40, 50],
    [75, 80],
    [30, 60],
    [90, 95],
    [50, 40]
])
y_train = np.array([1, 0, 1, 0, 1, 0])

# Melatih Model AI sederhana
model = LogisticRegression()
model.fit(X_train, y_train)

# Schema Input Data
class StudentInput(BaseModel):
    nama: str
    nilai_ujian: float
    kehadiran: float

# Koneksi Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_sekolah"
    )

# --- 2. ENDPOINT AI PREDIKSI & SIMPAN KE MYSQL ---
@app.post("/api/predict")
def predict_and_save(student: StudentInput):
    try:
        # Prediksi Menggunakan AI
        features = np.array([[student.nilai_ujian, student.kehadiran]])
        prediction = model.predict(features)[0]
        
        status_kelulusan = "LULUS" if prediction == 1 else "TIDAK LULUS"

        # Simpan Hasil Prediksi ke Database MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (nama, role) VALUES (%s, %s)"
        cursor.execute(query, (student.nama, f"Status AI: {status_kelulusan}"))
        conn.commit()
        
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return {
            "status": "Sukses",
            "id_record": new_id,
            "nama": student.nama,
            "nilai_ujian": student.nilai_ujian,
            "kehadiran": student.kehadiran,
            "hasil_prediksi_ai": status_kelulusan
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint GET Cek Data
@app.get("/api/users")
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nama, role FROM users")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        return {"error": str(e)}
    # --- 3. U (UPDATE) - Mengubah Data User ---
@app.put("/api/users/{user_id}")
def update_user(user_id: int, student: StudentInput):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET nama = %s WHERE id = %s"
        cursor.execute(query, (student.nama, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "Sukses", "message": f"Data ID {user_id} berhasil diubah"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- 4. D (DELETE) - Menghapus Data User ---
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "Sukses", "message": f"Data ID {user_id} berhasil dihapus"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))