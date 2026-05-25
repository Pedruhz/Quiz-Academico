# -*- coding: utf-8 -*-

import copy
import html
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
        "pergunta": "Em que ano ocorreu a reunificação oficial da Alemanha?",
        "opcoes": ["1989", "1990", "1991", "1993"],
        "resposta": "1990",
    },
    {
        "pergunta": "Qual cidade foi capital da Alemanha Ocidental antes da reunificação?",
        "opcoes": ["Bonn", "Hamburgo", "Dresden", "Frankfurt"],
        "resposta": "Bonn",
    },
    {
        "pergunta": "Qual é o nome da câmara baixa do parlamento alemão?",
        "opcoes": ["Bundestag", "Bundesrat", "Reichstag", "Landtag"],
        "resposta": "Bundestag",
    },
    {
        "pergunta": "Qual instituição representa os estados federados no sistema político alemão?",
        "opcoes": ["Bundesrat", "Bundestag", "Banco Central Europeu", "Tribunal de Berlim"],
        "resposta": "Bundesrat",
    },
    {
        "pergunta": "Quantos estados federados, chamados Bundesländer, formam a Alemanha?",
        "opcoes": ["12", "14", "16", "18"],
        "resposta": "16",
    },
    {
        "pergunta": "Qual estado alemão é conhecido por Munique e pela Oktoberfest?",
        "opcoes": ["Baviera", "Saxônia", "Hesse", "Sarre"],
        "resposta": "Baviera",
    },
    {
        "pergunta": "Qual rio forma parte importante da fronteira natural entre Alemanha e França?",
        "opcoes": ["Reno", "Elba", "Danúbio", "Oder"],
        "resposta": "Reno",
    },
    {
        "pergunta": "Qual rio passa por cidades como Dresden e Hamburgo?",
        "opcoes": ["Elba", "Reno", "Main", "Isar"],
        "resposta": "Elba",
    },
    {
        "pergunta": "Qual cidade alemã é um dos principais centros financeiros da Europa?",
        "opcoes": ["Frankfurt", "Leipzig", "Nuremberg", "Bremen"],
        "resposta": "Frankfurt",
    },
    {
        "pergunta": "Qual cidade alemã é famosa por seu porto e por histórica tradição comercial?",
        "opcoes": ["Hamburgo", "Colônia", "Stuttgart", "Dortmund"],
        "resposta": "Hamburgo",
    },
    {
        "pergunta": "Qual tratado encerrou formalmente muitos pontos pendentes após a Segunda Guerra e abriu caminho para a reunificação alemã?",
        "opcoes": ["Tratado Dois Mais Quatro", "Tratado de Versalhes", "Tratado de Maastricht", "Tratado de Roma"],
        "resposta": "Tratado Dois Mais Quatro",
    },
    {
        "pergunta": "Qual foi o nome dado ao período de forte crescimento econômico da Alemanha Ocidental no pós-guerra?",
        "opcoes": ["Milagre econômico", "Plano Quinquenal", "Nova Política Econômica", "Grande Salto"],
        "resposta": "Milagre econômico",
    },
    {
        "pergunta": "Qual indústria é uma das mais associadas à economia alemã no mercado mundial?",
        "opcoes": ["Automobilística", "Petrolífera", "Cinematográfica", "Mineração de ouro"],
        "resposta": "Automobilística",
    },
    {
        "pergunta": "Qual empresa alemã é conhecida mundialmente pela fabricação de automóveis com sede em Wolfsburg?",
        "opcoes": ["Volkswagen", "Porsche", "Opel", "MAN"],
        "resposta": "Volkswagen",
    },
    {
        "pergunta": "Qual filósofo alemão escreveu a Crítica da Razão Pura?",
        "opcoes": ["Immanuel Kant", "Karl Marx", "Friedrich Nietzsche", "Martin Heidegger"],
        "resposta": "Immanuel Kant",
    },
    {
        "pergunta": "Qual compositor alemão é associado a obras como a Nona Sinfonia?",
        "opcoes": ["Ludwig van Beethoven", "Johannes Brahms", "Richard Wagner", "Robert Schumann"],
        "resposta": "Ludwig van Beethoven",
    },
    {
        "pergunta": "Qual movimento religioso do século XVI teve forte ligação com Martinho Lutero na Alemanha?",
        "opcoes": ["Reforma Protestante", "Contrarreforma", "Iluminismo", "Romantismo"],
        "resposta": "Reforma Protestante",
    },
    {
        "pergunta": "Em qual cidade Martinho Lutero publicou suas 95 teses, segundo a tradição histórica?",
        "opcoes": ["Wittenberg", "Munique", "Aachen", "Lübeck"],
        "resposta": "Wittenberg",
    },
    {
        "pergunta": "Qual antiga rota comercial do norte europeu incluiu importantes cidades alemãs como Hamburgo e Lübeck?",
        "opcoes": ["Liga Hanseática", "Rota da Seda", "Liga Delos", "Caminho de Santiago"],
        "resposta": "Liga Hanseática",
    },
    {
        "pergunta": "Qual cidade alemã foi dividida em setores após a Segunda Guerra Mundial?",
        "opcoes": ["Berlim", "Colônia", "Düsseldorf", "Stuttgart"],
        "resposta": "Berlim",
    },
    {
        "pergunta": "Qual lado de Berlim era administrado por Estados Unidos, Reino Unido e França durante a Guerra Fria?",
        "opcoes": ["Berlim Ocidental", "Berlim Oriental", "Grande Berlim", "Berlim Norte"],
        "resposta": "Berlim Ocidental",
    },
    {
        "pergunta": "Qual era o nome oficial da Alemanha Oriental durante a Guerra Fria?",
        "opcoes": ["República Democrática Alemã", "República Federal Alemã", "Império Alemão", "Confederação Germânica"],
        "resposta": "República Democrática Alemã",
    },
    {
        "pergunta": "Qual era o nome oficial da Alemanha Ocidental durante a Guerra Fria?",
        "opcoes": ["República Federal da Alemanha", "República Democrática Alemã", "Reino da Prússia", "Confederação do Reno"],
        "resposta": "República Federal da Alemanha",
    },
    {
        "pergunta": "Qual cadeia montanhosa marca parte do sul da Alemanha e se estende por vários países europeus?",
        "opcoes": ["Alpes", "Pirineus", "Carpatos", "Apeninos"],
        "resposta": "Alpes",
    },
    {
        "pergunta": "Qual floresta alemã é famosa por suas paisagens densas e inspiração para lendas e contos?",
        "opcoes": ["Floresta Negra", "Floresta Amazônica", "Floresta de Sherwood", "Taiga Siberiana"],
        "resposta": "Floresta Negra",
    },
    {
        "pergunta": "Qual cidade alemã abriga a famosa catedral gótica próxima ao rio Reno?",
        "opcoes": ["Colônia", "Bremen", "Hannover", "Essen"],
        "resposta": "Colônia",
    },
    {
        "pergunta": "Qual área industrial histórica da Alemanha ficou conhecida pela produção de carvão e aço?",
        "opcoes": ["Região do Ruhr", "Vale do Loire", "Planície da Lombardia", "Delta do Danúbio"],
        "resposta": "Região do Ruhr",
    },
    {
        "pergunta": "Qual sistema de transporte alemão é conhecido por trens de alta velocidade chamados ICE?",
        "opcoes": ["Deutsche Bahn", "Lufthansa", "Autobahn", "Bundesliga"],
        "resposta": "Deutsche Bahn",
    },
    {
        "pergunta": "Qual termo se refere às rodovias alemãs conhecidas por trechos sem limite geral de velocidade?",
        "opcoes": ["Autobahn", "Bundestag", "S-Bahn", "U-Bahn"],
        "resposta": "Autobahn",
    },
    {
        "pergunta": "Qual campeonato nacional de futebol é o principal da Alemanha?",
        "opcoes": ["Bundesliga", "La Liga", "Serie A", "Premier League"],
        "resposta": "Bundesliga",
    },
]

