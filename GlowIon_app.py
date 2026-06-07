import streamlit as st
import time
import graphviz

# --- 1. Konfigurasi Halaman (Harus di baris pertama) ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- 2. CSS Terpadu (Glow, Animasi, dan Gaya) ---
st.markdown("""
<style>
    /* Background pastel bergerak */
    .stApp {
        background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
        background-size: 400% 400%;
        animation: bgmove 15s infinite alternate;
    }
    @keyframes bgmove {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    /* Font judul dan animasi pulse */
    .title-tabs { display: flex; justify-content: center; margin: 20px 0; font-family: 'Trebuchet MS', sans-serif; font-weight: bold; }
    .title-tab { padding: 14px 24px; border-radius: 12px 12px 0 0; margin: 0 6px; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.25); transition: 0.3s; cursor: pointer; animation: pulse 2s infinite; }
    @keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05); box-shadow: 0 0 15px rgba(255,255,255,0.7);} 100% {transform: scale(1);} }
    .tab1 { background: #42a5f5; } .tab2 { background: #ef5350; } .tab3 { background: #66bb6a; } .tab4 { background: #ab47bc; }
    .title-tab:hover { transform: translateY(-6px) scale(1.08); background: linear-gradient(45deg, #ffeb3b, #ff4081); box-shadow: 0 0 20px #ff4081; }
    
    /* Tombol lucu */
    button { background: linear-gradient(45deg, #ffccbc, #ffe0b2) !important; border-radius: 12px !important; font-weight: bold !important; color: #4e342e !important; transition: 0.3s; }
    button:hover { background: linear-gradient(45deg, #ff80ab, #ffeb3b) !important; color: white !important; transform: scale(1.1); }

    /* Animasi Centrifuge, Tube, dan Flame */
    .spin-icon { border: 8px solid #f3f3f3; border-top: 8px solid #1565c0; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 10px auto; }
    @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
    .flame { width:35px; height:35px; border-radius:50%; margin:10px; }
    .tube { width:60px; height:150px; border:2px solid #333; border-radius:0 0 30px 30px; position:relative; background:rgba(255,255,255,0.4); overflow:hidden; margin:20px auto; }
    .liquid { position:absolute; bottom:0; width:100%; opacity:0.6; }
    .pellet { position:absolute; bottom:0; width:100%; border-radius:0 0 27px 27px; animation: turun 2s ease-in-out; }
    @keyframes turun { 0% { bottom:120px; opacity:0; } 100% { bottom:0; opacity:1; } }

    /* Gelembung */
    .bubble-container {position:relative;width:100px;height:150px;background:#e0f7fa;border-radius:10px;margin:10px;}
    .bubble {position:absolute;bottom:0;width:20px;height:20px;border-radius:50%;background:#80deea;animation: rise 3s infinite;}
    .bubble:nth-child(2){left:30px;animation-delay:1s;}
    .bubble:nth-child(3){left:60px;animation-delay:2s;}
    @keyframes rise { 0% {bottom:0;opacity:1;} 100% {bottom:130px;opacity:0;} }
</style>

<div class="title-tabs">
    <div class="title-tab tab1">GlowIon</div>
    <div class="title-tab tab2">ANALISIS</div>
    <div class="title-tab tab3">KUALITATIF KATION</div>
    <div class="title-tab tab4">DAN ANION</div>
</div>
""", unsafe_allow_html=True)

st.title("GlowIon — Analisis Kualitatif Kation dan Anion (Metode Sentrifugasi)")

# --- 3. Fungsi Visual dan Aksi ---
def tube_viz(liq_color, p_color=None, p_height=40, dissolve=False):
    if dissolve:
        st.markdown(f'<div class="tube" style="background:{liq_color}; border:none; animation: fade 3s forwards;"></div>', unsafe_allow_html=True)
    else:
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

# --- 4. Bagian Materi ---
st.title("📚 Materi Kation dan Anion")
materi = st.selectbox("Pilih Materi", ["Kation", "Anion"])
if materi == "Kation":
    st.subheader("Pengertian Kation")
    st.write("Kation adalah ion bermuatan positif yang terbentuk karena kehilangan elektron. Kation dipisahkan secara sistematis berdasarkan pereaksi tertentu [4].")
    st.markdown("**Golongan I:** Ag⁺, Pb²⁺, Hg₂²⁺  \n**Golongan III:** Al³⁺, Fe³⁺  \n**Golongan V:** Ba²⁺, Sr²⁺, Ca²⁺ [4, 5]")
