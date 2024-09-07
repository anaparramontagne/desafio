#Ejercicio de Fragmentación de Artículos

##Descripción:

El objetivo de este ejercicio es procesar un archivo '.jsonl' que contiene documentación de Adereso, fragmentar los artículos en secciones que incluyan:
-**Resumen**: Un resumen del contenido del fragmento
-**Tags**: Palabras que describan el contenido
-**Título**: El título de cada fragmento
-**Referencia**: La URL del artículo original
-**Contenido**: El texto o contenido del artículo convertido en tokens
-**Referencias Relacionadas**: URL de los fragmentos que puedan coincidir en su contenido según un crítero particular.

##Tecnologías y librerias empleadas

- **Python** 3.8+
- **GPT-4 API** (gpt-40-mini)
- **SpaCy** para la comparación de similitud entre textos
- **Unittest** para las pruebas unitarias
- **JSONL** para procesamiento y salida

##Requisitos
1. GPT-4 API Token: es necesario que cuentes con un token válido y vigente para utilizar la API de OpenAI
2. Python: Asegúrate de tener Python 3.8 o superior instalado en tu equipo
3. Dependencias: Las dependencias del ejercicio están listadas en requirements.txt

##Instalación
Sigue estos pasos para configurar tu entorno local:

###Clonar el repositorio
Ejecuta en tu terminal: 
git clone https://github.com/anaparramontagne/desafio.git
cd desafio

###Crear y activar un entorno virtual
Ejecuta en tu terminal: 
python3 -m venv venv
source venv/bin/activate # En Windows utiliza: venv\Scripts\activate

###Instala las dependencias
Ejecuta en tu terminal: 
pip install -r requirements.txt

###Descarga el modelo de SpaCy
python -m spacy download en_core_md

##Configuración 

###Variables de entorno

Debes configurar las siguientes variables de entorno antes de ejecutar el proyecto:
1. GPT_API_KEY: Es la clave de la API de OpenAI para realizar solicitudes.

Puedes configurarla en tu entorno local o en un archivo .env (si lo tienes config con herramientas como python-dotenv)

###Ejemplo del archivo .env
GPT_API_KEY=tu_gpt_api_key

##Ejecución del proyecto
1. Dentro de la carpeta **data** debes almacenar el archivo de entrada (input.jsonl) y el archivo de salida ya se encuentra en esta carpeta (output.jsonl)
2. Para facilitar el proceso de ejecución esta incluido un notebook de Jupyter.

##Pruebas
Se han incluido algunas pruebas unitarias, para ejecutarlas utiliza el siguiente comando en tu terminal:
PYTHONPATH=src python -m unittest discover -s tests



