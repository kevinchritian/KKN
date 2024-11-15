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
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem; padding-bottom:0rem;}
</style>
"""

# Memasukkan CSS custom ke dalam aplikasi
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def convert_image_to_base64(image):
    # Konversi gambar ke RGB jika dalam mode RGBA (misalnya PNG dengan transparansi)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # Simpan gambar dalam buffer sebagai JPEG
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    
    # Encode gambar ke base64
    image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return image_base64


# Memuat gambar dengan PIL
image = Image.open('images/anorganik.png')
image_base64 = convert_image_to_base64(image)

images_banner = Image.open('images/about.jpg')
image_base65 = convert_image_to_base64(images_banner)


# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/style_about.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Banner

# Membaca gambar dan mengonversinya ke Base64
with open("images/logo.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()




# Menyisipkan gambar Base64 ke dalam tag <img>
st.markdown(f"""
<style>
    .try {{
        background-image: linear-gradient(to left, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.7)), url('data:image/jpg;base64,{image_base65}');
        background-reapat: no-reapet;
        background-size: cover;
        background-position:center;
    }}
</style>
<div class="container-fluid banner try">
    <div class="container banner-content d-flex align-items-center justify-content-center justify-content-sm-start">
        <div class="about">
            <h1 class="txt-banner">
                Tentang <span class="txt-banner2">Kami</span>
            </h1>
            <hr class="garis-banner">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# latar belakang
images_logo = Image.open('images/logo.png')
image_base77 = convert_image_to_base64(images_logo)

st.markdown(f"""
    <div class="container-fluid">
        <h2 class="pt-5 text-center">Latar Belakang</h2>
        <hr class="mb-5 custom-hr">
            <div class="container col-md-9">     
                <div>
                    <div class="logo mb-4">
                        <img src="data:image/jpeg;base64,{image_base77}">
                    </div>
                    <p class="latar-belakang-txt">
                        NatureAIClassify adalah aplikasi inovatif berbasis kecerdasan buatan yang hadir untuk membantu masyarakat 
                        dalam menghadapi tantangan besar terkait pengelolaan sampah. Dalam beberapa tahun terakhir, jumlah sampah, 
                        baik organik maupun anorganik, terus meningkat, sehingga memerlukan metode pengelolaan yang lebih tepat dan 
                        berkelanjutan. NatureAIClassify hadir sebagai solusi yang dapat mempercepat dan mempermudah proses pemilahan 
                        sampah dengan menggunakan model AI berbasis klasifikasi gambar. Aplikasi ini memungkinkan pengguna untuk mengidentifikasi 
                        jenis sampah hanya dengan mengambil fotonya, sehingga proses pemilahan tidak lagi memerlukan pengetahuan mendalam atau tenaga 
                        besar dari pengguna.
                    </p>
                    <p class="latar-belakang-txt">
                        Dengan Artificial Intelligence, NatureAIClassify mampu membedakan sampah organik, seperti sisa makanan dan dedaunan, dari sampah 
                        anorganik, seperti plastik dan kaleng. Hal ini sangat membantu dalam proses pengelolaan sampah, karena setiap jenis sampah 
                        memerlukan metode penanganan yang berbeda. Sampah organik dapat diolah menjadi kompos atau digunakan untuk kebutuhan pertanian, 
                        sedangkan sampah anorganik sering kali membutuhkan proses daur ulang atau pengolahan khusus. Aplikasi ini juga memberikan saran 
                        pengelolaan bagi setiap jenis sampah yang teridentifikasi, sehingga pengguna memiliki panduan langsung untuk langkah selanjutnya.
                    </p>
                    <p class="latar-belakang-txt pb-5">
                        Lebih dari sekadar website, NatureAIClassify adalah alat edukasi dan pemberdayaan masyarakat yang bertujuan meningkatkan kesadaran 
                        tentang pentingnya memilah sampah. Dengan antarmuka yang intuitif dan mudah digunakan, website ini dapat diakses oleh berbagai kalangan 
                        masyarakat, mulai dari anak-anak hingga orang dewasa. NatureAIClassify bukan hanya berperan sebagai alat bantu teknis, tetapi juga sebagai 
                        pendukung dalam upaya menjaga lingkungan yang lebih bersih dan sehat. Diharapkan, dengan NatureAIClassify, semakin banyak orang yang termotivasi 
                        untuk memilah sampah dan berkontribusi dalam menjaga kebersihan lingkungan, mengurangi polusi, serta melindungi ekosistem dari dampak buruk sampah 
                        yang tidak terkelola dengan baik.
                    </p>
                </div>   
            </div>
    </div>
""", unsafe_allow_html=True)


images_recycle = Image.open('images/recycle.jpg')
image_base69 = convert_image_to_base64(images_recycle)

images_pencemaran = Image.open('images/pencemaran.jpg')
image_base70 = convert_image_to_base64(images_pencemaran)

images_masyarakat = Image.open('images/masyarakat.jpg')
image_base71 = convert_image_to_base64(images_masyarakat)

images_AI = Image.open('images/AI.jpg')
image_base72 = convert_image_to_base64(images_AI)

