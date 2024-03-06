from telethon import TelegramClient, events
from telethon.tl import functions, types
from telethon import events, Button
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
import telegram
from keep_alive import keep_alive
import time
import threading
from cripto_api_plus import*
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.types import UpdateShortMessage
from db_tools import*
from telethon.tl.types import Message, PeerChannel
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipant
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import UserNotParticipantError
import ast
import json
import requests
from datetime import datetime, timezone
from translate_api import*
import re
keep_alive()
state=True
first_init=True
import telethon
import asyncio
api_id = '16620070'
api_hash = 'dbf692cdc9b6fb2977dda29fb1691df4'
user_dates={}
#group_ids = {}
#channel_ids={}
user_dates['chat_ids']=[]
channel_ids_swap={}
#pending_messages = {}
admins=[]
admin_wallet=''
bot_token = '6395817457:AAH1YxFN6h1arYwu70ESTtavNxFsGqoy7nc'
bot_token = '5850221861:AAEg7MPNSUkK2nYm0YPCk2hBQzNmD_EAnds'
test_mode=True
on_saving=False
txts=['🧩 Conectar Cuenta','💠 Conectar Canal','〽️ Agregar Grupos','⚙️ Configuración','👛 Suscripción','👁️ Remitente','⏳ Espera','🕖 Reenvío','✏️ Editar Grupos','🔰 Referidos','Siguiente ➡️','🔙 Volver','🔝 Menú principal','🧩 Más Cuentas','〽️ Más Canales','🔙 Volver','🔝 Menú principal','🚫 Cancel','🔖 Crear Mensaje','📮 Notificaciones','🔘 Pausar Reenvío','🖲️ Compartir Suscripción']
menu_system=[
    [[Button.text(txts[0],resize=True)],[Button.text(txts[1],resize=True),Button.text(txts[2],resize=True)],[Button.text(txts[3],resize=True)]],
    [[Button.text(txts[4],resize=True)],[Button.text(txts[5],resize=True),Button.text(txts[6],resize=True)],[Button.text(txts[7],resize=True),Button.text(txts[8],resize=True)],[Button.text(txts[9],resize=True),Button.text(txts[10],resize=True)],[Button.text(txts[11],resize=True),Button.text(txts[12],resize=True)]],      
    [[Button.text(txts[18],resize=True)],[Button.text(txts[19],resize=True),Button.text(txts[20],resize=True)],[Button.text(txts[21],resize=True)],[Button.text(txts[15],resize=True),Button.text(txts[16],resize=True)]]       
             ]
menu_history={}
traduct_menu=txt_to_dict('db/lg_db')
lenguage=['russian','english','chinese (traditional)','arabic']
if len(traduct_menu)==0:
    
    for txt in txts:
        print(txt)
        traduct_menu[txt]=[txt]
        for lg in lenguage:
            print(lg)
            traduct_menu[txt].append(translate(txt,lg))
            
            
        dict_to_txt(traduct_menu,'db/lg_db')
    
print(traduct_menu['💠 Conectar Canal'])

# Iniciar sesión como bot
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

phone_code_hash_=""
# Iniciar sesión como usuario
#user = TelegramClient('user', api_id, api_hash)
async def get_bot_id():
    me = await bot.get_me()
    return me.id

# Crea un decorador personalizado para filtrar los mensajes
def private_message_handler(func):
    async def wrapper(event):
        if event.is_private and event.sender_id != await get_bot_id():
            await func(event)
    return wrapper
async def get_custom_menu(event):
    sender = await event.get_sender()

    user_id=str(sender.id)
    txts_=['🧩 Conectar Cuenta','💠 Conectar Canal','〽️ Agregar Grupos','⚙️ Configuración','👛 Suscripción','👁️ Remitente','⏳ Espera','🕖 Reenvío','✏️ Editar Grupos','🔰 Referidos','Siguiente ➡️','🔙 Volver','🔝 Menú principal','🧩 Más Cuentas','〽️ Más Canales','🔙 Volver','🔝 Menú principal','🚫 Cancel','🔖 Crear Mensaje','📮 Notificaciones','🔘 Pausar Reenvío','🖲️ Compartir Suscripción']
    lg_id={'spanish':0,'russian':1,'english':2,'chinese (traditional)':3,'arabic':4}
    ind=0
    for t in txts_:
        translated=traduct_menu[t][lg_id[user_dates[user_id]['leng']]]
        txts_[ind]=translated
        ind+=1
    menu_system_=[
    [[Button.text(txts_[0],resize=True)],[Button.text(txts_[1],resize=True),Button.text(txts_[2],resize=True)],[Button.text(txts_[3],resize=True)]],
    [[Button.text(txts_[4],resize=True)],[Button.text(txts_[5],resize=True),Button.text(txts_[6],resize=True)],[Button.text(txts_[7],resize=True),Button.text(txts_[8],resize=True)],[Button.text(txts_[9],resize=True),Button.text(txts_[10],resize=True)],[Button.text(txts_[11],resize=True),Button.text(txts_[12],resize=True)]],      
    [[Button.text(txts_[18],resize=True)],[Button.text(txts_[19],resize=True),Button.text(txts_[20],resize=True)],[Button.text(txts_[21],resize=True)],[Button.text(txts_[15],resize=True),Button.text(txts_[16],resize=True)]]       
             ]
    
    return menu_system_
    
    
def event_to_dict(event):
    event_dict = {
        'type': type(event).__name__,
        'message': event.message,
        #'chat_id': event.chat_id,
        #'sender_id': event.sender_id,
        #'respond': event.respond,
        #'forward_to': event.forward_to,
        # Puedes agregar más campos según sea necesario
    }
    return event_dict

# Definir una función para convertir un diccionario en un objeto Event
def dict_to_event(event_dict):
    event_type = getattr(events, event_dict['type'])
    event = event_type()
    event.message = event_dict['message']
    #event.chat_id = event_dict['chat_id']
    #event.sender_id = event_dict['sender_id']
    #event.respond = event_dict['respond']
    #event.forward_to = event_dict['forward_to']
    # Puedes agregar más campos según sea necesario
    return event


async def init_dates():
    #return 0
    global first_init
    global user_dates
    
    if first_init:
        try:
            await download_db()
            #await upload_db()
            first_init=False
            user_dates=txt_to_dict('db/data')
            print(user_dates)
            print('Datos iniciados con exito')

        except Exception as e:
            print(e)
            

async def download_db():
    
    global on_saving
    if not on_saving:
        on_saving=True
        user = TelegramClient(str("admin"), api_id, api_hash)
        
        while True:
            try:
                await user.connect()
                break
            except Exception as e:
                print(e)
                try:
                    await user.disconnect()
                except:
                    print('error disconect')
                await asyncio.sleep(3)
                
        print("yes")      
        messages =await user.get_messages(-1002000640381, filter=InputMessagesFilterDocument, limit=10)

            # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
        for message in messages:
                if message.media:
                    file_path = await user.download_media(message.media,file='db/data')
        user.disconnect()  
        on_saving=False 
   
async def upload_db():
    #return 0
    global on_saving
    if not on_saving:
        on_saving=True 
        print("Uploading..")
        dict_to_txt(user_dates,'db/data')
        user = TelegramClient(str("admin"), api_id, api_hash)
        
        while True:
            try:
                await user.connect()
                break
            except Exception as e:
                print(e)
                try:
                    await user.disconnect()
                except:
                    print('error disconect in upload')
                await asyncio.sleep(3)
        while True:
            try:
                messages =await user.get_messages(-1002000640381, filter=InputMessagesFilterDocument, limit=10)
            # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
                for message in messages:
                    print(message.id)
                    await user.delete_messages(-1002000640381,[message.id])
                    
                await user.send_file(-1002000640381,'db/data', caption=f'saved: {str(time.time())}') 
                break
            except Exception as e:
                print("Datbase no guardada")
                print(e)

        user.disconnect() 
        on_saving=False
    
     
async def login_(event,password="not_set"):
    # Solicitar número de teléfono
    global user_dates
    sender = await event.get_sender()
    phone=user_dates[str(sender.id)]['phone']
    user_id=str(sender.id)
    phone_code_hash_= user_dates[str(sender.id)]['phone_code_hash']
    code=user_dates[str(sender.id)]['code']
    if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
            
    lg=user_dates[user_id]['leng']
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    try:
        await user.connect()
    except:
        await user.disconnect()
        await asyncio.sleep(1)
        await user.connect()
        
    chat = await event.get_chat()
    
    message = event.raw_text

 

    
    # Iniciar sesión con el número de teléfono y el código
    if password=="not_set":
        try:
            

            await user.sign_in(phone,code=code,phone_code_hash=phone_code_hash_.phone_code_hash)
                
        except telethon.errors.SessionPasswordNeededError:
            info='‼️La verificación en dos pasos está habilitada y se requiere una contraseña.Agreguela de la siguiente manera:\n\n• <b>Ejemplo</b>:\n\nSu contraseña es <b>123456</b>, luego ingrese <b>mypass123456</b>\n\n🧩 Por favor, introduzca su contraseña:'
            await event.respond(translate(info,lg),parse_mode='html')
            await user.disconnect()
            return 1
                    
            
                #await user.sign_in(phone, code)
                #await user.sign_in(phone,password='20050830')
        
    else:
        
        try:
                    
            await user.sign_in(password=password)
                    
        except Exception as e:
            print(e)
                    
                    
            await user.disconnect()
            return 2
        
    keyboard = await get_custom_menu(event)
    keyboard=keyboard[0]
    info="🐾 ¡Conexión Establecida con Éxito!\n\n🤜🤛 Gracias por elegir @Camariobot, ahora todos nuestros servicios están disponibles para usted!\n\n👣 Para comenzar a configurar su primera tarea de reenvío siga los siguientes pasos:\n \n#Paso1 - Debes agregar un canal el cual se utilizará para reenviar todas la publiciones a todos sus grupos agregados.\n\n• <b>/AgregarCanal</b><b>\n\n</b>#Paso2 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado.\n\n• <b>/AgregarGrupos</b><b>\n\n</b>⚙️ Para cualquier consulta, no dude en contactar con @CamarioAdmin\n\n🦎 Manténgase Informado con las últimas actualizaciones @Camario"
    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')
    await user.disconnect()
    return 0


