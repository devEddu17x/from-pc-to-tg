import streamlit as st
import requests

# --- CONFIGURACIÓN ---
# En local puedes poner los datos aquí, pero en producción usaremos 'Secrets'
TELEGRAM_TOKEN = st.secrets.get("TELEGRAM_TOKEN", "TU_TOKEN_SI_PRUEBAS_LOCAL")
CHAT_ID = st.secrets.get("CHAT_ID", "TU_ID_SI_PRUEBAS_LOCAL")
APP_PASSWORD = st.secrets.get("APP_PASSWORD", "1234") # La contraseña de acceso

def send_to_telegram(uploaded_file):
    """Envía el archivo a la API de Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    
    # Preparamos el archivo y los datos
    files = {'document': (uploaded_file.name, uploaded_file, uploaded_file.type)}
    data = {'chat_id': CHAT_ID, 'caption': f"📂 Archivo recibido: {uploaded_file.name}"}
    
    response = requests.post(url, data=data, files=files)
    return response

# --- INTERFAZ DE USUARIO ---
st.set_page_config(page_title="Mi Nube Personal", page_icon="☁️")

st.title("☁️ Enviar a mi Telegram")

# 1. Validación de Contraseña
password = st.text_input("Contraseña de acceso", type="password")

if password == APP_PASSWORD:
    st.success("Acceso concedido")
    
    # 2. Área de subida de archivos
    uploaded_file = st.file_uploader("Arrastra tu archivo aquí", accept_multiple_files=False)
    
    if uploaded_file is not None:
        # Botón de enviar
        if st.button("Enviar a Telegram 🚀"):
            with st.spinner("Enviando..."):
                try:
                    resp = send_to_telegram(uploaded_file)
                    if resp.status_code == 200:
                        st.balloons()
                        st.success(f"¡Éxito! {uploaded_file.name} enviado.")
                    else:
                        st.error(f"Error en Telegram: {resp.text}")
                except Exception as e:
                    st.error(f"Ocurrió un error: {e}")

elif password:
    st.warning("Contraseña incorrecta")