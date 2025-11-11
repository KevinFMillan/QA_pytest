import send_requests as sender
import data

def get_user_body(first_name):

    new_user_body = data.user_body.copy()
    new_user_body["firstName"] = first_name

    return new_user_body

def positive_assert(name):

    user_body = get_user_body(name)
    respuesta = sender.post_new_user(user_body)
                                     
    assert respuesta.status_code == 201
    assert respuesta.json()['authToken'] != ''

    users_table_response = sender.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + respuesta.json()["authToken"]
    
    assert users_table_response.text.count(str_user) == 1

def negative_asserts(name):

    user_body = get_user_body(name)
    respuesta = sender.post_new_user(user_body)

    assert respuesta.status_code == 400
    assert respuesta.json()["message"] == 'Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres.'
    assert respuesta.json()['code'] == 400

    # users_table_response = sender.get_users_table()
    # str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
    #            + user_body["address"] + ",,," + respuesta.json()["authToken"]
    
    # assert users_table_response.text.count(str_user) == 1

def negative_assert_sin_parametro():
    user = data.user_body.copy()
    user.pop("firstName")
    respuesta = sender.post_new_user(user)
    assert respuesta.status_code == 400
    assert respuesta.json()["message"] == "No se han aprobado todos los parámetros requeridos"
    assert respuesta.json()['code'] == 400


def test_positive_asserts(): # Se prueban los parametros que se sepone que dan positivo (automatizacion)
    positive_assert('aa')
    positive_assert('aaaaaaaaaaaaaaa')


def test_negative_asserts():
    negative_asserts('A') # Aprobado
    negative_asserts('Aaaaaaaaaaaaaaaa') # Aprobado
    # negative_asserts('A Aaa') # No aprobado
    negative_asserts('/"№%@=') # status code 201
    negative_asserts('1234') # status code 201
    #negative_assert_sin_parametro() # Para este y el de abajo de debe crear otra def con el message 
    # negative_asserts("") # de error correspondiente ya que es distinto al resto de pruebas negatidvas
    negative_asserts(134) # status code 201