st.markdown(f"""
    <div class="container-fluid tujuan py-5">
        <h2 class="text-center">Tujuan</h2>
        <hr class="mb-5 custom-hr">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="card mb-3">
                        <div class="row g-0 h-100">
                            <div class="col-md-4 col-4 d-flex align-items-center justify-content-center">
                                <img src="data:image/jpeg;base64,{image_base72}" class="img-fluid rounded-start card-img">
                            </div>
                            <div class="col-8 col-md-8 d-flex align-items-center">
                                <div class="card-body text-center">
                                    <h5 class="card-title title-txt">Memfasilitasi Pemilahan Sampah yang Akurat</h5>
                                    <p class="card-text tujuan-txt">Menyediakan teknologi yang mampu mengidentifikasi dan membedakan sampah organik dan anorganik secara tepat, membantu pengguna dalam memahami dan mempraktikkan pemilahan sampah berdasarkan jenisnya.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card mb-3">
                        <div class="row g-0 h-100">
                            <div class="col-md-4 col-4 d-flex align-items-center justify-content-center">
                                <img src="data:image/jpeg;base64,{image_base71}" class="img-fluid rounded-start card-img">
                            </div>
                            <div class="col-8 col-md-8 d-flex align-items-center">
                                <div class="card-body text-center">
                                    <h5 class="card-title title-txt">Memfasilitasi Pemilahan Sampah yang Akurat</h5>
                                    <p class="card-text tujuan-txt">Menyediakan teknologi yang mampu mengidentifikasi dan membedakan sampah organik dan anorganik secara tepat, membantu pengguna dalam memahami dan mempraktikkan pemilahan sampah berdasarkan jenisnya.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card mb-3">
                        <div class="row g-0 h-100">
                            <div class="col-md-4 col-4 d-flex align-items-center justify-content-center">
                                <img src="data:image/jpeg;base64,{image_base69}" class="img-fluid rounded-start card-img">
                            </div>
                            <div class="col-8 col-md-8 d-flex align-items-center">
                                <div class="card-body text-center">
                                    <h5 class="card-title title-txt">Memfasilitasi Pemilahan Sampah yang Akurat</h5>
                                    <p class="card-text tujuan-txt">Menyediakan teknologi yang mampu mengidentifikasi dan membedakan sampah organik dan anorganik secara tepat, membantu pengguna dalam memahami dan mempraktikkan pemilahan sampah berdasarkan jenisnya.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card mb-3">
                        <div class="row g-0 h-100">
                            <div class="col-md-4 col-4 d-flex align-items-center justify-content-center">
                                <img src="data:image/jpeg;base64,{image_base70}" class="img-fluid rounded-start card-img">
                            </div>
                            <div class="col-8 col-md-8 d-flex align-items-center">
                                <div class="card-body text-center">
                                    <h5 class="card-title title-txt">Memfasilitasi Pemilahan Sampah yang Akurat</h5>
                                    <p class="card-text tujuan-txt">Menyediakan teknologi yang mampu mengidentifikasi dan membedakan sampah organik dan anorganik secara tepat, membantu pengguna dalam memahami dan mempraktikkan pemilahan sampah berdasarkan jenisnya.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            <div>
        </div>
    </div>
""", unsafe_allow_html=True)


# Manfaat
images_manfaat1 = Image.open('images/1.jpg')
image_base73 = convert_image_to_base64(images_manfaat1)

images_manfaat2 = Image.open('images/2.png')
image_base74 = convert_image_to_base64(images_manfaat2)

images_manfaat3 = Image.open('images/3.png')
image_base75 = convert_image_to_base64(images_manfaat3)

images_manfaat4 = Image.open('images/4.png')
image_base76 = convert_image_to_base64(images_manfaat4)

st.markdown(f"""
    <div class="container-fluid py-5">
        <h2 class="text-center">Manfaat</h2>
        <hr class="mb-5 custom-hr">
        <div class="container col-10">
            <div class="row">
                <div class="col-lg-6 col-md-6">
                    <div class="card d-flex align-items-center justify-content-center text-center kartu-manfaat mb-1">
                            <img src="data:image/jpeg;base64,{image_base73}" class="gambar1">
                            <p class="fw-bold">Peningkatan Kesadaran Lingkungan</p>
                            <p class="manfaat col-9 col-md-11 col-lg-8">WasteMind mendorong masyarakat untuk lebih peduli dalam memilah sampah dengan cara yang sederhana dan interaktif.</p>
                        <div class="card-body">
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6">
                    <div class="card d-flex align-items-center justify-content-center text-center kartu-manfaat mb-4">
                            <img src="data:image/jpeg;base64,{image_base74}" class="gambar1">
                            <p class="fw-bold">Efesien Pengelolaan Sampah</p>
                            <p class="manfaat col-9 col-md-11 col-lg-8">Dengan identifikasi otomatis, pemilahan sampah menjadi lebih cepat, membantu petugas kebersihan dan masyarakat dalam mengurangi waktu pemilahan manual.</p>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6">
                    <div class="card d-flex align-items-center justify-content-center text-center kartu-manfaat mb-4">
                            <img src="data:image/jpeg;base64,{image_base75}" class="gambar1">
                            <p class="fw-bold">Dukungan Pengurangan Limbah</p>
                            <p class="manfaat col-9 col-md-11 col-lg-8">Dengan mempermudah identifikasi sampah, WasteMind membantu meningkatkan jumlah sampah yang didaur ulang dan mengurangi jumlah sampah yang berakhir di TPA.</p>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6">
                    <div class="card d-flex align-items-center justify-content-center text-center kartu-manfaat mb-4">
                            <img src="data:image/jpeg;base64,{image_base76}" class="gambar1">
                            <p class="fw-bold">Edukasi dan Pembelajaran</p>
                            <p class="manfaat col-9 col-md-11 col-lg-8">Website ini mengedukasi pengguna tentang jenis-jenis sampah serta cara pengelolaannya, menambah wawasan tentang pentingnya pengelolaan sampah yang bertanggung jawab.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
""",unsafe_allow_html=True)