DICAS_POR_RESPOSTA = {
    "1990": "Pense na sequência dos acontecimentos da Guerra Fria: primeiro veio a abertura da fronteira em Berlim, depois as negociações políticas e só então a unificação formal do país.",
    "Bonn": "A capital da Alemanha Ocidental não era uma das maiores cidades do país. Ela foi escolhida no pós-guerra como uma solução mais discreta e provisória, enquanto Berlim continuava dividida.",
    "Bundestag": "Na política alemã, procure pela instituição que funciona como a principal casa legislativa eleita pela população. É nela que deputados discutem leis e escolhem o chanceler.",
    "Bundesrat": "A Alemanha é uma federação. Então, além dos deputados eleitos nacionalmente, existe uma casa que permite aos governos dos estados participarem das decisões federais.",
    "16": "A Alemanha é dividida em estados federados, alguns grandes e famosos, outros bem pequenos, como cidades-estado. O número total fica entre 15 e 17.",
    "Baviera": "Associe a pergunta ao sul da Alemanha: montanhas, tradições regionais fortes, Munique, Oktoberfest e uma identidade cultural muito marcada dentro do país.",
    "Reno": "Esse rio é muito importante para transporte, comércio e fronteiras na Europa Ocidental. Ele passa por regiões industriais e também perto de cidades como Colônia.",
    "Elba": "Observe as cidades citadas: Dresden fica mais a leste, enquanto Hamburgo fica no norte e tem porto. O rio correto cria uma ligação entre essas duas áreas.",
    "Frankfurt": "Pense na cidade alemã ligada a bancos, Bolsa de Valores, Banco Central Europeu, feiras internacionais e um dos aeroportos mais movimentados do continente.",
    "Hamburgo": "A pista principal é o porto. Essa cidade do norte cresceu historicamente ligada ao comércio marítimo, à navegação e às rotas comerciais europeias.",
    "Tratado Dois Mais Quatro": "O acordo envolveu as duas Alemanhas e quatro potências vencedoras da Segunda Guerra Mundial. Ele resolveu questões externas que ainda impediam a reunificação completa.",
    "Milagre econômico": "Depois da Segunda Guerra, a Alemanha Ocidental passou por uma recuperação muito rápida, com crescimento industrial, aumento de consumo e reconstrução acelerada.",
    "Automobilística": "A Alemanha é muito associada à engenharia, exportações e marcas globais de carros. Pense no setor que inclui empresas como BMW, Mercedes-Benz, Audi, Porsche e Volkswagen.",
    "Volkswagen": "A sede dessa empresa fica em Wolfsburg, uma cidade fortemente ligada à produção de carros. O nome da marca também remete à ideia de carro popular.",
    "Immanuel Kant": "A obra citada pertence ao Iluminismo e discute os limites e possibilidades do conhecimento humano. O autor viveu em Königsberg e é central na filosofia moderna.",
    "Ludwig van Beethoven": "A Nona Sinfonia é famosa pelo trecho coral conhecido como Ode à Alegria. O compositor é um dos nomes mais lembrados da música clássica alemã.",
    "Reforma Protestante": "No século XVI, Martinho Lutero criticou práticas da Igreja Católica, especialmente a venda de indulgências, dando origem a um movimento religioso de grande impacto na Europa.",
    "Wittenberg": "A tradição histórica liga as 95 teses a uma cidade universitária da Saxônia. Ela virou um dos principais símbolos do início da Reforma.",
    "Liga Hanseática": "Durante a Idade Média, várias cidades do norte europeu se uniram para fortalecer o comércio. Hamburgo e Lübeck foram centros importantes dessa rede.",
    "Berlim": "Depois da Segunda Guerra, essa cidade ficou dividida em zonas controladas por potências diferentes. Mais tarde, tornou-se o maior símbolo da divisão entre capitalismo e socialismo na Europa.",
    "Berlim Ocidental": "Mesmo localizada dentro da Alemanha Oriental, essa parte da cidade era administrada por potências ocidentais e representava a presença capitalista durante a Guerra Fria.",
    "República Democrática Alemã": "Apesar do termo 'democrática' no nome, esse Estado era socialista, alinhado à União Soviética e localizado no lado oriental da divisão alemã.",
    "República Federal da Alemanha": "Esse nome estava ligado ao lado ocidental durante a Guerra Fria e continuou sendo o nome oficial do país após a reunificação.",
    "Alpes": "A pista está no sul da Alemanha. Essa cadeia montanhosa também passa por países vizinhos como Áustria, Suíça, Itália e França.",
    "Floresta Negra": "Essa região fica no sudoeste alemão, é conhecida por paisagens densas, vilarejos tradicionais, relógios cuco e forte presença em lendas e contos.",
    "Colônia": "A cidade fica às margens do Reno e possui uma catedral gótica muito alta e famosa, que sobreviveu como símbolo histórico e turístico.",
    "Região do Ruhr": "Procure pela área do oeste alemão marcada pela industrialização pesada. Ela foi muito importante na produção de carvão, aço e no crescimento econômico do país.",
    "Deutsche Bahn": "A pergunta fala de trens de alta velocidade. O nome correto é o da empresa nacional de ferrovias, responsável por muitos serviços ferroviários na Alemanha.",
    "Autobahn": "O termo se refere ao sistema de autoestradas. Ele ficou famoso internacionalmente porque alguns trechos não possuem limite geral fixo de velocidade.",
    "Bundesliga": "O campeonato nacional alemão usa um nome ligado à ideia de liga federal. É nele que clubes como Bayern de Munique e Borussia Dortmund competem.",
}

