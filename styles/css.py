"""
Estilos CSS para la aplicación
"""


def get_main_styles():
    """Retorna los estilos CSS principales"""
    return """
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
    
    /* Limitar ancho del contenedor principal */
    .main .block-container {
        max-width: 900px;
        padding-left: 2rem;
        padding-right: 2rem;
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
    </style>
    """


def get_password_hide_icon_style():
    """Retorna el estilo para ocultar el botón de mostrar contraseña"""
    return """
    <style>
    button[kind="icon"] {
        display: none !important;
    }
    </style>
    """


def get_password_error_style():
    """Retorna el estilo para indicar contraseña incorrecta"""
    return """
    <style>
    input[type="password"] {
        border-color: #ff4b4b !important;
        box-shadow: 0 0 0 0.2rem rgba(255, 75, 75, 0.25) !important;
    }
    </style>
    """
