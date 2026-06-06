import streamlit as st
import time
import graphviz

# --- Judul dengan tab warna + efek hover glow ---
st.markdown(""" ... """, unsafe_allow_html=True)

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- CSS tambahan untuk tampilan lucu ---
st.markdown("""
<style>
/* Background pastel bergerak */
.stApp {
    background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
    animation: bgmove 15s infinite alternate;
}
@keyframes bgmove {
    0% {background-position: left;}
    100% {background-position: right;}
}

/* Font judul playful */
.title-tabs {
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Tab judul pulse animasi */
.title-tab {
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.05); box-shadow: 0 0 15px rgba(255,255,255,0.7);}
    100% {transform: scale(1);}
}

/* Tombol lucu */
button {
    background: linear-gradient(45deg, #ffccbc, #ffe0b2);
    border-radius: 12px !important;
    font-weight: bold !important;
    color: #4e342e !important;
    transition: 0.3s;
}
button:hover {
    background: linear-gradient(45deg, #ff80ab, #ffeb3b);
    color: white !important;
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# --- CSS untuk animasi (spinner, flame, tube) ---
st.markdown(""" ... """, unsafe_allow_html=True)



#--- CSS untuk judul ---
st.title ("LABKIM — Analisis Kualitatif Kation DAN Anion (Metode Sentrifugasi) dan uji spesifik")
# --- Judul dengan tab warna + efek hover glow ---
st.markdown("""
<style>
.title-tabs {
    display: flex;
    justify-content: center;
    margin: 20px 0;
    font-family: 'Trebuchet MS', sans-serif;
    font-weight: bold;
}
.title-tab {
    padding: 14px 24px;
    border-radius: 12px 12px 0 0;
    margin: 0 6px;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.25);
    transition: transform 0.3s, background 0.3s, box-shadow 0.3s;
    cursor: pointer;
}
.tab1 { background: #42a5f5; }   /* biru */
.tab2 { background: #ef5350; }   /* merah */
.tab3 { background: #66bb6a; }   /* hijau */
.tab4 { background: #ab47bc; }   /* ungu */

/* Efek hover glow */
.title-tab:hover {
    transform: translateY(-6px) scale(1.08);
    background: linear-gradient(45deg, #ffeb3b, #ff4081);
    box-shadow: 0 0 20px #ff4081;
}
</style>

<div class="title-tabs">
    <div class="title-tab tab1">LABKIM</div>
    <div class="title-tab tab2">ANALISIS</div>
    <div class="title-tab tab3">KUALITATIF KATION</div>
    <div class="title-tab tab4">DAN ANION</div>
</div>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- CSS untuk animasi ---
st.markdown("""
<style>
.spin-icon {
    border: 8px solid #f3f3f3; border-top: 8px solid #1565c0;
    border-radius: 50%; width: 50px; height: 50px;
    animation: spin 1s linear infinite; margin: 10px auto;
}
@keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
.flame { width:35px; height:35px; border-radius:50%; margin:10px; }
.tube { width:55px; height:160px; border:2px solid #333; border-radius:0 0 30px 30px;
        position:relative; background:rgba(255,255,255,0.4); overflow:hidden; margin:10px;}
.liquid { position:absolute; bottom:0; width:100%; opacity:0.6;}
.pellet { position:absolute; bottom:0; width:100%; border-radius:0 0 27px 27px;}
</style>
""", unsafe_allow_html=True)

# --- Fungsi visual ---
def tube_viz(liq_color, p_color=None, p_height=0):
    p_html = f'<div class="pellet" style="height:{p_height}px; background:{p_color};"></div>' if p_color else ""
    st.markdown(f'<div class="tube"><div class="liquid" style="height:75%; background:{liq_color};"></div>{p_html}</div>', unsafe_allow_html=True)

def flame_viz(color):
    st.markdown(f'<div class="flame" style="background:{color}; box-shadow:0 0 20px {color};"></div>', unsafe_allow_html=True)

def centrifuge_action():
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="spin-icon"></div>', unsafe_allow_html=True)
        st.write("🌀 Memutar pada 3000 rpm...")
        time.sleep(2)
    placeholder.empty()
    st.success("✅ Pemisahan selesai!")

import streamlit as st

st.title("📚 Materi Kation dan Anion")

materi = st.selectbox(
    "Pilih Materi",
    ["Kation", "Anion"]
)

if materi == "Kation":

    st.subheader("Pengertian Kation")

    st.write("""
    Kation adalah ion bermuatan positif yang terbentuk karena kehilangan elektron.
    Pada praktikum ini kation dipisahkan berdasarkan pereaksi tertentu sehingga
    dapat diidentifikasi secara sistematis.
    """)

    st.markdown("""
    **Kation yang digunakan:**

    **Golongan I**
    - Ag⁺
    - Pb²⁺
    - Hg₂²⁺

    **Golongan III**
    - Al³⁺
    - Fe³⁺

    **Golongan V**
    - Ba²⁺
    - Sr²⁺
    - Ca²⁺
    """)

elif materi == "Anion":

    st.subheader("Pengertian Anion")

    st.write("""
    Anion adalah ion bermuatan negatif yang terbentuk karena menerima elektron.
    Identifikasi anion dilakukan menggunakan pereaksi spesifik yang menghasilkan
    perubahan warna, pembentukan endapan, atau gas.
    """)

    st.markdown("""
    **Anion yang digunakan:**

    - Cl⁻ (Klorida)
    - I⁻ (Iodida)
    - CO₃²⁻ (Karbonat)
    - SO₄²⁻ (Sulfat)
    """)

# --- Tab menu ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Bagan Alir (Mind Map)", 
    "🔹 Analisis Kation", 
    "🧪 Analisis Anion", 
    "📝 Kuis Kation & Anion"])

# --- TAB 1: BAGAN (tetap ada, jangan diubah) ---
with tab1:
    st.subheader("📊 Bagan Pemisahan Kation")
    if 'langkah' not in st.session_state:
        st.session_state.langkah = 0
    def buat_bagan(step):
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        dot.node('start','Campuran Gol I–V',style='filled',color='lavender')
        if step>=1:
            dot.node('hcl','+ HCl encer')
            dot.edge('start','hcl')
            dot.node('gol1','Endapan Gol I',style='filled',color='lightblue')
            dot.node('larutan','Larutan (Al,Fe,Ba,Sr,Ca)',style='filled',color='lightblue')
            dot.edge('hcl','gol1'); dot.edge('hcl','larutan')
        if step>=2:
            dot.node('h2o','+ H2O Panas'); dot.edge('gol1','h2o')
            dot.node('pb','Pb²⁺'); dot.node('residu','Residu Ag/Hg')
            dot.edge('h2o','pb'); dot.edge('h2o','residu')
            dot.node('nh4oh','+ NH₄OH'); dot.edge('larutan','nh4oh')
            dot.node('gol3','Endapan Gol III'); dot.node('gol4','Larutan Gol IV')
            dot.edge('nh4oh','gol3'); dot.edge('nh4oh','gol4')
        if step>=3:
            dot.edge('pb','PbCrO₄ (Kuning)',label='+ K₂CrO₄')
            dot.edge('gol3','Fe(OH)₃'); dot.edge('gol3','Al(OH)₄⁻')
            dot.edge('gol4','BaCrO₄ (Kuning)',label='+ K₂CrO₄')
            dot.edge('gol4','Sr²⁺, Ca²⁺')
        if step>=4:
            dot.edge('Fe(OH)₃','Fe(SCN)₃ (Merah)',label='+ SCN⁻')
            dot.edge('Al(OH)₄⁻','Al(OH)₃ (Putih)',label='+ HCl/Na₂CO₃')
            dot.edge('Sr²⁺, Ca²⁺','SrCO₃ (Putih)',label='+ Na₂CO₃')
            dot.edge('Sr²⁺, Ca²⁺','CaC₂O₄ (Putih)',label='+ H₂C₂O₄ + NH₄OH')
        return dot
    st.graphviz_chart(buat_bagan(st.session_state.langkah))
    if st.button("➡️ Langkah Berikutnya"):
        if st.session_state.langkah<4:
            st.session_state.langkah+=1; st.rerun()
    if st.button("🔄 Reset"):
        st.session_state.langkah=0; st.rerun()

# --- TAB 2: ANALISIS KATION (dengan animasi) ---
with tab2:
    st.subheader("🛠️ Analisis Kation")
    gol = st.selectbox("Pilih Golongan:",["Golongan I","Golongan III","Golongan IV"])

    if gol=="Golongan I":
        st.info("Uji dengan HCl encer → endapan AgCl, PbCl₂, Hg₂Cl₂.")
        
        if st.button("Jalankan Uji Gol I"):
            # Reaksi kation Golongan I
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow \text{ (Putih)}")
        
        # Animasi sentrifugasi
        centrifuge_action()
        
        # Visual tabung dengan endapan putih
        tube_viz("lightblue","white",40)

    elif gol=="Golongan III":
        st.info("Uji dengan NH₄OH → endapan Fe(OH)₃ & Al(OH)₃.")
        if st.button("Uji Fe³⁺"):
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow Fe(SCN)_3 (Merah)")
            tube_viz("#b71c1c")
        if st.button("Uji Al³⁺"):
            st.latex(r"Al^{3+} + 3OH^- \rightarrow Al(OH)_3 (Putih)")
            tube_viz("lightblue","white",35)
    elif gol=="Golongan IV":
        st.info("Identifikasi Ba²⁺, Sr²⁺, Ca²⁺ dengan uji nyala & endapan.")
        st.markdown("### Barium (Ba²⁺)")
        flame_viz("#adff2f"); st.write("Nyala hijau apel")
        st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4 (Kuning)")
        st.markdown("### Stronsium (Sr²⁺)")
        flame_viz("#ff0000"); st.write("Nyala merah karmin")
        st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3 (Putih)")
        st.markdown("### Kalsium (Ca²⁺)")
        flame_viz("#ff4500"); st.write("Nyala merah bata")
        st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4 (Putih)")

# --- TAB 3: ANALISIS ANION (lengkap + animasi gelembung) ---
with tab3:
    st.subheader("📝 Analisis Anion")
    anion = st.selectbox("Pilih Anion:",["Klorida (Cl⁻)","Iodida (I⁻)","Karbonat (CO₃²⁻)","Sulfat (SO₄²⁻)"])
    
    if anion=="Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("lightblue","white",35)

    elif anion=="Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        st.write("Jika KI berlebih → (HgI₄)²⁻ (Larutan Kuning)")
        tube_viz("yellow","red",35)

    elif anion=="Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("Uji: terbentuk gelembung gas CO₂ yang keluar dari larutan.")
        # animasi gelembung
        st.markdown("""
         <style>
        .bubble-container {position:relative;width:100px;height:150px;background:#e0f7fa;border-radius:10px;margin:10px;}
        .bubble {position:absolute;bottom:0;width:20px;height:20px;border-radius:50%;background:#80deea;animation: rise 3s infinite;}
        .bubble:nth-child(2){left:30px;animation-delay:1s;}
        .bubble:nth-child(3){left:60px;animation-delay:2s;}
        @keyframes rise {
            0% {bottom:0;opacity:1;}
            100% {bottom:130px;opacity:0;}
        }
        </style>
        <div class="bubble-container">
            <div class="bubble"></div>
            <div class="bubble"></div>
            <div class="bubble"></div>
        </div>
        """, unsafe_allow_html=True)

    elif anion=="Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-")
        st.write("Uji: terbentuk endapan putih BaSO₄ yang tidak larut dalam asam.")
        tube_viz("lightblue","white",35)

# --- TAB 4: KUIS ---
with tab4:
    st.subheader("📝 Kuis Kation dan Anion")

    skor = 0

    jawab1 = st.radio("1. Pereaksi yang digunakan untuk mengendapkan kation golongan I adalah ...",
                      ["NH₄OH", "HCl", "BaCl₂", "H₂SO₄"], index=None, key="s1")

    jawab2 = st.radio("2. Ion yang termasuk golongan I adalah ...",
                      ["Fe³⁺", "Ag⁺", "Ba²⁺", "Ca²⁺"], index=None, key="s2")

    jawab3 = st.radio("3. Endapan AgCl berwarna ...",
                      ["Merah", "Kuning", "Putih", "Hijau"], index=None, key="s3")

    jawab4 = st.radio("4. Kation Al³⁺ termasuk golongan ...",
                      ["I", "II", "III", "V"], index=None, key="s4")

    jawab5 = st.radio("5. Pereaksi yang digunakan untuk mengendapkan Al³⁺ dan Fe³⁺ adalah ...",
                      ["NH₄OH", "HCl", "BaCl₂", "KI"], index=None, key="s5")

    jawab6 = st.radio("6. Kation yang termasuk golongan V adalah ...",
                      ["Ag⁺", "Pb²⁺", "Ca²⁺", "Fe³⁺"], index=None, key="s6")

    jawab7 = st.radio("7. Pereaksi untuk identifikasi ion klorida (Cl⁻) adalah ...",
                      ["AgNO₃", "NaOH", "NH₄OH", "K₂CrO₄"], index=None, key="s7")

    jawab8 = st.radio("8. Anion yang menghasilkan gas CO₂ saat direaksikan dengan asam adalah ...",
                      ["Cl⁻", "I⁻", "CO₃²⁻", "SO₄²⁻"], index=None, key="s8")

    jawab9 = st.radio("9. Pereaksi untuk identifikasi ion sulfat adalah ...",
                      ["AgNO₃", "BaCl₂", "KI", "NH₄OH"], index=None, key="s9")

    jawab10 = st.radio("10. Ion yang menghasilkan endapan putih dengan BaCl₂ adalah ...",
                       ["SO₄²⁻", "Cl⁻", "I⁻", "NO₃⁻"], index=None, key="s10")

    if st.button("Lihat Hasil"):
        if jawab1 == "HCl": skor += 10
        if jawab2 == "Ag⁺": skor += 10
        if jawab3 == "Putih": skor += 10
        if jawab4 == "III": skor += 10
        if jawab5 == "NH₄OH": skor += 10
        if jawab6 == "Ca²⁺": skor += 10
        if jawab7 == "AgNO₃": skor += 10
        if jawab8 == "CO₃²⁻": skor += 10
        if jawab9 == "BaCl₂": skor += 10
        if jawab10 == "SO₄²⁻": skor += 10

        st.success(f"Skor Anda: {skor}/100")

        if skor >= 80:
            st.balloons()
            st.write("🎉 Sangat Baik! Pemahaman Anda sudah sangat baik.")
        elif skor >= 60:
            st.write("👍 Baik! Tetap semangat belajar.")
        else:
            st.write("📚 Perlu belajar lagi agar lebih memahami materi.")




