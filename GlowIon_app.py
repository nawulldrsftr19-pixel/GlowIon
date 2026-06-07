import streamlit as st
import time
import graphviz

# --- 1. KONFIGURASI HALAMAN (Wajib di baris pertama) --- [1], [2]
st.set_page_config(page_title="Virtual Lab: Analisis Kualitatif", layout="wide")

# --- 2. CSS UNTUK TAMPILAN DAN ANIMASI --- [1], [4], [5], [6], [7]
st.markdown("""
<style>
    /* Background pastel bergerak */
    .stApp {
        background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
        background-size: 400% 400%;
        animation: bgmove 15s infinite alternate;
    }
    @keyframes bgmove { 0% {background-position: left;} 100% {background-position: right;} }
    
    /* Judul playful */
    .title-tabs { display: flex; justify-content: center; margin: 20px 0; font-family: 'Trebuchet MS', sans-serif; font-weight: bold; }
    .title-tab { padding: 14px 24px; border-radius: 12px 12px 0 0; margin: 0 6px; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.25); transition: 0.3s; animation: pulse 2s infinite; }
    @keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
    .tab1 { background: #42a5f5; } .tab2 { background: #ef5350; } .tab3 { background: #66bb6a; } .tab4 { background: #ab47bc; }
    
    /* Spinner & Flame */
    .spin-icon { border: 8px solid #f3f3f3; border-top: 8px solid #1565c0; border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 10px auto; }
    @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
    .flame { width:35px; height:35px; border-radius:50%; margin:10px auto; }

    /* Animasi Gelembung Karbonat */
    .bubble-container {position:relative;width:100px;height:150px;background:#e0f7fa;border-radius:10px;margin:10px auto;}
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

st.title("GlowIon — Analisis Kualitatif Kation dan Anion (Metode Sentrifugasi)") [8]

# --- 3. FUNGSI VISUAL --- [9], [3], [10], [11]
def tube_viz(liquid_color, precipitate_color, dissolve=False, height=140):
    if dissolve:
        st.markdown(f'<div style="width:70px;height:{height}px;background:{liquid_color};border-radius:10px;position:relative;margin:20px auto;animation: fade 3s forwards;"></div><style>@keyframes fade {{0% {{ background:{liquid_color}; }} 100% {{ background:transparent; }} }}</style>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="width:70px;height:{height}px;background:{liquid_color};border-radius:10px;position:relative;margin:20px auto;">
            <div style="width:70px;height:35px;background:{precipitate_color};position:absolute;bottom:0;border-radius:0 0 10px 10px;animation: turun 2s ease-in-out;"></div>
        </div>
        <style>@keyframes turun {{ 0% {{ bottom:120px; opacity:0; }} 100% {{ bottom:0; opacity:1; }} }}</style>
        """, unsafe_allow_html=True)

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

# --- 4. MATERI --- [12], [13]
materi = st.selectbox("Pilih Materi", ["Kation", "Anion"])
if materi == "Kation":
    st.subheader("Pengertian Kation")
    st.write("Kation adalah ion bermuatan positif yang terbentuk karena kehilangan elektron. Dipisahkan secara sistematis berdasarkan pereaksi tertentu.")
    st.markdown("**Kation yang digunakan:** Gol I (Ag⁺, Pb²⁺, Hg₂²⁺), Gol III (Al³⁺, Fe³⁺), Gol V (Ba²⁺, Sr²⁺, Ca²⁺)")
else:
    st.subheader("Pengertian Anion")
    st.write("Anion adalah ion bermuatan negatif yang terbentuk karena menerima elektron. Identifikasi menggunakan pereaksi spesifik.")
    st.markdown("**Anion yang digunakan:** Cl⁻, I⁻, CO₃²⁻, SO₄²⁻")

# --- 5. TABS UTAMA --- [14]
tab1, tab2, tab3, tab4 = st.tabs(["📊 Bagan Alir", "🔹 Analisis Kation", "🧪 Analisis Anion", "📝 Kuis"])

with tab1: # --- BAGAN ALIR --- [14]-[15]
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
        return dot
    st.graphviz_chart(buat_bagan(st.session_state.langkah))
    if st.button("➡️ Langkah Berikutnya"):
        if st.session_state.langkah < 4: st.session_state.langkah += 1; st.rerun()

