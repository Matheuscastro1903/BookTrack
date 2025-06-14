import customtkinter as ctk
import requests
import json

# Carregar o dicionário de estados e siglas a partir do arquivo JSON
with open("estados.json", "r", encoding="utf-8") as arquivo:
    estados_siglas = json.load(arquivo)

def mostra_login():
    frame_topoinicial.pack_forget()
    tela_inicial.pack_forget()
    frame_login.pack(fill="both",expand=True)
def mostrar_cadastro():
    frame_topoinicial.pack_forget()
    tela_inicial.pack_forget()
    frame_cadastro.pack(fill="both",expand=True)
    

def voltar_inicial():
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_topoinicial.pack(fill="x")
    tela_inicial.pack(fill="both",expand=True)



def validar_numeros(novo_texto):  # Adicione o parâmetro
    return novo_texto.isdigit() or novo_texto == ""

def validar_letras_espacos(novo_texto):  # Adicione o parâmetro
    return all(c.isalpha() or c.isspace() for c in novo_texto) or novo_texto == ""

def cadastrar_conta():
    #passar os valores chamando a classe cadastro para ser verificado
    pass

def voltar_menu():

    pass


def obter_cidades(sigla_estado):
    try:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios"
        resposta = requests.get(url)
        dados = resposta.json()
        return [cidade["nome"] for cidade in dados]
    except:
        return ["Erro ao carregar cidades"]


# Função chamada quando um estado é selecionado
def atualizar_cidades(event=None):
    sigla = estados_siglas.get(combobox_estado.get(), None)
    if sigla:
        combobox_cidade.set("Carregando...")
        janela.update()
        cidades = obter_cidades(sigla)
        combobox_cidade.configure(values=cidades)
        combobox_cidade.set("Selecione a cidade")



ctk.set_appearance_mode("light")  # ou "light"

janela = ctk.CTk()
janela.title("BookTrack")
janela.geometry("500x600+400+150")
janela.resizable(False, False)

################################################################
#frame topo tela inical
frame_topoinicial=ctk.CTkFrame(janela,fg_color="Blue",height=80)
label_topoinicial=ctk.CTkLabel(frame_topoinicial,text="BookTrack",fg_color="Blue",text_color="white",font=("Arial", 18))
label_topoinicial.pack(pady=30)
#pady=cria espaços na vertical
#padx=cria espaco na horizontal




frame_topoinicial.pack(fill="x")




#Frame tela inicial

tela_inicial=ctk.CTkFrame(janela,fg_color="#ffffff")

#criação de um botão usando o ctk

label_inical=ctk.CTkLabel(tela_inicial,text="Qual opção você deseja ?",text_color="blue",fg_color="#ffffff",font=("Arial", 18))
label_inical.pack(pady=30)
botao_login = ctk.CTkButton(
    tela_inicial,
    text="Login",            # Texto no botão
    command=mostra_login,          # Função que será executada ao clicar
    width=150,                     # Largura
    height=40,                     # Altura
    corner_radius=10,              # Arredondamento das bordas
    fg_color="blue",               # Cor de fundo do botão
    hover_color="darkblue",        # Cor ao passar o mouse
    text_color="white",            # Cor do texto
    font=("Arial", 14, "bold"),    # Fonte//bold=estilo da fonte tipo negrito
    cursor="hand2"                 # Cursor tipo mão
)
botao_login.pack(pady=20)

botao_cadastro = ctk.CTkButton(
    tela_inicial,
    text="Cadastro",            # Texto no botão
    command=mostrar_cadastro,          # Função que será executada ao clicar
    width=150,                     # Largura
    height=40,                     # Altura
    corner_radius=10,              # Arredondamento das bordas
    fg_color="blue",               # Cor de fundo do botão
    hover_color="darkblue",        # Cor ao passar o mouse
    text_color="white",            # Cor do texto
    font=("Arial", 14, "bold"),    # Fonte
    cursor="hand2"                 # Cursor tipo mão
)
botao_cadastro.pack(pady=20)


tela_inicial.pack(fill="both",expand=True)


