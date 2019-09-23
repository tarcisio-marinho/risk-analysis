
import os
from pprint import pprint


dataset = {}
header = ['tipo', 'situacao', 'data', 'hora', 'bairro', 'endereco', 'numero', 'complemento', 'natureza', 'descricao', 'auto', 'moto', 'ciclom', 'ciclista', 'pedestre', 'onibus', 'caminhao', 'viatura', 'outros', 'vitimas', 'vitimasfatais']

files = os.listdir('data')
for f in files:
    with open(os.path.join('data', f)) as f:
        df = f.readlines()
    head = df[0].split(';')
    head = [h.replace('\n', '').replace("\"", "") for h in head]
    
    ret = df.pop(0)
    for f in df:
        line = f.replace("\"", "").replace("\n", '').split(";")
        print(line)
        break
    