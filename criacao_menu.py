### Aluno: Rodrigo da Conceição Barboza
### Disciplina: Raciocínio Computacional (11100010563_20242_01)
from multiprocessing.connection import default_family


### Funcoes
def mostrar_menu_principal():
    print("Bem-vindo ao menu!")
    print("1- Professores.")
    print("2- Turma")
    print("3- Matricula")
    print("4- Disciplina")
    print("5- Estudante")
    print("0- Sair")
    return input("Favor, escolha uma das opções acima:")


def mostrar_menu_secundario():
    print(f"Menu {opcao_1[int(opcao) - 1]}")

    print("1- Inserir")
    print("2- Excluir")
    print("3- Listar")
    print("4- Atualizar")
    print("0- Retornar")
    return input("Favor, escolha uma das opções acima:")


def cadastrar_estudantes(estudantes):
    codigo = int(input("Digite o código, por favor: "))
    nome = input("Digite o nome, por favor: ")
    cpf = input("Digite o CPF, por favor: ")

    dados_estudantes = {
        "Nome do estudante": nome,
        "Código do estudante": codigo,
        "CPF do estudante": cpf,
    }
    estudantes.append(dados_estudantes)
    print("Estudante cadastrado")
    input("Pressione ENTER para continuar")


def cadastrar_professor(professor):
    codigo = int(input("Digite o código, por favor: "))
    nome = input("Digite o nome, por favor: ")
    cpf = input("Digite o CPF, por favor: ")

    dados_professor = {
        "Nome do professor": nome,
        "Código do professor": codigo,
        "CPF do professor": cpf,
    }
    professor.append(dados_professor)
    print("Professor cadastrado")
    input("Pressione ENTER para continuar")


def mostrar_estudantes_cadastrados():
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        for dados in estudantes:
            print(dados)

    input("Pressione ENTER para continuar")


def mostrar_professores_cadastrados():
    if not professor:
        print("Não há professor cadastrados.")
    else:
        for dados in professor:
            print(dados)

    input("Pressione ENTER para continuar")


def excluir_estudantes():
    cod_p_excluir = int(input("Insira o código a ser excluído: "))
    estudante_excluir = None
    for encontrar_estudante in estudantes:
        if encontrar_estudante["Código do estudante"] == cod_p_excluir:
            estudante_excluir = encontrar_estudante
            break
    if estudante_excluir is None:
        print("Código do estudante não encontrado.")
    else:
        estudantes.remove(estudante_excluir)
    print("Estudante excluído.")
    input("Pressione ENTER para continuar")


def excluir_professor():
    cod_p_excluir = int(input("Insira o código a ser excluído: "))
    prof_excluir = None
    for encontrar_prof in professor:
        if encontrar_prof["Código do estudante"] == cod_p_excluir:
            prof_excluir = encontrar_prof
            break
    if prof_excluir is None:
        print("Código do professor não encontrado.")
    else:
        professor.remove(prof_excluir)
    print("Professor excluído.")
    input("Pressione ENTER para continuar")


def editar_informacoes_estudantes():
    cod_p_atualizar = int(input("Insira o código do estudante para atualizar: "))
    estudante_atualizar = None
    for encontrar_estudante in estudantes:
        if encontrar_estudante["Código do estudante"] == cod_p_atualizar:
            estudante_atualizar = encontrar_estudante
            break

    if estudante_atualizar:
        estudante_atualizar["Código do estudante"] = int(input("Por favor, digite o novo código: "))
        estudante_atualizar["Nome do estudante"] = input("Por favor, digite o novo nome: ")
        estudante_atualizar["CPF do estudante"] = input("Por favor, digite o novo CPF: ")
        print("Os dados do estudante foram atualizados")
    else:
        print("Código do estudante não encontrado.")

    input("Pressione ENTER para continuar")


def editar_informacoes_professor():
    cod_p_atualizar = int(input("Insira o código do estudante para atualizar: "))
    prof_atualizar = None
    for encontrar_prof in professor:
        if encontrar_prof["Código do professor"] == cod_p_atualizar:
            prof_atualizar = encontrar_prof
            break

    if prof_atualizar:
        prof_atualizar["Código do professor"] = int(input("Por favor, digite o novo código: "))
        prof_atualizar["Nome do professor"] = input("Por favor, digite o novo nome: ")
        prof_atualizar["CPF do professor"] = input("Por favor, digite o novo CPF: ")
        print("Os dados do professor foram atualizados")
    else:
        print("Código do professor não encontrado.")

    input("Pressione ENTER para continuar")


