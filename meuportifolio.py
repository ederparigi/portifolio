import streamlit as st
from PIL import Image

# Função principal
def main():
    st.set_page_config(page_title="Portfólio de Desenvolvedor", layout="wide")
    
    # Sidebar para navegação
    st.sidebar.title("Navegação")
    menu = st.sidebar.radio(
        "Escolha a Seção", 
        ("Início", "Currículo", "Portfólio", "Contatos")
    )
    
    # Exibição de conteúdo baseado na opção escolhida no menu
    if menu == "Início":
        exibir_inicio()
    elif menu == "Currículo":
        exibir_curriculo()
    elif menu == "Portfólio":
        exibir_portfolio()
    elif menu == "Contatos":
        exibir_contatos()

# Função para exibir a seção "Início"
def exibir_inicio():
    st.title("Bem-vindo ao Meu Portfólio")
    st.subheader("Mestre. Especialista em Engenharia Eletrica e Eletrônica")

    # Exibindo foto do desenvolvedor
    image = Image.open("foto_perfil.jpg")  # Coloque a imagem com o nome correto
    st.image(image, width=150, use_column_width=False)

    st.write("""
        Olá, eu sou um Engenheiro eletricista apaixonado por criar soluções inovadoras. 
        Tenho experiência com tecnologias modernas de desenvolvimento em Engenharia e estou sempre buscando novos desafios.
    """)

# Função para exibir a seção "Currículo"
def exibir_curriculo():
    st.title("Currículo Profissional")
    
    # Resumo das Qualificações
    st.header("Resumo das Qualificações")
    st.write("""
        - Desenvolvedor e executor de  Projetos de Planta Baixa de casas e barracões;
        - Desenvolvedor e executor de Projetos de Iluminação Pública;
        - Elaboração de projetos As-Built para Reurb;
        - Desenvolvedor e executor de Placas de Circuito Impresso;
        - Manutentor de equipamentos eletronicos inclusive contituidos componentes extremamente pequenos como SMD e TSOP.
        - Manutentor e executor de Projetos de Telecomunicações.
    """)
    
    # Experiência Profissional
    st.header("Experiência Profissional")
    st.write("""
        **Engenheiro Eletricista | Prefeitura Municipal de Ibitinga** (2023 - 2023)
        - Manutenção da parte elétrica dos prédios públicos.
                
        **Assessor Adjunto de Planejamento Urbanístico e Habitação | Prefeitura Municipal de Itápolis** (2021 - 2023)
        - Atualização da Planta IP de Vapor de Sódio para LED;
        - Elaboração e execução de projetos elétricos dos prédios públicos;
             
        **Auxiliar de Encarregado Operácional Jr. | Malosso Bioenergia S.A.** (20114 - 2015)
        - Auxiliar de manutenção da automação da planta fabril;
        - Auxiliar da manutenção das instalações elétrica fabril;
        
    """)
    
    # Educação
    st.header("Educação")
    st.write("""
        **Mestre em Engenharia Elétrica** | UNESP -Universidade Paulista Julio de Mesquita Filho (2017 - 2022)
        **Especialista em Engenharia Elétrica** | UNICAM - Universidade Candido Mendes (2017 - 2018)
        **Bacharel em Engenharia Elétrica** | UNIP - Universidade Paulista (2008 - 2013)
        **Técnico em Eletrônica** | LICEU - Liceu Noroeste Bauru (2006 - 2007)     
    """)
    
    # Habilidades Técnicas
    st.header("Habilidades Técnicas")
    st.write("""
        - Linguagens: Python;
        - Programas: Tango, AutoCad, Visual Studio Code, Proteus 7.0 e MathLab;
        """)
    
    # Projetos e Realizações
    st.header("Projetos e Realizações")
    st.write("""
        - **Projetos em Planta Baixa**: Diversos projetos desde elétrica residêncial até projétos de iluminação.
        - **Publicação de Artigo cientifico**: Inovação em desenvolvimento de diagnóstico para fuga de correntes parasitas voltadas a motores Brushless.
    """)
    
    # Idiomas
    st.header("Idiomas")
    st.write("""
        - Português (Nativo)
        - Inglês (Intermediário)
        - Espanhol (Básico)
    """)
    
    # Cursos e Treinamentos
    st.header("Cursos e Treinamentos")
    st.write("""
        - **Python** | SENAI (2024)
        - **AutoCad** | CONSTRUIR (2020)
    """)
    
    # Referências Profissionais
    st.header("Referências Profissionais")
    st.write("""
        **João ** - Gerente na Empresa XYZ | joao@empresa.com
        **Maria ** - Coordenadora na Empresa ABC | maria@empresa.com
    """)

# Função para exibir a seção "Portfólio"
def exibir_portfolio():
    st.title("Portfólio de Projetos")
    
    st.write("""
        Aqui estão alguns dos meus projetos de destaque:
    """)
    
    st.subheader("Projeto 1: As-Built: Adriana Biondo")
    st.write("""
        - **Descrição**: Projeto elétrico da planta existente para regularização de áres.
        - **Tecnologias**: .....
        - **Link**: [Repositório no GitHub](https://github.com/usuario/projeto1)
    """)
    
    st.subheader("Projeto 2: Padrão Agrupado para 3 relógios")
    st.write("""
        - **Descrição**: Padrão agrupado C3 em acrílico para 3 relógios B2  com barramento de distribuição.
        - **Tecnologias**: Normas .....
        - **Link**: [Repositório no GitHub](https://github.com/usuario/projeto2)
    """)
    
    # Aqui você pode adicionar mais projetos conforme necessário

# Função para exibir a seção "Contatos"
def exibir_contatos():
    st.title("Contatos")
    
    st.write("""
        - **E-mail**: [HOTMAIL](eder_parigi@hotmail.com)
        - **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/seuusuario)
        - **GitHub**: [GitHub](https://github.com/seuusuario)
        - **Site**: [seusite.com](https://www.seusite.com)
        - **Lattes**: (http://lattes.cnpq.br/4517887421494624)
    """)

# Executando o app
if __name__ == "__main__":
    main()
