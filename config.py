"""
Configuración de la aplicación
"""
import streamlit as st

# --- CONFIGURACIÓN ---
# En local puedes poner los datos aquí, pero en producción usaremos 'Secrets'
TELEGRAM_TOKEN = st.secrets.get("TELEGRAM_TOKEN", "TU_TOKEN_SI_PRUEBAS_LOCAL")
CHAT_ID = st.secrets.get("CHAT_ID", "TU_ID_SI_PRUEBAS_LOCAL")
APP_PASSWORD = st.secrets.get("APP_PASSWORD", "1234")  # La contraseña de acceso
