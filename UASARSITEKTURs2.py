import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Smart Sprinkler System",
    layout="centered",
    page_icon="💧"
)

# Judul Aplikasi
st.title("💧 Smart Sprinkler System")
st.markdown("Sistem ini akan menyalakan sprinkler berdasarkan kondisi tanah, cuaca, dan override manual.")

st.divider()

# Input dari pengguna (dalam bentuk checkbox)
st.header("🔍 Sensor dan Pengaturan Manual")
is_dry = st.checkbox("🌱 Tanah kering?")
is_raining = st.checkbox("🌧️ Sedang hujan?")
manual_override = st.checkbox("🧑‍🔧 Manual override aktif?")

st.divider()

# Logika penyiraman
sprinkler_on = (is_dry and not is_raining) or manual_override

# Output hasil
st.header("🚿 Status Sprinkler")
if sprinkler_on:
    st.success("✅ Sprinkler ON - Menyiram tanaman sekarang.")
else:
    st.error("❌ Sprinkler OFF - Tidak menyiram saat ini.")
