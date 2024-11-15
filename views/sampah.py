import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image
import base64
import io

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')


hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem;}
</style>
"""

# Memastikan CSS diterapkan langsung saat aplikasi dijalankan
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open("style/style_sampah.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


st.markdown("""
            <div>
                <h1 class="text-center mt-3">
                    Sampah
                </h1>
            </div>""", unsafe_allow_html=True)


st.markdown("""
    <div class="container-fluid">
        <div class="container">
            <div>
                <p>
                    Pengertian sampah pada umumnya merupakan sisa atau
                    hasil dari kegiatan manusia sehari-hari yang tidak lagi 
                    bisa dimanfaatkan. Dapat ditemui di berbagai tempat dengan 
                    jenis dan wujud yang berbeda-beda. Sampah organik dan anorganik 
                    adalah 2 jenis sampah yang sering dibahas pada umumnya.
                    Materi tentang sampah sangat penting untuk di ketahui. 
                    Selama manusia masih beraktivitas, sampah menjadi salah satu hal 
                    yang akan konsisten dihasilkan dan terus bertambah. Untuk itu 
                    diperlukan upaya penanganan sampah secara tepat dan bertanggung 
                    jawab agar volume sampah dapat dikurangi dan mencegahnya menumpuk 
                    mencemari lingkungan.
                    Lalu, bagaimana sebenarnya sampah didefinisikan atau 
                    diartikan? Apa saja ya hal terkait sampah yang perlu banyak 
                    orang ketahui?
                    Dan yang terpenting, apa saja jenis jenis sampah, apa 
                    definisi secara umum, apa saja macam macam sampah yang 
                    terkait material? Simak artikel ini hingga selesai yuk!
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