QUIZ_VERSAO = 7


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
        pergunta["dica"] = DICAS_POR_RESPOSTA[resposta]
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


def chave_resposta(pergunta):
    return f"resposta_{st.session_state.quiz_tentativa}_{pergunta['id']}"


def renderizar_resultado_quiz(perguntas, respostas_usuario):
    letras = ["A", "B", "C", "D"]
    blocos_questoes = []

    for indice, (pergunta, resposta_usuario) in enumerate(
        zip(perguntas, respostas_usuario), start=1
    ):
        acertou = resposta_usuario == pergunta["resposta"]
        cor_status = "#16a34a" if acertou else "#dc2626"
        fundo_status = "#f0fdf4" if acertou else "#fef2f2"
        alternativas = []

        for letra, opcao in zip(letras, pergunta["opcoes"]):
            foi_marcada = opcao == resposta_usuario

            if foi_marcada and acertou:
                estilo = "background:#dcfce7;border-color:#16a34a;color:#14532d;font-weight:600;"
            elif foi_marcada:
                estilo = "background:#fee2e2;border-color:#dc2626;color:#7f1d1d;font-weight:600;"
            else:
                estilo = "background:#f8fafc;border-color:#cbd5e1;color:#334155;"

            alternativas.append(
                f"""
            <div style="
                border: 1px solid;
                border-radius: 8px;
                padding: 10px 12px;
                margin: 6px 0;
                font-size: 17px;
                line-height: 1.35;
                {estilo}
            ">
                <strong>{letra})</strong> {html.escape(opcao)}
            </div>
            """
            )

        blocos_questoes.append(
            f"""
            <section style="
                border-left: 5px solid {cor_status};
                background: {fundo_status};
                padding: 14px 16px;
                margin: 14px 0;
                border-radius: 8px;
            ">
                <h3 style="
                    margin: 0 0 10px 0;
                    color: #111827;
                    font-size: 20px;
                    font-weight: 700;
                ">{indice}. {html.escape(pergunta["pergunta"])}</h3>
                {''.join(alternativas)}
            </section>
            """
        )

    st.markdown("".join(blocos_questoes), unsafe_allow_html=True)


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
respostas_usuario = [
    st.session_state.get(chave_resposta(pergunta)) for pergunta in perguntas
]
faltando_resposta = any(resposta is None for resposta in respostas_usuario)
mostrar_correcao = st.session_state.quiz_enviado and not faltando_resposta

