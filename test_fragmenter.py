import unittest
from unittest.mock import patch, MagicMock
from src.fragmenter import ArticleProcessor, GPTFragmenter

class TestArticleProcessor(unittest.TestCase):
    
    def setUp(self):
        """Se simula el procesador de artículos, incluyendo la GPT API Key."""
        self.gpt_fragmenter = GPTFragmenter(api_key='fake-api-key')
        self.processor = ArticleProcessor(self.gpt_fragmenter)

    @patch('gpt_api.openai.ChatCompletion.create')
    def test_fragment_content(self, mock_gpt_api):
        """Prueba la fragmentación de un artículo en 1000 tokens simulando la GPT API"""
        #Simular la respuesta de la GPT API
        mock_gpt_api.return_value = {
            'choices':[{
                'message': {
                    'content': "Contenido corto del artículo para fragmentar."
                }
            }]
        }

        #Ejecutar la fragmentación
        content = "Contenido corto del artículo para fragmentar."
        fragments = self.gpt_fragmenter.generate_fragment(content)

        #Validar que en el fragmento hay parte del contenido enviado 
        self.assertIn("Contenido", fragments)

    @patch('fragmenter.spacy.load')
    def test_generate_tags_from_content(self, mock_spacy_load):
        """Valida la extracción de las palabras clave más frecuentes para generar los tags de un fragmento"""
        mock_nlp = MagicMock()
        mock_doc = MagicMock()
       
        #Simular los tokens lematizados para este contenido
        mock_doc.__iter__.return_value = [
            MagicMock(lemma_="documento", is_alpha=True, is_stop=False),
            MagicMock(lemma_="proceso", is_alpha=True, is_stop=False),
            MagicMock(lemma_="documento", is_alpha=True, is_stop=False)
        ]
        mock_spacy_load.return_value = mock_nlp

        #Ejecutar la extracción de los tags
        content = "Esto es un documento ejemplo del proceso."
        tags = self.processor.generate_tags_from_content(content)

        #Validar que las palabras frecuentes encontradas corresponden
        self.assertEqual(tags, ['documento', 'ejemplo', 'proceso'])

if __name__ == '__main__':
    unittest.main()
  