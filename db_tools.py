import json


def dict_to_txt(dict, file):
    with open(file, "w") as file_:
        json.dump(dict, file_, default=str)


def txt_to_dict(file):
    # Leer el contenido del archivo como cadena
    with open(file, "r") as file_:
        contenido = file_.read()

    # Convertir la cadena JSON en un diccionario

    dict_ = json.loads(contenido)
    return dict_
