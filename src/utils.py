import json
import spacy

def load_jsonl(file_path):
    #Carga el archivo base, cuya ruta se recibe como parámetro
    articles = []
    with open(file_path, 'r') as file:
        for line in file:
            item = json.loads(line.strip())
            if item.get('type') == 'article': 
                articles.append(item)
    return articles

def write_output_file(fragments, output_path):
    #Almacena los fragmentos en el archivo de salida
    with open(output_path, 'w', encoding='utf-8') as file:
        for fragment in fragments:
            file.write(json.dumps(fragment) + '\n')

def find_related_references(articles, threshold=0.1): #Puede ajustarse el nivel de coincidencia deseado 
    #Encuentra referencias relacionadas basado en coincidencias semanticas.
    nlp = spacy.load('en_core_web_md') #Modelo de embeddings
    for i, article in enumerate(articles):
        related_references = set()
        current_doc = nlp(article['content'])

        #Comparar el contenido actual con los otros contenidos
        for j, other_article in enumerate(articles):
            if i != j: #Evitamos que se compare consigo mismo
                #Buscamos coincidencias entre el fragmento actual y los otros procesados
                other_doc = nlp(other_article['content'])
                similarity = current_doc.similarity(other_doc)
                
                #Evaluamos nivel de coincidencia y este debe ser mayor al umbral establecido
                if similarity > threshold: 
                    related_references.add(other_article['reference'])
        
    #Agregamos las referencias relacionadas al fragmento que estamos comparando
    article['related_references'] = list(related_references)

    return articles
