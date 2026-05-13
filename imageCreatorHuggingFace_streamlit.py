import streamlit as st
from groq import Groq
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

# Cliente Groq
clientGroq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def gerar_textoIngles(texto:str):
    # Chamada API do GROQ
    response = clientGroq.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
                    {
                        "role": "system",
                        "content": """Você é um especialista em traduzir textos de português para inglês. 
                                      Você apenas traduz o texto e entrega a tradução, sem mais nenhuma informação."""
                    },
                    {
                        "role": "user",
                        "content": texto
                    }
                ]
    )
    resposta = response.choices[0].message.content;
    return resposta;

def gerar_imagem(prompt: str, output_path: str = "imagem.png"):

    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    return image; 
 
   # image.save(output_path)
   # print(f"Imagem salva em {output_path}")

# Exemplo
# if __name__ == "__main__":
#     prompt = input("Digite aqui o prompt da sua imagem")
#     gerar_imagem(prompt, "gato_astro.png")

# Frontend
st.set_page_config(
    page_title="Gerador de Imagens",
    page_icon="🎨"
)

st.title("🎨 Gerador de Imagens IA")

prompt = st.text_input(
    "Digite o prompt da imagem"
)

if st.button("Gerar imagem"):

    if prompt:

        with st.spinner("Gerando imagem..."):

            textoEmIngles = gerar_textoIngles(prompt);
            image = gerar_imagem(textoEmIngles)

            # Mostra no frontend
            st.text("A tradução do seu prompt para enviar para o modelo de geração de imagens:");
            st.markdown("**" + textoEmIngles + "**");
            st.text("Veja o resultado abaixo:");
            st.image(image, caption="E aí, gostou do resultado? :D")

    else:
        st.warning("Digite um prompt 😄")