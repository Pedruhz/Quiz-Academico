import copy
import random

import streamlit as st


OPCAO_PADRAO = "Selecione uma opcao..."


st.set_page_config(
    page_title="Quiz-Alemanha",
    page_icon="📚",
    layout="wide",
)

st.markdown(
    """
    <style>
    div[data-testid="stAppToolbar"],
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }

    footer,
    #MainMenu,
    header {
        visibility: hidden;
    }

    .stRadio label {
        font-size: 20px !important;
    }

    .stButton button,
    .stFormSubmitButton button {
        width: 100%;
        height: 50px;
        font-size: 18px;
    }

    h1 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📚 Quiz-Alemanha")
st.write("Teste seus conhecimentos!")

PERGUNTAS = [
    {
        "pergunta": "Qual e a capital da Alemanha?",
        "opcoes": ["Hamburg", "Berlim", "Munique", "Frankfurt"],
        "resposta": "Berlim",
    },
    {
        "pergunta": "Qual destes rios famosos passa pela Alemanha?",
        "opcoes": ["Rio Elba", "Rio Danubio", "Rio Reno", "Rio Weser"],
        "resposta": "Rio Reno",
    },
    {
        "pergunta": "Qual e a maior cidade da Alemanha em termos de populacao?",
        "opcoes": ["Hamburg", "Berlim", "Munique", "Frankfurt"],
        "resposta": "Berlim",
    },
    {
        "pergunta": "Com quantos paises a Alemanha faz fronteira?",
        "opcoes": ["8", "11", "10", "9"],
        "resposta": "9",
    },
    {
        "pergunta": "Qual e a moeda oficial utilizada na Alemanha?",
        "opcoes": ["Dolar", "Franco alemao", "Libra", "Euro"],
        "resposta": "Euro",
    },
    {
        "pergunta": "Em qual continente a Alemanha esta localizada?",
        "opcoes": ["Africa", "Europa", "America", "Asia"],
        "resposta": "Europa",
    },
    {
        "pergunta": "Qual e a famosa cadeia de montanhas localizada no sul da Alemanha?",
        "opcoes": ["Pirineus", "Andes", "Alpes", "Himalaias"],
        "resposta": "Alpes",
    },
    {
        "pergunta": "O Pretzel e um tipo de pao muito popular na Alemanha. Qual e o seu formato caracteristico?",
        "opcoes": [
            "Redondo como uma bola",
            "Comprido como uma baguete",
            "Em formato de no ou laco",
            "Triangular como um croissant",
        ],
        "resposta": "Em formato de no ou laco",
    },
    {
        "pergunta": "Qual destas marcas de carro famosas NAO e de origem alema?",
        "opcoes": ["BMW", "Mercedes-Benz", "Volkswagen", "Toyota"],
        "resposta": "Toyota",
    },
    {
        "pergunta": "Qual e o nome do famoso compositor alemao conhecido por suas sinfonias e sonatas?",
        "opcoes": [
            "Johann Sebastian Bach",
            "Ludwig van Beethoven",
            "Wolfgang Amadeus Mozart",
            "Richard Wagner",
        ],
        "resposta": "Ludwig van Beethoven",
    },
    {
        "pergunta": "Qual destes contos de fadas ficou famoso gracas aos Irmaos Grimm, que eram alemaes?",
        "opcoes": ["Aladdin", "Pinoquio", "O Mago de Oz", "Cinderela"],
        "resposta": "Cinderela",
    },
    {
        "pergunta": "Qual e o esporte mais popular e praticado na Alemanha?",
        "opcoes": ["Hockey", "Basquete", "Futebol", "Volei"],
        "resposta": "Futebol",
    },
    {
        "pergunta": "Qual e o nome do famoso festival de cerveja que acontece anualmente em Munique, Alemanha?",
        "opcoes": [
            "Festival da Cerveja de Berlim",
            "Carnaval de Munique",
            "Oktoberfest",
            "Festa da Cerveja de Frankfurt",
        ],
        "resposta": "Oktoberfest",
    },
    {
        "pergunta": "Quais sao as cores da bandeira da Alemanha, de cima para baixo?",
        "opcoes": [
            "Amarelo, Vermelho, Preto",
            "Vermelho, Amarelo, Preto",
            "Preto, Vermelho, Amarelo",
            "Preto, Amarelo, Vermelho",
        ],
        "resposta": "Preto, Vermelho, Amarelo",
    },
    {
        "pergunta": "Qual famoso muro dividiu a capital alema durante a Guerra Fria e foi derrubado em 1989?",
        "opcoes": ["Muro de Munique", "Muro de Hamburgo", "Muro de Berlim", "Muro de Frankfurt"],
        "resposta": "Muro de Berlim",
    },
    {
        "pergunta": "Quem foi o famoso fisico alemao que desenvolveu a Teoria da Relatividade?",
        "opcoes": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Nikola Tesla"],
        "resposta": "Albert Einstein",
    },
    {
        "pergunta": "O castelo de Neuschwanstein, na Alemanha, serviu de inspiracao para o castelo de qual personagem famosa da Disney?",
        "opcoes": ["Bela e a Fera", "Branca de Neve", "Ariel", "Cinderela"],
        "resposta": "Cinderela",
    },
    {
        "pergunta": "Qual e o nome do famoso filosofo alemao conhecido por suas obras sobre a existencia e a angustia?",
        "opcoes": ["Immanuel Kant", "Friedrich Nietzsche", "Karl Marx", "Arthur Schopenhauer"],
        "resposta": "Friedrich Nietzsche",
    },
    {
        "pergunta": "Qual destas marcas de material esportivo foi fundada na Alemanha?",
        "opcoes": ["Under Armour", "Puma", "Nike", "Adidas"],
        "resposta": "Adidas",
    },
]


def criar_quiz():
    perguntas = copy.deepcopy(PERGUNTAS)
    random.shuffle(perguntas)

    for pergunta in perguntas:
        random.shuffle(pergunta["opcoes"])

    return perguntas


def reiniciar_quiz():
    st.session_state.quiz_perguntas = criar_quiz()
    st.session_state.quiz_enviado = False

    for chave in list(st.session_state.keys()):
        if chave.startswith("pergunta_"):
            del st.session_state[chave]


if "quiz_perguntas" not in st.session_state:
    st.session_state.quiz_perguntas = criar_quiz()

if "quiz_enviado" not in st.session_state:
    st.session_state.quiz_enviado = False


perguntas = st.session_state.quiz_perguntas
respostas_usuario = []

with st.form("quiz_form"):
    for i, pergunta in enumerate(perguntas):
        resposta = st.radio(
            f"{i + 1}. {pergunta['pergunta']}",
            [OPCAO_PADRAO] + pergunta["opcoes"],
            key=f"pergunta_{i}",
        )
        respostas_usuario.append(resposta)

    enviar = st.form_submit_button("Finalizar Quiz")

if enviar:
    st.session_state.quiz_enviado = True

if st.session_state.quiz_enviado:
    faltando_resposta = any(resposta == OPCAO_PADRAO for resposta in respostas_usuario)

    if faltando_resposta:
        st.warning("Responda todas as perguntas antes de finalizar.")
    else:
        pontuacao = sum(
            resposta == pergunta["resposta"]
            for resposta, pergunta in zip(respostas_usuario, perguntas)
        )
        porcentagem = (pontuacao / len(perguntas)) * 100

        st.success(f"Voce acertou {pontuacao} de {len(perguntas)} perguntas!")
        st.info(f"Pontuacao final: {porcentagem:.0f}%")

        if porcentagem == 100:
            st.balloons()
            st.write("Excelente desempenho!")
        elif porcentagem >= 70:
            st.write("Muito bom!")
        elif porcentagem >= 50:
            st.write("Bom trabalho!")
        else:
            st.write("Continue estudando!")

        st.button("Refazer Quiz", on_click=reiniciar_quiz)
