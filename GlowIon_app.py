import streamlit as st
import time
import graphviz

# --- 1. KONFIGURASI HALAMAN (HARUS DI BARIS PERTAMA) ---
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- 2. CSS UNTUK TAMPILAN DAN ANIMASI [1, 11, 13-15] ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
        background-size: 400% 400%;
        animation: bgmove 15s infinite alternate;
    }
    @keyframes bgmove { 0% {background-position: left;} 100% {background-position: right;} }
    
    .title-tabs { display: flex; justify-content: center; margin: 20px 0; font-family: 'Trebuchet MS', sans-serif; font-weight: bold; }
    .title-tab { padding: 14px 24px; border-radius: 12px 12px 0 0; margin: 0 6px; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.25); transition: 0.3s; animation: pulse 2s infinite; }
    @keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
    .tab1 { background: #42a5f5; } .tab2 { background: #ef5350; } .tab3 { background: #66bb6a; } .tab4 { background: #ab47bc; }
    
    .tube { width:60px; height:150px; border:2px solid #333; border-radius:0 0 30px 30px; position:relative; background:rgba(255,255,255,0.4); overflow:hidden; margin:20px auto; }
    .liquid { position:absolute; bottom:0; width:100%; opacity:0.6; }
    .pellet { position:absolute; bottom:0; width:100%; border-radius:0 0 27px 27px; animation: turun 2s ease-in-out; }
    @keyframes turun { 0% { bottom:120px; opacity:0; } 100% { bottom:0; opacity:1; } }
    
    .spin-icon { border: 8px solid #f3f3f3; border-top: 8px solid #1565c0; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 10px auto; }
    @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
    .flame { width:35px; height:35px; border-radius:50%; margin:10px auto; }
</style>

<div class="title-tabs">
    <div class="title-tab tab1">GlowIon</div>
    <div class="title-tab tab2">ANALISIS</div>
    <div class="title-tab tab3">KUALITATIF KATION</div>
    <div class="title-tab tab4">DAN ANION</div>
</div>
""", unsafe_allow_html=True)

# --- 3. FUNGSI VISUAL [16-19] ---
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

# --- 4. TABS MENU UTAMA [20] ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Bagan Alir", "🔹 Analisis Kation", "🧪 Analisis Anion", "📝 Kuis"])

# --- TAB 1: BAGAN [20-23] ---
with tab1:
    st.subheader("📊 Bagan Pemisahan Kation (Berdasarkan Bagan Alir)")
    if 'langkah' not in st.session_state: st.session_state.langkah = 0
    def buat_bagan(step):
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        dot.node('start','Campuran Gol I–V',style='filled',color='lavender')
        if step>=1:
            dot.node('hcl','+ HCl encer'); dot.edge('start','hcl')
            dot.node('gol1','Endapan Gol I',style='filled',color='lightblue')
            dot.node('larutan','Filtrat (Al,Fe,Ba,Sr,Ca)',style='filled',color='lightblue')
            dot.edge('hcl','gol1'); dot.edge('hcl','larutan')
        if step>=2:
            dot.node('h2o','+ H2O Panas'); dot.edge('gol1','h2o')
            dot.node('pb','Pb²⁺ Larutan'); dot.node('residu','Endapan AgCl & Hg2Cl2')
            dot.edge('h2o','pb'); dot.edge('h2o','residu')
            dot.node('nh4oh','+ NH₄OH Berlebih'); dot.edge('larutan','nh4oh')
            dot.node('gol3','Endapan (Al, Fe)'); dot.node('gol4','Filtrat (Ba, Sr, Ca)')
            dot.edge('nh4oh','gol3'); dot.edge('nh4oh','gol4')
        if step>=3:
            dot.edge('pb','PbCrO₄ (Kuning)',label='+ K₂CrO₄')
            dot.edge('gol3','Fe(OH)₃ / Al(OH)₄⁻', label='+ NaOH Berlebih')
            dot.edge('gol4','BaCrO₄ (Kuning)',label='+ K₂CrO₄')
        return dot
    st.graphviz_chart(buat_bagan(st.session_state.langkah))
    if st.button("➡️ Langkah Berikutnya"):
        if st.session_state.langkah < 4: st.session_state.langkah += 1; st.rerun()
    if st.button("🔄 Reset Bagan"): st.session_state.langkah = 0; st.rerun()

# --- TAB 2: ANALISIS KATION [6-9, 24] ---
with tab2:
    st.subheader("🛠️ Analisis Kation")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV (V)"])
    
    if gol == "Golongan I":
        st.info("Uji Umum: HCl encer → endapan AgCl, PbCl₂, Hg₂Cl₂ [24].")
        if st.button("Jalankan Uji Gol I"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            st.latex(r"Pb^{2+} + 2Cl^- \rightarrow PbCl_2(s) \downarrow \text{ (Putih)}")
            st.latex(r"Hg_2^{2+} + 2Cl^- \rightarrow Hg_2Cl_2(s) \downarrow \text{ (Putih)}")
            centrifuge_action(); tube_viz("lightblue", "white")
        
        st.markdown("---")
        t_ag, t_pb, t_hg = st.tabs(["Ag⁺", "Pb²⁺", "Hg₂²⁺"])
        with t_ag:
            st.latex(r"Ag^+ + K_2CrO_4 \rightarrow Ag_2CrO_4 \text{ (Merah Bata)} [6]")
            tube_viz("lightblue", "orange")
            if st.button("Uji Amonia (AgCl + NH₄OH)"):
                st.success("AgCl larut membentuk kompleks [Ag(NH₃)₂]⁺ [6].")
                tube_viz("lightblue", dissolve=True)
        with t_pb:
            st.latex(r"Pb^{2+} + K_2CrO_4 \rightarrow PbCrO_4 \text{ (Kuning)} [6]")
            tube_viz("lightblue", "yellow")
        with t_hg:
            st.latex(r"Hg_2Cl_2 + NH_4OH \rightarrow Hg(hitam) + Hg(NH_2)Cl(putih) [7]")
            tube_viz("lightblue", "gray")

    elif gol == "Golongan III":
        if st.button("Uji Besi (Fe³⁺)"):
            st.latex(r"Fe^{3+} + 3SCN^- \rightarrow Fe(SCN)_3 \text{ (Merah)} [7]")
            tube_viz("#b71c1c")
        if st.button("Uji Aluminium (Al³⁺)"):
            st.latex(r"Al^{3+} + 3OH^- \rightarrow Al(OH)_3 \text{ (Putih)} [8]")
            tube_viz("lightblue", "white")

    elif gol == "Golongan IV (V)":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Barium (Ba²⁺)**")
            flame_viz("#adff2f"); st.write("Nyala Hijau Apel [8]")
            st.latex(r"Ba^{2+} + CrO_4^{2-} \rightarrow BaCrO_4 \downarrow \text{(Kuning)}")
        with col2:
            st.write("**Stronsium (Sr²⁺)**")
            flame_viz("#ff0000"); st.write("Nyala Merah Karmin [8]")
            st.latex(r"Sr^{2+} + CO_3^{2-} \rightarrow SrCO_3 \downarrow \text{(Putih)}")
        with col3:
            st.write("**Kalsium (Ca²⁺)**")
            flame_viz("#ff4500"); st.write("Nyala Merah Bata [9]")
            st.latex(r"Ca^{2+} + C_2O_4^{2-} \rightarrow CaC_2O_4 \downarrow \text{(Putih)}")

# --- TAB 3: ANALISIS ANION [9-12] ---
with tab3:
    st.subheader("🧪 Analisis Anion")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)} [9]")
        tube_viz("lightblue", "white")
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)} [10]")
        tube_viz("yellow", "red")
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O [10]")
        st.write("💨 Terbentuk gelembung gas CO₂.")
        st.markdown('<div class="bubble-container"><div class="bubble"></div><div class="bubble"></div><div class="bubble"></div></div>', unsafe_allow_html=True)
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow [12]")
        tube_viz("lightblue", "white")

# --- TAB 4: KUIS [25-29] ---
with tab4:
    st.subheader("📝 Uji Pemahaman")
    q1 = st.radio("1. Pereaksi untuk mengendapkan kation Golongan I?", ["NH₄OH", "HCl", "BaCl₂"], index=None)
    if st.button("Kirim Jawaban"):
        if q1 == "HCl": st.success("Benar! (Skor: 100)"); st.balloons()
        else: st.error("Coba lagi!")
