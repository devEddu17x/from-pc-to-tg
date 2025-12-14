import streamlit as st
import requests
from io import BytesIO

# --- CONFIGURACIÓN ---
# En local puedes poner los datos aquí, pero en producción usaremos 'Secrets'
TELEGRAM_TOKEN = st.secrets.get("TELEGRAM_TOKEN", "TU_TOKEN_SI_PRUEBAS_LOCAL")
CHAT_ID = st.secrets.get("CHAT_ID", "TU_ID_SI_PRUEBAS_LOCAL")
APP_PASSWORD = st.secrets.get("APP_PASSWORD", "1234") # La contraseña de acceso

def send_to_telegram(uploaded_file):
    """Envía el archivo a la API de Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    
    # Preparamos el archivo y los datos
    # Reiniciamos el puntero del archivo
    uploaded_file.seek(0)
    files = {'document': (uploaded_file.name, uploaded_file, uploaded_file.type)}
    data = {'chat_id': CHAT_ID, 'caption': f"📂 Archivo recibido: {uploaded_file.name}"}
    
    response = requests.post(url, data=data, files=files)
    return response

def format_file_size(size_bytes):
    """Formatea el tamaño del archivo en formato legible"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Animación de entrada */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Animación de pulso para el área de arrastre */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        color: #f0f0f0;
        animation: fadeIn 0.8s ease-out;
        margin-bottom: 10px;
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
        animation: fadeIn 1s ease-out;
    }
    
    /* Tarjetas de archivo - diseño minimalista */
    .file-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0;
        color: #e0e0e0;
        animation: fadeIn 0.4s ease-out;
        transition: all 0.2s ease;
        backdrop-filter: blur(10px);
    }
    
    .file-card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateX(4px);
    }
    
    .file-name {
        font-size: 0.95em;
        font-weight: 500;
        margin-bottom: 4px;
        color: #ffffff;
    }
    
    .file-info {
        font-size: 0.8em;
        opacity: 0.6;
        color: #b0b0b0;
    }
    
    /* Área de carga con efecto hover */
    [data-testid="stFileUploader"] {
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        animation: pulse 2s infinite;
    }
    
    /* Botón de enviar - diseño minimalista consistente */
    .stButton > button {
        background: rgba(255, 255, 255, 0.08);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        padding: 14px 24px;
        font-size: 0.95em;
        font-weight: 500;
        transition: all 0.2s ease;
        backdrop-filter: blur(10px);
        width: 100%;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.3);
        transform: translateY(-1px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Mensaje de éxito personalizado */
    .success-message {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        animation: fadeIn 0.5s ease-out;
        margin: 20px 0;
    }
    
    /* Contenedor de estadísticas */
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 20px 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: white;
        min-width: 150px;
        animation: fadeIn 0.8s ease-out;
    }
    
    .stat-number {
        font-size: 2.5em;
        font-weight: bold;
    }
    
    .stat-label {
        font-size: 1em;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# --- INTERFAZ DE USUARIO ---
st.markdown('<div class="main-title">☁️ Enviar a mi Telegram</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Comparte tus archivos de forma segura y rápida</div>', unsafe_allow_html=True)

# Inicializar estado de sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'files_sent' not in st.session_state:
    st.session_state.files_sent = []

# 1. Validación de Contraseña - solo si no está autenticado
if not st.session_state.authenticated:
    # Ocultar el botón de mostrar contraseña con CSS
    st.markdown("""
        <style>
        button[kind="icon"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    password = st.text_input("🔐 Contraseña de acceso", type="password", placeholder="Ingresa tu contraseña", label_visibility="collapsed", key="password_input")
    
    # Aplicar estilo de error si la contraseña es incorrecta
    if password and password != APP_PASSWORD:
        st.markdown("""
            <style>
            input[type="password"] {
                border-color: #ff4b4b !important;
                box-shadow: 0 0 0 0.2rem rgba(255, 75, 75, 0.25) !important;
            }
            </style>
        """, unsafe_allow_html=True)
    
    if password == APP_PASSWORD:
        st.session_state.authenticated = True
        st.rerun()

if st.session_state.authenticated:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. Área de subida de archivos (ahora acepta múltiples)
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
                st.success(f"Se enviaron {success_count} archivo(s) correctamente" + 
                          (f" | ⚠️ {error_count} con error" if error_count > 0 else ""))
            else:
                st.error("❌ No se pudo enviar ningún archivo")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Mostrar archivos en formato compacto
        for idx, file in enumerate(uploaded_files):
            file_size = format_file_size(file.size)
            st.markdown(f"""
                <div class="file-card">
                    <div class="file-name">• {file.name}</div>
                    <div class="file-info">
                        {file_size} · {file.type if file.type else 'Desconocido'}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Mostrar historial de archivos enviados
    if st.session_state.files_sent:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<p style="color: #888; font-size: 0.85em; margin-bottom: 10px;">Enviados recientemente</p>', unsafe_allow_html=True)
        
        for file_info in reversed(st.session_state.files_sent[-5:]):  # Últimos 5
            st.markdown(f"""
                <div class="file-card">
                    <div class="file-name">✓ {file_info['name']}</div>
                    <div class="file-info">{file_info['size']}</div>
                </div>
            """, unsafe_allow_html=True)