def cadastrar_disciplina(disciplina):
    codigo = int(input("Digite o código, por favor: "))
    nome = input("Digite o nome, por favor: ")

    dados_disciplina = {
        "Nome da disciplina": nome,
        "Código da disciplina": codigo,

    }
    disciplina.append(dados_disciplina)
    print("Disciplina cadastrada")
    input("Pressione ENTER para continuar")


def mostrar_disciplina():
    if not disciplina:
        print("Não há disciplina cadastrada.")
    else:
        for dados in disciplina:
            print(dados)

    input("Pressione ENTER para continuar")


def excluir_disciplina():
    cod_p_excluir = int(input("Insira o código a ser excluído: "))
    disciplina_excluir = None
    for encontrar_disciplina in disciplina:
        if encontrar_disciplina["Código do estudante"] == cod_p_excluir:
            estudante_excluir = encontrar_disciplina
            break
    if disciplina_excluir is None:
        print("Código da disciplina não encontrada.")
    else:
        disciplina.remove(disciplina_excluir)
    print("Disciplina excluída.")
    input("Pressione ENTER para continuar")


def editar_disciplina():
    cod_p_atualizar = int(input("Insira o código da disciplina: "))
    disciplina_atualizar = None
    for encontrar_estudante in estudantes:
        if encontrar_estudante["Código do estudante"] == cod_p_atualizar:
            disciplina_atualizar = encontrar_estudante
            break

    if disciplina_atualizar:
        disciplina_atualizar["Código da disciplina"] = int(input("Por favor, digite o novo código: "))
        disciplina_atualizar["Nome da disciplina"] = input("Por favor, digite o novo nome: ")
        print("A disciplina foi atualizada")
    else:
        print("Disciplina não encontrada.")

    input("Pressione ENTER para continuar")


def cadastrar_turma(turma):
    codigo_da_turma = int(input("Digite o código da turma, por favor: "))
    codigo_professor = input("Digite o código do professor, por favor:")
    nome = input("Digite o nome, por favor: ")

    dados_turma = {
        "Nome da turma": nome,
        "Código da turma": codigo_da_turma,
        "Código do professor": codigo_professor

    }
    turma.append(dados_turma)
    print("Turma cadastrada")
    input("Pressione ENTER para continuar")


def mostrar_turma_cadastrados():
    if not turma:
        print("Não há turma cadastrada.")
    else:
        for dados in turma:
            print(dados)

    input("Pressione ENTER para continuar")


def excluir_turma():
    cod_p_excluir = int(input("Insira o código a ser excluído: "))
    turma_excluir = None
    for encontrar_turma in turma:
        if encontrar_turma["Código do estudante"] == cod_p_excluir:
            estudante_excluir = encontrar_turma
            break
    if turma_excluir is None:
        print("Código da turma não encontrado.")
    else:
        turma.remove(turma_excluir)
    print("Turma excluída.")
    input("Pressione ENTER para continuar")


def editar_informacoes_turma():
    cod_p_atualizar = int(input("Insira o código do estudante para atualizar: "))
    turma_atualizar = None
    for encontrar_turma in estudantes:
        if encontrar_turma["Código do estudante"] == cod_p_atualizar:
            turma_atualizar = encontrar_turma
            break

    if turma_atualizar:
        turma_atualizar["Código da turma"] = int(input("Por favor, digite o novo código da turma: "))
        turma_atualizar["Nome da turma"] = input("Por favor, digite o novo nome: ")
        turma_atualizar["Código do professor"] = input("Por favor, digite o novo código do professor: ")
        print("Os dados da turma foram atualizados")
    else:
        print("Código da turma não encontrado.")

    input("Pressione ENTER para continuar")


def cadastrar_matricula():
    codigo_da_turma = int(input("Digite o código da turma, por favor: "))
    codigo_estudante = int(("Digite o código do professor, por favor:"))
    nome = input("Digite o nome, por favor: ")

    dados_matricula = {
        "Código da turma": codigo_da_turma,
        "Código do professor": codigo_estudante
    }
    turma.append(dados_matricula)
    print("Matricula cadastrada")
    input("Pressione ENTER para continuar")


