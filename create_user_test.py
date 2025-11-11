import send_requests as sender
import data

def get_user_body(first_name):
    new_user_body = data.user_body.copy()
    new_user_body["first_name"] = first_name
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

def test_positive_asserts(): # Se prueban los parametros que se sepone que dan positivo (automatizacion)
    positive_assert('kevinatest1')
    positive_assert('kevinatest2')
    positive_assert('kevinatest3')