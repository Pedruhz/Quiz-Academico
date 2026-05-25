import copy
import random

import streamlit as st


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
        "pergunta": "Em que ano ocorreu a reunificacao oficial da Alemanha?",
        "opcoes": ["1989", "1990", "1991", "1993"],
        "resposta": "1990",
    },
    {
        "pergunta": "Qual cidade foi capital da Alemanha Ocidental antes da reunificacao?",
        "opcoes": ["Bonn", "Hamburgo", "Dresden", "Frankfurt"],
        "resposta": "Bonn",
    },
    {
        "pergunta": "Qual e o nome da camara baixa do parlamento alemao?",
        "opcoes": ["Bundestag", "Bundesrat", "Reichstag", "Landtag"],
        "resposta": "Bundestag",
    },
    {
        "pergunta": "Qual instituicao representa os estados federados no sistema politico alemao?",
        "opcoes": ["Bundesrat", "Bundestag", "Banco Central Europeu", "Tribunal de Berlim"],
        "resposta": "Bundesrat",
    },
    {
        "pergunta": "Quantos estados federados, chamados Bundeslander, formam a Alemanha?",
        "opcoes": ["12", "14", "16", "18"],
        "resposta": "16",
    },
    {
        "pergunta": "Qual estado alemao e conhecido por Munique e pela Oktoberfest?",
        "opcoes": ["Baviera", "Saxonia", "Hesse", "Sarre"],
        "resposta": "Baviera",
    },
    {
        "pergunta": "Qual rio forma parte importante da fronteira natural entre Alemanha e Franca?",
        "opcoes": ["Reno", "Elba", "Danubio", "Oder"],
        "resposta": "Reno",
    },
    {
        "pergunta": "Qual rio passa por cidades como Dresden e Hamburgo?",
        "opcoes": ["Elba", "Reno", "Main", "Isar"],
        "resposta": "Elba",
    },
    {
        "pergunta": "Qual cidade alema e um dos principais centros financeiros da Europa?",
        "opcoes": ["Frankfurt", "Leipzig", "Nuremberg", "Bremen"],
        "resposta": "Frankfurt",
    },
    {
        "pergunta": "Qual cidade alema e famosa por seu porto e por historica tradicao comercial?",
        "opcoes": ["Hamburgo", "Colonia", "Stuttgart", "Dortmund"],
        "resposta": "Hamburgo",
    },
    {
        "pergunta": "Qual tratado encerrou formalmente muitos pontos pendentes apos a Segunda Guerra e abriu caminho para a reunificacao alema?",
        "opcoes": ["Tratado Dois Mais Quatro", "Tratado de Versalhes", "Tratado de Maastricht", "Tratado de Roma"],
        "resposta": "Tratado Dois Mais Quatro",
    },
    {
        "pergunta": "Qual foi o nome dado ao periodo de forte crescimento economico da Alemanha Ocidental no pos-guerra?",
        "opcoes": ["Milagre economico", "Plano Quinquenal", "Nova Politica Economica", "Grande Salto"],
        "resposta": "Milagre economico",
    },
    {
        "pergunta": "Qual industria e uma das mais associadas a economia alema no mercado mundial?",
        "opcoes": ["Automobilistica", "Petrolifera", "Cinematografica", "Mineracao de ouro"],
        "resposta": "Automobilistica",
    },
    {
        "pergunta": "Qual empresa alema e conhecida mundialmente pela fabricacao de automoveis com sede em Wolfsburg?",
        "opcoes": ["Volkswagen", "Porsche", "Opel", "MAN"],
        "resposta": "Volkswagen",
    },
    {
        "pergunta": "Qual filosofo alemao escreveu a Critica da Razao Pura?",
        "opcoes": ["Immanuel Kant", "Karl Marx", "Friedrich Nietzsche", "Martin Heidegger"],
        "resposta": "Immanuel Kant",
    },
    {
        "pergunta": "Qual compositor alemao e associado a obras como a Nona Sinfonia?",
        "opcoes": ["Ludwig van Beethoven", "Johannes Brahms", "Richard Wagner", "Robert Schumann"],
        "resposta": "Ludwig van Beethoven",
    },
    {
        "pergunta": "Qual movimento religioso do seculo XVI teve forte ligacao com Martinho Lutero na Alemanha?",
        "opcoes": ["Reforma Protestante", "Contrarreforma", "Iluminismo", "Romantismo"],
        "resposta": "Reforma Protestante",
    },
    {
        "pergunta": "Em qual cidade Martinho Lutero publicou suas 95 teses, segundo a tradicao historica?",
        "opcoes": ["Wittenberg", "Munique", "Aachen", "Lubeck"],
        "resposta": "Wittenberg",
    },
    {
        "pergunta": "Qual antiga rota comercial do norte europeu incluiu importantes cidades alemas como Hamburgo e Lubeck?",
        "opcoes": ["Liga Hanseatica", "Rota da Seda", "Liga Delos", "Caminho de Santiago"],
        "resposta": "Liga Hanseatica",
    },
    {
        "pergunta": "Qual cidade alema foi dividida em setores apos a Segunda Guerra Mundial?",
        "opcoes": ["Berlim", "Colonia", "Dusseldorf", "Stuttgart"],
        "resposta": "Berlim",
    },
    {
        "pergunta": "Qual lado de Berlim era administrado por Estados Unidos, Reino Unido e Franca durante a Guerra Fria?",
        "opcoes": ["Berlim Ocidental", "Berlim Oriental", "Grande Berlim", "Berlim Norte"],
        "resposta": "Berlim Ocidental",
    },
    {
        "pergunta": "Qual era o nome oficial da Alemanha Oriental durante a Guerra Fria?",
        "opcoes": ["Republica Democratica Alema", "Republica Federal Alema", "Imperio Alemao", "Confederacao Germanica"],
        "resposta": "Republica Democratica Alema",
    },
    {
        "pergunta": "Qual era o nome oficial da Alemanha Ocidental durante a Guerra Fria?",
        "opcoes": ["Republica Federal da Alemanha", "Republica Democratica Alema", "Reino da Prussia", "Confederacao do Reno"],
        "resposta": "Republica Federal da Alemanha",
    },
    {
        "pergunta": "Qual cadeia montanhosa marca parte do sul da Alemanha e se estende por varios paises europeus?",
        "opcoes": ["Alpes", "Pirineus", "Carpatos", "Apeninos"],
        "resposta": "Alpes",
    },
    {
        "pergunta": "Qual floresta alema e famosa por suas paisagens densas e inspiracao para lendas e contos?",
        "opcoes": ["Floresta Negra", "Floresta Amazonica", "Floresta de Sherwood", "Taiga Siberiana"],
        "resposta": "Floresta Negra",
    },
    {
        "pergunta": "Qual cidade alema abriga a famosa catedral gotica proxima ao rio Reno?",
        "opcoes": ["Colonia", "Bremen", "Hannover", "Essen"],
        "resposta": "Colonia",
    },
    {
        "pergunta": "Qual area industrial historica da Alemanha ficou conhecida pela producao de carvao e aco?",
        "opcoes": ["Regiao do Ruhr", "Vale do Loire", "Planicie da Lombardia", "Delta do Danubio"],
        "resposta": "Regiao do Ruhr",
    },
    {
        "pergunta": "Qual sistema de transporte alemao e conhecido por trens de alta velocidade chamados ICE?",
        "opcoes": ["Deutsche Bahn", "Lufthansa", "Autobahn", "Bundesliga"],
        "resposta": "Deutsche Bahn",
    },
    {
        "pergunta": "Qual termo se refere as rodovias alemas conhecidas por trechos sem limite geral de velocidade?",
        "opcoes": ["Autobahn", "Bundestag", "S-Bahn", "U-Bahn"],
        "resposta": "Autobahn",
    },
    {
        "pergunta": "Qual campeonato nacional de futebol e o principal da Alemanha?",
        "opcoes": ["Bundesliga", "La Liga", "Serie A", "Premier League"],
        "resposta": "Bundesliga",
    },
]

