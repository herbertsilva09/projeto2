from time import sleep
def linha():
    print('-' * 70)
while True:
    print('''Vamos calcular gastos mensais ''')
    linha()
    sleep(5)
    try :
        renda = int(input('Qual é sua renda? '))
        sleep(2)
        linha()
        desnecessario = int(input('Quantos é gasto com coisas não necessario? '))
        sleep(2)
        linha()
        investimento = int(input('''Quantos é gasto em algum investimento ? '''))
        sleep(2)
        linha()
        despesas= renda - desnecessario - investimento
        resultado = despesas / 2 
        outra_parte = resultado 

        agua = int(input('Quantos é gasto com  agua ?'))
        sleep(2)
        linha()
        mercado = int(input('Quantos é gasto com a compra do mês ?'))
        sleep(2)
        linha()
        luz = int(input('Quantos é gasto com a luz ?'))
        sleep(2)
        linha()
        gas = int(input(' Quantos é gasto com gás?'))
        sleep(2)
        linha()
        sobra = resultado - agua 
        sobra2 = sobra - luz
        s = sobra2 - mercado
        g = s - gas
        opcional = g + outra_parte
        print(f'Sobrou o valor de {opcional}  , guardar ....')
        linha()
        linha()
        pergunta = int(input('''Você paga aluguel ? Se sim digite  o valor do aluguel ...... Se nao digite 0  .  
    Aluguel ?'''))
        sleep(2)
        linha()
        pergunta2 = int(input('''Quantos gasta em transporte ?  '''))
        sleep(2)
        linha()
        aluguel = opcional - pergunta
        transporte = opcional - pergunta2
        sobrou = aluguel + transporte
        final = sobrou - opcional
        linha()
        break
    except:
        linha()
        linha()
        print('O programa só aceita numeros ..... numeros inteiros , Tente novamente')
        linha()
        print('Digite [0] para continuar  , Digite [1] para sair do programa')
        linha()
        z = int(input('digite :  '))
        if  z == 1:
            break
lista =[f'renda = {renda}' ,  f'gastos desnecessarios = {desnecessario} ', f'investimento = {investimento}' , f'agua = {agua}',f'mercado = {mercado}',f'luz = {luz}',f'gás = {gas}',f'aluguel = {pergunta} ', f'Transporte = {pergunta2}',f'sobrou = {final}']
print('Tabela dos gastos mensais')
print(' ' * 70)
print(' ' * 70)
def pontos():
    print('.' * 70)  
for c in range(0,9):
    print(lista[c])
    pontos()
print(lista[9])
print(' ' * 70)
print(' ' * 70)








