"""
Configuración de la aplicación
"""
import os
import streamlit as st

# --- CONFIGURACIÓN ---
# Prioridad: 1. Variables de entorno (Koyeb), 2. Streamlit secrets (local), 3. Defaults

def get_config_value(key, default=""):
    """
    Obtiene valores de configuración en orden de prioridad:
    1. Variables de entorno (para Docker/Koyeb)
    2. Streamlit secrets (para desarrollo local)
    3. Valor por defecto
    """
    # Primero intentar variables de entorno
    env_value = os.getenv(key)
    if env_value:
        return env_value
    
    # Luego intentar Streamlit secrets
    try:
        return st.secrets.get(key, default)
    except:
        return default

TELEGRAM_TOKEN = get_config_value("TELEGRAM_TOKEN", "TU_TOKEN_SI_PRUEBAS_LOCAL")
CHAT_ID = get_config_value("CHAT_ID", "TU_ID_SI_PRUEBAS_LOCAL")
APP_PASSWORD = get_config_value("APP_PASSWORD", "1234")
