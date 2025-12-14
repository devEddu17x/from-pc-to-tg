"""
Funciones de utilidad para la aplicación
"""
import requests
from config import TELEGRAM_TOKEN, CHAT_ID


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
