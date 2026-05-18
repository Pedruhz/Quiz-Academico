import streamlit as st
import random

# Configuração da página
st.set_page_config(
    page_title="Quiz Acadêmico",
    page_icon="📚",
    layout="wide"
)

st.markdown(
    """
    <style>
    [data-testid="stBottom"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    footer {visibility: hidden;}        
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .stRadio label {
        font-size: 20px !important;
    }

    .stButton button {
        width: 100%;
        height: 50px;
        font-size: 18px;
    }

    h1 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.title("📚 Quiz Acadêmico")
st.write("Teste seus conhecimentos!")

# Perguntas
perguntas = [
    {
        "pergunta": "Qual é a capital da Alemanha?",
        "opcoes": ["Hamburg", "Berlim", "Munique", "Frankfurt"],
        "resposta": "Berlim"
    },
    {
        "pergunta": "Qual destes rios famosos passa pela Alemanha?",
        "opcoes": ["Rio Elba", "Rio Danúbio", "Rio Rino", "Rio Weser"],
        "resposta": "Rio Rino"
    },
    {
        "pergunta": "Qual é a maior cidade da Alemanha em termos de população?",
        "opcoes": ["Hamburg", "Berlim", "Munique", "Frankfurt"],
        "resposta": "Berlim"
    },
    {
        "pergunta": "Com quantos países a Alemanha faz fronteira?",
        "opcoes": ["8", "11", "11", "10", "9"],
        "resposta": "9"
    },
    {
        "pergunta": "Qual é a moeda oficial utilizada na Alemanha?",
        "opcoes": ["Dolar", "Franco alemão", "Libra", "Euro"],
        "resposta": "Euro"
    },
    {
        "pergunta": "Em qual continente a Alemanha está localizada?",
        "opcoes": ["África", "Europa", "América", "Ásia"],
        "resposta": "Europa"
    },
    {
        "pergunta": "Qual é a famosa cadeia de montanhas localizada no sul da Alemanha?",
        "opcoes": ["Pirineus", "Andes", "Alpes", "Himalaias"],
        "resposta": "Alpes"
    },
    {
        "pergunta": "O  Pretzel é um tipo de pão muito popular na Alemanha. Qual é o seu formato característico?",
        "opcoes": ["Redondo como uma bola", "Comprido como uma baguete", "Em formato de nó ou laço", "Triangular como um croissant"],
        "resposta": "Em formato de nó ou laço"
    },
    {
        "pergunta": "Qual destas marcas de carro famosas NÃO é de origem alemã?",
        "opcoes": ["BMW", "Mercedes-Benz", "Volkswagen", "Toyota"],
        "resposta": "Toyota"
    },
    {
        "pergunta": "Qual é o nome do famoso compositor alemão conhecido por suas sinfonias e sonatas?",
        "opcoes": ["Johann Sebastian Bach", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Richard Wagner"],
        "resposta": "Ludwig van Beethoven"
    },
    {
        "pergunta": "Qual destes contos de fadas ficou famoso graças aos Irmãos Grimm, que eram alemães?",
        "opcoes": ["Aladdin", "Pinóquio", "O Mago de Oz", "Cinderela"],
        "resposta": "Cinderela"
    },
    {
        "pergunta": "Qual é o esporte mais popular e praticado na Alemanha?",
        "opcoes": ["Hockey", "Basquete", "Futebol", "Vôlei"],
        "resposta": "Futebol"
        },
    {
        "pergunta": "Qual é o nome do famoso festival de cerveja que acontece anualmente em Munique, Alemanha?",
        "opcoes": ["Festival da Cerveja de Berlim", "Carnaval de Munique", "Oktoberfest", "Festa da Cerveja de Frankfurt"],
        "resposta": "Oktoberfest"
    },
    {
        "pergunta": "Quais são as cores da bandeira da Alemanha, de cima para baixo?",
        "opcoes": ["Amarelo, Vermelho, Preto", "Vermelho, Amarelo, Preto", "Preto, Vermelho, Amarelo", "Preto, Amarelo, Vermelho"],
        "resposta": "Preto, Vermelho, Amarelo"
    },
    {
        "pergunta": "Qual famoso muro dividiu a capital alemã durante a Guerra Fria e foi derrubado em 1989?",
        "opcoes": ["Muro de Munique", "Muro de Hamburgo", "Muro de Berlim", "Muro de Frankfurt"],
        "resposta": "Muro de Berlim"
    },
    {
        "pergunta": "Quem foi o famoso físico alemão que desenvolveu a Teoria da Relatividade?",
        "opcoes": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Nikola Tesla"],
        "resposta": "Albert Einstein"
    },
    {
        "pergunta": "O castelo de Neuschwanstein, na Alemanha, serviu de inspiração para o castelo de qual personagem famosa da Disney?",
        "opcoes": ["Bela e a Fera", "Branca de Neve", "Ariel", "Cinderela"],
        "resposta": "Cinderela"
    },
    {
        "pergunta": "Qual é o nome do famoso filósofo alemão conhecido por suas obras sobre a existência e a angústia?",
        "opcoes": ["Immanuel Kant", "Friedrich Nietzsche", "Karl Marx", "Arthur Schopenhauer"],
        "resposta": "Friedrich Nietzsche"
    },
    {
        "pergunta": "Qual destas marcas de material esportivo foi fundada na Alemanha?",
        "opcoes": ["Under Armour", "Puma", "Nike", "Adidas"],
        "resposta": "Adidas"
    }



]

random.shuffle(perguntas)

for pergunta in perguntas:
    random.shuffle(pergunta["opcoes"])

pontuacao = 0
respostas_usuario = []

# Formulário
with st.form("quiz_form"):

    for i, pergunta in enumerate(perguntas):
        resposta = st.radio(
            f"{i+1}. {pergunta['pergunta']}",
            pergunta["opcoes"],
            index=None,
            key=i
        )

        respostas_usuario.append(resposta)

    enviar = st.form_submit_button("Finalizar Quiz")

# Resultado
if enviar:
    if None in respostas_usuario:
        st.warning("Responda todas as perguntas antes de finalizar.")

    else:

        for i, pergunta in enumerate(perguntas):
            if respostas_usuario[i] == pergunta["resposta"]:
                pontuacao += 1

        st.success(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")

        porcentagem = (pontuacao / len(perguntas)) * 100

        st.info(f"Pontuação final: {porcentagem:.0f}%")

        # Feedback
        if porcentagem == 100:
            st.balloons()
            st.write("Excelente desempenho!")
        elif porcentagem >= 70:
            st.write("Muito bom!")
        elif porcentagem >= 50:
            st.write("Bom trabalho!")
        else:
            st.write("Continue estudando!")

# Botão de reiniciar
if st.button("Refazer Quiz"):
    st.rerun()  