def mostrar_matricula_cadastrados():
    if not matricula:
        print("Não há matricula cadastrada.")
    else:
        for dados in matricula:
            print(dados)

    input("Pressione ENTER para continuar")


def excluir_matricula():
    cod_p_excluir = int(input("Insira o código a ser excluído: "))
    matricula_excluir = None
    for encontrar_matricula in matricula:
        if encontrar_matricula["Código do estudante"] == cod_p_excluir:
            matricula_excluir = encontrar_matricula
            break
    if matricula_excluir is None:
        print("Código da matricula não encontrado.")
    else:
        estudantes.remove(matricula_excluir)
    print("Matricula excluída.")
    input("Pressione ENTER para continuar")


def editar_informacoes_matricula():
    cod_p_atualizar = int(input("Insira o código do estudante para atualizar: "))
    matricula_atualizar = None
    for encontrar_matricula in matricula:
        if encontrar_matricula["Código do estudante"] == cod_p_atualizar:
            matricula_atualizar = encontrar_matricula
            break

    if matricula_atualizar:
        matricula_atualizar["Código da turma"] = int(input("Por favor, digite o novo código da turma: "))
        matricula_atualizar["Nome da turma"] = input("Por favor, digite o novo nome: ")
        matricula_atualizar["Código do professor"] = input("Por favor, digite o novo código do professor: ")
        print("Os dados da turma foram atualizados")
    else:
        print("Código da turma não encontrado.")

    input("Pressione ENTER para continuar")


### Listas
opcao_1 = ['Professores', 'Turma', 'Matricula', 'Disciplina', 'Estudante']
opcao_2 = ['Inserir', 'Excluir', 'Listar', 'Atualizar']
estudantes = []
professor = []
disciplina = []
turma = []
matricula = []

while True:
    ### mostrar menu principal
    opcao = mostrar_menu_principal()

    if opcao == "5":
        while True:
            opcao2 = mostrar_menu_secundario()

            ### Menu aluno
            if opcao2 == "1":
                cadastrar_estudantes(estudantes)
            ### Mostrar lista de alunos
            elif opcao2 == "3":
                mostrar_estudantes_cadastrados()
            elif opcao2 == "2":
                excluir_estudantes()
            elif opcao2 == "4":
                editar_informacoes_estudantes()

    elif opcao == "1":
        while True:
            opcao2 = mostrar_menu_secundario()
            ### Menu professor
            if opcao2 == "1":
               cadastrar_professor(professor)
            elif opcao2 == "3":
                 mostrar_professores_cadastrados()
            elif opcao2 == "2":
                 excluir_professor()
            elif opcao2 == "4":
                 editar_informacoes_professor()

    elif opcao == "2":
        while True:
            opcao2 = mostrar_menu_secundario()
            ### Menu turma
            if opcao2 == "1":
               cadastrar_turma(turma)
            elif opcao2 == "3":
                 mostrar_turma_cadastrados()
            elif opcao2 == "2":
                 excluir_turma()
            elif opcao2 == "4":
                 editar_informacoes_turma()


    elif opcao == "3":
        while True:
            opcao2 = mostrar_menu_secundario()
            ### Menu turma
            if opcao2 == "1":
               cadastrar_matricula(matricula)
            elif opcao2 == "3":
                 mostrar_matricula_cadastrados()
            elif opcao2 == "2":
                 excluir_matricula()
            elif opcao2 == "4":
                 editar_informacoes_matricula()

    elif opcao == "4":
        while True:
            opcao2 = mostrar_menu_secundario()
            ### Menu turma
            if opcao2 == "1":
               cadastrar_disciplina(disciplina)
            elif opcao2 == "3":
                 mostrar_disciplina()
            elif opcao2 == "2":
                 excluir_disciplina()
            elif opcao2 == "4":
                 editar_disciplina()

            ### Tratar opção de retornar ao menu principal
            elif opcao2 == "0":
                break

        ### Tratar opção inválida no menu secundário
            else:
                print("Digite uma opção válida, por favor")

### Tratar opção de sair do menu principal
    elif opcao == "0":
        print("Você escolheu Sair.")
        break

    ## Tratar opção inválida no menu principal
    else:
        print("Digite uma opção válida, por favor.")