# -----> ALUNA: Débora Dâmaso Lopes, RM: 97836

# OBS 1 -> Prof, achei interessante fazer uma def para permitir APENAS LETRAS no input do nome:
# Ou seja, não será aceito números ou characters que não sejam letras.
# OBS 2 -> Fiz uma situação hipotética imaginando caso o usuário digite apenas 1 nome:
# Nesse caso, o programa pede para que digite pelo menos 1 nome e 1 sobrenome.

# -----> Essa def tem que separar o nome do sobrenome
def separar_nome_sobrenome(nome_completo):
    partes = nome_completo.split()
    if len(partes) <= 1:
        return None, None
    primeiro_nome = partes[0]
    sobrenome = ' '.join(partes[1:])
    return primeiro_nome, sobrenome

# -----> Essa def conta as palavras do nome
def contar_palavras(nome_completo):
    palavras = nome_completo.split()
    return len(palavras)

# -----> Essa def formata o nome no estilo bibliografico
def formatar_bibliografia(nome_completo):
    partes = nome_completo.split()
    if len(partes) <= 1:
        return None
    sobrenome = partes[-1].upper()
    nome = ' '.join(partes[:-1])
    return f"{sobrenome}, {nome}"

# -----> Def para permitir apenas letras no input do nome
def possui_apenas_letras(texto):
    for char in texto:
        if char.isdigit() or (not char.isalpha() and char != ' '):
            return False
    return True

# -----> Essa é a def principal, que contem menu e escolhas
def main():
    nome_completo = ""

    while True:
        print("MENU")
        print("\n0 – SAIR")
        print("1 – Digite um nome completo")
        print("2 – Exibe separado o Nome do Sobrenome")
        print("3 – Conta quantas palavras há no nome completo")
        print("4 – Exibir em formato de bibliografia")
        escolha = input("\nEscolha: ")

        if escolha == '0':
            print("\nPROGRAMA ENCERRADO.")
            break
        elif escolha == '1':
            while True:
                nome_completo = input("Digite um nome completo:\n")
                if possui_apenas_letras(nome_completo):
                    partes = nome_completo.split()
                    if len(partes) > 1:
                        break
                    else:
                        print("Digite pelo menos um nome e um sobrenome.")
                else:
                    print("Digite um nome válido (apenas letras).")
        elif escolha == '2':
            if not nome_completo:
                print("Primeiramente digite um nome na opção 1")
            else:
                primeiro_nome, sobrenome = separar_nome_sobrenome(nome_completo)
                if primeiro_nome and sobrenome:
                    print(f"Nome: {primeiro_nome}")
                    print(f"Sobrenome: {sobrenome}")
        elif escolha == '3':
            if not nome_completo:
                print("Primeiramente digite um nome na opção 1")
            else:
                num_palavras = contar_palavras(nome_completo)
                print(f"O nome {nome_completo} tem {num_palavras} palavras.")
        elif escolha == '4':
            if not nome_completo:
                print("Primeiramente digite um nome na opção 1")
            else:
                bibliografia = formatar_bibliografia(nome_completo)
                if bibliografia:
                    print(bibliografia)
        else:
            print("Opção inválida, digite um item de 0 a 4.")


if __name__ == "__main__":
    main()