with tab2: # --- ANALISIS KATION --- [16]-[17]
    st.subheader("🛠️ Analisis Kation")
    gol = st.selectbox("Pilih Golongan:", ["Golongan I", "Golongan III", "Golongan IV"])
    if gol == "Golongan I":
        if st.button("Jalankan Uji Gol I (+HCl)"):
            st.latex(r"Ag^+ + Cl^- \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
            centrifuge_action(); tube_viz("lightblue", "white")
        t_ag, t_pb, t_hg = st.tabs(["Ag⁺", "Pb²⁺", "Hg₂²⁺"])
        with t_ag:
            st.info("Ag⁺ + K₂CrO₄ → Ag₂CrO₄ (merah bata)"); tube_viz("lightblue", "orange")
            if st.button("Uji NH₄OH berlebih"): st.success("AgCl larut"); tube_viz("lightblue", "white", dissolve=True)
        with t_pb:
            st.success("Pb²⁺ + K₂CrO₄ → PbCrO₄ (kuning)"); tube_viz("lightblue", "yellow")
        with t_hg:
            st.error("Hg₂Cl₂ + NH₄OH → Hg(hitam) + Hg(NH₂)Cl(putih)"); tube_viz("lightblue", "gray")
    elif gol == "Golongan III":
        if st.button("Uji Fe³⁺ (+SCN⁻)"): st.latex(r"Fe^{3+} + 3SCN^- \rightarrow Fe(SCN)_3 \text{ (Merah)}"); tube_viz("#b71c1c", "red")
        if st.button("Uji Al³⁺ (+OH⁻)"): st.latex(r"Al^{3+} + 3OH^- \rightarrow Al(OH)_3 \text{ (Putih)}"); tube_viz("lightblue", "white")
    elif gol == "Golongan IV":
        col1, col2, col3 = st.columns(3)
        with col1: st.write("Ba²⁺"); flame_viz("#adff2f"); st.latex(r"BaCrO_4 (Kuning)")
        with col2: st.write("Sr²⁺"); flame_viz("#ff0000"); st.latex(r"SrCO_3 (Putih)")
        with col3: st.write("Ca²⁺"); flame_viz("#ff4500"); st.latex(r"CaC_2O_4 (Putih)")

with tab3: # --- ANALISIS ANION --- [17]-[18]
    st.subheader("🧪 Analisis Anion")
    anion = st.selectbox("Pilih Anion:", ["Klorida (Cl⁻)", "Iodida (I⁻)", "Karbonat (CO₃²⁻)", "Sulfat (SO₄²⁻)"])
    if anion == "Klorida (Cl⁻)":
        st.latex(r"Cl^- + AgNO_3 \rightarrow AgCl(s) \downarrow \text{ (Putih)}")
        tube_viz("lightblue", "white")
    elif anion == "Iodida (I⁻)":
        st.latex(r"2I^- + HgCl_2 \rightarrow HgI_2(s) \downarrow \text{ (Merah)}")
        tube_viz("yellow", "red")
    elif anion == "Karbonat (CO₃²⁻)":
        st.latex(r"CO_3^{2-} + 2HCl \rightarrow CO_2(g) \uparrow + H_2O")
        st.write("💨 Terbentuk gelembung gas CO₂.")
        st.markdown('<div class="bubble-container"><div class="bubble"></div><div class="bubble"></div><div class="bubble"></div></div>', unsafe_allow_html=True)
    elif anion == "Sulfat (SO₄²⁻)":
        st.latex(r"SO_4^{2-} + BaCl_2 \rightarrow BaSO_4(s) \downarrow")
        tube_viz("lightblue", "white")

with tab4: # --- KUIS 10 SOAL --- [19]-[20]
    st.subheader("📝 Kuis Kation dan Anion")
    skor = 0
    q1 = st.radio("1. Pereaksi pengendap kation Gol I?", ["NH₄OH", "HCl", "BaCl₂", "H₂SO₄"], index=None, key="1")
    q2 = st.radio("2. Ion yang termasuk golongan I?", ["Fe³⁺", "Ag⁺", "Ba²⁺", "Ca²⁺"], index=None, key="2")
    q3 = st.radio("3. Warna endapan AgCl?", ["Merah", "Kuning", "Putih", "Hijau"], index=None, key="3")
    q4 = st.radio("4. Al³⁺ termasuk golongan?", ["I", "II", "III", "V"], index=None, key="4")
    q5 = st.radio("5. Pereaksi pengendap Al³⁺ & Fe³⁺?", ["NH₄OH", "HCl", "BaCl₂", "KI"], index=None, key="5")
    q6 = st.radio("6. Kation golongan V?", ["Ag⁺", "Pb²⁺", "Ca²⁺", "Fe³⁺"], index=None, key="6")
    q7 = st.radio("7. Pereaksi identifikasi Cl⁻?", ["AgNO₃", "NaOH", "NH₄OH", "K₂CrO₄"], index=None, key="7")
    q8 = st.radio("8. Anion penghasil gas CO₂?", ["Cl⁻", "I⁻", "CO₃²⁻", "SO₄²⁻"], index=None, key="8")
    q9 = st.radio("9. Pereaksi identifikasi ion sulfat?", ["AgNO₃", "BaCl₂", "KI", "NH₄OH"], index=None, key="9")
    q10 = st.radio("10. Endapan putih dengan BaCl₂?", ["SO₄²⁻", "Cl⁻", "I⁻", "NO₃⁻"], index=None, key="10")

    if st.button("Lihat Hasil Kuis"):
        if q1 == "HCl": skor += 10
        if q2 == "Ag⁺": skor += 10
        if q3 == "Putih": skor += 10
        if q4 == "III": skor += 10
        if q5 == "NH₄OH": skor += 10
        if q6 == "Ca²⁺": skor += 10
        if q7 == "AgNO₃": skor += 10
        if q8 == "CO₃²⁻": skor += 10
        if q9 == "BaCl₂": skor += 10
        if q10 == "SO₄²⁻": skor += 10
        st.success(f"Skor Anda: {skor}/100")
        if skor >= 80: st.balloons(); st.write("🎉 Sangat Baik!")