################################################################
#frame rodape
frame_rodape=ctk.CTkFrame(janela,fg_color="#ffffff",height=30)
frame_rodape.pack(fill="x", side="bottom")#bottom=fundo-->"fenda do bikini"
label_rodape=ctk.CTkLabel(frame_rodape,text="Versão 1.0 • Suporte: matheus.castro2@ufrpe.com",fg_color="#ffffff",text_color="#5f6368",font=("Arial", 10))
label_rodape.pack(pady=5)








#frame login
frame_login=ctk.CTkFrame(janela,fg_color="#ffffff")

#frame cadastro
frame_cadastro=ctk.CTkFrame(janela,fg_color="#ffffff")
label_cadastro=ctk.CTkLabel(frame_cadastro,text="Informe seus dados:",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_cadastro.pack(pady=10)
label_aviso=ctk.CTkLabel(frame_cadastro,text=" ",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_aviso.pack(pady=10)

#entrada de dados
#widthe serve para aumentar o tamanho da caixa de entrada horizontalmente
#
label_nome = ctk.CTkLabel(frame_cadastro, text="Nome Completo (apenas letras):",text_color="#000000",anchor="w",width=300)
label_nome.pack(pady=(10, 0))

entrada_nome = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_letras_espacos), "%P"))
entrada_nome.pack(pady=5)

# 2. Campo Quantidade de Livros fisicos
label_livrosfisicos = ctk.CTkLabel(frame_cadastro,text="Quantidade de livros fisicos lidos (apenas números):",text_color="#000000",anchor="w",width=300)
label_livrosfisicos.pack(pady=(10, 0))
entrada_livrosfisicos = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_livrosfisicos.pack(pady=5)

# 3. Campo Quantidade de Livros digitais
label_livrosdigitais= ctk.CTkLabel(frame_cadastro,text="Quantidade de livros digitais lidos (apenas números):",text_color="#000000",anchor="w",width=300)
label_livrosdigitais.pack(pady=(10, 0))
entrada_livrosdigitais = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_livrosdigitais .pack(pady=5)


# 4. Campo Horas de Estudo
label_horas = ctk.CTkLabel(frame_cadastro,text="Horas semanais de leitura para estudo:",text_color="#000000",anchor="w",width=300)
label_horas.pack(pady=(10, 0))

entrada_horas = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_horas.pack(pady=5)

# 5. Campo Horas de Estudo
label_entretenimento = ctk.CTkLabel(frame_cadastro,text="Horas semanais de leitura por entretenimento(apenas números):",text_color="#000000",anchor="w",width=300)
label_entretenimento.pack(pady=(10, 0))

entrada_entretenimento = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_entretenimento.pack(pady=5)




# 6. Campo Senha
label_senha = ctk.CTkLabel(frame_cadastro,text="Senha (mínimo 4 caracteres):",text_color="#000000",anchor="w",width=300)
label_senha.pack(pady=(10, 0))

entrada_senha = ctk.CTkEntry(frame_cadastro,width=300,show="*")
entrada_senha.pack(pady=5)

#7.Combox Estados
# Combobox de estados
combobox_estado = ctk.CTkComboBox(frame_cadastro, values=list(estados_siglas.keys()))
combobox_estado.pack(pady=10)
combobox_estado.set("Selecione o estado")
combobox_estado.bind("<<ComboboxSelected>>", atualizar_cidades)

# Combobox de cidades (inicialmente vazia)
combobox_cidade = ctk.CTkComboBox(frame_cadastro, values=["Primeiro selecione o estado"])
combobox_cidade.pack(pady=10)
combobox_cidade.set("Cidade") 

# Botão de cadastro
botao_cadastrar = ctk.CTkButton(frame_cadastro, text="Cadastrar",fg_color="blue",width=300,command=cadastrar_conta)
botao_cadastrar.pack(pady=20)