QUIZ_VERSAO = 3


def criar_posicoes_respostas(total_perguntas, total_opcoes):
    contagem_posicoes = {
        posicao: total_perguntas // total_opcoes for posicao in range(total_opcoes)
    }

    for posicao in range(total_perguntas % total_opcoes):
        contagem_posicoes[posicao] += 1

    posicoes = []

    while len(posicoes) < total_perguntas:
        ultima_posicao = posicoes[-1] if posicoes else None
        candidatas = [
            posicao
            for posicao, quantidade in contagem_posicoes.items()
            if quantidade > 0 and posicao != ultima_posicao
        ]

        if not candidatas:
            candidatas = [
                posicao
                for posicao, quantidade in contagem_posicoes.items()
                if quantidade > 0
            ]

        maior_quantidade = max(contagem_posicoes[posicao] for posicao in candidatas)
        melhores_candidatas = [
            posicao
            for posicao in candidatas
            if contagem_posicoes[posicao] == maior_quantidade
        ]
        posicao_escolhida = random.choice(melhores_candidatas)

        posicoes.append(posicao_escolhida)
        contagem_posicoes[posicao_escolhida] -= 1

    return posicoes


def criar_quiz():
    perguntas = copy.deepcopy(PERGUNTAS)
    random.shuffle(perguntas)
    posicoes_respostas = criar_posicoes_respostas(
        total_perguntas=len(perguntas),
        total_opcoes=len(perguntas[0]["opcoes"]),
    )

    for i, pergunta in enumerate(perguntas):
        pergunta["id"] = i
        resposta = pergunta["resposta"]
        alternativas_erradas = [
            opcao for opcao in pergunta["opcoes"] if opcao != resposta
        ]
        random.shuffle(alternativas_erradas)

        posicao_resposta = posicoes_respostas[i]
        opcoes_embaralhadas = alternativas_erradas
        opcoes_embaralhadas.insert(posicao_resposta, resposta)
        pergunta["opcoes"] = opcoes_embaralhadas


    return perguntas