def tree_ref(id):
    global user_dates
    lvl1=[]
    saldo=0
    for id_ in user_dates:
        if id_!='all_hashes' and id_!="chat_ids":
            if 'saldo' not in user_dates[id_]:
                user_dates[id_]['saldo']=0
            
            if'invitator' not in user_dates[id_]:
                user_dates[id_]['invitator']="None"
                
            invitator=user_dates[id_]['invitator']

            
            if id==invitator:
                saldo+=user_dates[id_]['saldo']
                lvl1.append(id_)
            
    return [lvl1,round(saldo*0.25,4)]

           

def deposit_check_(user_address,admin_address):
    if 'all_hashes' not in user_dates:
        user_dates['all_hashes']=[]
    user_address = "your_user_address"
    admin_address = "your_admin_address"

    response = requests.get(f"https://apilist.tronscanapi.com/api/new/token_trc20/transfers?limit=100&start=0&fromAddress={user_address}&toAddress={admin_address}")
    data = json.loads(response.text)

    transactions = data['token_transfers']
    total_amount=0
    for transact in transactions:
        hash = transact['transaction_id']
        to = transact['to_address']
        from_ = transact['from_address']
        token_name = transact['tokenInfo']['tokenAbbr']
        result = transact['finalResult']
        confirmed = transact['confirmed']
        timestamp = transact['block_ts']
        decimals = transact['tokenInfo']['tokenDecimal']
        amount = float(transact['quant']) / 10**decimals
        if (hash not in user_dates['all_hashes' ]) and (result == 'SUCCESS') and (confirmed):
            total_amount+=amount*get_price(token_name)
        
        
    return round(total_amount,4)
        
  
async def deposit_check():
    bot_ =await TelegramClient('bot_dep', api_id, api_hash).start(bot_token=bot_token)
    while True:
            print('-')
        
        #try:
            for id_ in user_dates:
                if id_!='all_hashes' and id_!="chat_ids":
                    if 'invoice_id' in user_dates[id_] and user_dates[id_]['invoice_id']!="None":
                        actual_time=time.time()
                        
                        if 'invitator' not in user_dates[id_]:
                            user_dates[id_]['invitator']="None"
                                                         
                        if 'saldo' not in user_dates[id_]:
                                user_dates[id_]['saldo']=0
                        if 'status' not in user_dates[id_]:
                            user_dates[id_]['status']={} 
                            user_dates[id_]['status']['cat']='basic'    
                            user_dates[id_]['status']['lote']=0
                            user_dates[id_]['status']['buyed']=0
                            
                        if 'leng' not in user_dates[id_]:
                            user_dates[id_]['leng']='spanish'
                        lg=user_dates[id_]['leng']
                        if actual_time>=user_dates[id_]['status']['lote']+user_dates[id_]['status']['buyed']:
                            
                            if user_dates[id_]['status']['cat']!='basic':  
                                if user_dates[id_]['status']['cat']=='trial': 
                                    msg='💠 Su servicio gratis ha concluido, el precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛'
                                    user_dates[id_]['status']['cat_historial']=['trial']
                                    keyboard_inline = [Button.inline(translate('👛 Pagar',lg), data=b'buy_premium1')]
                                    await bot_.send_message(int(id_), translate(msg,lg),butons=keyboard_inline,parse_mode='html')   
                                user_dates[id_]['status']['lote']=0
                                user_dates[id_]['status']['buyed']=0
                                user_dates[id_]['status']['cat']='basic'  
                                
                              
                        id=user_dates[id_]['invoice_id']
                        verify_resp=verificar_pago(int(id),test_mode)
                        if verify_resp:
                            if len(verify_resp['result']['items'])>0:
                                factura_status=verify_resp['result']['items'][0]['status']

                                if factura_status=='paid':
                                    payed_usd=verify_resp['result']['items'][0]['amount']
                                    fee_usd=verify_resp['result']['items'][0]['fee_in_usd']
                                    cripto_payed=verify_resp['result']['items'][0]['paid_asset']
                                    print(f"----------PAYED-------------\nReal_recived={payed_usd}USD\nFee:{fee_usd}\nCripto:{cripto_payed}")
                                    user_dates[id_]['saldo']+=float(payed_usd)
                                    if user_dates[id_]['invitator']!="None":
                                        if 'saldo' not in user_dates[str(user_dates[id_]['invitator'])]:
                                            user_dates[str(user_dates[id_]['invitator'])]['saldo']=0
                                            
                                        user_dates[str(user_dates[id_]['invitator'])]['saldo']+=float(payed_usd)*0.25
                                    
            
                                    user_dates[id_]['invoice_id']="None"
                                   
                                    user_dates[id_]['status']['cat']='premium' 
                                    print(round(float(payed_usd)))
                                    if int(payed_usd)==5:
                                        
                                        user_dates[id_]['status']['lote']+=60*60*24*30
                                        if  user_dates[id_]['status']['buyed']==0:
                                                user_dates[id_]['status']['buyed']=time.time()
                                        
                                    if int(payed_usd)==9:
                                        user_dates[id_]['status']['lote']+=60*60*24*60
                                        if  user_dates[id_]['status']['buyed']==0:
                                                user_dates[id_]['status']['buyed']=time.time()
                                        
                                    if int(payed_usd)==12:
                                        user_dates[id_]['status']['lote']+=60*60*24*90
                                        if  user_dates[id_]['status']['buyed']==0:
                                            user_dates[id_]['status']['buyed']=time.time()

                                    fecha = datetime.fromtimestamp(user_dates[id_]['status']['buyed']+user_dates[id_]['status']['lote'])


                                    fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                                    if  user_dates[id_]['status']['lote']==0:
                                        fecha_formateada="No premium activo"
                                        
                                     
                                    msg=f"----------PAYED-------------\nReal_recived={payed_usd}USD\nFee:{fee_usd}\nCripto:{cripto_payed}\nStatus: {user_dates[id_]['status']['cat']} \nVencimiento del premium: {fecha_formateada}"
                                    
                                    await bot_.send_message(int(id_), translate(msg,lg),parse_mode='html')
                                    await upload_db()
                                else:
                                    print("No pay")
                            else:
                                print('Error')
                            
      
                        
                        
        #except Exception as e:
        #    print(e)
                   
            time.sleep(10)
        
async def deposit_solicity(event,amount):
    global user_dates
    sender = await event.get_sender()
    user_id=str(sender.id)
    if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
            
    lg=user_dates[user_id]['leng']
    '''
    if 'invoice_id' in user_dates[user_id] and user_dates[user_id]['invoice_id']!="None":
        id=user_dates[user_id]['invoice_id']
        verify_resp=verificar_pago(id,test_mode)
        
        pay_url=verify_resp['result']['items'][0]['bot_invoice_url']


        await event.respond(f'Realizar pago de: {amount} USD ', buttons=[(Button.url('🦎 Pagar Factura', pay_url))],parse_mode='html')         
                            
'''
                        
    #else:
        
    create_dates=crear_factura(amount,test_mode)
    id=create_dates['invoice_id']
    pay_url=create_dates['bot_invoice_url']
    user_dates[user_id]['invoice_id']=id
    await event.respond(translate(f'Realizar pago de: {amount} USD ',lg), buttons=[(Button.url(translate('🦎 Pagar Factura',lg), pay_url))],parse_mode='html')
    await upload_db() 
    

def get_price(cripto):
    while True:
        try:
            response = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={cripto}&tsyms=USD")
            data = json.loads(response.text)
            
            data1 = data['DISPLAY'][cripto]['USD']
            PRICE = data1['PRICE']
            HIGHDAY = data1['HIGHDAY']
            LOWDAY = data1['LOWDAY']
            CHANGEPCT24HOUR = data1['CHANGEPCT24HOUR']
            LASTUPDATE = data1['LASTUPDATE']
            return PRICE
            break

        except Exception as e:
            print(e)

async def select_lenguage(event):
    sender = await event.get_sender()
    user_id=str(sender.id)   
    if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
            
    lg=user_dates[user_id]['leng']
    keyboard = [[Button.inline('🇷🇺 Русский', data=b'lg_ru'),Button.inline('🇺🇸 English', data=b'lg_en')],[Button.inline('🇪🇸 Español', data=b'lg_es'),Button.inline('🇨🇳 中国人o', data=b'lg_chi')],[Button.inline('🇦🇪 عربي', data=b'lg_ar')]]
    await event.respond(translate('Seleccione un idioma',lg),buttons=keyboard ,parse_mode='html')


async def check_subscription(user_id,channel_id):
    client_ = TelegramClient('admin_check', api_id, api_hash)
    while True:
            try:
                await client_.connect()
                break
            except Exception as e:
                print(e)
                try:
                    await client_.disconnect()
                except:
                    print('error disconect in upload')
                await asyncio.sleep(3)
    
    async with client_:
        channel = await client_.get_entity(channel_id)
        user = await client_.get_entity(user_id)
        
        try:
            participant = await client_(GetParticipantRequest(channel=channel, participant=user))
            print("El usuario está suscrito al canal.")
            return True
        except UserNotParticipantError:
            print("El usuario no está suscrito al canal.")
            return False

#Comands
@bot.on(events.NewMessage(pattern='/premium'))
async def premiunm_admin(event):
    
    info="Panel de administracion\n\n"
    for user_id in user_dates:
        if user_id!='all_hashes' and user_id!="chat_ids":
            
            user_data=user_dates[user_id]
            if 'beginner' not in user_dates[user_id]:
                user_dates[user_id]['beginner']=True
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            info+=f'{user_id} status actual: {user_dates[user_id]["status"]["cat"]} subir_status: /upstatus_{user_id} bajar_status: /downstatus_{user_id} :\n\n'   
            
    await event.respond(info,parse_mode='html')
    
@bot.on(events.NewMessage(pattern='/upstatus_'))
async def test_on(event):
        message = event.raw_text


            
        if len(message.split('_'))==2:
            user_id=str(message.split('_')[1])
            if user_dates[user_id]['status']['cat']=='basic':
                user_dates[user_id]['status']['cat']='trial'
                info=f"{user_id} Ascendido a trial"
                await event.respond(info,parse_mode='html')
            elif user_dates[user_id]['status']['cat']=='trial':
                user_dates[user_id]['status']['cat']='premium'
                info=f"{user_id} Ascendido a premium"
                await event.respond(info,parse_mode='html')
            
            
            

            
