import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Ouvidoria - Instituto Social São Lucas", layout="centered")

# CSS para customização (Cores Institucionais)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #1565c0; color: white; }
    .stProgress > div > div > div > div { background-color: #1565c0; }
    </style>
    """, unsafe_allow_html=True)

# Título e Cabeçalho
st.image("https://via.placeholder.com/200x80?text=LOGO+SAO+LUCAS") # Substitua pela URL da logo real
st.title("Sistema de Ouvidoria")
st.subheader("Instituto Social São Lucas")

# Inicialização do estado do formulário (Passos)
if 'passo' not in st.session_state:
    st.session_state.passo = 1

# --- TELA 1: BOAS-VINDAS E LGPD ---
if st.session_state.passo == 1:
    st.info("No Instituto Social São Lucas, acreditamos que a humanização e a escuta ativa são pilares essenciais. Queremos ouvir a sua voz!")
    st.write("Nosso compromisso: Tempo médio para análise e resposta é de 4 dias úteis.")
    
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
    perfil = st.selectbox("Perfil de Relacionamento", ["Paciente, Familiar ou Acompanhante", "Colaborador", "Médico", "Fornecedor ou Outro"])
    identifica = st.radio("Deseja se identificar?", ["Quero fazer um relato anônimo", "Quero me identificar"])

    if identifica == "Quero me identificar":
        nome = st.text_input("Nome Completo")
        cpf = st.text_input("CPF ou Matrícula")
        email = st.text_input("E-mail")
        tel = st.text_input("Telefone / WhatsApp")
        retorno = st.checkbox("Deseja receber um retorno sobre sua manifestação?")
    else:
        st.warning("Relatos anônimos são tratados internamente, mas não permitem o envio de protocolo ou resposta direta.")

    if st.button("Próximo"):
        st.session_state.passo = 3
        st.rerun()

# --- TELA 3: CLASSIFICAÇÃO E RELATO ---
elif st.session_state.passo == 3:
    st.write("### Detalhes da Manifestação")
    
    unidade = st.selectbox("Unidade da Ocorrência", [
        "Aripuanã", "Campo Novo do Parecis - CAPS", "Campo Verde", "Guarantã do Norte", 
        "Juína", "Juscimeira", "Pedro de Toledo", "Pontes e Lacerda", 
        "São José do Rio Claro - Hospital", "São José do Rio Claro - PAM", 
        "São Lourenço da Serra", "Sumaré - Área Cura", "Sumaré - Macarenko", "Sumaré - Matão"
    ])
    
    tipo = st.selectbox("Tipo de Manifestação", ["Elogio", "Sugestão", "Solicitação", "Reclamação", "Denúncia"])
    
    assunto = st.selectbox("Assunto Principal", [
        "Atendimento Assistencial", "Tempo de Espera e Acesso", "Conduta Profissional e Ética", 
        "Infraestrutura e Hotelaria", "Apoio Diagnóstico e Terapêutico", "Administrativo e Burocrático"
    ])
    
    relato = st.text_area("Descrição do Relato", placeholder="Descreva o que aconteceu...")
    arquivo = st.file_uploader("Anexar Evidências (Opcional)", type=["jpg", "png", "pdf", "mp3"])

    if st.button("Enviar Manifestação"):
        if relato:
            # Simulação de Automação de Backend
            with st.spinner('Processando automações...'):
                progresso = st.progress(0)
                st.write("Salvando no Banco de Dados Local...")
                time.sleep(1)
                progresso.progress(40)
                
                st.write("Integrando com Jira Service Management...")
                time.sleep(1)
                progresso.progress(80)
                
                if tipo == "Denúncia":
                    st.write("⚠️ Alerta Crítico enviado à Diretoria.")
                    time.sleep(1)
                
                progresso.progress(100)
                st.session_state.passo = 4
                st.rerun()
        else:
            st.error("Por favor, descreva o seu relato antes de enviar.")

# --- TELA 4: SUCESSO ---
elif st.session_state.passo == 4:
    st.success("Manifestação Registrada com Sucesso!")
    st.write("Sua participação é fundamental para o Instituto Social São Lucas.")
    
    # Simulação da regra de protocolo (apenas se tiver e-mail)
    st.write("---")
    st.info("Status da Notificação:")
    st.write("- Registro gravado no servidor local (On-premise)")
    st.write("- Ticket aberto no Jira com SLA de 4 dias")
    
    if st.button("Voltar ao Início"):
        st.session_state.passo = 1
        st.rerun()
