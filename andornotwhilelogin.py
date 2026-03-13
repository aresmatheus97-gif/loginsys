entrada = input('[E]ntrar [S]air: ')
name = input('Nome: ')
exibname = f'Bem vindo, {name}'
if entrada == 'E' or entrada == 'e':
    print(exibname)
else:
    print("Você saiu")
    exit()
creat = input("Deseja Criar um usuario?")
if creat == "S" or "s":
 while True:
    usercreat = input("Crie seu usuario: ")
    if not usercreat:
        print("Insira um valor")
        continue  # continua no loop até que um valor válido seja inserido

    senhacreat = input("Crie sua senha: ")
    if not senhacreat:
        print("Insira uma senha")
        continue  # continua no loop até que uma senha válida seja inserida
    break # sai do loop se ambos usercreat e senhacreat forem válidos
else:
    print("Ok, continue")
    
print("Bem vindo, faça seu login!")
## início do loop e checagem de compatibilidade de senha e usuário
while True:
    user = input("Insira seu usuario: ")  # guarda o valor de usuário para ser checado
    senha = input("Insira sua senha: ")

    usercheck = (user == usercreat)
    senhacheck = (senha == senhacreat)

    if usercheck and senhacheck:  # aqui, estamos checando as duas entradas juntas, podemos também fazer separado apenas mudando a estrutura
        print("Logado com sucesso, aguarde.")
        break  # aqui há break caso a checagem seja TRUE
    else:
        if not usercheck:  # neste momento iremos retornar para o usuário qual de suas credenciais estão incorretas.
            print("Usuario incorreto")
        if not senhacheck:
            print("Senha incorreta, tente novamente")

## not inverte a expressão-