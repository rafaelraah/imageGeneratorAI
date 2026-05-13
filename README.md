# 🎨 Gerador de Imagens com IA

Projeto desenvolvido em Python utilizando Streamlit, Groq e Hugging Face para geração de imagens com Inteligência Artificial.

O sistema permite que o usuário digite prompts em português. O texto é automaticamente traduzido para inglês utilizando um modelo LLM hospedado na Groq e, em seguida, enviado para um modelo de geração de imagens da Hugging Face.

---

# 🚀 Tecnologias utilizadas

* Python
* Streamlit
* Groq API
* Hugging Face Inference API
* FLUX.1-schnell

---

# 🧠 Funcionalidades

✅ Tradução automática de prompts PT-BR → EN

✅ Geração de imagens com IA

✅ Interface web simples com Streamlit

✅ Integração com APIs modernas de IA

✅ Exibição do prompt traduzido antes da geração da imagem

---

# 📸 Como funciona

1. O usuário digita um prompt em português
2. O sistema traduz o texto para inglês utilizando um LLM
3. O prompt traduzido é enviado para o modelo FLUX.1-schnell
4. A imagem gerada é exibida no frontend

---

# ⚙️ Instalação

Clone o projeto:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

Entre na pasta:

```bash
cd seurepositorio
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

## Windows

```bash
.venv\Scripts\activate
```

## Linux/macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 🔑 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
HUGGINGFACE_API_KEY=sua_chave
GROQ_API_KEY=sua_chave
```

---

# ▶️ Executando o projeto

```bash
streamlit run app.py
```

---

# 🖼️ Modelo de geração de imagens

Modelo utilizado:

* black-forest-labs/FLUX.1-schnell

---

# 📚 Objetivo do projeto

Este projeto foi desenvolvido com foco em aprendizado prático de:

* Inteligência Artificial
* APIs de IA
* Python
* Streamlit
* Integração entre modelos generativos

---

# 👨‍💻 Autor

Rafael Nascimento
