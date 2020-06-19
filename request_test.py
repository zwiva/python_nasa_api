import json
import requests

# results = ""
test_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000"
test_api_key = "api_key=iA435kVAfBUEHbkCpcZrSiklgadN9LAUU3xz5Bvc"

def request(requested_url,api_key):
    url = str(requested_url)+"&"+str(api_key)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    results = json.loads(response.text)
    return results
    # return url

# request(url,api_key)
results = request(test_url, test_api_key)

#print(results) # hasta aqui funciona!!!
html=""

def build_web_page(results):
    html=""
    html_attach = ""
    results
    for i in range(0,15):
        each_photo = results["photos"][i]["img_src"]
        height = "250px"
        width = "250px"
        html_attach += "<p>Photo {}</p>\n<img src=\"{}\" height=\"{}\" width=\"{}\">\n".format((i+1), each_photo, height, width)
        
        # html_attach += "<img src=\"{}\" height=\"{}\" width=\"{}\">\n".format(each_photo, height, width) cuidado, funca!!!
        
    html += """<html>
    <head>
    </head>
    <body style="background-color:gray;">
    <h2 style="color:white;">Showing 15 photos... </h2>
    {}
    </body>
    </html>""".format(html_attach)
    print(html)

    with open("curiosity_photos.html","w") as f:
        f.write(html)
    return html

build_web_page(results)

# --------------------------- NO TERMINADO ---------------------------
# Pregunta bonus: Crear la función photos_count que reciba el diccionario de respuesta, y devuelva un nuevo diccionario con el nombre de la cámara y la cantidad de fotos.

results

def photos_count(results):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    for i in range(0,856):
        each_id = results["photos"][i]["camera"]["id"]
        if each_id == 20:
            a += 1
        elif each_id == 21:
            b += 1
        elif each_id == 22:  
            c += 1
        elif each_id == 23:  
            d += 1
        elif each_id == 24:  
            e += 1
        elif each_id == 25:
            f += 1
        elif each_id == 26:
            g += 1

    print("camera 20:",a)
    print("camera 21:",b)
    print("camera 22:",c)
    print("camera 23:",d)
    print("camera 24:",e)
    print("camera 25:",f)
    print("camera 26:",g)
    print(a+b+c+d+e+f+g)
    

photos_count(results)

    #{nombre_camara(1 de 7):int(cantidad_de_fotos),...}
