from tqdm import tqdm
import requests
import time

# for numero in tqdm(range(100)):
#     time.sleep(1)
#
#
# lista = [1,2,3,4,5,6,7,8,9,10]
#
# for char in tqdm(lista):
#     time.sleep(1)

# with tqdm(total=10) as barra_progresso:
#     for i in range(5): # quantas vezes a barra irá aumentar, nesse caso 5 vezes, de 20% em 20%
#         time.sleep(1)
#         barra_progresso.update(2)

with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")
# passo 2: pegar as informações de cada cep
enderecos_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    # passo 3: verificar se a cidade é RIo de Janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    # passo 4: printar o cep e o bairro
    if cidade == "Rio de Janeiro":
        enderecos_entrega.append((cep, bairro))
print(enderecos_entrega)

