![Logo del Asistente Virtual](https://github.com/bladealex9848/Asistente-Virtual/blob/main/logo.jpg)

# Asistente Virtual: Tu compañero digital multiexperto

## Descripción

El Asistente Virtual es una herramienta de inteligencia artificial diseñada para proporcionar ayuda en español sobre una amplia variedad de temas. Utilizando la potencia de la API de OpenAI, este asistente ofrece respuestas precisas, claras y personalizadas a tus preguntas y tareas.

## Introducción

Con el Asistente Virtual, podrás interactuar con una IA avanzada capaz de asistirte en diversos temas y tareas. Ya sea que necesites información, análisis, cálculos o sugerencias creativas, este asistente está listo para ayudarte en español. Para desarrollar esta aplicación se utilizaron:

- OpenAI API
- Streamlit

## ¿Cómo funciona?

1. El usuario introduce una pregunta o solicitud.
2. La aplicación crea un hilo de conversación con OpenAI.
3. La pregunta se envía al asistente de OpenAI.
4. El asistente procesa la solicitud y genera una respuesta.
5. La respuesta se muestra al usuario en la interfaz de Streamlit.

## Funcionalidades

- **Respuestas en tiempo real**: Proporciona respuestas instantáneas a tus preguntas.
- **Multiexperto**: Capaz de asistir en una amplia gama de temas y tareas.
- **Interfaz amigable**: Diseñado con Streamlit para una experiencia de usuario intuitiva.
- **Persistencia de conversación**: Mantiene el contexto de la conversación para una interacción más natural.

## Instalación

1. Asegúrate de tener Python 3.8 o superior instalado en tu máquina.
2. Clona este repositorio: `git clone https://github.com/bladealex9848/asistente-virtual.git`
3. Navega al directorio del proyecto: `cd asistente-virtual`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Crea un archivo `.streamlit/secrets.toml` y añade tu ASSISTANT_ID de OpenAI:
   ```
   ASSISTANT_ID = "tu-assistant-id-aqui"
   ```
6. Configura tu clave API de OpenAI como variable de entorno o en el archivo `secrets.toml`.

## Uso

1. Ejecuta la aplicación: `streamlit run app.py`
2. Abre tu navegador y ve a `http://localhost:8501`
3. Comienza a interactuar con el Asistente Virtual escribiendo tus preguntas o solicitudes.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, haz un fork del repositorio, crea una nueva rama para tus cambios, y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

Creado por Alexander Oviedo Fadul

[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)