# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Dalam proyek ini, dilakukan analisis terhadap data siswa untuk memahami faktor-faktor yang berkontribusi terhadap keberhasilan akademik maupun potensi dropout. Proyek ini bertujuan untuk membantu institusi membuat keputusan berbasis data dalam merancang bimbingan yang efektif dan strategi peningkatan layanan pendidikan.

### Permasalahan Bisnis

Berdasarkan latar belakang yang ditulis sebelumnya, banyak siswa yang tidak menyelesaikan pendidikannya atau dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Berikut adalah pertanyaan yang akan dijawab untuk menyelesaikan permasalahan tersebut.

- Bagaimana memprediksi status mahasiswa (Dropout, Graduate, atau Enrolled) berdasarkan data historis mereka?
- Faktor-faktor apa saja yang paling memengaruhi mahasiswa untuk dropout?
- Bagaimana institusi dapat memantau risiko dropout secara real time menggunakan dashboard visual?
- Apakah karakteristik tertentu seperti prestasi akademik awal, latar belakang ekonomi, atau demografi dapat digunakan sebagai indikator prediksi dropout?

### Cakupan Proyek

Jaya Jaya Institut ingin mengatahui dengan cepat siswa yang berpotensi tidak menyelesaikan pendidikannya atau dropout. Untuk memprediksi kemungkinan dropout siswa dengan cepat dan efisien, kita akan membuat sebuah dashboard menggunakan streamlit yang dapat memprediksi status dari siswa berdasarkan inputan yang dimasukkan. Selain itu, kita juga akan membuat sebuah business dashboard yang menampilkan visualisasi data siswa yang dapat memantau faktor-faktor yang menyebabkan tingginya jumlah siswa yang tidak menyelesaikan pendidikannya.

Untuk menyelesaikan permasalahan bisnis ini, proyek akan mencakup tahapan-tahapan berikut:

1. **Persiapan Environment**: Melakukan persiapan environment seperti membuat virtual environment, memilih library yang digunakan, dll.
2. **Data Understanding**: Memahami isi atau fitur fitur yang terdapat pada dataset yang disediakan. Kegiatan ini meliputi pengecekan missing value dan data duplikat, melihat statistik data, dan melihat visualisasi hubungan antara fitur dan target. Visualisasi data dilakukan untuk melihat fitur fitur yang cukup berpengaruh terhadap status siswa.
3. **Data Preparation**: Pada tahap ini, fitur-fitur yang memiliki korelasi cukup baik dengan status akan dipilih dan menghasilkan sebuah dataframe baru. Dataframe tersebut kemudian akan dibagi menjadi data training dan data testing. Lalu, data tersebut akan distandarisasi menggunakan standar scaler agar skalanya sama.
4. **Pembuatan Model**: Dilakukan pelatihan dan pengujian terhadap beberapa model klasifikasi yaitu logistic regression, random forest, gradient boosting, dan SVM.
5. **Evaluation**: Model terbaik akan dipilih berdasarkan nilai F1 score tertinggi. Model tersebut yang akan digunakan untuk pembuatan dashboard menggunakan streamlit.
6. **Pembuatan Dashboard Streamlit**: Membuat model prediksi interaktif menggunakan streamlit untuk memprediksi status siswa dengan cepat dan efisien.
7. **Pembuatan Business Dashboard**: Mengembangkan dashboard bisnis menggunakan Tableau untuk memberikan wawasan yang dapat diakses secara cepat dan intuitif.

### Persiapan

