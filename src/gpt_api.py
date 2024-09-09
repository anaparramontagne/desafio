import openai

class GPTFragmenter:
    def __init__(self, api_key): 
        openai.api_key = api_key

    def generate_fragment(self, content, num_tokens=1000): #Por defecto es 1000 
        """Se invoca a la GPT API para obtener el contenido con el número de tokens."""
        messages = [
            {"role": "system", "content": "Estas siendo de ayuda para procesar este contenido."},
            {"role": "user", "content": f"Por favor fragmenta el contenido en secciones de {num_tokens} tokens:\n{content}"}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages = messages,
            max_tokens=num_tokens
        )
        return response['choices'][0]['message']['content'].strip()