# 📁 Estructura del Proyecto

Aplicación modular para enviar archivos a Telegram usando Streamlit.

## 📂 Estructura de Carpetas

```
from-pc-to-tg/
├── app.py                      # Archivo principal de la aplicación
├── config.py                   # Configuración (tokens, passwords)
├── requirements.txt            # Dependencias
│
├── components/                 # Componentes de interfaz
│   ├── __init__.py
│   ├── auth.py                # Autenticación y login
│   ├── ui.py                  # Componentes de UI (header, cards, etc)
│   └── uploader.py            # Upload y envío de archivos
│
├── styles/                     # Estilos CSS
│   ├── __init__.py
│   └── css.py                 # Todos los estilos CSS
│
└── utils/                      # Utilidades
    ├── __init__.py
    └── helpers.py             # Funciones helper (send_to_telegram, etc)
```

## 📝 Descripción de Módulos

### `app.py`

- Punto de entrada principal
- Orquesta todos los componentes
- Maneja el flujo de la aplicación

### `config.py`

- Configuración centralizada
- Variables de entorno y secrets
- Tokens de Telegram y contraseñas

### `components/auth.py`

- Inicialización de session state
- Renderizado del formulario de login
- Verificación de autenticación

### `components/ui.py`

- Componentes visuales reutilizables
- Header de la aplicación
- Tarjetas de archivos
- Historial de envíos

### `components/uploader.py`

- Manejo de carga de archivos
- Procesamiento de envío a Telegram
- Barra de progreso y feedback

### `styles/css.py`

- Estilos CSS organizados por función
- Animaciones
- Temas y colores

### `utils/helpers.py`

- Funciones de utilidad
- Envío a Telegram API
- Formateo de tamaños de archivo

## 🚀 Uso

```bash
streamlit run app.py
```
