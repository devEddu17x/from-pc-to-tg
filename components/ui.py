"""
Componentes de interfaz de usuario
"""
import streamlit as st
from utils.helpers import format_file_size


def render_header():
    """Renderiza el encabezado de la aplicación"""
    st.markdown('<div class="main-title">☁️ Enviar a mi Telegram</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Comparte tus archivos de forma segura y rápida</div>', unsafe_allow_html=True)


def render_file_card(file_name, file_size, file_type=None, is_sent=False):
    """Renderiza una tarjeta de archivo"""
    icon = "✓" if is_sent else "•"
    
    if is_sent:
        # Tarjeta simple para archivos enviados
        st.markdown(f"""
            <div class="file-card">
                <div class="file-name">{icon} {file_name}</div>
                <div class="file-info">{file_size}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Tarjeta completa para archivos pendientes
        type_info = f" · {file_type}" if file_type else ""
        st.markdown(f"""
            <div class="file-card">
                <div class="file-name">{icon} {file_name}</div>
                <div class="file-info">
                    {file_size}{type_info}
                </div>
            </div>
        """, unsafe_allow_html=True)


def render_file_list(uploaded_files):
    """Renderiza la lista de archivos cargados"""
    for file in uploaded_files:
        file_size = format_file_size(file.size)
        file_type = file.type if file.type else 'Desconocido'
        render_file_card(file.name, file_size, file_type)


def render_history(files_sent):
    """Renderiza el historial de archivos enviados"""
    if files_sent:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<p style="color: #888; font-size: 0.85em; margin-bottom: 10px;">Enviados recientemente</p>', unsafe_allow_html=True)
        
        for file_info in reversed(files_sent[-5:]):  # Últimos 5
            render_file_card(file_info['name'], file_info['size'], is_sent=True)
