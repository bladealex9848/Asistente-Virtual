# Asistente Virtual 🤖

![Logo del Asistente Virtual](https://github.com/bladealex9848/Asistente-Virtual/blob/main/logo.jpg)

[![Version](https://img.shields.io/badge/versión-1.0.0-darkgreen.svg)](https://github.com/bladealex9848/Asistente-Virtual)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-ff4b4b.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI_API-v2-00C244.svg)](https://platform.openai.com/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](LICENSE)
[![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fasistentevirtual.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)](https://asistentevirtual.streamlit.app)

## 🤖 Descripción

El Asistente Virtual es una potente herramienta de inteligencia artificial desarrollada con Streamlit y la API de OpenAI. Este asistente multiexperto está diseñado para proporcionar ayuda en español sobre una amplia variedad de temas, ofreciendo respuestas precisas, claras y personalizadas a tus preguntas y tareas.

Este asistente está concebido para ser tu compañero digital ideal, capaz de asistirte en diversos temas y tareas, desde búsqueda de información hasta análisis complejos, cálculos, planificación, y generación de contenido creativo. Todo esto disponible en español, con una interfaz intuitiva y accesible para usuarios de todos los niveles técnicos.

## 🔍 Funcionalidades Principales

### 1. Asistencia Informativa
- **Consultas Generales**: Respuestas precisas sobre una amplia variedad de temas
- **Explicaciones Detalladas**: Desgloses claros de conceptos complejos
- **Recomendaciones**: Sugerencias personalizadas basadas en tus necesidades
- **Actualidad**: Información sobre eventos y temas relevantes

### 2. Apoyo en Tareas Específicas
- **Análisis de Datos**: Interpretación y síntesis de información numérica
- **Cálculos**: Resolución de problemas matemáticos y estadísticos
- **Planificación**: Ayuda en la organización de proyectos y actividades
- **Toma de Decisiones**: Evaluación de opciones y alternativas

### 3. Generación de Contenido
- **Redacción**: Creación de textos para diferentes propósitos y audiencias
- **Resúmenes**: Condensación de información extensa en puntos clave
- **Correcciones**: Mejora de estilo, gramática y claridad en textos
- **Creatividad**: Generación de ideas, historias y contenido original

### 4. Solución de Problemas
- **Diagnóstico**: Identificación de causas raíz en situaciones problemáticas
- **Estrategias**: Desarrollo de enfoques para abordar desafíos
- **Alternativas**: Presentación de diferentes soluciones posibles
- **Paso a Paso**: Guías detalladas para implementar soluciones

### 5. Procesamiento de Documentos
- **Análisis**: Extracción de información clave de documentos cargados
- **Resumen**: Condensación de documentos extensos
- **Interpretación**: Explicación de términos técnicos y conceptos
- **Comparación**: Análisis de similitudes y diferencias entre documentos

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- Pip (administrador de paquetes de Python)
- Cuenta en OpenAI con acceso a la API
- Asistente Virtual configurado en OpenAI

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/bladealex9848/Asistente-Virtual.git
   cd Asistente-Virtual
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar credenciales**

   **Opción A: Usando variables de entorno**
   ```bash
   # En Windows
   set OPENAI_API_KEY=tu-api-key-aqui
   set ASSISTANT_ID=tu-assistant-id-aqui
   
   # En macOS/Linux
   export OPENAI_API_KEY=tu-api-key-aqui
   export ASSISTANT_ID=tu-assistant-id-aqui
   ```

   **Opción B: Usando archivo secrets.toml**
   
   Crea un archivo `.streamlit/secrets.toml` con el siguiente contenido:
   ```toml
   OPENAI_API_KEY = "tu-api-key-aqui"
   ASSISTANT_ID = "tu-assistant-id-aqui"
   ```

## ⚙️ Uso

### Iniciar la Aplicación

```bash
streamlit run app.py
```

Esto lanzará la aplicación y abrirá automáticamente una ventana del navegador en `http://localhost:8501`.

### Funcionalidades del Asistente

1. **Consultas de Información**
   - Realiza preguntas sobre cualquier tema de tu interés
   - Ejemplo: "¿Cuáles son las energías renovables más eficientes actualmente?"

2. **Ayuda con Tareas**
   - Solicita asistencia para análisis, cálculos o planificación
   - Ejemplo: "Ayúdame a crear un plan de estudios para aprender Python en 3 meses"

3. **Generación de Contenido**
   - Pide la creación de textos, resúmenes o ideas
   - Ejemplo: "Escribe un correo formal solicitando una extensión para entregar un proyecto"

4. **Resolución de Problemas**
   - Describe situaciones problemáticas y solicita soluciones
   - Ejemplo: "¿Cómo puedo optimizar el rendimiento de mi equipo de trabajo remoto?"

5. **Análisis de Documentos**
   - Sube documentos para extraer información relevante
   - El asistente puede procesar y analizar diversos tipos de documentos

## ⚠️ Limitaciones

- El Asistente Virtual proporciona información general y no constituye asesoramiento profesional especializado
- La información se basa en el conocimiento disponible hasta octubre de 2023
- Para temas que requieren expertise profesional (legal, médico, financiero), consulta a especialistas calificados
- El análisis de documentos es preliminar y puede requerir revisión profesional en casos complejos

## 📊 Escenarios de Uso

### 1. Entorno Educativo
- Apoyo en la investigación y estudio de diversos temas
- Explicación de conceptos complejos de forma accesible
- Ayuda en la preparación de trabajos y presentaciones
- Respuesta a dudas específicas sobre materias académicas

### 2. Ámbito Profesional
- Asistencia en la redacción de correos, informes y propuestas
- Análisis rápido de datos e información corporativa
- Generación de ideas para proyectos y soluciones
- Optimización de procesos de trabajo y planificación

### 3. Uso Personal
- Respuesta a consultas sobre salud, finanzas, tecnología y otros temas cotidianos
- Ayuda en la planificación de actividades personales
- Asistencia en la toma de decisiones informadas
- Generación de contenido creativo para uso personal

## 👥 Contribuciones

Las contribuciones son bienvenidas. Para contribuir al desarrollo del Asistente Virtual:

1. Realiza un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Implementa tus cambios
4. Envía un pull request

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **OpenAI** por proporcionar la tecnología que impulsa el asistente
- **Streamlit** por facilitar el desarrollo de interfaces intuitivas
- **Comunidad de código abierto** por sus innumerables contribuciones que hacen posible proyectos como este

## 👤 Autor

Creado con ❤️ por [Alexander Oviedo Fadul](https://github.com/bladealex9848)

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)

---

## 💼 Mensaje Final

El Asistente Virtual busca democratizar el acceso a la información y las capacidades de la inteligencia artificial, poniéndolas al servicio de todos en español. Este asistente evoluciona constantemente para ofrecerte respuestas cada vez más precisas, contextualizadas y útiles.

*"La tecnología más poderosa es aquella que desaparece en el fondo y se integra perfectamente en nuestras vidas, facilitándonos tareas, expandiendo nuestras capacidades y permitiéndonos centrarnos en lo que realmente importa: nuestras metas, ideas y conexiones humanas."*