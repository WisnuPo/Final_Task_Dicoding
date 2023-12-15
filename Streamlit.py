import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Analisis Data Bike Sharing Dataset")

# Membaca dataset
dataset = pd.read_csv('day.csv')

# Menampilkan deskripsi dataset
st.subheader("Deskripsi Dataset")
st.write(dataset.describe())

# Menambahkan pemilihan variabel untuk ditampilkan
selected_variable = st.selectbox("Pilih Variabel:", dataset.columns)

# Menampilkan histogram menggunakan Matplotlib
fig, ax = plt.subplots()
ax.hist(dataset[selected_variable], bins=30, color='skyblue', alpha=0.7)
ax.set_title('Visualisasi')
ax.set_xlabel(selected_variable)
ax.set_ylabel('Frequency')

# Menambahkan keterangan pada histogram
st.pyplot(fig)
st.caption(f'Histogram untuk variabel {selected_variable}')

# Menambahkan pemilihan kolom untuk regresi
st.subheader("Visualisasi Regresi")
selected_x = st.selectbox("Pilih Variabel X untuk Regresi:", dataset.columns)
selected_y = st.selectbox("Pilih Variabel Y untuk Regresi:", dataset.columns)

# Menampilkan visualisasi regresi menggunakan Seaborn
if selected_x != selected_y:
    sns.regplot(x=selected_x, y=selected_y, data=dataset, scatter_kws={'alpha': 0.5})
    st.pyplot()
    st.caption(f'Regresi antara {selected_x} dan {selected_y}')
else:
    st.warning("Pilih dua variabel yang berbeda untuk regresi.")

# Menambahkan teks informatif
st.markdown("""
    Streamlit ini digunakan untuk membuat sebuah dashboard analisis dataset bike sharing. Saya menggunakan beberapa fitur, termasuk selectbox untuk 
            menentukan kolom mana yang akan dibuat visualisasinya. Pada dashboard ini, disediakan dua jenis visualisasi, yaitu histogram dan regresi. Kedua jenis visualisasi
            ini digunakan untuk menjawab pertanyaan bisnis yang sudah dijelaskan sebelumnya.
""")
