# Importación de bibliotecas necesarias
import os
import openai
import streamlit as st
import time

# Configuración de la página de Streamlit para Asistente Virtual
st.set_page_config(
    page_title="Asistente Virtual: Tu compañero digital multiexperto, siempre listo para ayudarte en español con respuestas precisas, claras y personalizadas en cualquier tema o tarea.",  # Título de la página
    page_icon="🤖",  # Icono de la página
    initial_sidebar_state='collapsed',
    layout="wide",
    menu_items={
        'Get Help': 'https://www.isabellaea.com',
        'Report a bug': None,
        'About': "Asistente Virtual: Tu compañero digital multiexperto, siempre listo para ayudarte en español con respuestas precisas, claras y personalizadas en cualquier tema o tarea."
    }
)

# Función para verificar si el archivo secrets.toml existe
def secrets_file_exists():
    secrets_path = os.path.join('.streamlit', 'secrets.toml')
    return os.path.isfile(secrets_path)

# Intentar obtener el ID del asistente de OpenAI desde st.secrets si el archivo secrets.toml existe
if secrets_file_exists():
    try:
        ASSISTANT_ID = st.secrets['ASSISTANT_ID']
    except KeyError:
        ASSISTANT_ID = None
else:
    ASSISTANT_ID = None

# Si no está disponible, pedir al usuario que lo introduzca
if not ASSISTANT_ID:
    ASSISTANT_ID = st.sidebar.text_input('Introduce el ID del asistente de OpenAI', type='password')

# Si aún no se proporciona el ID, mostrar un error y detener la ejecución
if not ASSISTANT_ID:
    st.sidebar.error("Por favor, proporciona el ID del asistente de OpenAI.")
    st.stop()

assistant_id = ASSISTANT_ID

# Inicialización del cliente de OpenAI
client = openai

# Presentación del Asistente Virtual
st.title("Bienvenido a tu Asistente Virtual 🤖")

st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <h3 style="color: #1f77b4;">¡Hola! Soy tu Asistente Virtual</h3>
    <p>Tu compañero digital multiexperto, siempre listo para ayudarte en español con respuestas precisas, claras y personalizadas en cualquier tema o tarea.</p>
    
    <h4 style="color: #2ca02c;">¿En qué puedo ayudarte hoy? 🤔</h4>
    <ul>
        <li>Responder a tus preguntas sobre una amplia variedad de temas.</li>
        <li>Asistirte en tareas como análisis, cálculos o planificación.</li>
        <li>Proporcionar explicaciones detalladas y ejemplos prácticos.</li>
        <li>Ofrecer sugerencias y soluciones creativas a tus problemas.</li>
        <li>Y mucho más...</li>
    </ul>
    
    <p><strong>No dudes en preguntarme sobre cualquier tema. ¡Estoy aquí para ayudarte en español!</strong></p>
</div>
""", unsafe_allow_html=True)

# Inicialización de variables de estado de sesión
st.session_state.start_chat = True
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# Cargar la clave API de OpenAI
API_KEY = os.environ.get('OPENAI_API_KEY') or st.secrets.get('OPENAI_API_KEY')
if not API_KEY:
    API_KEY = st.sidebar.text_input('Introduce tu clave API de OpenAI', type='password')

if not API_KEY:
    st.sidebar.error("Por favor, proporciona una clave API para continuar.")
    st.stop()

openai.api_key = API_KEY

def process_message_with_citations(message):
    """Extraiga y devuelva solo el texto del mensaje del asistente."""
    if hasattr(message, 'content') and len(message.content) > 0:
        message_content = message.content[0]
        if hasattr(message_content, 'text'):
            nested_text = message_content.text
            if hasattr(nested_text, 'value'):
                return nested_text.value
    return 'No se pudo procesar el mensaje'

# Crear un hilo de chat inmediatamente después de cargar la clave API
if not st.session_state.thread_id:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id
    st.write("ID del hilo: ", thread.id)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Cómo puedo ayudarte hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("usuario"):
        st.markdown(prompt)

    # Enviar mensaje del usuario
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=prompt
    )

    # Crear una ejecución para el hilo de chat
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=assistant_id
    )

    while run.status != 'completed':
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=run.id
        )

    # Recuperar mensajes agregados por el asistente
    messages = client.beta.threads.messages.list(
    thread_id=st.session_state.thread_id
    )

    # Procesar y mostrar mensajes del asistente
    for message in messages:
        if message.run_id == run.id and message.role == "assistant":
            full_response = process_message_with_citations(message)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            with st.chat_message("assistant"):
                st.markdown(full_response)
                
# Footer
st.sidebar.markdown('---')
st.sidebar.subheader('Creado por:')
st.sidebar.markdown('Alexander Oviedo Fadul')
st.sidebar.markdown("[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)")