Sumber data: [Dicoding](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

```
# 1. Buat direktori proyek
mkdir proyek-dropout-prediction
cd proyek-dropout-prediction

# 2. Buat virtual environment
python -m venv venv

# 3. Aktifkan virtual environment
# Untuk Windows Powershell:
venv\Scripts\activate.ps1

# 4. Install library yang diperlukan
pip install -r requirements.txt
```

## Business Dashboard

Untuk membantu memahami faktor-faktor yang mempengaruhi tingginya jumlah siswa yang dropout, dibuat sebuah dashboard interaktif yang menampilkan metrik dan visualisasi penting terkait kondisi karyawan dan attrition. Dashboard ini dibuat menggunakan **Tableau**, dengan total **4424 siswa** dan **32%** persentase siswa yang dropout. Penjelasan singkat mengenai dashboard tersebut :

- **Jumlah Siswa dan Persentase Dropout**

  - **Jumlah total siswa:** 4424
  - **Persentase siswa yang berhasil lulus:** 49,93%
  - **Persentase siswa yang dropout:** 32,12%

- **Jumlah Siswa Berdasarkan Status**

  - **Graduate:** 2209
  - **Enrolled:** 794

- **Pada application mode**, siswa yang dropout memiliki application mode di atas 23 tahun, sedangkan yang graduate memiliki application mode fase pertama - general contingent.

- **Semester Curicular Units Avg Grade dan Units Approved**

  - Pada average grade, siswa yang dropout memiliki grade yang lebih rendah daripada graduate baik pada semester 1 mupun semester keduanya. Hal ini menjelaskan bahwa siswa dengna nilai rendah cenderung untuk dropout.
  - Pada units approved, siswa yang keluar atau dropout memiliki units yang di approved sangat rendah dibandingkan yang graduate, baik pada semester pertama maupun semester kedua. Hal ini mengidikasikan siswa yang memiliki units lebih sedikit cenderung untuk dropout.

- **Tutition fees update vs Status**

  - **No:** Pembayaran yang tidak dilakukan menyuebabkan siswa yang dropout lebih banyak, bahkan mayoritas siswa yang tidak melanjutkan pembayaran keluar dari institut. Hal ini mengindikasikan siswa yang tidak mampu membayar biaya pendidikan, sehingga memilih mundur. Institur seharusnya bisa memberikan bantuan atau beasiswa untuk siswa yang kesulitan melakukan pembayaran uang pendidikan.
  - **Yes:** Siswa yang melakukan pembayaran secara teratur, cenderung untuk menyelesaikan pendidikannya sampai lulus, walaupun ada siswa yang tetap tidak menyelesaikan pendidikannya.

- **Displace vs Status**
  Pada kolom ini, tidak terlihat perbedaan yang mencolok dari grafik yang disajikan, sehingga displace tidak terlalu berpengaruh terhadap status akhir siswa.

- **Debtor vs Status**

  - **No:** Siswa yang tidak mengutang cenderung untuk menyelesaikan pendidikannya. Walaupun masih ada siswa yang tidak menyelesaikan pendidikannya.
  - **Yes:** Siswa yang memiliki utang mayoritas tidak dapat menyelesaikan pendidikannya. Hal ini dapat menjadi penyebab siswa tersebut tidak membayar uang pendidikan dikarenakan memiliki utang yang harus dibayar.

- **Scholarship Holder vs Status**

  - **No:** Siswa tanpa beasiswa (No) memiliki proporsi dropout yang lebih besar. Hal ini mengindikasikan bahwa ketidakmampuan finansial mungkin menjadi salah satu penyebab utama dropout.
  - **Yes:** Grafik menunjukkan bahwa jumlah graduate paling tinggi berasal dari kelompok penerima beasiswa. Ini menunjukkan korelasi positif antara penerimaan beasiswa dan keberhasilan studi.

- **Avg Admission Grade vs Status**  
  Dari grafik yang telah dibuat, dapat dilihat bahwa siswa yang berhasil graduate memiliki nilai rata-rata tinggi dibandingkan siswa yang dropout. Mahasiswa dengan nilai masuk lebih rendah berisiko tinggi mengalami dropout, bisa jadi karena kesiapan akademik yang kurang.

- **Enrollment Age vs Status**  
  Usia pendaftaran tertinggi pada mahasiswa dropout (26 tahun). Mahasiswa graduate memiliki usia masuk lebih muda (~21 tahun). Semakin tua usia saat mendaftar, semakin besar kemungkinan untuk dropout, bisa terkait tanggung jawab lain di luar akademik.

**Link Dashboard:** [Tableau](https://public.tableau.com/shared/7H2NFTQ82?:display_count=n&:origin=viz_share_link)

## Menjalankan Sistem Machine Learning

Prototipe dibuat menggunakan streamlit. Berikut adalah cara menjalankan sistem machine learning tersebut di lingkungan lokal:

```
1. Pastikan ada file app.py yang telah dibuat sebelumnya.

2. Buat virtual environment agar proyek terisolasi dari lingkungan  lain :
python -m venv venv

3. Aktifkan virtual environment
Untuk Windows Powershell:
venv\Scripts\activate.ps1

4. Install library yang diperlukan
pip install -r requirements.txt

5. Jalankan app.py
streamlit run app.py

```

Link streamlit cloud :
[Streamlit](https://students-dropout-prediction-project.streamlit.app/)

## Conclusion

Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi status akademik Siswa, khususnya kecenderungan mereka untuk dropout dari institusi pendidikan. Dengan memanfaatkan machine learning (model Random Forest), data historis siswa dapat dipelajari untuk memprediksi kemungkinan dropout dengan cukup akurat.

Berdasarkan hasil analisis dan model prediktif yang dibangun, diperoleh beberapa insight penting:

- Siswa dengan nilai rendah pada semester awal (baik dari sisi grade maupun jumlah mata kuliah yang lulus) memiliki kecenderungan lebih tinggi untuk dropout.
- Faktor sosial seperti tidak mendapatkan beasiswa, tidak membayar biaya kuliah tepat waktu, dan status sebagai debtor juga berkorelasi dengan tingkat dropout yang lebih tinggi.
- Siswa yang masuk pada usia lebih tua (misalnya, Over 23 years old) juga menunjukkan kecenderungan dropout yang lebih tinggi dibandingkan kelompok usia muda.
- Terdapat perbedaan distribusi status akademik berdasarkan Application Mode, di mana siswa yang masuk melalui jalur umum pada fase pertama cenderung memiliki hasil lebih baik daripada jalur transfer atau perubahan jurusan.

Dengan hasil ini, institusi kini dapat lebih proaktif dalam memantau dan memberi dukungan kepada siswa berisiko tinggi sejak dini.

### Rekomendasi Action Items

Rekomendasi action yang dapat dilakukan berdasarkan kesimpulan sebelumnya yaitu:

- **Bimbingan Dini Berdasarkan Prediksi.**
  Gunakan model prediksi secara berkala (misal setiap akhir semester) untuk mendeteksi siswa dengan risiko tinggi dropout Prioritaskan siswa yang memiliki nilai rendah di semester pertama dan tidak membayar biaya kuliah tepat waktu untuk mendapatkan perhatian khusus.
- **Program Pendampingan Akademik**  
  Buat program mentoring atau tutoring bagi siswa tahun pertama, terutama yang memiliki nilai rendah. Libatkan siswa tingkat akhir atau pengajar sebagai mentor akademik.
- **Dukungan Keuangan yang Lebih Tertarget**
  Tawarkan bantuan keuangan atau program beasiswa tambahan bagi siswa yang masuk kategori risiko tinggi dan tidak mampu. Evaluasi ulang kebijakan beasiswa agar lebih berbasis kebutuhan, bukan hanya prestasi.
- **Buat sistem** notifikasi atau reminder otomatis untuk siswa agar memenuhi kewajiban akademik dan administrasi tepat waktu.