elif materi == "Anion":
    st.subheader("Pengertian Anion")
    st.write("Anion adalah ion bermuatan negatif. Identifikasi dilakukan menggunakan pereaksi spesifik yang menghasilkan warna, endapan, atau gas [5].")
    st.markdown("**Anion:** Cl⁻, I⁻, CO₃²⁻, SO₄²⁻ [5]")

# --- 5. Tab Menu Utama ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Bagan Alir", "🔹 Analisis Kation", "🧪 Analisis Anion", "📝 Kuis"])

# --- TAB 1: BAGAN ALIR ---
with tab1:
    st.subheader("📊 Bagan Pemisahan Kation")
    if 'langkah' not in st.session_state: st.session_state.langkah = 0
    def buat_bagan(step):
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        dot.node('start','Campuran Gol I–V',style='filled',color='lavender')
        if step>=1:
            dot.node('hcl','+ HCl encer'); dot.edge('start','hcl')
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
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Langkah Berikutnya") and st.session_state.langkah < 4:
            st.session_state.langkah += 1; st.rerun()
    with col2:
        if st.button("🔄 Reset"):
            st.session_state.langkah = 0; st.rerun()

# --- TAB 2: ANALISIS KATION ---
with tab2:
    st.subheader("🛠️ Analisis Kation")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.info("Uji Umum: HCl encer → endapan AgCl, PbCl₂, Hg₂Cl₂ [6].")
        if st.button("Jalankan Uji Gol I"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{(Putih)}")
            centrifuge_action(); tube_viz("lightblue", "white")
        
        st.markdown("---")
        st.subheader("📄 Uji Spesifik Golongan I")
        t_ag, t_pb, t_hg = st.tabs(["Ag⁺", "Pb²⁺", "Hg₂²⁺"])
        with t_ag:
            st.write("Ag⁺ + K₂CrO₄ → Ag₂CrO₄ (merah bata)"); tube_viz("lightblue", "orange")
            if st.button("AgCl + NH₄OH berlebih"):
                st.success("Larut membentuk [Ag(NH₃)₂]⁺"); tube_viz("lightblue", dissolve=True)
        with t_pb:
            st.write("Pb²⁺ + K₂CrO₄ → PbCrO₄ (kuning)"); tube_viz("lightblue", "yellow")
        with t_hg:
            st.write("Hg₂²⁺ + NH₄OH → Hg(hitam) + Hg(NH₂)Cl(putih)"); tube_viz("lightblue", "gray")

    elif gol == "Golongan III":
        if st.button("Uji Fe³⁺ (+ SCN⁻)"):
            st.latex(r"Fe(SCN)_3 \text{ (Merah)}"); tube_viz("#b71c1c")
        if st.button("Uji Al³⁺ (+ OH⁻)"):
            st.latex(r"Al(OH)_3 \text{ (Putih)}"); tube_viz("lightblue", "white")

    elif gol == "Golongan IV":
        st.markdown("### Uji Nyala & Endapan")
        col_ba, col_sr, col_ca = st.columns(3)
        with col_ba: 
            st.write("Ba²⁺ (Hijau Apel)"); flame_viz("#adff2f")
            st.latex(r"BaCrO_4 \downarrow")
        with col_sr: 
            st.write("Sr²⁺ (Merah Karmin)"); flame_viz("#ff0000")
            st.latex(r"SrCO_3 \downarrow")
        with col_ca: 
            st.write("Ca²⁺ (Merah Bata)"); flame_viz("#ff4500")
            st.latex(r"CaC_2O_4 \downarrow")

# --- TAB 3: ANALISIS ANION ---
with tab3:
    st.subheader("📝 Analisis Anion")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow"); tube_viz("lightblue", "white")
    elif anion == "Karbonat (CO₃²⁻)":
        st.write("Terbentuk gelembung gas CO₂ [7].")
        st.markdown('<div class="bubble-container"><div class="bubble"></div><div class="bubble"></div><div class="bubble"></div></div>', unsafe_allow_html=True)

# --- TAB 4: KUIS ---
with tab4:
    st.subheader("📝 Kuis Kation dan Anion")
    q1 = st.radio("1. Pereaksi endapan Golongan I?", ["NH₄OH", "HCl", "BaCl₂"], index=None)
    if st.button("Lihat Hasil"):
        skor = 0
        if q1 == "HCl": skor += 100
        st.success(f"Skor Anda: {skor}/100")
        if skor == 100: st.balloons()