if not mostrar_correcao:
    with st.form("quiz_form"):
        respostas_usuario = []

        for i, pergunta in enumerate(perguntas):
            resposta = st.radio(
                f"{i + 1}. {pergunta['pergunta']}",
                pergunta["opcoes"],
                index=None,
                key=chave_resposta(pergunta),
            )
            with st.expander("Ver dica"):
                st.write(pergunta["dica"])
            respostas_usuario.append(resposta)

        enviar = st.form_submit_button("Finalizar Quiz")

    if enviar:
        st.session_state.quiz_enviado = True
        faltando_resposta = any(resposta is None for resposta in respostas_usuario)

    if st.session_state.quiz_enviado and faltando_resposta:
        st.warning("Responda todas as perguntas antes de finalizar.")

else:
    pontuacao = sum(
        resposta == pergunta["resposta"]
        for resposta, pergunta in zip(respostas_usuario, perguntas)
    )
    porcentagem = (pontuacao / len(perguntas)) * 100

    st.success(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")
    st.info(f"Pontuação final: {porcentagem:.0f}%")

    if porcentagem == 100:
        st.balloons()
        st.write("Excelente desempenho!")
    elif porcentagem >= 70:
        st.write("Muito bom!")
    elif porcentagem >= 50:
        st.write("Bom trabalho!")
    else:
        st.write("Continue estudando!")

    renderizar_resultado_quiz(perguntas, respostas_usuario)

    st.button("Refazer Quiz", on_click=reiniciar_quiz)
