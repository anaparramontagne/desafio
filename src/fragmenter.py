from src.gpt_api import GPTFragmenter
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
import spacy

if not stopwords:
    nltk.download('stopwords') #Descargamos las stopwords o palabras omitibles 
    
class ArticleProcessor:
    def __init__(self, gpt_fragmenter):

        self.gpt_fragmenter = gpt_fragmenter
        self.stop_words = set(stopwords.words('spanish')) #Puede ser cualquier otro idioma como 'english'
        self.processed_articles = [] #Almacenará los fragmentos procesados
        self.nlp = spacy.load('en_core_web_md') #Modelo de embeddings

    def process_article(self, article, keywords=[]):
        content = article['text']
        title = article.get('title', self.generate_title(content))
        summary = self.generate_summary(content)
        reference = article.get('url', 'Sin referencias')

        #Invoca la API GPT para generar fragmentos
        fragment = self.gpt_fragmenter.generate_fragment(content)

        #Generamos las palabras más comúnes como tags 
        tags = self.generate_tags_from_content(content)

        #Creamos el fragmento sin referencias relacionadas
        processed_fragment = {
            'summary': summary,
            'tags': tags,
            'title': title,
            'reference': reference,
            'content': fragment,
            'related_references': [] #Se agregara contenido más adelante
        }

        return processed_fragment

    def generate_title(self, content):
        """Extrae las primeras 4 palabras de contenido para generar el titulo del fragmento"""
        words_title = content.split()[:4] #Puede ajustarse la cantidad de palabras que se consideren necesarias
        
        #Se crea la cadena de caracteres que será el titulo
        return ' '.join(words_title)
    
    def generate_summary(self, content):
        """Extrae las primeras 20 palabras de contenido para generar el resumen del articulo"""
        words_summary = content.split()[:20] #Puede ajustarse la cantidad de palabras que se consideren necesarias
        
        #Se crea la cadena de caracteres que será el resumen (summary)
        return ' '.join(words_summary)
    
    def generate_tags_from_content(self, content, top_n=5):
        """Genera una lista con las palabras más repetidas en el contenido, excluyendo stopwords"""
        words = re.findall(r'\b\w+\b', content.lower()) #Generamos tokens del contenido para eliminar signos de puntuación y lo llevamos a minúsculas

        #Filtramos las stopwords (p.ej: de, el, la)
        filtered_words = [word for word in words if word not in self.stop_words]

        #Contamos la frecuencia de las palabras
        word_counts = Counter(filtered_words)

        #Obtenemos las palabras más frecuentes
        common_words = [word for word, count in word_counts.most_common(top_n)] 

        return common_words