@bot.on(events.NewMessage(pattern='/downstatus_'))
async def test_on(event):
    
        message = event.raw_text


            
        if len(message.split('_'))==2:
            user_id=str(message.split('_')[1])
            if user_dates[user_id]['status']['cat']=='trial':
                user_dates[user_id]['status']['cat']='basic'
                info=f"{user_id} Degradado a basic"
                await event.respond(info,parse_mode='html')
            elif user_dates[user_id]['status']['cat']=='premium':
                user_dates[user_id]['status']['cat']='trial'
                info=f"{user_id} Degradado a trial"
                await event.respond(info,parse_mode='html')
    
    

@bot.on(events.NewMessage(pattern='/test_on'))
async def test_on(event):
    global test_mode
    test_mode=True
    await event.respond('Test Mode activado',parse_mode='html')
@bot.on(events.NewMessage(pattern='/test_off'))
async def test_on(event):
    global test_mode
    test_mode=False
    await event.respond('Test Mode desactivado',parse_mode='html')
    
@bot.on(events.NewMessage(pattern='/leng'))
async def test_on(event):

    await select_lenguage(event)
    

    

@bot.on(events.NewMessage(pattern='/start'))
async def start(event,beginner=False):
    
   

    global user_dates
    
    # Crear un "InlineKeyboardButton" para el "Online Button"
    online_button = types.KeyboardButtonCallback(text='Online', data=b'online')

# Crear un "KeyboardButton" para el "Keyboard Button"
    keyboard_button = telegram.KeyboardButton(text='Keyboard Button')
    
    
    
