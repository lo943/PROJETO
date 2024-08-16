#Café da manhã

print("Vamos montar um cardápio personalizado?")

breakfast = []
Lunch = []
dinner = []

print("Café da manhã:")
for X in range(0,3)
    opcao = input(f"Digite a opção {X+1}:")
    breakfast.append(opcao)
    if opcao == "leite" or opcao == "queijo" or opcao == "pão":
        print("Alimento não recomendado!")
print("Eis as opções escolhidas:", breakfast)

#Almoço

print("Almoço:")
for X in range(0,4):
    opcao = input(f"Digite a opção {X+1}:")
    dinner.append(opcao)
    if opcao == "camarão" or opcao == "pimenta":
        print("Alimento não recomendado!")
print("Eis as opções escolhidas:", dinner)