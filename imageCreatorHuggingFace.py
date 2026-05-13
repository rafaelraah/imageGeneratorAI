from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Carrega .env
load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Cliente Hugging Face
client = InferenceClient(
    provider="hf-inference",
    api_key=API_KEY
)

def gerar_imagem(prompt: str, output_path: str = "imagem.png"):

    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    image.save(output_path)

    print(f"Imagem salva em {output_path}")

# Exemplo
if __name__ == "__main__":

    prompt = input("Digite aqui o prompt da sua imagem")

    gerar_imagem(prompt, "gato_astro.png")