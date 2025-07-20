import streamlit as st

st.set_page_config(page_title="Smart Sprinkler System", layout="centered")

st.title("💧 Smart Sprinkler System")

# Input pengguna dalam bentuk checkbox (boolean)
is_dry = st.checkbox("Tanah kering?")
is_raining = st.checkbox("Sedang hujan?")
manual_override = st.checkbox("Manual override aktif?")

# Logika penyiraman
sprinkler_on = (is_dry and not is_raining) or manual_override

# Output hasil
st.markdown("## 🚿 Status Sprinkler:")
if sprinkler_on:
    st.success("✅ Sprinkler ON")
else:
    st.error("❌ Sprinkler OFF")