def limpar_respostas():
    for chave in list(st.session_state.keys()):
        if chave.startswith(("pergunta_", "resposta_")):
            del st.session_state[chave]


def reiniciar_quiz():
    limpar_respostas()
    st.session_state.quiz_tentativa += 1
    st.session_state.quiz_perguntas = criar_quiz()
    st.session_state.quiz_enviado = False


if "quiz_tentativa" not in st.session_state:
    st.session_state.quiz_tentativa = 0

if st.session_state.get("quiz_versao") != QUIZ_VERSAO:
    limpar_respostas()
    st.session_state.quiz_perguntas = criar_quiz()
    st.session_state.quiz_enviado = False
    st.session_state.quiz_versao = QUIZ_VERSAO
elif "quiz_perguntas" not in st.session_state:
    limpar_respostas()
    st.session_state.quiz_perguntas = criar_quiz()

if "quiz_enviado" not in st.session_state:
    st.session_state.quiz_enviado = False


perguntas = st.session_state.quiz_perguntas
respostas_usuario = []

with st.form("quiz_form"):
    for i, pergunta in enumerate(perguntas):
        resposta = st.radio(
            f"{i + 1}. {pergunta['pergunta']}",
            pergunta["opcoes"],
            index=None,
            key=f"resposta_{st.session_state.quiz_tentativa}_{pergunta['id']}",
        )
        respostas_usuario.append(resposta)

    enviar = st.form_submit_button("Finalizar Quiz")

if enviar:
    st.session_state.quiz_enviado = True

if st.session_state.quiz_enviado:
    faltando_resposta = any(resposta is None for resposta in respostas_usuario)

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
