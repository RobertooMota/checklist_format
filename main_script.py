from openpyxl import load_workbook

path = "C:/Users/Roberto/Desktop/exemplo.xlsx"

tipo = 4
item = 2
quantidade = 6
descricao = 3


def format(caminhoOriginal, filtro):
    planilha = load_workbook(caminhoOriginal)
    sheets = planilha.sheetnames[0]
    folha = planilha[sheets]

    lista = selectRows(folha, filtro)
    dados = selectData(folha, lista)

    planilha.close()


def selectRows(folha, filtro) -> list:
    contador = 0
    linhas = list()
    for rows in folha:
        contador += 1
        if filtro in rows[item].value and 'P' in rows[tipo].value:
            # print(f'{rows[item].value}  {rows[tipo].value}  {rows[descricao].value}   {rows[quantidade].value}')
            linhas.append(contador)
    return linhas


def selectData(folha, lista) -> list:
    _item = 'C'
    _descricao = 'D'
    _tipo = 'E'
    _quantidade = 'G'
    contador = 0
    Colunas = []
    Matriz = []
    for row in folha:
        contador += 1
        indexMatriz = 0
        for index in lista:
            if contador == index:
                # print(f'{folha.cell(row=index, column=item + 1).value}  {row[tipo].value}')

                Colunas.append(folha.cell(row=index, column=item + 1).value)
                Colunas.append(folha.cell(row=index, column=descricao + 1).value)
                Colunas.append(folha.cell(row=index, column=quantidade + 1).value)
                Colunas.append(folha.cell(row=index, column=tipo + 1).value)
                Matriz.append(Colunas.copy())
                Colunas.clear()

    for i in Matriz:
        print(i)

    return Colunas


if __name__ == "__main__":
    format(path, "90-200")
