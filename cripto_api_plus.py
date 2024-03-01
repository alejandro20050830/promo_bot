import requests
import json
import time
# Configura tu token de autenticación
"""
   Test=True
   TOKEN = '155841:AAZtbKQZ9t1IIWIwOHWxnWk2HBGqep0SpQo'
   if Test:
        TOKEN = '11367:AAFq63GgUBVGKRLkxNq9LyZTBf9okBlCCmx'
    BASE_URL = 'https://pay.crypt.bot/api/'
    if Test:
        BASE_URL='https://testnet-pay.crypt.bot/api/'
"""
# Crear una nueva factura
def crear_factura(amount,Test=False):
    TOKEN = '155841:AAZtbKQZ9t1IIWIwOHWxnWk2HBGqep0SpQo'
    if Test:
        TOKEN = '11367:AAFq63GgUBVGKRLkxNq9LyZTBf9okBlCCmx'
    BASE_URL = 'https://pay.crypt.bot/api/'
    if Test:
        BASE_URL='https://testnet-pay.crypt.bot/api/'

    endpoint = 'createInvoice'
    url = BASE_URL + endpoint
    
    headers = {
        'Crypto-Pay-API-Token':TOKEN,

    }

    data = {
        'currency_type':'fiat',
        'fiat':"USD",
        #'asset': "TRX",
        #'accepted_assets':["BTC","TRX","USDT"],
        'amount': amount,  # Cantidad en la moneda especificada
        
        'description': 'Pago de servicios'  # Descripción de la factura
    }

    response = requests.get(url, headers=headers,params=data)

    if response.status_code == 200:
        resp=response.json()['result']
        print(f"Id:{resp['invoice_id']}\nURL:{resp['bot_invoice_url']}")
        return resp
    else:
        print(response.json())
        return None

# Verificar el estado de una factura
def verificar_pago(id_factura,Test=False):
    TOKEN = '155841:AAZtbKQZ9t1IIWIwOHWxnWk2HBGqep0SpQo'
    if Test:
        TOKEN = '11367:AAFq63GgUBVGKRLkxNq9LyZTBf9okBlCCmx'
    BASE_URL = 'https://pay.crypt.bot/api/'
    if Test:
        BASE_URL='https://testnet-pay.crypt.bot/api/'

    
    endpoint = 'getInvoices'
    url = BASE_URL + endpoint
    headers = {
        'Crypto-Pay-API-Token':TOKEN,

    }

    data = {
        'invoice_ids':id_factura# Descripción de la factura
    }


    response = requests.get(url, headers=headers,params=data)

    if response.status_code == 200:
        factura = response.json()
        print(factura)
        #if len(response.json()['result']['items'])!=0:
            #factura_status=response.json()['result']['items'][0]['status']
       
        return factura # True si la factura ha sido pagada, False si no
    else:
        return None




#id=create_dates['invoice_id']
#pay_url=create_dates['bot_invoice_url']
"""
while True:
    verify_resp=verificar_pago(id)
    if verify_resp:
        factura_status=verify_resp['result']['items'][0]['status']

        if factura_status=='paid':
            payed_usd=verify_resp['result']['items'][0]['paid_usd_rate']
            fee_usd=verify_resp['result']['items'][0]['fee_in_usd']
            cripto_payed=verify_resp['result']['items'][0]['paid_asset']
            print(f"----------PAYED-------------\nReal_recived={payed_usd}USD\nFee:{fee_usd}\nCripto:{cripto_payed}")
            break
        print("No pay")
    else:
        print('Error')
    
    time.sleep(5)
"""
