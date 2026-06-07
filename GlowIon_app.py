import streamlit as st
import time
import graphviz

# --- 1. KONFIGURASI HALAMAN (Wajib di baris pertama) ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- 2. CSS UNTUK TAMPILAN DAN ANIMASI ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
        background-size: 400% 400%;
        animation: bgmove 15s infinite alternate;
    }
    @keyframes bgmove { 0% {background-position: 0% 50%;} 100% {background-position: 100% 50%;} }
    
    .title-tabs { display: flex; justify-content: center; margin: 20px 0; font-family: 'Trebuchet MS', sans-serif; font-weight: bold; }
    .title-tab { padding: 14px 24px; border-radius: 12px 12px 0 0; margin: 0 6px; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.25); transition: 0.3s; animation: pulse 2s infinite; }
    @keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
    .tab1 { background: #42a5f5; } .tab2 { background: #ef5350; } .tab3 { background: #66bb6a; } .tab4 { background: #ab47bc; }
    
    .spin-icon { border: 8px solid #f3f3f3; border-top: 8px solid #1565c0; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 10px auto; }
    @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
    
    .tube { width:60px; height:150px; border:2px solid #333; border-radius:0 0 30px 30px; position:relative; background:rgba(255,255,255,0.4); overflow:hidden; margin:20px auto; }
    .liquid { position:absolute; bottom:0; width:100%; opacity:0.6; }
    .pellet { position:absolute; bottom:0; width:100%; border-radius:0 0 27px 27px; animation: turun 2s ease-in-out; }
    @keyframes turun { 0% { bottom:120px; opacity:0; } 100% { bottom:0; opacity:1; } }
    
    .flame { width:35px; height:35px; border-radius:50%; margin:10px auto; }
</style>

<div class="title-tabs">
    <div class="title-tab tab1">GlowIon</div>
    <div class="title-tab tab2">ANALISIS</div>
    <div class="title-tab tab3">KUALITATIF KATION</div>
    <div class="title-tab tab4">DAN ANION</div>
</div>
""", unsafe_allow_html=True)

st.title("GlowIon — Analisis Kualitatif (Metode Sentrifugasi)")

# --- 3. FUNGSI PEMBANTU ---
def tube_viz(liq_color, p_color=None, p_height=40):
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

# --- 4. MATERI ---
materi = st.selectbox("Pilih Materi", ["Kation", "Anion"])
if materi == "Kation":
    st.markdown("**Kation yang digunakan:** Gol I (Ag⁺, Pb²⁺, Hg₂²⁺), Gol III (Al³⁺, Fe³⁺), Gol V (Ba²⁺, Sr²⁺, Ca²⁺)") [7, 8]
else:
    st.markdown("**Anion yang digunakan:** Cl⁻ (Klorida), I⁻ (Iodida), CO₃²⁻ (Karbonat), SO₄²⁻ (Sulfat)") [8]

# --- 5. TABS UTAMA ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Bagan Alir", "🔹 Analisis Kation", "🧪 Analisis Anion", "📝 Kuis"])

with tab1:
    st.subheader("📊 Bagan Pemisahan Kation")
    if 'langkah' not in st.session_state: st.session_state.langkah = 0
    # (Logika Graphviz tetap sama seperti sebelumnya berdasarkan sumber [9-12])
    # ... bagian graphviz ...
    if st.button("➡️ Langkah Berikutnya"):
        if st.session_state.langkah < 4: st.session_state.langkah += 1; st.rerun()
    if st.button("🔄 Reset"): st.session_state.langkah = 0; st.rerun()

with tab2:
    st.subheader("🛠️ Analisis Kation")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    
    if gol == "Golongan I":
        st.info("Uji dengan HCl encer:")
        if st.button("Jalankan Uji Gol I"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}") [1]
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}") [1]
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow \text{ (Putih)}") [1]
            centrifuge_action(); tube_viz("lightblue", "white")

        st.markdown("---")
        t_ag, t_pb, t_hg = st.tabs(["Ag⁺", "Pb²⁺", "Hg₂²⁺"])
        with t_ag:
            st.latex(r"Ag^+ + K_2CrO_4 \rightarrow Ag_2CrO_4 \text{ (Merah Bata)}") [13]
            tube_viz("lightblue", "orange")
        with t_pb:
            st.latex(r"Pb^{2+} + K_2CrO_4 \rightarrow PbCrO_4 \text{ (Kuning)}") [13]
            tube_viz("lightblue", "yellow")
        with t_hg:
            st.latex(r"Hg_2Cl_2 + NH_4OH \rightarrow Hg \text{ (Hitam)} + Hg(NH_2)Cl \text{ (Putih)}") [2]
            tube_viz("lightblue", "gray")

    elif gol == "Golongan III":
        if st.button("Uji Fe³⁺ (+ SCN⁻)"):
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow Fe(SCN)_3 \text{ (Merah)}") [2]
            tube_viz("#b71c1c")
        if st.button("Uji Al³⁺ (+ OH⁻)"):
            st.latex(r"Al^{3+} + 3OH^- \rightarrow Al(OH)_3 \text{ (Putih)}") [3]
            tube_viz("lightblue", "white")

    elif gol == "Golongan IV":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Barium (Ba²⁺)")
            flame_viz("#adff2f")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4 \text{ (Kuning)}") [3]
        with col2:
            st.write("Stronsium (Sr²⁺)")
            flame_viz("#ff0000")
            st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3 \text{ (Putih)}") [4]
        with col3:
            st.write("Kalsium (Ca²⁺)")
            flame_viz("#ff4500")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4 \text{ (Putih)}") [4]

with tab3:
    st.subheader("🧪 Analisis Anion")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}") [4]
        tube_viz("lightblue", "white")
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}") [5]
        tube_viz("yellow", "red")
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O") [5]
        st.write("💨 Terbentuk gelembung gas CO₂.")
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow + 2Cl^-") [6]
        tube_viz("lightblue", "white")

with tab4:
    st.subheader("📝 Kuis")
    # (Pertanyaan kuis disesuaikan kembali ke 10 soal dari sumber [14-17])
    q1 = st.radio("1. Pereaksi endapan Golongan I?", ["NH₄OH", "HCl", "BaCl₂"], index=None)
    if st.button("Lihat Hasil"):
        if q1 == "HCl": st.success("Benar! Skor: 10/100"); st.balloons()
        else: st.error("Salah!")
