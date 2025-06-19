import customtkinter as ctk

from tkinter import ttk
import requests
import json
import re

# Carregar o dicionário de estados e siglas a partir do arquivo JSON
with open("estados.json", "r", encoding="utf-8") as arquivo:
    estados_siglas = json.load(arquivo)

with open(r"dados_usuarios.json", "r", encoding="utf-8") as arquivo:
            arquivo_lido = json.load(arquivo)
            dados_nome= arquivo_lido["nome"]
            dados_nome = arquivo_lido["nome"]
            dados_idade = arquivo_lido["idade"]
            dados_senha = arquivo_lido["senha"]
            dados_livrosdigitais = arquivo_lido["livros_digitais"]
            dados_livrosfisicos = arquivo_lido["livros_fisicos"]
            dados_preferencia = arquivo_lido["preferencia"]
            dados_estudo = arquivo_lido["horas_estudo"]
            dados_entretenimento = arquivo_lido["horas_entretenimento"]
            dados_estado = arquivo_lido["estado"]
            dados_cidade = arquivo_lido["cidade"]


def mostrar_login():
    frame_topoinicial.pack_forget()
    tela_inicial.pack_forget()
    frame_aviso.pack_forget()
    frame_login.pack(fill="both",expand=True)

def conferir_logar():
    email = entrada_nome.get().strip()
    senha = entrada_senhalogin.get().strip()

    # Limpa aviso anterior
    label_avisologin.configure(text="", text_color="blue")

    # Verifica campos vazios
    if email == "" or senha == "":
        label_avisologin.configure(text="Preencha todos os campos.", text_color="red")
        return

    logar(email,senha)

