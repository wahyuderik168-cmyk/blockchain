import streamlit as st
from core import Blockchain

# Konfigurasi Halaman
st.set_page_config(page_title="Blockchain Explorer", page_icon="🔗", layout="wide")
st.title("📦 Blockchain for Halal Coffee Supply Chain")

# Inisialisasi Session State
if 'my_blokchain' not in st.session_state:
    st.session_state.my_blokchain = Blockchain()

# Sidebar Input Data
st.sidebar.header("➕ Tambah Data Baru")
petani = st.sidebar.text_input("Nama Petani/Aktor:")
jumlah_kopi = st.sidebar.number_input("Jumlah Panen (kg):", min_value=1)
lokasi = st.sidebar.text_input("Lokasi Kebun:")

# Proses Saat Tombol Diklik
if st.sidebar.button("Tambahkan ke Blockchain"):
    if petani.strip() != "" and lokasi.strip() != "":
        # Gabungkan data
        data_transaksi = f"Petani: {petani} | Panen: {jumlah_kopi}(kg) | Lokasi: {lokasi}"
        
        # Tambahkan ke blockchain
        st.session_state.my_blokchain.add_block(data_transaksi)
        
        # Tampilkan pesan sukses dan REFRESH LAYAR SEKETIKA
        st.sidebar.success("Blok berhasil ditambahkan!")
        st.rerun() 
    else:
        st.sidebar.error("Harap isi nama petani dan lokasi!")

# Main Area / Buku Besar
st.header("📜 Blockchain Ledger (Buku Besar)")

is_valid = st.session_state.my_blokchain.is_chain_valid()
if is_valid:
    st.success("✔️ Status Jaringan : Rantai Valid (Aman)")
else:
    st.error("❌ PERINGATAN: Integritas Rantai Rusak (Telah Dimanipulasi)")

# Looping Menampilkan Semua Blok
for block in st.session_state.my_blokchain.chain:
    with st.expander(f"Blok #{block.index} | Hash: {block.hash[:15]}..."):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Data Payload:**")
            st.info(block.data)
            st.write(f"**Timestamp:** {block.timestamp_readable}")
        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash Saat Ini:**")
            st.code(block.hash, language='python')
            st.write("**Hash Sebelumnya (Pointer):**")
            st.code(block.prev_hash, language='python')