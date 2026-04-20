import streamlit as st
import time
import uuid
from datetime import datetime

st.set_page_config(
    page_title="Ouvidoria — Instituto Social São Lucas",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── MOBILE FIRST ── */
@media (max-width: 768px) {
  .main .block-container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 1rem !important;
  }
  .header-strip {
    padding: 0.9rem 1rem !important;
    border-radius: 10px !important;
  }
  .header-strip h2 { font-size: 1rem !important; }
  .step-title { font-size: 1.1rem !important; }
  .protocol-box h2 { font-size: 1.2rem !important; }
  .resumo-item { flex-direction: column; gap: 2px; }
  .resumo-value { text-align: left !important; }
  [data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
    min-width: 100% !important;
  }
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Fundo geral */
.stApp {
    background-color: #EEF6FB;
}
.main .block-container {
    background-color: #EEF6FB;
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 680px;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

/* Card container */
.card {
    background: #ffffff;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 2px 12px rgba(0, 174, 239, 0.08);
    border: 1px solid #D6EDF8;
    margin-bottom: 1.5rem;
}

/* Cabeçalho */
.header-strip {
    background: linear-gradient(135deg, #00AEEF 0%, #0090cc 100%);
    border-radius: 14px;
    padding: 1.2rem 1.8rem;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.header-strip p {
    color: #EEF6FB;
    margin: 0;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.header-strip h2 {
    color: #ffffff !important;
    margin: 0 !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
}

/* Etapa / step badge */
.step-badge {
    display: inline-block;
    background: #00AEEF;
    color: #EEF6FB;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 0.4rem;
}
.step-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #00AEEF;
    margin-bottom: 0.2rem;
}
.step-sub {
    font-size: 0.85rem;
    color: #7ab8d4;
    margin-bottom: 1.5rem;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #00AEEF, #0090cc);
    border-radius: 4px;
}
.stProgress > div > div {
    background-color: #D6EDF8;
    border-radius: 4px;
    height: 6px !important;
}

/* Labels */
label, .stSelectbox label, .stTextInput label,
.stTextArea label, .stFileUploader label {
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #005f8a !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 2px !important;
}

/* Inputs */
.stTextInput input, .stTextArea textarea {
    border: 1.5px solid #C4E3F5 !important;
    border-radius: 8px !important;
    background: #F7FCFF !important;
    color: #1a3a4a !important;
    font-size: 0.95rem !important;
    padding: 10px 14px !important;
    transition: border-color 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #00AEEF !important;
    box-shadow: 0 0 0 3px rgba(0,174,239,0.12) !important;
}

/* Select */
.stSelectbox > div > div {
    border: 1.5px solid #C4E3F5 !important;
    border-radius: 8px !important;
    background: #F7FCFF !important;
    color: #1a3a4a !important;
    font-size: 0.95rem !important;
}
.stSelectbox > div > div:focus-within {
    border-color: #00AEEF !important;
    box-shadow: 0 0 0 3px rgba(0,174,239,0.12) !important;
}

/* Radio */
.stRadio > label,
div[data-testid="stRadio"] > label {
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    color: #005f8a !important;
    -webkit-text-fill-color: #005f8a !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.stRadio > div {
    gap: 8px;
}
.stRadio > div > label,
div[data-testid="stRadio"] div[role="radiogroup"] label {
    background: #F7FCFF !important;
    border: 1.5px solid #C4E3F5 !important;
    border-radius: 8px !important;
    padding: 10px 16px !important;
    cursor: pointer !important;
    transition: all 0.15s !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: #2e2e2e !important;
    -webkit-text-fill-color: #2e2e2e !important;
    text-transform: none !important;
    letter-spacing: normal !important;
}
.stRadio > div > label:hover,
div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
    border-color: #00AEEF !important;
    background: #EEF6FB !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label p,
div[data-testid="stRadio"] div[role="radiogroup"] label span,
.stRadio > div > label p,
.stRadio > div > label span {
    color: #2e2e2e !important;
    -webkit-text-fill-color: #2e2e2e !important;
    font-weight: 600 !important;
}

/* Checkbox — texto */
.stCheckbox label, .stCheckbox span, .stCheckbox p,
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] span,
div[data-testid="stCheckbox"] p {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: #2e2e2e !important;
    text-transform: none !important;
    letter-spacing: normal !important;
    -webkit-text-fill-color: #2e2e2e !important;
    opacity: 1 !important;
}
/* Checkbox — caixa com contorno azul visível */
div[data-testid="stCheckbox"] > label > div:first-child {
    border: 2px solid #00AEEF !important;
    border-radius: 4px !important;
    background-color: #F7FCFF !important;
    min-width: 20px !important;
    min-height: 20px !important;
}
div[data-testid="stCheckbox"] > label > div:first-child svg {
    color: #00AEEF !important;
    fill: #00AEEF !important;
}

/* Buttons */
.stButton > button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.stButton > button[kind="primary"],
.stButton > button:not([kind]) {
    background: #00AEEF !important;
    color: #EEF6FB !important;
    border: none !important;
    box-shadow: 0 2px 8px rgba(0,174,239,0.25) !important;
}
.stButton > button:hover {
    background: #0090cc !important;
    box-shadow: 0 4px 14px rgba(0,174,239,0.35) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* Botão Voltar */
div[data-testid="column"]:first-child .stButton > button {
    background: #EEF6FB !important;
    color: #00AEEF !important;
    border: 1.5px solid #00AEEF !important;
    box-shadow: none !important;
}
div[data-testid="column"]:first-child .stButton > button:hover {
    background: #D6EDF8 !important;
    transform: translateY(-1px) !important;
}

/* Alert boxes */
.stAlert {
    border-radius: 10px !important;
    border-left-width: 4px !important;
}

/* File uploader */
.stFileUploader {
    border: 1.5px dashed #C4E3F5 !important;
    border-radius: 10px !important;
    background: #F7FCFF !important;
    padding: 0.5rem !important;
}

/* Divider */
hr {
    border: none;
    border-top: 2px solid #D6EDF8;
    margin: 1.5rem 0;
}

/* Success box */
.success-card {
    background: linear-gradient(135deg, #00AEEF 0%, #0090cc 100%);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    color: #EEF6FB;
    margin-bottom: 1.5rem;
}
.success-card h1 {
    color: #ffffff !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    margin: 0.5rem 0 0.3rem !important;
}
.success-card p {
    color: rgba(238,246,251,0.85);
    font-size: 0.9rem;
    margin: 0;
}
.protocol-box {
    background: #EEF6FB;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    margin: 1.5rem 0 0.5rem;
    text-align: center;
}
.protocol-box p {
    font-size: 0.75rem;
    font-weight: 700;
    color: #005f8a;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 4px;
}
.protocol-box h2 {
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #00AEEF !important;
    font-family: 'Courier New', monospace !important;
    margin: 0 !important;
    letter-spacing: 0.05em;
}
.resumo-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #D6EDF8;
    font-size: 0.9rem;
}
.resumo-label {
    color: #7ab8d4;
    font-weight: 600;
}
.resumo-value {
    color: #1a3a4a;
    font-weight: 600;
    text-align: right;
}
.status-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    background: #F7FCFF;
    border-radius: 8px;
    margin-bottom: 8px;
    font-size: 0.88rem;
    color: #1a3a4a;
    font-weight: 500;
}
.dot-ok {
    width: 8px; height: 8px;
    background: #008B8B;
    border-radius: 50%;
    flex-shrink: 0;
}
</style>
""", unsafe_allow_html=True)

# Inicialização
if 'passo' not in st.session_state:
    st.session_state.passo = 1
if 'dados' not in st.session_state:
    st.session_state.dados = {}
if 'protocolo' not in st.session_state:
    st.session_state.protocolo = ""

# ── CABEÇALHO ──────────────────────────────────────────────────────────────────
try:
    st.image("logo-sao-lucas.png", width=180)
except:
    pass

st.markdown("""
<div class="header-strip">
  <div>
    <p>Canal Oficial</p>
    <h2>Sistema de Ouvidoria</h2>
  </div>
</div>
""", unsafe_allow_html=True)

# ── BARRA DE PROGRESSO DISCRETA ───────────────────────────────────────────────
if st.session_state.passo <= 4:
    pct = int(((st.session_state.passo - 1) / 3) * 100)
    st.progress(pct)
    st.markdown("<div style='margin-bottom:1.5rem;'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA 1 — BOAS-VINDAS E LGPD
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.passo == 1:
    st.markdown("""
    <div class="step-badge">Etapa 1 de 4</div>
    <div class="step-title">Bem-vindo à Ouvidoria</div>
    <div style="font-size:0.85rem;color:#3a3a3a;margin-bottom:1.2rem;font-weight:500;">
        Seu canal direto de escuta ativa com o Instituto Social São Lucas
    </div>
    <div style="background:#F7FCFF;border:1.5px solid #C4E3F5;border-radius:10px;
         padding:1.1rem 1.3rem;margin-bottom:1.2rem;font-size:0.92rem;
         color:#2e2e2e;line-height:1.75;font-weight:400;">
        No Instituto Social São Lucas, acreditamos que a humanização e a escuta ativa 
        são pilares essenciais para oferecer uma saúde pública com afeto, respeito e 
        excelência. Este é o seu canal de comunicação direto, seguro e confidencial. 
        Queremos ouvir a sua voz! Você pode utilizar este espaço para registrar 
        <strong style="color:#00AEEF;">Elogios, Sugestões, Solicitações, Reclamações ou Denúncias</strong> 
        referentes aos nossos serviços e unidades.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#F7FCFF;border:1.5px solid #C4E3F5;border-radius:10px;
         padding:1rem 1.2rem;margin:1rem 0 1.2rem;">
      <div style="font-size:0.78rem;font-weight:700;color:#005f8a;text-transform:uppercase;
           letter-spacing:0.08em;margin-bottom:6px;">🔒 Aviso de Privacidade — LGPD</div>
      <div style="font-size:0.88rem;color:#1a3a4a;line-height:1.6;">
        As informações fornecidas serão utilizadas exclusivamente para análise e resposta 
        da sua manifestação, em conformidade com a <strong>Lei nº 13.709/2018 (LGPD)</strong>.
        Você pode optar pelo anonimato na próxima etapa.
      </div>
    </div>
    <div style="background:#EEF6FB;border-radius:8px;padding:0.75rem 1rem;
         display:flex;gap:12px;align-items:center;margin-bottom:1.2rem;">
      <div style="font-size:1.3rem;">⏱️</div>
      <div style="font-size:0.88rem;color:#1a3a4a;">
        <strong>Prazo de resposta:</strong> até <strong style="color:#00AEEF;">4 dias úteis</strong> 
        após o registro da manifestação.
      </div>
    </div>
    """, unsafe_allow_html=True)

    aceite = st.checkbox("Li e concordo com a Política de Privacidade e o tratamento dos meus dados conforme a LGPD.")
    st.write("")
    if st.button("Iniciar Manifestação →", use_container_width=True):
        if aceite:
            st.session_state.passo = 2
            st.rerun()
        else:
            st.error("É necessário aceitar os termos da LGPD para prosseguir.")

# ══════════════════════════════════════════════════════════════════════════════
# TELA 2 — IDENTIFICAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.passo == 2:
    st.markdown("""
    <div class="step-badge">Etapa 2 de 4</div>
    <div class="step-title">Identificação</div>
    <div class="step-sub">Você pode se identificar ou manter seu anonimato</div>
    """, unsafe_allow_html=True)

    perfil = st.selectbox("Perfil de Relacionamento", [
        "— Selecione —",
        "Paciente",
        "Acompanhante",
        "Prestador",
        "Colaborador",
        "Fornecedor",
        "Outro"
    ])

    st.write("")
    identifica = st.radio("Como deseja prosseguir?", [
        "Quero fazer um relato anônimo",
        "Quero me identificar"
    ])

    nome = cpf = email = tel = ""
    retorno = False

    if identifica == "Quero me identificar":
        st.markdown("<div style='margin-top:0.8rem;'></div>", unsafe_allow_html=True)
        nome = st.text_input("Nome Completo", placeholder="Seu nome completo")
        cpf = st.text_input("CPF ou Matrícula", placeholder="000.000.000-00")
        email = st.text_input("E-mail", placeholder="seu@email.com")
        tel = st.text_input("Telefone / WhatsApp", placeholder="(00) 00000-0000")
        st.write("")
        retorno = st.checkbox("✉️  Desejo receber retorno sobre minha manifestação por e-mail")
    else:
        st.markdown("""
        <div style="background:#FFF8E1;border:1.5px solid #FFD54F;border-radius:10px;
             padding:0.9rem 1.1rem;margin-top:0.8rem;">
          <div style="font-size:0.88rem;color:#6d4c00;line-height:1.6;">
            <strong>ℹ️ Relato anônimo:</strong> Sua identidade será totalmente preservada. 
            Não será possível enviar protocolo ou resposta direta ao registrante.
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    if st.button("Próximo →", use_container_width=True):
        if perfil == "— Selecione —":
            st.error("Selecione seu perfil de relacionamento para continuar.")
        elif identifica == "Quero me identificar" and not nome.strip():
            st.error("Informe seu nome completo para prosseguir identificado.")
        else:
            st.session_state.dados.update({
                'perfil': perfil, 'identifica': identifica,
                'nome': nome, 'cpf': cpf, 'email': email,
                'tel': tel, 'retorno': retorno
            })
            st.session_state.passo = 3
            st.rerun()
    if st.button("← Voltar", use_container_width=True, type="secondary"):
        st.session_state.passo = 1
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA 3 — DETALHES DA MANIFESTAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.passo == 3:
    st.markdown("""
    <div class="step-badge">Etapa 3 de 4</div>
    <div class="step-title">Detalhes da Manifestação</div>
    <div class="step-sub">Preencha todos os campos para garantir o melhor encaminhamento</div>
    """, unsafe_allow_html=True)

    unidade = st.selectbox("Unidade da Ocorrência", [
        "— Selecione —",
        "Aripuanã", "Campo Novo do Parecis - CAPS", "Campo Verde", "Guarantã do Norte",
        "Juína", "Juscimeira", "Matriz", "Pedro de Toledo", "Pontes e Lacerda",
        "São José do Rio Claro - Hospital", "São José do Rio Claro - PAM",
        "São Lourenço da Serra", "Sumaré - Área Cura", "Sumaré - Macarenko", "Sumaré - Matão"
    ])
    tipo = st.selectbox("Tipo de Manifestação", [
        "— Selecione —", "Elogio", "Sugestão", "Reclamação", "Denúncia"
    ])

    assunto = st.selectbox("Assunto Principal", [
        "— Selecione —",
        "Atendimento",
        "Tempo de Espera",
        "Conduta Profissional",
        "Exames",
        "Estrutura Predial",
        "Limpeza",
        "Outros"
    ])

    if tipo == "Denúncia":
        st.markdown("""
        <div style="background:#FFEBEE;border:1.5px solid #EF9A9A;border-radius:10px;
             padding:0.9rem 1.1rem;margin:0.5rem 0;">
          <div style="font-size:0.88rem;color:#b71c1c;line-height:1.6;">
            <strong>🚨 Atenção:</strong> Denúncias são tratadas com <strong>prioridade máxima</strong> 
            e geram notificação imediata à Diretoria Executiva.
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    relato = st.text_area(
        "Descrição Detalhada",
        placeholder="Descreva com clareza o que aconteceu. Inclua data, horário, local e pessoas envolvidas sempre que possível...",
        height=160
    )
    char_count = len(relato)
    cor_count = "#00AEEF" if char_count >= 30 else "#7ab8d4"
    st.markdown(f"<div style='font-size:0.75rem;color:{cor_count};text-align:right;margin-top:-10px;'>{char_count} caracteres</div>", unsafe_allow_html=True)

    st.write("")


    st.write("")
    if st.button("Enviar Manifestação ✓", use_container_width=True):
        erros = []
        if unidade == "— Selecione —": erros.append("Selecione a unidade da ocorrência.")
        if tipo == "— Selecione —": erros.append("Selecione o tipo de manifestação.")
        if assunto == "— Selecione —": erros.append("Selecione o assunto principal.")
        if not relato.strip() or len(relato.strip()) < 30:
            erros.append("Descreva o relato com pelo menos 30 caracteres.")
        if erros:
            for e in erros:
                st.error(e)
        else:
            st.session_state.dados.update({
                'unidade': unidade, 'tipo': tipo,
                'assunto': assunto, 'relato': relato
            })
            st.session_state.protocolo = (
                "OUV-" +
                datetime.now().strftime("%Y%m%d") +
                "-" + str(uuid.uuid4()).upper()[:6]
            )
            with st.spinner("Processando sua manifestação..."):
                bar = st.progress(0)
                st.caption("💾 Salvando no banco de dados local...")
                time.sleep(0.8); bar.progress(33)
                st.caption("🔗 Integrando com o Jira Service Management...")
                time.sleep(0.8); bar.progress(66)
                if tipo == "Denúncia":
                    st.caption("🚨 Enviando alerta crítico à Diretoria...")
                    time.sleep(0.6)
                bar.progress(100)
                time.sleep(0.4)
            st.session_state.passo = 4
            st.rerun()
    if st.button("← Voltar", use_container_width=True, type="secondary"):
        st.session_state.passo = 2
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA 4 — CONFIRMAÇÃO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.passo == 4:
    dados = st.session_state.dados
    protocolo = st.session_state.protocolo
    tem_email = dados.get('retorno') and dados.get('email')
    anonimo = dados.get('identifica') == "Quero fazer um relato anônimo"

    st.markdown("""
    <div style="text-align:center;padding:2rem 1rem 1.5rem;">
      <div style="font-size:3rem;margin-bottom:0.5rem;">✅</div>
      <div style="font-size:1.5rem;font-weight:700;color:#00AEEF;">Manifestação Registrada!</div>
      <div style="font-size:0.9rem;color:#7ab8d4;margin-top:4px;">
        Obrigado por contribuir com a melhoria dos nossos serviços.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Ticket e protocolo
    if not anonimo and tem_email:
        st.markdown(f"""
        <div class="protocol-box">
          <p>Número do Protocolo / Ticket</p>
          <h2>{protocolo}</h2>
          <div style="font-size:0.78rem;color:#7ab8d4;margin-top:6px;">
            Enviado para <strong>{dados.get('email')}</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)
    elif not anonimo:
        st.markdown(f"""
        <div class="protocol-box">
          <p>Número do Ticket</p>
          <h2>{protocolo}</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("**Relato anônimo registrado.** Seu sigilo está garantido. O protocolo não foi gerado conforme a política de anonimato.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<div style='font-size:0.78rem;font-weight:700;color:#005f8a;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:10px;'>Resumo do Registro</div>", unsafe_allow_html=True)
    for label, key in [("Perfil", "perfil"), ("Unidade", "unidade"), ("Tipo", "tipo"), ("Assunto", "assunto")]:
        st.markdown(f"""
        <div class="resumo-item">
          <span class="resumo-label">{label}</span>
          <span class="resumo-value">{dados.get(key, '—')}</span>
        </div>
        """, unsafe_allow_html=True)

    # Status simplificado — só alerta crítico se denúncia
    if dados.get('tipo') == "Denúncia":
        st.markdown("<div style='margin-top:1.2rem;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="status-item" style="background:#FFEBEE;border:1px solid #EF9A9A;">
          <div class="dot-ok" style="background:#c62828;"></div>
          <span style="color:#b71c1c;font-weight:600;">Alerta crítico enviado à Diretoria Executiva</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.5rem;font-size:0.8rem;color:#7ab8d4;text-align:center;'>Prazo de análise e resposta: até <strong style='color:#00AEEF;'>4 dias úteis</strong></div>", unsafe_allow_html=True)
    st.write("")
    if st.button("Registrar Nova Manifestação", use_container_width=True):
        st.session_state.passo = 1
        st.session_state.dados = {}
        st.session_state.protocolo = ""
        st.rerun()

# Rodapé
st.markdown("""
<div style="text-align:center;margin-top:2rem;font-size:0.75rem;color:#7ab8d4;">
  Instituto Social São Lucas · Ouvidoria Institucional · 
  <span style="color:#00AEEF;font-weight:600;">ouvidoria@saolucas.org.br</span>
</div>
""", unsafe_allow_html=True)
