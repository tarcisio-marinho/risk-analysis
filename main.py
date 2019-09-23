import requests, json, os
from pprint import pprint

def busca_dicionario(p, d):
    key2 = 'AIzaSyDaY5QRWxXSN-2PCncnGv3R3oyjVJffJPE'
    link = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&key={2}&language=pt".format(p, d, key2)
    req = requests.get(link)
    return json.loads(req.text)

def get_bairros(dicionario):
    all_bairros = {}
    percurso = (dicionario["routes"][0]["legs"][0]["steps"])
    for i in percurso: 
        geolocation_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=AIzaSyDaY5QRWxXSN-2PCncnGv3R3oyjVJffJPE' %(i['end_location']['lat'], i['end_location']['lng'])
        location = requests.get(geolocation_url)
        obj = json.loads(location.text)
        for i in obj['results']:
            try:
                bairro = (i['formatted_address'].split('-')[1].split(',')[0].replace(" ", "").upper())
                cidade = i['formatted_address'].split('-')[1].split(',')[1]
                try:
                    int(bairro)
                except:
                    if(not all_bairros.get(bairro) and len(bairro) > 2):
                        all_bairros[bairro] = cidade.upper()
            except:
                pass

    return all_bairros

if __name__== "__main__":
    p = 'rua araripina 419 santo amaro'
    d = 'rua são matheus iputinga'
    dicionario = busca_dicionario(p, d)
    lista_bairros = get_bairros(dicionario)
    print(lista_bairros)
