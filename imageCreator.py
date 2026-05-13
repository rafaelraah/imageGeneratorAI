import base64
from groq import Groq
from dotenv import load_dotenv
from colorama import Fore, Style, init
import os

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def gerar_imagem(prompt: str, output_path: str = "imagem.png"):
    # Payload para o modelo de texto‑para‑imagem
    response = client.chat.completions.create(
        model="stabilityai/sdxl-base",  # um dos modelos gratuitos no catálogo Groq
        messages=[
            {"role": "user", "content": f"Generate an image for: {prompt}"}
        ],
        max_tokens=0, # não gerar texto, só a imagem
        temperature=0.0,
        top_p=1,
        stream=False,
    )

    img_b64 = response.choices[0].message.content
    img_bytes = base64.b64decode(img_b64)

    # Salva a imagem no disco
    with open(output_path, "wb") as f:
        f.write(img_bytes)

    print(f"Imagem salva em {output_path}")

# Exemplo de uso
if __name__ == "__main__":
    prompt = "um gato astronauta flutuando no espaço, estilo digital art"
    gerar_imagem(prompt, "gato_astro.png")