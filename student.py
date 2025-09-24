# Leia uma linha com o número do cartão
#Isabela Raposeiras e Luísa Del' Duca
numero = input()
impares= []
for i in numeros [-1::-2]:
  impares.append(int(i))
pares = []
for i in numeros[-2::-2]:
  if 2*int(i)<10:
    pares.append(2*int(i))
  else:
    pares.append(2*int(i)-10+1)
soma = sum(pares)+sum(impares)
if int(soma/10) == soma/10:
  print ("Cartão válido")
  else:
    print ("Cartão inválido")
# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.
print("--- Informações do Curso ---")
print(f"Nome: {nome_curso}")
print(f"Ano: {ano}")
print(f"Versão: {versao_apostila}")
print(f"Está ativo? {curso_ativo}")
print("-" * 20)

numero_a = 15
numero_b = 4

soma = numero_a + numero_b
subtracao = numero_a - numero_b
multiplicacao = numero_a * numero_b
divisao = numero_a / numero_b
potencia = numero_b ** 2

print("\n--- Demonstração de Operações Aritméticas ---")
print(f"{numero_a} + {numero_b} = {soma}")
print(f"{numero_a} - {numero_b} = {subtracao}")
print(f"{numero_a} * {numero_b} = {multiplicacao}")
print(f"{numero_a} / {numero_b} = {divisao}")
print(f"{numero_b} ao quadrado é {potencia}")

saudacao = "Olá, "
aluno = "Estudante"
mensagem_completa = saudacao + aluno + "!"
print(f"Mensagem concatenada: {mensagem_completa}")
print("-" * 20)

idade_minima_para_votar = 16

print("\n--- Verificação de Idade para Votação ---")
idade_texto = input("Digite sua idade: ")
idade_numero = int(idade_texto)

if idade_numero >= idade_minima_para_votar and idade_numero < 18:
    print("Você pode votar, mas não é obrigatório.")
elif idade_numero >= 18 and idade_numero < 70:
    print("Seu voto é obrigatório.")
elif idade_numero < 16:
    print("Você ainda não pode votar.")
else:
    print("Seu voto é opcional.")
print("-" * 20)

print("\n--- Demonstração de Loops ---")
print("Contagem com 'while':")
contador = 1
while contador <= 3:
    print(f"Número: {contador}")
    contador = contador + 1

print("\nContagem com 'for':")
for i in range(4):
    print(f"Iteração número: {i}")
print("-" * 20)

print("\n--- Acesso ao Sistema ---")
senha_correta = "python123"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Por favor, digite a senha para continuar: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("\nSenha correta! Acesso concedido ao sistema.")
# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
