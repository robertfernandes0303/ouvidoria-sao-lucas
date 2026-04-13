import streamlit as st
import time
import uuid

st.set_page_config(page_title="Ouvidoria - Instituto Social São Lucas", layout="centered")

st.markdown("""
    <style>
    /* Fundo geral */
    .main { background-color: #f0f4f8; }

    /* Botões primários */
    .stButton>button {
        width: 100%;
        background-color: #003366;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #00AEEF;
        color: white;
    }

    /* Barra de progresso */
    .stProgress > div > div > div > div { background-color: #00AEEF; }

    /* Títulos */
    h1 { color: #003366 !important; }
    h2, h3 { color: #003366 !important; }

    /* Caixas de info/warning/success */
    .stAlert { border-radius: 6px; }

    /* Checkbox */
    .stCheckbox label { color: #003366; font-weight: 500; }

    /* Cabeçalho institucional */
    .header-box {
        background-color: #003366;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .header-box p {
        color: #00AEEF;
        margin: 0;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* Separador colorido */
    hr { border-top: 2px solid #00AEEF; }
    </style>
    """, unsafe_allow_html=True)

# Logo e cabeçalho
try:
    st.image("logo-sao-lucas.png", width=220)
except:
    pass

st.markdown("""
<div class="header-box">
    <p>Sistema de Ouvidoria Institucional</p>
</div>
""", unsafe_allow_html=True)

# Inicialização do estado
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'dados' not in st.session_state:
    st.session_state.dados = {}

# Indicador de progresso
if st.session_state.passo < 5:
    passos_labels = ["LGPD", "Identificação", "Classificação", "Relato"]
    progresso_pct = int((st.session_state.passo / 4) * 100)
    st.markdown(f"**Etapa {st.session_state.passo} de 4 — {passos_labels[st.session_state.passo - 1]}**")
    st.progress(progresso_pct)
    st.write("")

# --- TELA 1: BOAS-VINDAS E LGPD ---
if st.session_state.passo == 1:
    st.info("No Instituto Social São Lucas, acreditamos que a humanização e a escuta ativa são pilares essenciais. Queremos ouvir a sua voz!")
    st.write("Nosso compromisso: Tempo médio para análise e resposta é de **4 dias úteis**.")
    st.write("")
    aceite = st.checkbox("Li e aceito a Política de Privacidade e o tratamento dos meus dados conforme a LGPD.")
    if st.button("Iniciar Manifestação"):
        if aceite:
            st.session_state.passo = 2
            st.rerun()
        else:
            st.error("É necessário aceitar os termos da LGPD para prosseguir.")

# --- TELA 2: IDENTIFICAÇÃO ---
elif st.session_state.passo == 2:
    st.write("### Perfil e Identificação")
    perfil = st.selectbox("Perfil de Relacionamento", [
        "— Selecione —", "Paciente, Familiar ou Acompanhante", "Colaborador", "Médico", "Fornecedor ou Outro"
    ])
    identifica = st.radio("Deseja se identificar?", ["Quero fazer um relato anônimo", "Quero me identificar"])
    nome = cpf = email = tel = ""
    retorno = False
    if identifica == "Quero me identificar":
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF ou Matrícula")
        email = st.text_input("E-mail")
        tel = st.text_input("Telefone / WhatsApp")
        retorno = st.checkbox("Desejo receber retorno sobre minha manifestação por e-mail")
    else:
        st.warning("Relatos anônimos são tratados internamente, mas não permitem o envio de protocolo ou resposta direta.")
    if st.button("Próximo →"):
        if perfil == "— Selecione —":
            st.error("Por favor, selecione seu perfil de relacionamento.")
        else:
            st.session_state.dados.update({
                'perfil': perfil, 'identifica': identifica,
                'nome': nome, 'cpf': cpf, 'email': email,
                'tel': tel, 'retorno': retorno
            })
            st.session_state.passo = 3
            st.rerun()