def logar(email,senha):
    try:
        with open("dados_usuarios.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            dados_senha=dados["senha"]

        # Verifica se o email existe
        if email not in dados_senha:
            label_avisologin.configure(text="Email não cadastrado.", text_color="red")
            return

        # Verifica a senha
        if dados_senha[email] != senha:
            label_avisologin.configure(text="Senha incorreta.", text_color="red")
            return
        
        mostrar_menu(email)
        
        
    except FileNotFoundError:
        label_avisologin.configure(text="Arquivo de dados não encontrado.", text_color="red")
    except json.JSONDecodeError:
        label_avisologin.configure(text="Erro ao ler os dados.", text_color="red")
    

def voltar_inicial():
    frame_login.pack_forget()
    frame_cadastro.pack_forget()
    frame_topoinicial.pack(fill="x")
    tela_inicial.pack(fill="both",expand=True)


def mostrar_cadastro():
    frame_topoinicial.pack_forget()
    tela_inicial.pack_forget()
    frame_cadastro.pack(fill="both",expand=True)
    
def cadastrar_conta():
    
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    senha = entrada_senha.get()
    livros_fisicos = entrada_livrosfisicos.get()
    livros_digitais = entrada_livrosdigitais.get()
    horas_estudo = entrada_horas.get()
    horas_entretenimento = entrada_entretenimento.get()
    preferencia = combobox_preferencia.get()  
    estado = combobox_estado.get()
    cidade = combobox_cidade.get()
    

    entradas = [
        nome, idade, email, senha,
        livros_fisicos, livros_digitais,
        horas_estudo, horas_entretenimento
    ]
    #parar qualquer campo vazio na lista entradas,irá retornar o label aviso="Campos não preenchidos ainda"
    if any(campo == "" for campo in entradas):
        label_aviso.configure(text="Campos não preenchidos ainda.", text_color="red")
        #Return usado para parar a função
        return
    #Aqui terá a verificação de cada combobox em relação aos "valores iniciais"
    if preferencia == "Selecione sua preferência de leitura":
        label_aviso.configure(text="Selecione sua preferência de leitura.", text_color="red")
        return
    if estado == "Selecione o estado":
        label_aviso.configure(text="Selecione o estado.", text_color="red")
        return
    if cidade == "Primeiro selecione o estado" or not cidade:
        label_aviso.configure(text="Selecione a cidade.", text_color="red")
        return
    

    cadastro = Cadastro(nome, idade, email, senha,livros_fisicos, livros_digitais,horas_estudo, horas_entretenimento,preferencia, estado, cidade)


# Define a função principal de cadastro de conta

def mostrar_menu(email):
    frame_login.pack_forget()
    frame_menu.pack(fill="both",expand=True)




def obter_cidades(sigla_estado):
    try:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios"
        resposta = requests.get(url)
        dados = resposta.json()
        return [cidade["nome"] for cidade in dados]
    except:
        label_aviso.configure(text="Erro ao carregar cidades. Verifique sua conexão.",text_color="Red")


# Função chamada quando um estado é selecionado
def atualizar_cidades(event=None):
    sigla = estados_siglas.get(combobox_estado.get(), None)
    if sigla:
        combobox_cidade.set("Carregando...")
        janela.update()
        #dentro da variável cidade ficará armazada toda a lista de cidades procuradas com a API
        cidades = obter_cidades(sigla)
        #atualização dos comboboxcidade
        combobox_cidade.configure(values=cidades)
        #
        combobox_cidade.set("Selecione a cidade")

def validar_numeros(novo_texto):  # Adicione o parâmetro
    return novo_texto.isdigit() or novo_texto == ""

def validar_letras_espacos(novo_texto):  # Adicione o parâmetro
    return all(c.isalpha() or c.isspace() for c in novo_texto) or novo_texto == ""





def aviso_sistema():
    frame_cadastro.pack_forget()
    frame_aviso.pack(fill="both",expand=True)
  
    
    # Cria o frame_aviso se não existir
    
    

def sair_sistema():
    janela.destroy()  # Fecha a janela principal
    # Ou qualquer outra lógica de saída que você preferir



ctk.set_appearance_mode("light")  # ou "light"

janela = ctk.CTk()
janela.title("BookTrack")
janela.geometry("650x750+400+150")
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
    command=mostrar_login,          # Função que será executada ao clicar
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
label_login=ctk.CTkLabel(frame_login,text="Informe seus dados:",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_login.pack(pady=2)
label_avisologin=ctk.CTkLabel(frame_login,text=" ",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_avisologin.pack(pady=2)

#1-entrada email
label_nome = ctk.CTkLabel(frame_login, text="Digite seu email:",text_color="#000000",anchor="w",width=300)
label_nome.pack(pady=(2, 0))

entrada_nome = ctk.CTkEntry(frame_login,width=300)
entrada_nome.pack(pady=2)

#2-entrada senha
label_senhalogin = ctk.CTkLabel(frame_login,text="Digite sua senha:",text_color="#000000",anchor="w",width=300)
label_senhalogin.pack(pady=(2, 0))

entrada_senhalogin = ctk.CTkEntry(frame_login,width=300,show="*")
entrada_senhalogin.pack(pady=2)


#botão logar
botao_logar = ctk.CTkButton(frame_login, text="Logar",fg_color="blue",text_color="#ffffff",width=300,command=conferir_logar)
botao_logar.pack(pady=2)
#botão voltar
botao_voltarinicial=ctk.CTkButton(frame_login, text="Voltar",fg_color="blue",text_color="#ffffff",width=300,command=voltar_inicial)
botao_voltarinicial.pack()





#frame cadastro
frame_cadastro=ctk.CTkFrame(janela,fg_color="#ffffff")
label_cadastro=ctk.CTkLabel(frame_cadastro,text="Informe seus dados:",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_cadastro.pack(pady=2)


label_aviso=ctk.CTkLabel(frame_cadastro,text=" ",fg_color="#ffffff",text_color="blue",font=("Arial", 20))
label_aviso.pack(pady=2)

#entrada de dados
#widthe serve para aumentar o tamanho da caixa de entrada horizontalmente

#1-Entrada Nome
label_nome = ctk.CTkLabel(frame_cadastro, text="Nome Completo (apenas letras):",text_color="#000000",anchor="w",width=300)
label_nome.pack(pady=(2, 0))

entrada_nome = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_letras_espacos), "%P"))
entrada_nome.pack(pady=2)

label_idade = ctk.CTkLabel(frame_cadastro, text="Digite sua idade:",text_color="#000000",anchor="w",width=300)
label_idade.pack(pady=(2, 0))

entrada_idade = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_idade.pack(pady=2)


#2-Entrada Email
label_email = ctk.CTkLabel(frame_cadastro, text="Digite seu melhor email:",text_color="#000000",anchor="w",width=300)
label_email.pack(pady=(2, 0))
entrada_email = ctk.CTkEntry(frame_cadastro,width=300)
entrada_email.pack(pady=2)

# 3-Entrada Senha
label_senha = ctk.CTkLabel(frame_cadastro,text="Senha (mínimo 4 caracteres):",text_color="#000000",anchor="w",width=300)
label_senha.pack(pady=(2, 0))

entrada_senha = ctk.CTkEntry(frame_cadastro,width=300,show="*")
entrada_senha.pack(pady=2)

# 4. Campo Quantidade de Livros fisicos
label_livrosfisicos = ctk.CTkLabel(frame_cadastro,text="Quantidade de livros fisicos lidos (apenas números):",text_color="#000000",anchor="w",width=300)
label_livrosfisicos.pack(pady=(2, 0))
entrada_livrosfisicos = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_livrosfisicos.pack(pady=2)

# 5. Campo Quantidade de Livros digitais
label_livrosdigitais= ctk.CTkLabel(frame_cadastro,text="Quantidade de livros digitais lidos (apenas números):",text_color="#000000",anchor="w",width=300)
label_livrosdigitais.pack(pady=(2, 0))
entrada_livrosdigitais = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_livrosdigitais .pack(pady=2)


# 6. Campo Horas de Estudo
label_horas = ctk.CTkLabel(frame_cadastro,text="Horas semanais de leitura para estudo:",text_color="#000000",anchor="w",width=300)
label_horas.pack(pady=(2, 0))

entrada_horas = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_horas.pack(pady=2)

# 7. Campo Horas de Estudo
label_entretenimento = ctk.CTkLabel(frame_cadastro,text="Horas semanais de leitura por entretenimento(apenas números):",text_color="#000000",anchor="w",width=300)
label_entretenimento.pack(pady=(2, 0))

entrada_entretenimento = ctk.CTkEntry(frame_cadastro,width=300,validate="key",validatecommand=(janela.register(validar_numeros), "%P"))
entrada_entretenimento.pack(pady=2)

#8-Entrada preferência de leitura
combobox_preferencia = ttk.Combobox(frame_cadastro, values=["Digital(kindle)","Livro físico"], state="readonly", width=35)
#define o texto padrão do combobox
combobox_preferencia.set("Selecione sua preferência de leitura")
combobox_preferencia.pack(pady=2)
#9.Combox Estados

# Combobox de estados
# Combobox de Estado (readonly)=impossibilita o usuário de editar a combobox,tendo apenas aquelas opções 
combobox_estado = ttk.Combobox(frame_cadastro, values=list(estados_siglas.keys()), state="readonly", width=35)
#define o texto padrão do combobox
combobox_estado.set("Selecione o estado")
combobox_estado.pack(pady=2)
#Quando o usuário escolhe algum valor(comboxselected),a função atualizar cidades é chamada pra fazer a ligação com a API e assim poder pegar os valores das cidades
combobox_estado.bind("<<ComboboxSelected>>", atualizar_cidades)

#10- Combobox de Cidade (readonly, inicia vazio)
combobox_cidade = ttk.Combobox(frame_cadastro, values=[""], state="readonly", width=35)
combobox_cidade.set("Primeiro selecione o estado")
combobox_cidade.pack(pady=10)

# Botão de cadastro
botao_cadastrar = ctk.CTkButton(frame_cadastro, text="Cadastrar",fg_color="blue",text_color="#ffffff",width=300,command=cadastrar_conta)
botao_cadastrar.pack(pady=2)

#botão de voltar
botao_voltarinicial=ctk.CTkButton(frame_cadastro, text="Voltar",fg_color="blue",text_color="#ffffff",width=300,command=voltar_inicial)
botao_voltarinicial.pack()




## Frame aviso (criação básica sem pack)
frame_aviso=ctk.CTkFrame(janela,fg_color="#ffffff")
 # Label de aviso
label = ctk.CTkLabel(frame_aviso, text="Cadastro realizado com sucesso!", font=("Arial", 20), text_color="green")
label.pack(pady=(40, 20))

    # Botão para ir para login
botao_login = ctk.CTkButton(frame_aviso, text="Ir para Login", width=200, command=mostrar_login)
botao_login.pack(pady=(0, 10))

    # Botão para sair do sistema
botao_sair = ctk.CTkButton(frame_aviso, text="Sair do Sistema", width=200, fg_color="red", hover_color="#cc0000", command=sair_sistema)
botao_sair.pack()





class Cadastro:
    """
    Essa Classe tem o objetivo de cadastrar os usuários,recebendo os dados básicos para ser possível fazer a conta,conferir se os dados são permitidos
    e assim cadastrar a conta
    """
    def __init__(self,nome, idade, email, senha,livros_fisicos, livros_digitais,horas_estudo, horas_entretenimento,preferencia, estado, cidade):
        #RECEBE OS DADOS NECESSÁRIOS PARA CADASTRAR UMA CONTA
        self.nome=nome
        self.email =email
        self.estado=estado
        self.cidade=cidade
        self.qlivrofisico=livros_fisicos
        self.qlivrodigital=livros_digitais
        self.qpreferencia_leitura=preferencia
        self.horas_estudo=horas_estudo
        self.horas_entretenimento=horas_entretenimento
        self.senha=senha
        self.idade=idade
        print(self.email)

       
        #chama função conferir código
        self.conferir_senha()

    # precisa passar o self como parâmetro para conseguir pegar as informações  do init

    def conferir_senha(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE A SENHA É VÁLIDA OU NÃO
        
        if 4 <= len(self.senha) and len(self.senha) <= 20:
            
            self.email_valido()  
            # Chama o próximo passo do cadastro
        #return para a função que estava sendo rodada e deixa rodando apenas a função que rodará
            return
        else:
            label_aviso.configure(text="Tamanho da senha inválido",text_color="red")
            return

        

    def email_valido(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE O EMAIL É VÁLIDO OU NÃO
        dominios_validos = ['gmail.com', 'outlook.com', '...']  # Seus domínios

        
    
    # Verificação 1: Formato básico
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email.strip()):
            label_aviso.configure(text="Formato inválido", text_color="red")
            return False
    
    # Verificação 2: Domínio válido
        dominio = self.email.split('@')[1].lower()
        if dominio not in dominios_validos:
            label_aviso.configure(text="Domínio não aceito", text_color="red")
            return False

        self.conferir_email()
        return True  # Todas as validações passaram
           

        

        

    
    def conferir_email(self):
        #FUNÇÃO UTILIZADA PARA CONFERIR SE O EMAIL JÁ ESTÁ CADASTRADO OU NÃO
        
        with open(r"dados_usuarios.json", "r", encoding="utf-8") as arquivo:
            arquivo_lido = json.load(arquivo)
            dados_nome= arquivo_lido["nome"]
            dados_idade = arquivo_lido["idade"]
            dados_senha = arquivo_lido["senha"]
            dados_livrosdigitais = arquivo_lido["livros_digitais"]
            dados_livrosfisicos = arquivo_lido["livros_fisicos"]
            dados_preferencia = arquivo_lido["preferencia"]
            dados_estudo = arquivo_lido["horas_estudo"]
            dados_entretenimento = arquivo_lido["horas_entretenimento"]
            dados_estado = arquivo_lido["estado"]
            dados_cidade = arquivo_lido["cidade"]

            if self.email.strip() in dados_nome:#dessa forma verificará se o email está já cadastrado ou não
                label_aviso.configure(text="Email já cadastrado.",text_color="red")
                
                return
            
            else:
                self.salvar_dados()  # Continua o processo normalmente
    
    def salvar_dados(self):
        dados_nome[self.email] = self.nome
        dados_senha[self.email] = self.senha
        dados_livrosfisicos[self.email] = self.qlivrofisico
        dados_livrosdigitais[self.email] = self.qlivrodigital
        dados_preferencia[self.email] = self.qpreferencia_leitura
        dados_estudo[self.email] = self.horas_estudo
        dados_entretenimento[self.email] = self.horas_entretenimento
        dados_estado[self.email] = self.estado
        dados_cidade[self.email] = self.cidade

# Supondo que a idade esteja em self.idade (você não informou, mas seria assim)
# Se não tiver, pode ignorar essa linha ou ajustar conforme o seu código
        dados_idade[self.email] = self.idade

# Salvar tudo novamente no arquivo JSON, mantendo o formato
        with open(r"dados_usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump({"nome": dados_nome,"idade": dados_idade,"senha": dados_senha,"livros_digitais": dados_livrosdigitais,"livros_fisicos": dados_livrosfisicos,"preferencia": dados_preferencia,
                   "horas_estudo": dados_estudo,"horas_entretenimento": dados_entretenimento,
                   "estado": dados_estado,
                    "cidade": dados_cidade }, arquivo, indent=4, ensure_ascii=False)
        

        aviso_sistema()





#frame menu
frame_menu=ctk.CTkFrame(janela,fg_color="green") 


############################


janela.mainloop()