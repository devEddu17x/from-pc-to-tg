"""
Aplicación principal para enviar archivos a Telegram
"""
import streamlit as st
from styles.css import get_main_styles
from components.auth import initialize_session_state, render_login, is_authenticated
from components.ui import render_header, render_history
from components.uploader import handle_file_upload


def main():
    """Función principal de la aplicación"""
    # Configuración de la página
    st.set_page_config(
        page_title="Enviar a Telegram",
        page_icon="☁️"
    )
    
    # Aplicar estilos CSS
    st.markdown(get_main_styles(), unsafe_allow_html=True)
    
    # Renderizar encabezado
    render_header()
    
    # Inicializar estado de sesión
    initialize_session_state()
    
    # Manejo de autenticación
    if not is_authenticated():
        render_login()
    else:
        # Usuario autenticado - mostrar interfaz principal
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Manejar upload de archivos
        handle_file_upload()
        
        # Mostrar historial
        render_history(st.session_state.files_sent)


if __name__ == "__main__":
    main()