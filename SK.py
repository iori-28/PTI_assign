"""
Buat program tentang nilai mahasiswa untuk semester 1 menggunakan Array. Program dibuat dengan Bahasa Pemrograman Python
"""

# Array mata_kuliah berisi daftar nama mata kuliah untuk semester 1.

subjects = [
    'Statistika & Probabilitas', 
    'Algoritma', 
    'Pendidikan Pancasila', 
    'Bahasa Inggris',
    'Pendidikan Agama',
    'Kalkulus',
    'Pengantar Teknologi Informasi'
]

# Array data_mahasiswa digunakan untuk menyimpan nama dan nilai setiap mahasiswa.

student_data = [
    {"name": "A", "score": {}},
    {"name": "B", "score": {}},
    {"name": "C", "score": {}},
    {"name": "D", "score": {}}
]

# Fungsi hitung_nilai_akhir menghitung nilai akhir untuk setiap mata kuliah berdasarkan bobot tugas, UTS, dan UAS.

def count_final_score(kehadiran, tugas, uts, uas):
    # Bobot: Kehadiran 15%, Tugas 20%, UTS 30%, UAS 35%
    return (kehadiran * 0.15) + (tugas * 0.2) + (uts * 0.3) + (uas * 0.35)

def determine_letter_value(final_score):
    if final_score >= 85:
        return 'A'
    elif final_score >= 80:
        return 'A-'
    elif final_score >= 75:
        return 'B+'
    elif final_score >= 70:
        return 'B'
    elif final_score >= 65:
        return 'B-'
    elif final_score >= 60:
        return 'C+'
    elif final_score >= 55:
        return 'C'
    elif final_score >= 40:
        return 'D'
    else:
        return 'E'

# Setiap mahasiswa akan memasukkan nilai tugas, UTS, dan UAS untuk setiap mata kuliah, yang kemudian dihitung nilai akhirnya.

for student in student_data:
    print(f"Masukkan nilai untuk {student['name']}:")
    for subject in subjects:
        kehadiran = float(input(f"  {subject} - Kehadiran Score: "))
        tugas = float(input(f"  {subject} - Tugas Score: "))
        uts = float(input(f"  {subject} - UTS Score: "))
        uas = float(input(f"  {subject} - UAS Score: "))
        
        final_score = count_final_score(kehadiran, tugas, uts, uas)
        letter_value = determine_letter_value(final_score)
        
        student['score'][subject] = {
            'final_score': final_score,
            'letter_value': letter_value
        }

# Program menampilkan nilai akhir dan huruf nilai untuk setiap mata kuliah dan mahasiswa.

print("\nNilai Akhir dan Huruf Nilai:")
for student in student_data:
    print(f"\n{student['name']}:")
    for subject, score_data in student['score'].items():
        print(f"  {subject} - Nilai Akhir: {score_data['final_score']:.2f}, Huruf Nilai: {score_data['letter_value']}")