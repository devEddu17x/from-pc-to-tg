"""
Componente de autenticación
"""
import streamlit as st
from config import APP_PASSWORD
from styles.css import get_password_hide_icon_style, get_password_error_style


def initialize_session_state():
    """Inicializa el estado de sesión"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'files_sent' not in st.session_state:
        st.session_state.files_sent = []


def render_login():
    """Renderiza el formulario de login y maneja la autenticación"""
    # Ocultar el botón de mostrar contraseña
    st.markdown(get_password_hide_icon_style(), unsafe_allow_html=True)
    
    password = st.text_input(
        "🔐 Contraseña de acceso",
        type="password",
        placeholder="Ingresa tu contraseña",
        label_visibility="collapsed",
        key="password_input"
    )
    
    # Aplicar estilo de error si la contraseña es incorrecta
    if password and password != APP_PASSWORD:
        st.markdown(get_password_error_style(), unsafe_allow_html=True)
    
    # Si la contraseña es correcta, autenticar
    if password == APP_PASSWORD:
        st.session_state.authenticated = True
        st.rerun()


def is_authenticated():
    """Verifica si el usuario está autenticado"""
    return st.session_state.get('authenticated', False)
