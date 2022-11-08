from openpyxl import load_workbook

path = "C:/Users/Roberto/Desktop/exemplo.xlsx"

tipo = 4
codigo = 2


def format(caminhoOriginal, filtro):
    planilha = load_workbook(caminhoOriginal)
    sheets = planilha.sheetnames[0]
    folha = planilha[sheets]
    lista = selectRows(folha, filtro)
    print(lista)

    planilha.close()


def selectRows(folha, filtro):
    contador = 0
    linhas = list()
    for rows in folha:
        # print(f'{rows[2].value}  {rows[4].value}')
        contador += 1
        if filtro in rows[codigo].value and 'P' in rows[tipo].value:
            print(f'{contador} - {rows[codigo].value}  {rows[tipo].value}')
            linhas.append(contador)

    return linhas


if __name__ == "__main__":
    format(path, "90-200")
