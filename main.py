from openpyxl import load_workbook

colunaPN = 2
colunaDescricao = 1
colunaTipo = 3
colunaQuant = 4


def formatChecklist():
    caminhoOriginal = "C:/Users/Roberto/Desktop/CHEKCLIST.xlsx"
    planilha = load_workbook(caminhoOriginal)
    folha = planilha['Planilha1']

    # print(f"Valor: {folha['A1'].value}")
    if deletColuns(folha):
        folha = deletColuns(folha)
        print("Colunas deletadas com sucesso!")
        folha = SelectDeletRows(folha)

        planilha.save(caminhoOriginal)
        planilha.close()
    else:
        print("Erro ao deletar colunas")


def SelectDeletRows(pagina):
    count = 0
    deletarLinhas = list()

    for linhas in pagina:
        count += 1

        if "90-000" in linhas[colunaPN].value:
            print(f"Valor da linha {count}: {linhas[0].value} --> Conjunto final!")
            deletarLinhas.append(count)
        elif "90-110" in linhas[colunaPN].value:
            print(f"Valor da linha {count}: {linhas[0].value} --> Conjunto soldado!")
            deletarLinhas.append(count)
        elif "4-260" in linhas[colunaPN].value:
            print(f"Valor da linha {count}: {linhas[0].value} --> Consignados!")
            deletarLinhas.append(count)
        elif "9-200" in linhas[colunaPN].value:
            print(f"Valor da linha {count}: {linhas[0].value} --> Usinados!")
            deletarLinhas.append(count)
        else:
            print(f"Valor da linha {count}: {linhas[colunaPN].value}")
    print(f"Lista de linhas para serem excluidas: {deletarLinhas}")
    paginaTratada = deletRow(pagina, deletarLinhas)
    return paginaTratada


def deletColuns(pagina):
    try:
        for index in range(8, 16):
            pagina.delete_cols(5)
        return pagina
    except:
        return False


def deletRow(pagina, linha):
    print(f'Linhas recebidas para exclusao: {linha}')
    contador = 0
    for index in linha:
        print(f'{index}  {type(index)}')
        pagina.delete_rows(index - contador)
        contador += 1

    for item in pagina:
        print(item[colunaPN].value)

    return pagina


if __name__ == "__main__":
    formatChecklist()
