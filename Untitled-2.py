print("Digite o número referente ao dia da semana")
print("1. Domingo")
print("2. Segunda")
print("3. Terça")
print("4. Quarta")
print("5. Quinta")
print("6. Sexta")
print("7. Sábado")
semana = int(input())

match semana:
    case 1: 
        print("Aos domingos, te recomendamos ir à feira.")
    case 2: 
        print("Às segundas, te recomendamos caminhar e praticar exercícios para começar a semana com energia")
    case 3: 
        print("Às terças, te recomendamos ir ao museu.")
    case 4:
        print("Às quartas, te recomendamos ir ao cinema")
    case 5:
        print("Às quintas, te recomendamos ir ao parque olímpico")
    case 6: 
        print("Às sextas, te recomendamos ir em algum evento cultural")
    case 7:
        print("Aos sábados, te recomendamos ir ao mercadão")