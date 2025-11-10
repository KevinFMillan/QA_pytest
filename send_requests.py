import requests as req
import configuracion as conf
import data

def get_docs():
    return req.get(conf.URL_SERVICE + conf.DOC_PATH)

def get_logs():
    return req.get(conf.URL_SERVICE + conf.LOG_MAIN_PATH)

def get_users_table():
    return req.get(conf.URL_SERVICE + conf.USERS_TABLE_PATH)

def post_new_user(body):
    return req.post(conf.URL_SERVICE + conf.CREATE_USER_PATH,  
                         json=body,  
                         headers=data.headers)

def post_products_kits(products_ids):
    return req.post(conf.URL_SERVICE + conf.PRODUCTS_KITS_PATH,
                         json=products_ids, 
                         headers=data.headers)