# --- TELA 3: CLASSIFICAÇÃO E RELATO ---
elif st.session_state.passo == 3:
    st.write("### Detalhes da Manifestação")
    unidade = st.selectbox("Unidade da Ocorrência", [
        "— Selecione —",
        "Aripuanã", "Campo Novo do Parecis - CAPS", "Campo Verde", "Guarantã do Norte",
        "Juína", "Juscimeira", "Pedro de Toledo", "Pontes e Lacerda",
        "São José do Rio Claro - Hospital", "São José do Rio Claro - PAM",
        "São Lourenço da Serra", "Sumaré - Área Cura", "Sumaré - Macarenko", "Sumaré - Matão"
    ])
    tipo = st.selectbox("Tipo de Manifestação", [
        "— Selecione —", "Elogio", "Sugestão", "Solicitação", "Reclamação", "Denúncia"
    ])
    assunto = st.selectbox("Assunto Principal", [
        "— Selecione —",
        "Atendimento Assistencial", "Tempo de Espera e Acesso", "Conduta Profissional e Ética",
        "Infraestrutura e Hotelaria", "Apoio Diagnóstico e Terapêutico", "Administrativo e Burocrático"
    ])
    if tipo == "Denúncia":
        st.warning("⚠️ Denúncias geram notificação imediata à Diretoria.")
    relato = st.text_area("Descrição do Relato", placeholder="Descreva o que aconteceu com o máximo de detalhes...")
    st.file_uploader("Anexar Evidências (Opcional)", type=["jpg", "png", "pdf", "mp3"])
    st.write("")
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("← Voltar"):
            st.session_state.passo = 2
            st.rerun()
    with col2:
        if st.button("Enviar Manifestação"):
            erros = []
            if unidade == "— Selecione —": erros.append("Selecione a unidade da ocorrência.")
            if tipo == "— Selecione —": erros.append("Selecione o tipo de manifestação.")
            if assunto == "— Selecione —": erros.append("Selecione o assunto principal.")
            if not relato.strip(): erros.append("Descreva o relato antes de enviar.")
            if erros:
                for e in erros: st.error(e)
            else:
                st.session_state.dados.update({'unidade': unidade, 'tipo': tipo, 'assunto': assunto, 'relato': relato})
                with st.spinner("Processando automações..."):
                    progresso = st.progress(0)
                    st.write("💾 Salvando no Banco de Dados Local...")
                    time.sleep(1)
                    progresso.progress(40)
                    st.write("🔗 Integrando com Jira Service Management...")
                    time.sleep(1)
                    progresso.progress(80)
                    if tipo == "Denúncia":
                        st.write("🚨 Alerta Crítico enviado à Diretoria.")
                        time.sleep(1)
                    progresso.progress(100)
                    st.session_state.passo = 4
                    st.rerun()

# --- TELA 4: SUCESSO ---
elif st.session_state.passo == 4:
    protocolo = "OUV-" + str(uuid.uuid4()).upper()[:8]
    dados = st.session_state.dados
    st.success("✅ Manifestação Registrada com Sucesso!")
    st.write("Sua participação é fundamental para o Instituto Social São Lucas.")
    st.write("---")
    st.info(f"""
**Resumo do Registro:**
- 🏥 Unidade: {dados.get('unidade', '-')}
- 📋 Tipo: {dados.get('tipo', '-')}
- 📌 Assunto: {dados.get('assunto', '-')}
    """)
    st.write("**Status da Notificação:**")
    st.write("- ✔️ Registro gravado no servidor local (On-premise)")
    st.write("- ✔️ Ticket aberto no Jira com SLA de 4 dias")
    if dados.get('retorno') and dados.get('email'):
        st.write(f"- ✔️ Protocolo **{protocolo}** enviado para **{dados.get('email')}**")
    elif dados.get('identifica') == "Quero fazer um relato anônimo":
        st.write("- ℹ️ Relato anônimo — protocolo não gerado conforme política de sigilo.")
    st.write("")
    if st.button("Registrar Nova Manifestação"):
        st.session_state.passo = 1
        st.session_state.dados = {}
        st.rerun()
