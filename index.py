import xmltodict
import os
import json

#analise dos dados
def pegar_info(nome_arquivo):
    print(f"Pegou os arquivos: {nome_arquivo}")
    print("-=" * 30)
    with open(f"xml/{nome_arquivo}", "rb") as arquivo_xml:
        dicionario_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dicionario_arquivo, indent=4))
        infos_nota = dicionario_arquivo["nota_fiscal"]
        empresa_emissora = infos_nota["emitente"]["razao_social"]
        nome_cliente = infos_nota["cliente"]["razao_social"]
        endereco = infos_nota["cliente"]["endereco"]

        print(f"Empresa emissora: {empresa_emissora} \nNome do cliente: {nome_cliente} \nEndereço do cliente: {endereco}")


#coletando o arquivo
pasta_arquivos = os.listdir("xml")

for arquivo in pasta_arquivos:
    pegar_info(arquivo)
    break
