import random
import re

class Dado():
    def busca_dado(message):
        padrao = re.compile("\A[0-9]{0,4}[dD][0-9]{1,4}") #padrão da mensagem para só rodar o código quando segue o padrão (0 a 4 números no começo, um d e mais 0 a 4 numeros dps)
        #ele tambem tira fora o resto da mensagem, se for d20+10 ele pega só o d20
        return padrao.search(message.content)

    async def roda_dado(busca, message):
        dnumero = busca.group()
        print(f'dado: {dnumero} ({message.author.name})')
        if dnumero[0].isnumeric(): #se o primeiro digito é um numero fica mais complexo, se não é só rodar o dado
            dnumero = dnumero.lower() #transformar o D maiusculo em d para rodar a linha 24 sem quebrar
            num1, num2 = dnumero.split('d')    
            #num1 = numero de dados pra rolar, num2 = dado
            lista = [] #lista dos resultados
            for quantidadededados in range(int(num1)):
                n_aleatorio = random.randint(1, int(num2))
                lista.append(str(n_aleatorio))
            lista.sort(reverse = True, key = int) #lista ordenada dos dados, da ordem do maior para o menor resultado
            dado = lista
            soma = 0
            for x in range(len(lista)):
                soma += int(lista[x]) #somar todos os resultados dos dados
        else:
            num2 = dnumero.replace(dnumero[0], '') #troca o d do d20 para '' vazio, então sobra só o 20
            soma = random.randint(1, int(num2))
            dado = f'[{soma}]'

        if type(dado) == str: #parte do código que deixa em negrito se tirar o dado máximo
            if soma == int(num2):
                dado = f'[**{soma}**]'
        else:
            for x in range(len(dado)):
                if dado[x] == num2:
                    numero = dado[x]
                    dado[x] = f'**{numero}**'
            dado = (f"[{', '.join(dado)}]")

        try:
            teste_de_erro = str(message.content[len(dnumero)]) #linha para dar erro se não houver conta matemática no dado ex: d20+10, se não houver + ou - vai pro except
            complemento = str(message.content[len(dnumero):]) #+10
            conta = str(soma) + complemento#resultado do dado + complemento ex: d20+10 -> 6 + 10, ele resolve a conta no eval()
            await message.channel.send(f':monkey: {message.content} -> {dado}{complemento} -> {eval(conta)} :monkey:')
        except IndexError:
            if dnumero[0].isnumeric():
                await message.channel.send(f':monkey: {message.content} -> {dado} -> {soma} :monkey:')    
            else:
                await message.channel.send(f':monkey: {message.content} -> {dado} :monkey:')