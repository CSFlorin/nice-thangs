from docxtpl import DocxTemplate, R
import pandas as pd
import os


def format_name(name):
    if ',' in name:
        name = name.split(',')
        name = list(map(lambda x: x.strip(), name))
        name = ' '.join(name[::-1])
    return name


if __name__ == "__main__":
    dir = 'out/'
    if not os.path.exists(dir):
        os.makedirs(dir)

    df = pd.read_csv("nice-thangs.csv")
    df = df.drop(['Timestamp'], axis=1)

    for column in df:
        thangs = df[column].dropna().sample(frac=1).values
        thangs = '\t' + '\n\n'.join(thangs)  # for Python 2: .decode('utf-8')

        doc = DocxTemplate("template.docx")
        context = {
            'name' : format_name(column),
            'thangs': R(thangs)
        }
        doc.render(context)
        doc.save("out/" + column + ".docx")
