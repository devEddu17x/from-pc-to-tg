# Telegram File Uploader

Aplicación web para enviar archivos a Telegram. Soporta múltiples archivos, protegido con contraseña y con interfaz minimalista.

## Ejecutar Localmente

### Sin Docker

Crear `.streamlit/secrets.toml`:

```toml
TELEGRAM_TOKEN = "tu_bot_token"
CHAT_ID = "tu_chat_id"
APP_PASSWORD = "tu_contraseña"
```

Ejecutar:

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Con Docker

```bash
docker build -t telegram-uploader .
docker run -p 8501:8501 \
  -e TELEGRAM_TOKEN="tu_bot_token" \
  -e CHAT_ID="tu_chat_id" \
  -e APP_PASSWORD="tu_contraseña" \
  telegram-uploader
```

La aplicación estará disponible en `http://localhost:8501`
