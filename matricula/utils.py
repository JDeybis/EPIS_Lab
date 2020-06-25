from tabula import read_pdf


def repite(cad, tupl):
    flag = False
    for k in tupl:
        if k in cad:
            flag = True
    return flag


def save_pdf_data(file):
    df1 = read_pdf(file, pages='all', guess=False)  # , lattice=True)
    df2 = read_pdf(file, pages='all', guess=False, lattice=True)
    keys = ('CURSO', 'ESCUELA')
    alumnos = []
    e1 = []
    for pc in range(len(df1)):
        for name in df1[pc].iterrows():
            a1 = []
            for c in name[1]:
                if isinstance(c, str):
                    if repite(c, keys):
                        a1.append(c)
            if a1:
                e1.append(a1)

    e1[0][0] = e1[0][0].replace('ESCUELA PROFESIONAL :', '')
    e1[1][0] = e1[1][0].replace('SIGLA :', '')

    escuela = e1[0][0][:e1[0][0].index(':') - 10]
    semestre = e1[0][0][e1[0][0].index(':') + 1:]
    cur = e1[1][0][e1[1][0].index(':') + 2:len(e1[1][0]) - 6]
    sigla = e1[1][0][len(e1[1][0]) - 6:]
    serie = sigla[4] + '00'

    for p in range(0, len(df2)):
        for row in df2[p].iterrows():
            a = []
            for i in row[1]:
                if not isinstance(i, float):
                    if isinstance(i, int):
                        if len(str(i)) == 8:
                            a.append(i)
                    else:
                        a.append(i)
            alumnos.append(a)
    data = {
        "alumnos": alumnos,
        "escuela": escuela,
        "serie": serie.upper(),
        "sigla": sigla,
        "curso": cur.upper(),
        "semestre": semestre
    }
    return data

# archivos = ['27_CC-121.pdf', '27_IS-141.pdf', '27_IS-241.pdf', '27_IS-341.pdf', '27_IS-441.pdf',
#             '27_IS-443.pdf',
#             '27_IS-445.pdf', '27_IS-451.pdf', '27_IS-453.pdf', '27_IS-545.pdf', '27_IS-553.pdf']
#
# a = save_pdf_data('/home/jhon/Public/developer/testpdf/' + archivos[0])
# print(a['alumnos'])
#         alumnos.append(item)