# Crear un teclado con los botones
    #keyboard = types.ReplyKeyboardMarkup([Button.text('Mi Botón')], resize=True,persistent=True)
    keyboard = [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('💠 Conectar Canal',resize=True),Button.text('〽️ Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]]
    chat = await event.get_chat()
    sender = await event.get_sender()
    id_=str(sender.id)
    
    #print(message)
    chat_username = chat.username
    print(f"Nuevo mensaje de {sender.id} en el chat {chat.id}")
    #print(f"Mensaje: {message}")

    

    if str(sender.id) not in user_dates:
        
            message = event.raw_text


            user_dates[str(sender.id)]={}
            user_dates[str(sender.id)]['saldo']=0
            user_dates[str(sender.id)]['register_date']=time.time()
            
            if len(message.split(' '))==2:
                user_dates[str(sender.id)]['invitator']=str(message.split(' ')[1])
                
            else:
                user_dates[str(sender.id)]['invitator']="None"
            
            user_dates[str(sender.id)]['beginner']=True
            user_dates[str(sender.id)]['beginner_trial']=True

            await upload_db()       
            await select_lenguage(event)

           
    else :  
    
            if 'beginner' not in user_dates[str(sender.id)]:
                user_dates[str(sender.id)]['beginner']=True
                
            if user_dates[str(sender.id)]['beginner']:

                await select_lenguage(event)
                return 0
            keyboard = [[Button.text(translate('🧩 Conectar Cuenta',user_dates[str(sender.id)]['leng']),resize=True)],[Button.text(translate('💠 Conectar Canal',user_dates[str(sender.id)]['leng']),resize=True),Button.text(translate('〽️ Agregar Grupos',user_dates[str(sender.id)]['leng']),resize=True)],[Button.text(translate('⚙️ Configuración',user_dates[str(sender.id)]['leng']),resize=True)]]
            if beginner:
                
                keyboard_inline = [Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan'),Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]
                #await event.respond(translate('💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛\n\nPrueba Gratis ✖️ 5 Días 🎉',user_dates[str(sender.id)]['leng']), buttons=keyboard_inline,parse_mode='html')
                await event.respond(translate('🤜🤛 Gracias por elegir @Camariobot!\n\n👣 Para comenzar a configurar su cuenta siga los siguientes pasos:\n\n#Paso1 - El primero de 3 simplemente pasos a seguir será conectar su cuenta de Telegram con nuestro bot!\n\n• /ConectarCuenta\n\n#Paso2 - Debes agregar un canal el cual se utilizará para reenviar todas la publicaciones a todos los grupos agregados!\n\n• /AgregarCanal\n\n#Paso3 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado!\n\n• /AgregarGrupos',user_dates[str(sender.id)]['leng']), buttons=keyboard,parse_mode='html')
            else:
                await event.respond(translate('Bienvenido',user_dates[str(sender.id)]['leng']), buttons=keyboard,parse_mode='html')
    #keyboard_inline = [Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan'),Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]     
    #await event.respond("a",buttons=keyboard_inline)
            
    #await event.respond('• Manténgase Actualizado:', buttons=[(Button.url('🦎 Camario', 'http://t.me/Camario'))],parse_mode='html')
    
    await upload_db()
@bot.on(events.NewMessage(pattern='/db'))
async def down(event):
    
    await download_db()
    await upload_db()
    


@bot.on(events.NewMessage(pattern='/connect'))
async def send_code(event):
    # Solicitar número de teléfono
    global user_dates
    
    sender = await event.get_sender()
    user_id=str(sender.id)
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
    try:
        await user.connect()
    except:
        await user.disconnect()
        await asyncio.sleep(1)
        await user.connect()
        
    chat = await event.get_chat()
    
    message = event.raw_text
    comand=message.split(' ')
    if len(message.split(' '))==2:
        
        phone=comand[1]
        try:
            numero = int(phone)  # Intentar convertir a entero
        except ValueError:
            info='🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555'
            await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
            return 'not_number'
 
        phone_code_hash_=await user.send_code_request(phone)
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['phone']=phone
        user_dates[str(sender.id)]['phone_code_hash']=phone_code_hash_

        info='📨 Ingrese el código de inicio de sesión enviado a la aplicación Telegram o SMS (<b>Sin espacios</b>)\n\n• <b>Ejemplo</b>:\n\nSu código de inicio de sesión es <b>123456</b>, luego ingrese <b>mycode123456</b>\n\n🧩 Por favor, introduzca el código resivido:'
        await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
    else:
        info='🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555'
        await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
        
    
    await user.disconnect()
    
@bot.on(events.NewMessage(pattern='/delgroup'))
async def delgroup(event):
    # Solicitar número de teléfono
    global user_dates
    sender = await event.get_sender()
    user_id=str(sender.id)
    message = event.raw_text
    comand=message.split('_')
    if len(comand)==2:
        comand.pop(0)
        if "-" not in comand:
                comand="-"+str(comand[0])
                
        if 'group_ids' not in user_dates[str(sender.id)] :
           return 'no_dates'
        if int(comand) in user_dates[str(sender.id)]['group_ids']:
            user_dates[str(sender.id)]['group_ids'].remove(int(comand))
            id_chat=sender.id
            id_msg= user_dates[str(sender.id)]['edit_groups_msg_id']
            user = TelegramClient(str(sender.id), api_id, api_hash)
            
            try:
                    await user.connect()
            except:
                    await user.disconnect()
                    await asyncio.sleep(1)
                    await user.connect()
            
            
            groups=""
            if len(user_dates[str(sender.id)]['group_ids'])==0:
                groups="No tiene grupos"
                
            for group_id in user_dates[str(sender.id)]['group_ids']:
                    chat_entity = await user.get_entity(int(group_id))
                    try:
                        username_=chat_entity.username
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
                    except:
                        username_=""
                    
                    groups+=f"/delgroup_{str(group_id).replace('-','')}  Eliminar: <a href='https://t.me/{username_}'>{chat_entity.title}</a>\n"
                  
                    
            await user.disconnect()

            msg=translate(groups ,user_dates[user_id]['leng'])
            await bot.edit_message(id_chat,id_msg,msg,parse_mode='html')
            await upload_db()
        else:
            return 'no_dates'
          
                
        
        
        
    
@bot.on(events.NewMessage(pattern='/get_groups'))
async def get_groups(event):
    # Solicitar número de teléfono
    global user_dates
    
    sender = await event.get_sender()
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    user_id=str(sender.id)
    try:
        await user.connect()
    except:
        await user.disconnect()
        await asyncio.sleep(1)
        await user.connect()
    
    chats = await user.get_dialogs()
    info=f"{translate('Grupos',user_dates[user_id]['leng'])}:\n"
    


    for chat in chats:
        if chat.is_group:
            chanel_entity = await user.get_entity(int(chat.id))
            try:
                username_=chanel_entity.username
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
            except:
                username_=""
            print(chat.id)
            info+=f"<code>{str(chat.id)}</code> <a href='https://t.me/{username_}'>{chat.title}</a>\n"
            print(f'ID del grupo: {chat.id}, Nombre del grupo: {chat.title}')
            
    keyboard = [Button.inline(translate('🗑️ Eliminar Mensaje',user_dates[user_id]['leng']), data=b'del_groups_msg')]    
    msg_send=await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
    msg_id=msg_send.id
    if str(sender.id) not in user_dates:
        user_dates[str(sender.id)]={}
    user_dates[str(sender.id)]['groups_msg_id']=msg_id
    message = event.raw_text
    
      
    await user.disconnect()



@bot.on(events.NewMessage(pattern='/login'))
async def login(event):
    # Solicitar número de teléfono
    global phone_code_hash_
    sender = await event.get_sender()
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
    try:
        await user.connect()
    except:
        await user.disconnect()
        await asyncio.sleep(1)
        await user.connect()
    chat = await event.get_chat()
    
    message = event.raw_text
    comand=message.split('_')
    if comand[0]=='/login':
        
        phone=comand[1]
        code=comand[2]
        password=""
        if len(comand)==4:
            password=comand[3]
    

    
    # Iniciar sesión con el número de teléfono y el código
        try:

            await user.sign_in(phone,code=code,phone_code_hash=phone_code_hash_.phone_code_hash)
        except telethon.errors.SessionPasswordNeededError:
            try:
                await user.sign_in(password=password)
            except:
                await event.respond('‼️La verificación en dos pasos está habilitada y se requiere una contraseña.Agreguela de la siguiente manera:\n\n• <b>Ejemplo</b>:\n\nSu contraseña es <b>123456</b>, luego ingrese <b>mypass123456</b>\n\n🧩 Por favor, introduzca su contraseña:',parse_mode='html')
                
                
           
            #await user.sign_in(phone, code)
            #await user.sign_in(phone,password='20050830')
        await event.respond('logeado')
        
    await user.disconnect()
  
  
@bot.on(events.NewMessage(pattern='/id '))
async def add_chat(event):


    chat = await event.get_chat()
    sender = await event.get_sender()
    user_id=str(sender.id)
    message = event.raw_text
    comand=message.split(' ')
    if len(comand)>1:
        comand.pop(0)
        msg='〽️ <b>Grupos Agregados</b>!\n\n• Sus grupos:\n\n'
        for id_chat in comand:
            if "-" not in id_chat:
                id_chat="-"+str(id_chat)
            if 'group_ids' not in user_dates[str(sender.id)]:
               user_dates[str(sender.id)]['group_ids']=[int(id_chat)]
            else:
                user_dates[str(sender.id)]['group_ids'].append(int(id_chat))
            
            msg+=id_chat
            msg+='\n\n'
        msg+='✏️ <b>Puedes editar</b>, <b>agregar</b> <b>o</b> <b>eliminar grupos desde</b>:\n\n• /EditarGrupos'
        keyboard=menu_system[0]
        
        await event.respond(translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        await upload_db()

    
@bot.on(events.NewMessage(pattern='/channel '))
async def add_channel(event):
    #await get_custom_menu(event)
    # Solicitar número de teléfono
    #print (chat_ids)
    #print(channel_ids)
    chat = await event.get_chat()
    sender = await event.get_sender()
    message = event.raw_text
    user_id=str(sender.id)
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    while True:
        try:
            await user.connect()
            break
        except Exception as e:
            print(e)
            try:
                await user.disconnect()
            except:
                print('error disconect')
            
            
    
    comand=message.split(' ')
    if len(comand)==2:
        comand.pop(0)
        msg='💠 <b>Canal Conectado</b>!\n\n• Su canal '
        for id_channel in comand:
            if "-" not in id_channel:
                id_channel="-"+str(id_channel)
            user_dates['chat_ids'].append(int(id_channel))
            if 'channel_ids' not in user_dates[str(sender.id)]:
               user_dates[str(sender.id)]['channel_ids']=[]
            
            if sender.id not in admins:
                if len(user_dates[str(sender.id)]['channel_ids'])>0:
                    chanel_entity = await user.get_entity(int(user_dates[str(sender.id)]['channel_ids'][0]))
                    if sender.id not in channel_ids_swap:
                        channel_ids_swap[sender.id]=[]
                    if len(channel_ids_swap[sender.id])==0:
                        channel_ids_swap[sender.id].append(1)
                        
                    channel_ids_swap[sender.id].pop(0)
                    channel_ids_swap[sender.id].append(int(id_channel))
                    
                    keyboard = [Button.inline(translate('〽️ Si',user_dates[user_id]['leng']) ,data=b'yes_swap_channel'),Button.inline(translate('🚫 No',user_dates[user_id]['leng']), data=b'no_swap_channel')]
                    info=f'〽️ Usted ya configuro un canal de reenvío anteriormente!\n\n• <b>Su canal</b> - <a href="https://t.me/{chanel_entity.username}">{user_dates[str(sender.id)]["channel_ids"][0]}</a>\n\n⁉️ Deseas eliminar esté canal y configurar otro:'
                    await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
                    await user.disconnect() 
                    await upload_db() 
                    return 'not admin'
                else:
                    user_dates[str(sender.id)]['channel_ids'].append(int(id_channel))
                    
                    
            else:
                user_dates[str(sender.id)]['channel_ids'].append(int(id_channel))
                
            

            
            msg+=id_channel
            msg+="\n"
        keyboard=await get_custom_menu(event)
        keyboard=keyboard[0]
        await user.disconnect() 
        await upload_db() 
        await event.respond(translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        
     
@bot.on(events.NewMessage(pattern='/time'))
async def time_(event):
    sender = await event.get_sender()
    user_id=str(sender.id)
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    if len(comand)==2:
        time=int(comand[1])
    
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
            
            
        user_dates[str(sender.id)]['sleep_time']=time
        
        await upload_db()
        info=f'Tiempo de reenvio modiificado a {time} seg entre cada menaje'
        await event.respond(translate(info,user_dates[user_id]['leng']))
        
@bot.on(events.NewMessage(pattern='/ree'))
async def resend_time_(event):
    sender = await event.get_sender()
    user_id=str(sender.id)
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    keyboard=await get_custom_menu(event)
    keyboard=keyboard[1]
    if len(comand)==2:
        time_=int(comand[1])*60
    
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
            
        if time_/60>=30 or time_==0 or time_/60==1:   
            user_dates[str(sender.id)]['resend_loop']=time_
            await upload_db()
            info=f'⏱️ <b>Tiempo de reenvío automático modificado a</b> {time_/60} <b>Minutos</b>!'
            await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        else:
            info='🚫 <b>El tiempo mínimo de reenvío es</b> 30 <b>Minutos</b>!\n\n• Debes enviar un tiempo igual o mayor que 30 Minutos!\n\n💡 <b>Su tiempo es</b> 60 <b>minutos usted enviará</b>:\n\n/ree 60'
            await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        
@bot.on(events.NewMessage(pattern='/wait'))
async def wait(event):
    sender = await event.get_sender()
    user_id=str(sender.id)
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    if len(comand)==2:
        w_time=int(comand[1])
    
        if sender.id not in user_dates:
            
            user_dates[str(sender.id)]={}
            
        await upload_db()   
        user_dates[str(sender.id)]['wait_time']=w_time
        keyboard=await get_custom_menu(event)
        keyboard=keyboard[1]
        info=f'Tiempo de retraso reenvio modiificado a {w_time} seg entre cada menaje'
        await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')



@bot.on(events.NewMessage(pattern='/send_anounce'))
async def send_anounce_(event):
    global user_dates
    
   
    sender = await event.get_sender()
    user_id=str(sender.id)
    user = TelegramClient(str(sender.id), api_id, api_hash)
    try:
        await user.connect()
    except:
        await user.disconnect()
        await asyncio.sleep(1)
        await user.connect()
    chat = await event.get_chat()
    if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
    if 'sleep_time' not in user_dates[str(sender.id)]:
        user_dates[str(sender.id)]['sleep_time']=1
        
    sleep_time= user_dates[str(sender.id)]['sleep_time']
    message = event.raw_text
    comand=message.split('->')
    if len(comand)==2:
        msg=comand[1]
    

    
        if 'group_ids' not in  user_dates[str(sender.id)]:
            await event.respond('No tiene chats agregados') 
        # Enviar un mensaje como usuario
        else:
            for group_id in user_dates[str(sender.id)]['group_ids']:
                try:
                    
                    await user.send_message(group_id, msg)
                    await asyncio.sleep(sleep_time)
                except Exception as e:
                    print(e)
            
            await event.respond('Mensajes reenviados.')
    user.disconnect()
        
    



#Controlador de mensajes entrantes en el canal
@bot.on(events.NewMessage())
async def handle_channels_new_message(event):
    global user_dates
    chat_id = event.chat_id
    sender = await event.get_sender()
    user_id=str(sender.id)
    print(sender.id)
    
    user_id=str(sender.id)
    is_configured=False


    if chat_id in user_dates['chat_ids']:
        
        print(f"Nuevo mensaje en el canal ._. {event.chat.title}: {event.text}")


        print(chat_id)
        print(f"Nuevo mensaje en el canal {event.chat.title}: {event.text}")
        for key in user_dates:
            if 'channel_ids' in user_dates[key]:
                if chat_id in user_dates[key]['channel_ids']:
                    is_configured=True
                    user_id=key
                    if user_id not in user_dates:
                
                        user_dates[user_id]={}
                        
                    if 'pending_messages' not in user_dates[user_id]:
                
                       user_dates[user_id]['pending_messages']=[]

        #user = TelegramClient(str(user_id), api_id, api_hash)
        
        if is_configured:
            if 'sleep_time' not in user_dates[user_id]:
                user_dates[user_id]['sleep_time']=1
            
            sleep_time= user_dates[user_id]['sleep_time']
        
            if 'wait_time' not in user_dates[user_id]:
                user_dates[user_id]['wait_time']=1
            
            wait_time= user_dates[user_id]['wait_time']
            
            
            #await user.connect()
            chat = await event.get_chat()
        
            msg = event.raw_text
            
            # Enviar un mensaje como usuario
            if 'group_ids' not in  user_dates[user_id]:
                info='No tiene chats agregados'
                await event.respond(translate(info ,user_dates[user_id]['leng']) )
            else:
                
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
                date_in={'time':timestamp,'msg':msg,'event':event.message}
                global state
                state=False
                await asyncio.sleep(3)
                user_dates[user_id]['pending_messages'].append(date_in)
                await upload_db()
                await asyncio.sleep(1)
                state=True
            
                
                
                #for group_id in group_ids[user_id]:
                    
                #    try:
                #        await user.forward_messages(int(group_id),event.message)
                        #await user.send_message(int(group_id), msg)
                #        await asyncio.sleep(sleep_time)
                #   except Exception as e:
                #        print(e)
                if 'notifications' not in user_dates[user_id]:
                    user_dates[user_id]['notifications']=True
                info="Mensaje agregado"
                if  user_dates[user_id]['notifications']:
                    await bot.send_message(int(user_id),translate(info ,user_dates[user_id]['leng']))
                
            #user.disconnect()
    else:
        print("Mensaje de un canal no registrado. ._.")
        

async def send_anounce(event):
            global user_dates
            chat_id = event.chat_id
            sender = await event.get_sender()
            user_id=str(sender.id)
            print(sender.id)
    
            user_id=str(sender.id)
            if 'sleep_time' not in user_dates[user_id]:
                user_dates[user_id]['sleep_time']=1
            
            sleep_time= user_dates[user_id]['sleep_time']
        
            if 'wait_time' not in user_dates[user_id]:
                user_dates[user_id]['wait_time']=1
            
            wait_time= user_dates[user_id]['wait_time']
            
            
            #await user.connect()
            chat = await event.get_chat()
        
            msg = event.raw_text
            
            # Enviar un mensaje como usuario
            if 'group_ids' not in  user_dates[user_id]:
                info='No tiene chats agregados'
                await event.respond(translate(info ,user_dates[user_id]['leng']) )
            else:
                
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
                date_in={'time':timestamp,'msg':msg,'event':'not_remitent'}
                global state
                state=False
                await asyncio.sleep(3)
                user_dates[user_id]['pending_messages'].append(date_in)
                await upload_db()
                await asyncio.sleep(1)
                state=True
            
                
                
                #for group_id in group_ids[user_id]:
                    
                #    try:
                #        await user.forward_messages(int(group_id),event.message)
                        #await user.send_message(int(group_id), msg)
                #        await asyncio.sleep(sleep_time)
                #   except Exception as e:
                #        print(e)
                if 'notifications' not in user_dates[user_id]:
                    user_dates[user_id]['notifications']=True
                info="Mensaje agregado"
                if  user_dates[user_id]['notifications']:
                    await bot.send_message(int(user_id),translate(info ,user_dates[user_id]['leng']))   

    
#Controlador de mensajes entrantes    
@bot.on(events.NewMessage())
@private_message_handler
async def handler(event):
    global first_init
    sender = await event.get_sender()
    user_id=str(sender.id)
    await init_dates()
    
    if "-" not in str(sender.id):
        
        global user_dates
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
        if 'beginner' not in user_dates[user_id]:
            user_dates[user_id]['beginner']=True
        if 'status' not in user_dates[user_id]:
            user_dates[user_id]['status']={} 
            user_dates[user_id]['status']['cat']='basic'    
            user_dates[user_id]['status']['lote']=0
            user_dates[user_id]['status']['buyed']=0
            
        if 'saldo' not in user_dates[str(sender.id)]:
            user_dates[str(sender.id)]['saldo']=0
        
        if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
        if 'historial' not in user_dates[user_id]:
            user_dates[user_id]['historial']=[]
        lg=user_dates[user_id]['leng']
            
        # Este bloque de código se ejecutará cada vez que llegue un nuevo mensaje
        chat = await event.get_chat()
    
        message = event.raw_text
        
        #user = TelegramClient(str(sender.id), api_id, api_hash)
        #await user.connect()
        if message in traduct_menu["👛 Suscripción"] or message=='/Suscripcion':
                keyboard = [[Button.inline(translate('🔘 1 Mes - $5',lg), data=b'buy_premium1')],[Button.inline(translate('🔰  2 Meses - $9',lg), data=b'buy_premium2'),Button.inline(translate('🧩 3 Meses - $12',lg), data=b'buy_premium3')]] 
                info="👛 Elige un período de suscripción:"
                await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')  
                return 0
        if user_dates[user_id]['status']['cat']!='basic' or user_id in admins or user_dates[user_id]['beginner']: 
            if user_dates[user_id]['beginner']:
                keyboard_inline = [Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan'),Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]
               
                await event.respond(translate('#💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛\n\nPrueba Gratis ✖️ 5 Días 🎉',user_dates[str(sender.id)]['leng']), buttons=keyboard_inline,parse_mode='html')
                return 0
            if message in traduct_menu['🧩 Conectar Cuenta'] or message=='/ConectarCuenta':
                user = TelegramClient(str(sender.id), api_id, api_hash)
                try:
                    await user.connect()
                except:
                    await user.disconnect()
                    await asyncio.sleep(1)
                    await user.connect()
                if sender.id not in menu_history:
                    menu_history[sender.id]=[message]
                else:
                    menu_history[sender.id].append(message)
                    
                    
                if await user.is_user_authorized():
                    keyboard = [Button.inline(translate('🧩 Conectar Cuenta',lg), data=b'connect')]
                    
                    info="🧩 Su cuenta actualmente está conectada con @Camariobot!"
                    
                    await event.respond(translate(info,lg),parse_mode='html',link_preview=False)
                    
                    
                else:
                    keyboard = [Button.inline(translate('🧩 Conectar Cuenta',lg), data=b'connect')]
                    info='🧩 <b>Menú de Conectividad</b>:\n\n• Utilice esto para forjar una conexión entre su cuenta y @CamarioBot.\n\n• Una conexión con al menos una cuenta es esencial para utilizar los servicios.\n\n• Ingrese el número de teléfono asociado a la cuenta de Telegram, incluya el prefijo de país, elimine el espacio entre el prefijo y el número.\n\n💡 <b>Parámetros de Conexión</b>:\n\n<code>/connect</code> (Número de teléfono completo sin espacios)\n\n• <b>Ejemplo</b>: su número es <b>+84 55555</b>, debes enviar\n\n/connect +8455555\n\n🌐 <b>Descubre el prefijo de cada país visitando este </b><b><a href="https://countrycode.org/">Enlace</a></b>\n\n• No estás seguro de cómo proceder, contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n🧩 <b>Conecte su Cuenta</b>:'
                    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html',link_preview=False)
                await user.disconnect()
        

            elif message in traduct_menu['🚫 Cancel']:
                keyboard = await menu_action('cancel',event)
                await event.respond(translate('🚫 Cancel',lg),buttons=keyboard)
            
            elif message in traduct_menu['💠 Conectar Canal'] or message=='/AgregarCanal':
                keyboard = [Button.inline(translate('〽️ Conectar Canal' ,lg),data=b'add_channel')]
                info='💠 <b>Utilice esto para forjar una conexión entre su canal y </b>@CamarioBot.\n\n• Una conexión con al menos un canal es esencial para utilizar los servicios de reenvío automático.\n\n🤖 <b>@Camariobot</b><b> deberá ser añadido como administrador en el canal configurado</b>!\n\n• Si no añade @Camariobot los servicios no funcionarán con normalidad.\n\n💡 <b>Parámetros de Conexión</b>:\n\n<code>/channel</code> (ID del Canal)\n\n• <b>Ejemplo</b>:\n\n/channel 1002065562952\n\n🔍 <b>Localice el ID de su canal utilizando </b>@ScanIDBot.\n\n• ¿No estás seguro de cómo proceder?Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n💠 <b>Conecte</b> <b>un Canal</b>:'
                await event.respond(translate(info ,lg) ,buttons=keyboard,parse_mode='html',link_preview=False)
                
            elif message in traduct_menu['〽️ Agregar Grupos'] or message=='/AgregarGrupos':  
                keyboard = [[Button.inline(translate('〽️ Agregar Grupos' ,lg),data=b'add_group')]]
                info='〽️ ¡<b>Agrega el ID de los grupos a los cuales se reenviarán las publicaciones</b>!\n\n• Deberá ser miembro de todos los grupos agregados.\n\n• No existe un límite de grupos para reenviar publicaciones.\n\n• Para editar, eliminar o agregar nuevos grupos debera dirigirse ha "⚙️Configuración".\n\n💡 <b>Parámetros de Conexión</b>:\n\n/id (ID de los grupos, separe con un espacio cada ID)\n\n• <b>Ejemplo</b>:\n\n/id 1001256118443 1001484740111\n\n• ¿No estás seguro de cómo proceder? Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n〽️ <b>Agregue los Grupos</b>:'
                await event.respond(translate(info ,lg),buttons=keyboard,parse_mode='html',link_preview=False)

            elif message in traduct_menu['⚙️ Configuración']:
                keyboard = await get_custom_menu(event)
                keyboard=keyboard[1]
                await event.respond(translate("⚙️ Configuración",lg),buttons=keyboard,parse_mode='html')
                
        
       # elif message in traduct_menu['💼 Billetera']:
       #     keyboard = [Button.inline(translate('👛 Fondos',lg), data=b'founds')]
        #    info='💷 0.00 TRX\n\n💶 0.00 USDT'
        #    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')
        #    await deposit_solicity(event,1)
        
            elif message in traduct_menu['👁️ Remitente']:
                if str(sender.id) not in user_dates:
                    user_dates[str(sender.id)]={}
                if 'remitent' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['remitent']=True
                    
                state="Off"
                if user_dates[str(sender.id)]['remitent']:
                    state="On" 
                
                    
                msg=f'📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - {state}'
                keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline(translate('🌑 Off',lg), data=b'off_remitent')]
                msg_send=await event.respond(translate(msg,lg), buttons=keyboard,parse_mode='html')
                msg_id=msg_send.id

                
                user_dates[str(sender.id)]['remitent_msg_id']=msg_id
                await upload_db()


            elif message in traduct_menu['⏳ Espera']:
                
                if sender.id not in menu_history:
                    menu_history[sender.id]=[message]
                else:
                    menu_history[sender.id].append(message)
                    
                if 'wait_time' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['wait_time']=1
                
                wait_time= user_dates[str(sender.id)]['wait_time']
                keyboard = [Button.inline(translate('⏳ Modificar Espera',lg), data=b'resend_time')]
                info=f'⏳ <b>Espera PreEnvío</b>.\n\n• Tiempo: {wait_time} Segundos \n\n💡 <b>La espera previa al reenvío te permite establecer un retraso entre el envío de la publicación en el canal y el reenvío en los grupos</b>.\n\n• Dentro de esos segundos puedes editar el mensaje o eliminarlo antes de que se reenvié.\n\n• Tenga en cuenta que el tiempo de espera transcurre solo entre la recepción y el reenvío de ese único mensaje.'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')
            
            elif message=='🕖 Reenvío':
                if sender.id not in menu_history:
                    menu_history[sender.id]=[message]
                else:
                    menu_history[sender.id].append(message)
                
                if 'resend_loop' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['resend_loop']=0
                
                resend_time= user_dates[str(sender.id)]['resend_loop']
                keyboard = [Button.inline(translate('🕖 Aumentar Tiempo',lg), data=b'more_time')]
                info=f'🕖 <b>Tiempo entre Reenvíos</b>.\n\n• Tiempo: {resend_time/60} Minutos\n\n💡 <b>Desde aquí podrás configurar el tiempo que transcurre entre un reenvío y otro</b>.\n\n• Manteniendo el contador en 0 Minutos optas por un solo reenvío de la publicación.\n\n• Tenga en cuenta que el tiempo de reenvío transcurre entre la repetición del mismo mensaje a los grupos.'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')  
            
            
            elif message in traduct_menu['✏️ Editar Grupos']:
                keyboard = [Button.inline(translate('✏️ Editar Grupos',lg), data=b'edit_groups')]
                groups=""
                print(user_dates)
                if 'group_ids' in  user_dates[str(sender.id)]:
                    
                    for group_id in user_dates[str(sender.id)]['group_ids']:
                        groups+=f'{str(group_id)}\n'
                    if len(user_dates[str(sender.id)]['group_ids']) ==0:
                        groups="No hay grupos configurados\n" 
                        
                else:
                    
                    groups="No hay grupos configurados\n" 
                
                groups=translate(groups,lg)
                info=f'〽️ <b>Actualmente los grupos agregados son</b>:\n\n{groups}\n✏️ <b>Edita</b>, <b>agrega o elimina grupos desde el botón</b>:'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')   
                
            elif message in traduct_menu['🔰 Referidos']:
                keyboard = [Button.inline(translate('♻️ Generar Enlace',lg), data=b'generate_ref_link')]
                info=f'🔰 ¡Gane el 25% de los fondos aumentados por sus referidos!\n\n• <b>Referidos</b> - {len(tree_ref(str(sender.id))[0])}\n\n• <b>Comisiones</b> - {str(tree_ref(str(sender.id))[1])} USD\n\n👛 Los Referidos existen para brindarle la oportunidad de adquirir suscripciónes de pago gratis!'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')  
            
            elif message in traduct_menu['Siguiente ➡️']:
                keyboard = await get_custom_menu(event)
                keyboard=keyboard[2]
                info="Siguiente ➡️"
                await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
            
            elif message in traduct_menu['🧩 Más Cuentas']:
                keyboard = [Button.inline(translate('➕ Agregar Cuentas',lg), data=b'more_accounts')]
                info='🧩 Para evitar pagar múltiples pagos, desde este menú podrás agregar hasta un máximo de 3 cuentas!\n\n• Una vez caducada la suscripción de está cuenta las cuentas agregadas también perderán todos los beneficios.'
                await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')   
            
            elif message in traduct_menu['〽️ Más Canales']:
                info='〽️ Más Canales'
                await event.respond(translate(info,lg),parse_mode='html')     
            
            elif message in traduct_menu['🔙 Volver']:
                keyboard=await menu_action('back',event)
                info='🔙 Back'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')  
                
            elif message in traduct_menu['🔝 Menú principal']:
                keyboard=await menu_action('home',event)
                info='🔝 Main Menu'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
            
            
            elif message in traduct_menu['🔖 Crear Mensaje']:
                user_dates[user_id]['historial']=['🔖 Crear Mensaje']
                keyboard = [Button.text(translate('🚫 Cancel',lg),resize=True)]
                info='✍️ ¡<b>Escriba y envié un nuevo mensaje</b>!\n\n• También puedes Reenviar texto desde otro chat o canal:'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
            
            elif message in traduct_menu['📮 Notificaciones']:
                if str(sender.id) not in user_dates:
                    user_dates[str(sender.id)]={}
                if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
                    
                state='🌑Apagar'
                if user_dates[str(sender.id)]['notifications']:
                    state='🟢Encender'
                keyboard = [Button.inline(translate('🟢Encender',lg), data=b'on_notif'),Button.inline(translate('🌑Apagar',lg), data=b'off_notif')]
                info=f'📮 ¿<b>Deseas dejar de resivir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.\n\n🔘 <b>Actualmente</b> - {state}'
                msg_send=await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
                msg_id=msg_send.id
                user_dates[str(sender.id)]['notifications_msg_id']=msg_id
                await upload_db()
            
                        
            elif message in traduct_menu['🔘 Pausar Reenvío']:
                
                keyboard = [Button.inline(translate('⚠️Pausar',lg), data=b'pause_auto_send')]
                info='‼️ ¿<b>Estás seguro de pausar el reenvío de mensajes automáticos</b>?\n\n• Nota:\n\n¡Luego de pausar el reenvío podrás reanudarlo desde aquí!\n\n⚠️ <b>Pause el reenvío</b>:'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
            
            elif message in traduct_menu['🖲️ Compartir Suscripción']:
                
                keyboard = [Button.text(translate('🚫 Cancel',lg),resize=True)]
                info='🖲️ ¡<b>Solo puedes compartir tu suscripción con cuentas propias</b>!\n\n• El máximo de cuentas que puedes agregar excede a 3 Cuentas.\n\n💡 <b>Envié los</b> ID de <b>las cuentas con las que compartirás tu suscripción luego del comando</b> <code>/Share</code>\n\n• Ejemplo:\n\n/Share 5734929663\xa0 6602317993 1693581428\n\n• Utilize @ScanIDBot para saber el ID.\n\n🖲️ <b>Envié el ID de las cuentas</b>:'
                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
            
            elif  'mycode' in message:
                
                code=message.replace(translate('mycode',lg),'')
                if str(sender.id) not in user_dates:
                    
                    user_dates[str(sender.id)]={}
                    
                user_dates[str(sender.id)]['code']=code
                await login_(event)
                
                    
            
            elif  'mypass' in message:
                password=message.replace(translate('mypass',lg),'')
                if str(sender.id) not in user_dates:
                    
                    user_dates[str(sender.id)]={}
                    
                user_dates[str(sender.id)]['password']=password
                respond=await login_(event,password)
                if respond!=0:
                    info='Error'
                    await event.respond(translate(info,lg),parse_mode='html') 
            
            elif len(user_dates[user_id]['historial'])>0:
                print('added')
                if  user_dates[user_id]['historial'][0]=='🔖 Crear Mensaje':
                    user_dates[user_id]['historial']=[]
                    
                    await send_anounce(event)
            print(f"ad:{user_dates[user_id]['historial']}")       
                
        #await user.disconnect()
        else:
            keyboard = await get_custom_menu(event)
            keyboard=keyboard[1]

            info="Su plan ha concluido por favor compre uno para poder seguir utilizando el bot.\nDirijase a la seccion 👛 Suscripción o presione el comando /Suscripcion para realizar la compra "
            await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')  
                
            
#Controlador de menu 
async def menu_action(action,event):
    sender = await event.get_sender()
    if action=='back':
        men_=await get_custom_menu(event)
        
        return men_[0]
        
    if action=='home':
        men_=await get_custom_menu(event)
        
        return men_[0]
        
    if action=='cancel':
        men_=await get_custom_menu(event)
        
        return men_[0]
        
    
     
        
#Manejador de callbacks     
@bot.on(events.CallbackQuery)
async def callback_handler(event):
    global user_dates
    
    chat_id = event.chat_id
    sender = await event.get_sender()
    user_id=str(sender.id)   
     
    if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
            
    if 'beginner' not in user_dates[user_id]:
        user_dates[user_id]['beginner']=True
        user_dates[str(sender.id)]['beginner_trial']=True
    if 'beginner_trial' not in user_dates[user_id]:
        user_dates[str(sender.id)]['beginner_trial']=True
    if 'status' not in user_dates[user_id]:
        user_dates[user_id]['status']={} 
        user_dates[user_id]['status']['cat']='basic'    
        user_dates[user_id]['status']['lote']=0
        user_dates[user_id]['status']['buyed']=0
    if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
            
    lg=user_dates[user_id]['leng']
    
    

    if user_dates[user_id]['status']['cat']=='basic' and user_id not in admins and not user_dates[str(sender.id)]['beginner'] and not  user_dates[str(sender.id)]['beginner_trial']:
        keyboard = await get_custom_menu(event)
        keyboard=keyboard[1]
        if event.data == b'buy_premium1':
            await deposit_solicity(event,5) 
            return 0
        if event.data == b'buy_premium2': 
            await deposit_solicity(event,9)   
            return 0
        if event.data == b'buy_premium3': 
            await deposit_solicity(event,12)  
            return 0 
        info="Su plan ha concluido por favor compre uno para poder seguir utilizando el bot.\nDirijase a la seccion 👛 Suscripción o presione el comando /Suscripcion para realizar la compra "
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')  
        
        return 0
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
    if user_dates[user_id]['beginner']:
                keyboard_inline = [Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan'),Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]
                if event.data ==  b'lg_ru':

                    user_id=str(sender.id)
                    user_dates[user_id]['leng']='russian'
                    await upload_db()
                    if user_dates[str(sender.id)]['beginner']:
                        user_dates[str(sender.id)]['beginner']=False
                        await start(event,beginner=True)
                    else:
                        await start(event)
                    
                if event.data ==  b'lg_en':
                    user_id=str(sender.id)
                    user_dates[user_id]['leng']='english'
                    await upload_db()
                    
                    if user_dates[str(sender.id)]['beginner']:
                        user_dates[str(sender.id)]['beginner']=False
                        await start(event,beginner=True)
                    else:
                        await start(event)
                if event.data ==  b'lg_es':
                    user_id=str(sender.id)
                    user_dates[user_id]['leng']='spanish'
                    await upload_db()
                    if user_dates[str(sender.id)]['beginner']:
                        user_dates[str(sender.id)]['beginner']=False
                        await start(event,beginner=True)
                    else:
                        await start(event)
                    
                if event.data ==  b'lg_chi':
                    user_id=str(sender.id)
                    user_dates[user_id]['leng']='chinese (traditional)'
                    await upload_db()
                    if user_dates[str(sender.id)]['beginner']:
                        user_dates[str(sender.id)]['beginner']=False
                        await start(event,beginner=True)
                    else:
                        await start(event)
                if event.data ==  b'lg_ar':
                    user_id=str(sender.id)
                    user_dates[user_id]['leng']='arabic'
                    await upload_db()
                    if user_dates[str(sender.id)]['beginner']:
                        user_dates[str(sender.id)]['beginner']=False
                        await start(event,beginner=True)
                    else:
                        await start(event)
                await event.respond(translate('💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛\n\nPrueba Gratis ✖️ 5 Días 🎉',user_dates[str(sender.id)]['leng']), buttons=keyboard_inline,parse_mode='html')
                return 0
    if event.data == b'connect':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='🧩 <b>Ingrese el número de teléfono asociado a su cuenta de Telegram, elimine el espacio entre el prefijo y el número</b>.\n\n• <b>Ejemplo</b>, su número es <b>+84</b> 55555, <b>deberás enviar</b>:\n\n/connect +8455555'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'resend_time':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='🕖 El tiempo máximo de espera es de 2 minutos (120 segundos)\n\n• <b>Ejemplo</b>, el tiempo que deseas agregar es de 60 segundos enviarás:\n\n/wait 60\n\n⏳ Envía ahora el número de segundos que deben pasar antes de reenviar:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'more_time':

        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='⏰ El tiempo mínimo de espera entre reenvíos es de (30 minutos)\n\n• Si deseas agregar un intervalo de reenvío de 60 minutos el formato correcto es:\n\n/ree 60\n\n⏱️ Envía el número de minutos que deben pasar entre cada reenvío, recuerde utilizar el comando <code>/ree</code>:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    
    if event.data == b'add_group':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='🔘 <b>Recibe en un mensaje el ID de todos sus grupos enviando el comando</b>:\n\n• /get_groups\n\n💡 <b>Utilize un espacio para separar un ID de otro</b>.\n\n• Ejemplo:\n\n/id 1001256118443 1001484740111 1001368540342\n\n🔎 <b>Ingrese el</b> ID <b>de los Grupos</b>:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    if event.data == b'add_channel':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='💠 <b>Recuerde añadir a </b><b>@Camariobot</b><b> en el canal</b> <b>agregado</b>!\n\n💡 <b>Deberás ingresar el ID del canal luego del comando</b> <code>/chanel</code>\n\n• Ejemplo:\n\n/chanel 1001368540342\n\n🔎 <b>Ingrese el</b> ID <b>del Canal</b>:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'more_accounts':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='🆔 Envié el ID de las cuentas que deseas agregar:\n\n• Utilice @ScanIDBot Para obtener el ID de sus cuentas!\n\n🧩 Solo puedes agregar un máximo de 3 cuentas!\n\n/add (ID de sus cuentas, separe con un espacio cada ID) \n\n• Ejemplo:\n\n/add 1878166234 1459865634 181862566234\n\n🚫 Tenga en cuenta que tendrás que conectar cada cuenta con @Camariobot!\n\n• Esté menú no facilita la conexión entre cuentas, simplemente compartirá su suscripción con otras cuentas.\n\n🔎 Envié el ID de las Cuentas:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'generate_ref_link':

        
        keyboard = [Button.inline(translate('🧩 Reenvio automatico',lg), data=b'auto_send_ref_link')]
        info=f'https://t.me/Camariobot?start={sender.id}'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        
    if event.data == b'auto_send_ref_link':
        user_id=str(sender.id)
        if user_id not in user_dates:
            
            user_dates[user_id]={}
        if 'resend_loop' not in user_dates[user_id]:
            user_dates[user_id]['resend_loop']=0
            

        
        sleep_time=user_dates[user_id]['resend_loop']
        keyboard = [Button.inline(translate('🧩 Continuar',lg), data=b'yes_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        info=f'🧩 Reenviaras tu enlace a todos los grupos con un intervalo de reenvío de {str(sleep_time/60)} Minutos.\n\n• Está acción es gratis\n\n⁉️ Deseas continuar con el reenvío:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    if event.data == b'yes_auto_send_ref_link':
        keyboard = [Button.inline(translate('🧩 Continuar',lg), data=b'cont_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        user_id=str(sender.id)

        if user_id not in user_dates:
            
            user_dates[user_id]={}
                    
        if 'pending_messages' not in user_dates[user_id]:
                
            user_dates[user_id]['pending_messages']=[]
            

            
        if 'group_ids' in  user_dates[user_id]:
            info='🔎 Necesitas agregar grupos para reenviar automáticamente su enlace a ellos!\n\n• /AgregarGrupos'
            await event.respond(translate(info,lg),parse_mode='html') 
        else:
            if len(user_dates[user_id]['group_ids'])==0:
                info='🔎 Necesitas agregar grupos para reenviar automáticamente su enlace a ellos!\n\n• /AgregarGrupos'
                await event.respond(translate(info,lg),parse_mode='html') 
            else:
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
                date_in={'time':timestamp,'msg':f'https://t.me/Camariobot?start={sender.id}','event':'not_remitent'}
                user_dates[user_id]['pending_messages'].append(date_in)
                await upload_db()
            
        
                
    if event.data == b'buy_premium1':
        
        await deposit_solicity(event,5) 
    if event.data == b'buy_premium2': 
        await deposit_solicity(event,9)   
    if event.data == b'buy_premium3': 
        await deposit_solicity(event,12)         
        
          
    if event.data == b'yes_swap_channel':
        
        user_dates[str(sender.id)]['channel_ids'][0]=channel_ids_swap[sender.id][0]
        keyboard=await get_custom_menu(event)
        keyboard=keyboard[0]
        await upload_db()
        info='〽️ Si\nNuevo canal configurado'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        
    if event.data == b'no_swap_channel':
        keyboard=menu_system[0]
        keyboard = [Button.inline(translate('🧩 Continuar',lg), data=b'cont_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        info='🚫 No\nNo se ha realizado ningun cambio'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'del_groups_msg':
        await bot.delete_messages(sender.id, [user_dates[str(sender.id)]['groups_msg_id'],user_dates[str(sender.id)]['groups_msg_id']-1])
        #await bot.delete_messages(sender.id, [user_dates[str(sender.id)]['groups_msg_id']])
        
    if event.data == b'on_remitent':
        keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline(translate('🌑 Off',lg), data=b'off_remitent')]
        if str(sender.id) not in user_dates:     
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['remitent']=True
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['remitent_msg_id']
        state="Off"
        if user_dates[str(sender.id)]['remitent']:
            state="On" 
        msg=f'📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - {state}'
        await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'off_remitent':
        keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline('🌑 Off', data=b'off_remitent')]
        if str(sender.id) not in user_dates:     
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['remitent']=False
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['remitent_msg_id']
        state="Off"
        if user_dates[str(sender.id)]['remitent']:
            state="On" 
        msg=f'📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - {state}'
        await bot.edit_message(id_chat,id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
        
    if event.data == b'on_notif':
      
        if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}
        if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
        
        user_dates[str(sender.id)]['notifications']=True      
        state='🌑Apagar'
        if user_dates[str(sender.id)]['notifications']:
            state='🟢Encender'
        keyboard = [Button.inline(translate('🟢Encender',lg), data=b'on_notif'),Button.inline(translate('🌑Apagar',lg), data=b'off_notif')]
        msg=f'📮 ¿<b>Deseas dejar de resivir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.\n\n🔘 <b>Actualmente</b> - {state}'
            
        
        id_chat=sender.id
        id_msg= user_dates[str(sender.id)]['notifications_msg_id']
        

        await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'off_notif':
      
        if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}
        if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
        
        user_dates[str(sender.id)]['notifications']=False     
        state='🌑Apagar'
        if user_dates[str(sender.id)]['notifications']:
            state='🟢Encender'
        keyboard = [Button.inline(translate('🟢Encender',lg), data=b'on_notif'),Button.inline(translate('🌑Apagar',lg), data=b'off_notif')]
        msg=f'📮 ¿<b>Deseas dejar de resivir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.\n\n🔘 <b>Actualmente</b> - {state}'
            
        
        id_chat=sender.id
        id_msg= user_dates[str(sender.id)]['notifications_msg_id']
        

        await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'pause_auto_send':
        user_id=str(sender.id)
        user_dates[user_id]['resend_loop']=0
        
    if event.data ==  b'edit_groups':
            print(user_dates)
            user_id=str(sender.id)
        
            groups=""

            if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}

            if 'group_ids' in  user_dates[str(sender.id)]:
                if len(user_dates[str(sender.id)]['group_ids'])==0:
                    groups="No tiene grupos"
                
                user = TelegramClient(str(sender.id), api_id, api_hash)
            
                try:
                    await user.connect()
                except:
                    await user.disconnect()
                    await asyncio.sleep(1)
                    await user.connect()
            
            
                
                for group_id in user_dates[user_id]['group_ids']:
                    chat_entity = await user.get_entity(int(group_id))
                    try:
                        username_=chat_entity.username
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
                    except:
                        username_=""
                    
                    groups+=f"/delgroup_{str(group_id).replace('-','')}  Eliminar: <a href='https://t.me/{username_}'>{chat_entity.title}</a>\n"
                  
                    
                await user.disconnect()
                    
            else:
               groups="No hay grupos configurados\n" 
               
            msg_send=await event.respond(translate(groups,lg),parse_mode='html')
            msg_id=msg_send.id
      
            user_dates[str(sender.id)]['edit_groups_msg_id']=msg_id
            await upload_db()
            
            
    #Idioma:
    
    if event.data ==  b'lg_ru':

        user_id=str(sender.id)
        user_dates[user_id]['leng']='russian'
        await upload_db()
        if user_dates[str(sender.id)]['beginner']:
            user_dates[str(sender.id)]['beginner']=False
            await start(event,beginner=True)
        else:
            await start(event)
        
    if event.data ==  b'lg_en':
        user_id=str(sender.id)
        user_dates[user_id]['leng']='english'
        await upload_db()
        
        if user_dates[str(sender.id)]['beginner']:
            user_dates[str(sender.id)]['beginner']=False
            await start(event,beginner=True)
        else:
            await start(event)
    if event.data ==  b'lg_es':
        user_id=str(sender.id)
        user_dates[user_id]['leng']='spanish'
        await upload_db()
        if user_dates[str(sender.id)]['beginner']:
            user_dates[str(sender.id)]['beginner']=False
            await start(event,beginner=True)
        else:
            await start(event)
        
    if event.data ==  b'lg_chi':
        user_id=str(sender.id)
        user_dates[user_id]['leng']='chinese (traditional)'
        await upload_db()
        if user_dates[str(sender.id)]['beginner']:
            user_dates[str(sender.id)]['beginner']=False
            await start(event,beginner=True)
        else:
            await start(event)
    if event.data ==  b'lg_ar':
        user_id=str(sender.id)
        user_dates[user_id]['leng']='arabic'
        await upload_db()
        if user_dates[str(sender.id)]['beginner']:
            user_dates[str(sender.id)]['beginner']=False
            await start(event,beginner=True)
        else:
            await start(event)
    
    if event.data ==  b'trial_plan':
        id_=str(sender.id)

        info='🦎 Suscríbase para utilizar nuestros servicios gratis:\n\n• @Camario'
        keyboard_inline = [Button.inline(translate('☑️ Listo',lg), data=b'check_subscribed')]
        msg_trial_send=await event.respond(translate(info,lg),buttons=keyboard_inline,parse_mode='html')
        msg_trial_id=msg_trial_send.id
        user_dates[user_id]['check_sub_trial_id']=msg_trial_id
    if event.data == b'check_subscribed':
        chanel_id=-1002023830162
        us_id=int(sender.id)
        id_=str(sender.id)
        resp=await check_subscription(us_id,chanel_id)
        print('check')
        if resp:
            if 'status' not in user_dates[id_]:
                    user_dates[id_]['status']={} 
                    user_dates[id_]['status']['cat']='basic'    
                    user_dates[id_]['status']['lote']=0
                    user_dates[id_]['status']['buyed']=0
            if user_dates[str(sender.id)]['beginner_trial']:

                    user_dates[str(sender.id)]['status']['cat']='trial' 
                    user_dates[str(sender.id)]['status']['lote']+=60*60*24*5
                    user_dates[str(sender.id)]['beginner_trial']=False
                    info='El plan de prueba vence en 5 dias'
                    msg=translate(info ,lg)
                    id_chat=sender.id
                    id_msg= user_dates[user_id]['check_sub_trial_id']
                    
                    await bot.edit_message(id_chat,id_msg,msg,parse_mode='html')
                    user_dates[str(sender.id)]['beginner_trial']=False
                    
        else:
            
            info='No estas subscrito,🦎 Suscríbase para utilizar nuestros servicios gratis:\n\n• @Camario'
            msg=translate(info ,lg)
            id_chat=sender.id
            id_msg= user_dates[user_id]['check_sub_trial_id']
            keyboard_inline = [Button.inline(translate('☑️ Listo',lg), data=b'check_subscribed')]
            await bot.edit_message(id_chat,id_msg,msg,buttons=keyboard_inline,parse_mode='html')

            
    
    
        
#@bot.on(events.CallbackQuery)
#async def mod_time(event):
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
#    keyboard = [Button.text('🚫 Cancel', resize=True)]
#    await event.respond('🕖 El tiempo máximo de espera es de 2 minutos (120 segundos)\n\n• Envía ahora el número de segundos que deben pasar antes de reenviar:',buttons=keyboard,parse_mode='html')
 
#@bot.on(events.CallbackQuery)
#async def more_time(event):
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
#    keyboard = [Button.text('🚫 Cancel', resize=True)]
#    await event.respond('⏰ El tiempo mínimo de espera entre reenvíos es de (30 minutos)\n\n• Envía ahora el número de minutos que deben pasar entre cada reenvío:',buttons=keyboard,parse_mode='html')
 
 
async def schedule_messages():
    
        bot_ =await TelegramClient('bot_', api_id, api_hash).start(bot_token=bot_token)
        while True:
            try:
                global user_dates
                
                
                print('.')
                if state:
                    
                    for id_us in  user_dates:
                        if id_us!='all_hashes' and id_us!="chat_ids":
                            if 'beginner' not in user_dates[id_us]:
                                user_dates[id_us]['beginner']=True
                            if 'status' not in user_dates[id_us]:
                                user_dates[id_us]['status']={} 
                                user_dates[id_us]['status']['cat']='basic'    
                                user_dates[id_us]['status']['lote']=0
                                user_dates[id_us]['status']['buyed']=0
                            if user_dates[id_us]['status']['cat']=='basic' and id_us not in admins:
                                continue
                            if state==False:
                                    break
                            if 'pending_messages' not in user_dates[id_us]:
                                user_dates[id_us]['pending_messages']=[]
                            
                            if 'leng' not in user_dates[id_us]:
                                user_dates[id_us]['leng']='spanish'
            
                            lg=user_dates[id_us]['leng']
                                    
                            if len(user_dates[id_us]['pending_messages'])>0:


                                

                                if 'remitent' not in user_dates[id_us]:
                                    user_dates[id_us]['remitent']=True
                                if 'sleep_time' not in user_dates[id_us]:
                                    user_dates[id_us]['sleep_time']=1
                        
                                sleep_time= user_dates[id_us]['sleep_time']
                    
                                if 'wait_time' not in user_dates[id_us]:
                                    user_dates[id_us]['wait_time']=1
                        
                                wait_time= user_dates[id_us]['wait_time'] 
                                if 'resend_loop' not in user_dates[id_us]:
                                    user_dates[id_us]['resend_loop']=0
                                if 'notifications' not in user_dates[id_us]:
                                    user_dates[id_us]['notifications']=True
                                resend_loop= user_dates[id_us]['resend_loop']

                                user = TelegramClient(str(id_us), api_id, api_hash)
                                
                                while True:
                                    try:
                                        await user.connect()
                                        break
                                    except Exception as e:
                                        print(e)
                                        try:
                                            await user.disconnect()
                                        except:
                                            print('error disconect')
                    
                                

                                msg_dates= user_dates[id_us]['pending_messages']
                                index=0
                                desv=0 
                                for msg_date in msg_dates:
                                                not_errors=True
                                                
                                                programed_time=msg_date['time']
                                        #for programed_time in msg_date:
                                        #   if programed_time!='event':
                                                event_message=msg_date['event']
                                                event_message_string=event_message
                                                if type(event_message) == str and event_message!="not_remitent" :
                                                    print("string")
                                                    match = re.match(r"Message\(id=(\d+), peer_id=PeerChannel\(channel_id=(\d+)\), date=datetime\.datetime\(([\d, ]+), tzinfo=datetime\.timezone\.utc\), message='([^']+)', out=(\w+), mentioned=(\w+), media_unread=(\w+), silent=(\w+), post=(\w+), from_scheduled=(\w+), legacy=(\w+), edit_hide=(\w+), pinned=(\w+), noforwards=(\w+), invert_media=(\w+), from_id=(\w+), saved_peer_id=(\w+), fwd_from=(\w+), via_bot_id=(\w+), reply_to=(\w+), media=(\w+), reply_markup=(\w+), entities=\[([^]]*)\], views=(\d+), forwards=(\d+), replies=(\w+), edit_date=(\w+), post_author='([^']+)', grouped_id=(\w+), reactions=(\w+), restriction_reason=\[([^]]*)\], ttl_period=(\w+)\)", event_message_string)

                                                    # Crea el objeto Message
                                                    event_message = Message(
                                                        id=int(match.group(1)),
                                                        peer_id=PeerChannel(channel_id=int(match.group(2))),
                                                        date=datetime(*map(int, match.group(3).split(", ")), tzinfo=timezone.utc),
                                                        message=match.group(4),
                                                        out=bool(match.group(5)),
                                                        mentioned=bool(match.group(6)),
                                                        media_unread=bool(match.group(7)),
                                                        silent=bool(match.group(8)),
                                                        post=bool(match.group(9)),
                                                        from_scheduled=bool(match.group(10)),
                                                        legacy=bool(match.group(11)),
                                                        edit_hide=bool(match.group(12)),
                                                        pinned=bool(match.group(13)),
                                                        noforwards=bool(match.group(14)),
                                                        invert_media=bool(match.group(15)),
                                                        from_id=None if match.group(16) == 'None' else int(match.group(16)),
                                                        saved_peer_id=None if match.group(17) == 'None' else int(match.group(17)),
                                                        fwd_from=None if match.group(18) == 'None' else int(match.group(18)),
                                                        via_bot_id=None if match.group(19) == 'None' else int(match.group(19)),
                                                        reply_to=None if match.group(20) == 'None' else int(match.group(20)),
                                                        media=None if match.group(21) == 'None' else int(match.group(21)),
                                                        reply_markup=None if match.group(22) == 'None' else int(match.group(22)),
                                                        entities=[] if match.group(23) == '' else list(map(int, match.group(23).split(", "))),
                                                        views=int(match.group(24)),
                                                        forwards=int(match.group(25)),
                                                        replies=None if match.group(26) == 'None' else int(match.group(26)),
                                                        edit_date=None if match.group(27) == 'None' else int(match.group(27)),
                                                        post_author=match.group(28),
                                                        grouped_id=None if match.group(29) == 'None' else int(match.group(29)),
                                                        reactions=None if match.group(30) == 'None' else int(match.group(30)),
                                                        restriction_reason=[] if match.group(31) == '' else list(map(int, match.group(31).split(", "))),
                                                        ttl_period=None if match.group(32) == 'None' else int(match.group(32))
                                                    )

                                                msg=msg_date['msg']

                                                actual_time = time.time()
                                                

                                                if float(actual_time)>=float(programed_time):
                                                    print(f"Time:{programed_time}=>actual:{actual_time} ")
                                                    await asyncio.sleep(wait_time)
                                                    error_groups=""
                                                    for group_id in user_dates[id_us]['group_ids']:
                                                        print(group_id)
                                                        try:
                                                            if user_dates[id_us]['remitent'] and event_message!='not_remitent':
                                                                
                                                                await user.forward_messages(int(group_id),event_message)
                                                            else:
                                                                await user.send_message(int(group_id), msg,parse_mode='html')
                                                            print('send')
                                                            
                                                            await asyncio.sleep(sleep_time)
                                                        except Exception as e:
                                                            not_errors=False
                                                            error_groups+=f"{str(group_id)}\n"
                                                            print(f"resend_error:{e}")
                                                        
                                                    if not_errors:
                                                        if user_dates[id_us]['notifications']:
                                                            await bot_.send_message(int(id_us),translate("Mensaje reenviado",lg))
                                                        if  resend_loop==0:
                                                            msg_dates.pop(index-desv)
                                                            desv+=1
                                                             
                                                        else:
                                                            print('loop_resend')
                                                            msg_date['time']=actual_time+resend_loop
                                                            
                                                    else:
                                                        if user_dates[id_us]['notifications']:
                                                            await bot_.send_message(int(id_us), f"{translate('Error en el reenvio en',lg)} : {error_groups}")
                                                        msg_dates.pop(index-desv)
                                                        
                                                        desv+=1


                                                    await upload_db() 
                                            
                                            
                                                index+=1
                                                
                                             
                                                
                                
                                             
                                
                                await user.disconnect()   
                                 
                await asyncio.sleep(1)   
            except Exception as e:
                print(f'error{e}')
                print(state)
                #print(user_dates[id_us]['pending_messages'])
                try:
                    await asyncio.sleep(1)
                    await user.disconnect()
                except:
                    print('desconectado')  
        #threading.Thread(target=main).start()
        

        
    

def main():
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(init_dates())
        loop.run_until_complete(schedule_messages())
    except Exception as e:
        loop.close()
        print(f"main exception :{e}")
        threading.Thread(target=main).start()
        
def main_():
    
    loop1 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop1)
    try:
        
        loop1.run_until_complete(deposit_check())
    except Exception as e:
        loop1.close()
        print(f"main exception1 :{e}")
        threading.Thread(target=main_).start()
        
       

    


    
# Crea un nuevo bucle de eventos
threading.Thread(target=main).start()
threading.Thread(target=main_).start()

with bot:
   bot.run_until_disconnected()
# Iniciar el bot

     
