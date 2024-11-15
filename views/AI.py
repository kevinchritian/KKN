import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image
import base64
import io
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageOps
import streamlit as st



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

st.set_page_config(page_title="My Webpage", page_icon=":tada:")

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
with open("style/style_sampah.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/style_AI.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
    <h1 class="text-center mt-3">Klasifikasi Sampah Organik dan Anorganik</h1>
""", unsafe_allow_html=True)

st.write('---')


# Memuat model sekali di luar blok if untuk menghemat memori
model = tf.keras.models.load_model("views/hello.h5")

# Fungsi untuk melakukan praproses gambar
def preprocess_image(image):
    # Mengonversi gambar ke format RGB
    image = image.convert("RGB")
    # Mengubah gambar ke ukuran (200, 200)
    image = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
    # Mengubah gambar ke numpy array dan rescale ke rentang 0-1
    img_array = np.array(image) / 255.0
    # Menambahkan dimensi agar sesuai dengan input model
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Streamlit tampilan
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['Kamera','Photo'],
        icons=["camera", "images"],
        menu_icon="cast",
        default_index=0,
        orientation='horizontal',
        styles={
            "nav-link-selected":{"background-color":"#17A2B8"}
        }
    )

if selected == 'Kamera':
    st.markdown("""
                <div class="mt-3">
                    <p>Langkah - langkah :</p>
                    <ol>
                        <li>Buka kamera pada handphone atau laptop.</li>
                        <li>Foto gambar sampah organik atau anorganik dengan mengklik Take Photo seperti botol plastik, daun kering, buah busuk, dan lain lain.</li>
                        <li>Setelah gambar difoto, muncul hasil gambar.</li>
                        <li>Klik pada button predict</li>
                        <li>Sistem akan menghasilkan output organik atau anorganik.</li>
                    </ol>
                </div>""", unsafe_allow_html=True)
    st.write('---')

    col1, col2, col3 = st.columns(3)
    with col2:  # Menempatkan di kolom tengah
        picture = st.camera_input("")
        
        if picture:
            # Menampilkan gambar yang diambil
            st.image(picture, use_column_width=True)
            # Membaca gambar dan melakukan praproses
            image = Image.open(picture)
            img_array = preprocess_image(image)
    if picture:
            if st.button("Prediksi"):
                img_array = preprocess_image(image)
                prediction = model.predict(img_array)
                if prediction[0] > 0.5:
                    result = "Anorganik"
                    color = "background-color: red; color: white;"
                else:
                    result = "Organik"
                    color = "background-color: green; color: white;"

                # Tampilkan hasil prediksi dengan latar belakang berwarna
                st.markdown(f"""
                    <div style="{color}; padding: 10px; border-radius: 5px; text-align: center;">
                        Hasil Prediksi: {result}
                    </div>
                    """, unsafe_allow_html=True)

if selected == "Photo":
    st.markdown("""
                <div class="mt-3">
                    <p>Langkah - langkah :</p>
                    <ol>
                        <li>Pilih Browser File</li>
                        <li>Pilih gambar yang ingin dipilih. (jpeg, jpg, atau png)</li>
                        <li>Selanjutnya akan muncul gambar yang dipilih dan button prediksi</li>
                        <li>Klik button prediksi</li>
                        <li>Sistem akan menghasilkan output organik atau anorganik.</li>
                    </ol>
                </div>""", unsafe_allow_html=True)
    st.write('---')

    # Mengatur file_uploader untuk hanya menerima satu file
    uploaded_file = st.file_uploader(
        "Choose an image file", type=["jpg", "png", "jpeg"], accept_multiple_files=False
    )

    # Proses hanya jika ada file yang diunggah
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.write("Filename:", uploaded_file.name)
        st.image(image, caption=uploaded_file.name, use_column_width=True)

        # Tombol untuk melakukan prediksi
        if st.button("Prediksi"):
            # Praktek praproses gambar dan prediksi
            img_array = preprocess_image(image)
            prediction = model.predict(img_array)
            if prediction[0] > 0.5:
                result = "Anorganik"
                color = "background-color: red; color: white;"
            else:
                result = "Organik"
                color = "background-color: green; color: white;"

            # Tampilkan hasil prediksi dengan latar belakang berwarna
            st.markdown(f"""
                <div style="{color}; padding: 10px; border-radius: 5px; text-align: center;">
                    Hasil Prediksi: {result}
                </div>
                """, unsafe_allow_html=True)