class Cadastro:
    """
    Essa Classe tem o objetivo de cadastrar os usuários,recebendo os dados básicos para ser possível fazer a conta,conferir se os dados são permitidos
    e assim cadastrar a conta
    """
    def __init__(self,nome,email,estado,cidade,qlivrofisico,qlivrodigital,preferencia_leitura,horas_estudo,horas_entretenimento,senha):
        #RECEBE OS DADOS NECESSÁRIOS PARA CADASTRAR UMA CONTA
        self.nome=nome
        self.email =email
        self.estado=estado
        self.cidade=cidade
        self.qlivrofisico=qlivrofisico
        self.qlivrodigital=qlivrodigital
        self.qpreferencia_leitura=preferencia_leitura
        self.horas_estudo=horas_estudo
        self.horas_entretenimento=horas_entretenimento
        self.senha=senha

       
        #chama função conferir código
        self.conferir_senha()

    # precisa passar o self como parâmetro para conseguir pegar as informações  do init

    def conferir_senha(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE A SENHA É VÁLIDA OU NÃO
        tentativas = 3
        while tentativas > 0:
            if 4 <= len(self.senha) and len(self.senha) <= 20:
                #print("Senha aceita.")
                self.email_valido()  # Chama o próximo passo do cadastro
            #return para a função que estava sendo rodada e deixa rodando apenas a função que rodará
                return
            else:
                print("Número de caracteres inválido. Sua senha deve ter entre 4 e 20 caracteres.")
                self.senha = input("Digite sua senha novamente: ").strip()
                tentativas -= 1
                print(f"Tentativas restantes: {tentativas}")

        print("Número máximo de tentativas atingido. Tente novamente mais tarde.")

    def email_valido(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE O EMAIL É VÁLIDO OU NÃO
        dominios_validos = [
            'gmail.com', 'outlook.com', 'hotmail.com',
            'yahoo.com', 'icloud.com'
        ]

        tentativas_email = 3
        while tentativas_email != 0:
            # VERIFICA SE O FORMATO DO EMAIL ESTÁ ESCRITO CORRETAMENTE
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
                print("FORMATO DE EMAIL INVÁLIDO, UTILIZE UM DOMÍNIO VÁLIDO")
                self.email = input("Digite novamente seu email: ").strip()
                tentativas_email -= 1
                print(f"Tentativas restantes: {tentativas_email}")

                continue  # volta pro início do while para validar de novo,caso esteja correto,irá passar pelo verificador

            # VERIFICA APENAS O DOMÍNIO,SEPARA TODO O RESTO E PEGA APENAS A PARTE DO DOMÍNIO
            dominio = self.email.split('@')[1].lower()
            if dominio not in dominios_validos:
                print("Domínio não aceito. Use: Gmail, Outlook, Yahoo, iCloud, etc.")
                self.email = input("Digite novamente seu email: ").strip()
                tentativas_email -= 1
                print(f"Tentativas restantes: {tentativas_email}")

                # continuar o loop sem parar
                continue

        # Se chegou aqui, formato e domínio estão corretos
            break

        else:
            print("Limite de tentativas atingido. Encerrando o processo de cadastro.")
            return

        self.conferir_email()

    
    def conferir_email(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE O EMAIL JÁ ESTÁ CADASTRADO OU NÃO
        
        with open(r"banco_dados.JSON", "r", encoding="utf-8") as arquivo:
            arquivo_lido = json.load(arquivo)
            dados_conta = arquivo_lido["senha"]
            dados_familia = arquivo_lido["familia"]
            dados_quantidade = arquivo_lido["membros"]
            dados_pontos = arquivo_lido["pontos"]
            dados_apartamento = arquivo_lido["apartamento"]
            dados_codigov = arquivo_lido["verificador"]

            if self.email in dados_conta:
                print("EMAIL JÁ POSSUI UMA CONTA.")
                tentativas = 3
                while tentativas != 0:
                    resposta1 = input(
                    "Deseja tentar refazer a conta ou ir para tela de login caso já possua conta? (refazer/login) ").strip().lower()
                    if resposta1 in ["login", "tela de login", "logi"]:
                        login()
                        return
                    elif resposta1 in ["refazer", "retentar", "conta", "refazer conta"]:
                        self.email = input("Digite novamente seu email: ").strip()
                        self.conferir_email()
                        return
                    else:
                        print("Resposta inválida")
                        tentativas -= 1
                        print(f"Tentativas restantes {tentativas}")
                else:
                    print(
                    "Limite de tentativas atingido. Encerrando o processo de cadastro.")
                    return
            else:
                self.conferir_nome()  # Continua o processo normalmente
    def conferir_localidade():

        pass
    def conferir_nome():
        pass


#frame menu
frame_menu=ctk.CTkFrame(janela) 


############################


janela.mainloop()