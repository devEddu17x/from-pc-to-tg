"""
Componente de upload y envío de archivos
"""
import streamlit as st
from utils.helpers import send_to_telegram, format_file_size
from components.ui import render_file_list


def handle_file_upload():
    """Maneja la carga de archivos y renderiza el botón de envío"""
    uploaded_files = st.file_uploader(
        "Arrastra tus archivos aquí o haz clic para seleccionar",
        accept_multiple_files=True,
        help="Puedes subir varios archivos a la vez. Límite: 200MB por archivo",
        label_visibility="collapsed"
    )
    
    if uploaded_files:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón de enviar al inicio
        if st.button("Enviar a Telegram", use_container_width=True):
            process_file_upload(uploaded_files)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Mostrar archivos en formato compacto
        render_file_list(uploaded_files)


def process_file_upload(uploaded_files):
    """Procesa el envío de archivos a Telegram"""
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    success_count = 0
    error_count = 0
    
    for idx, file in enumerate(uploaded_files):
        status_text.text(f"📤 Enviando {idx + 1}/{len(uploaded_files)}: {file.name}...")
        
        try:
            resp = send_to_telegram(file)
            if resp.status_code == 200:
                success_count += 1
                st.session_state.files_sent.append({
                    'name': file.name,
                    'size': format_file_size(file.size),
                    'status': 'success'
                })
            else:
                error_count += 1
                st.error(f"❌ Error al enviar {file.name}: {resp.text}")
        except Exception as e:
            error_count += 1
            st.error(f"❌ Error con {file.name}: {e}")
        
        progress_bar.progress((idx + 1) / len(uploaded_files))
    
    status_text.empty()
    progress_bar.empty()
    
    # Mostrar resultado final
    if success_count > 0:
        st.balloons()
        st.success(
            f"Se enviaron {success_count} archivo(s) correctamente" +
            (f" | ⚠️ {error_count} con error" if error_count > 0 else "")
        )
    else:
        st.error("❌ No se pudo enviar ningún archivo")
