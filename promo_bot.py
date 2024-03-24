import os
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
from telethon.tl.functions.channels import DeleteMessagesRequest
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
import shutil
import random
from pathlib import Path
keep_alive()
state=True
first_init=True
getentity_state="off"
chunk_size = 10
import telethon
import asyncio
import psutil
import signal
from session_save import*
api_id = '16620070'
api_hash = 'dbf692cdc9b6fb2977dda29fb1691df4'
user_dates={}
#group_ids = {}
#channel_ids={}
user_dates['chat_ids']=[]
ids_entity={}
channel_ids_swap={}
#pending_messages = {}
admins=[]
resend_channel=-1002017124784
admin_comand='/g2r7a0t2n2h5bw41b5'
admin_wallet=''
bot_token = '6395817457:AAH1YxFN6h1arYwu70ESTtavNxFsGqoy7nc'
#bot_token = '5850221861:AAFfZUP2HYaeaNE6vxBq8FSwN7n8n6dyrfI'
test_mode=False
on_saving=False
txts=['🧩 Conectar Cuenta','💠 Conectar Canal','〽️ Agregar Grupos','⚙️ Configuración','👛 Suscripción','👁️ Remitente','⏳ Espera','🕖 Reenvío','✏️ Editar Grupos','🔰 Referidos','Siguiente ➡️','🔙 Volver','🔝 Menú principal','🧩 Más Cuentas','〽️ Más Canales','🔙 Volver','🔝 Menú principal','🚫 Cancelar','🔖 Crear Mensaje','📮 Notificaciones','🔘 Pausar Reenvío','🖲️ Compartir Suscripción']
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
accounts_conected={}

async def enviar_mensaje(chat_id, mensaje, error_chats,client,event_message):
    
    try:
        if mensaje=="None":
            await client.forward_messages(int(chat_id),event_message)
        else:
            await client.send_message(int(chat_id),mensaje,parse_mode='html')  
        
        print(f'Mensaje enviado a {chat_id}: {mensaje}')
    except Exception as e:
        error_chats.append(chat_id)
        
        print(f'Error al enviar mensaje a {chat_id}: {e}')
    
async def enviar_mensajes_concurrentes(chat_ids, mensaje, error_chats,client,event_messag):
    tasks = [enviar_mensaje(chat_id, mensaje, error_chats,client,event_messag) for chat_id in chat_ids]
    await asyncio.gather(*tasks)

async def get_entitys_():
    print('getting')
    global ids_entity
    global getentity_state
    global user_dates
    getentity_state="on"
    print(user_dates)
    global accounts_conected
    for key in user_dates:
        
        if not 'group_ids' in  user_dates[key]:
            continue
        groups=user_dates[key]['group_ids']
        if len(groups)==0:
            continue
        ruta_original=f'{str(key)}.session'
        ruta_copia=f'cache/{str(key)}_get_ent.session'
        id_us=key
        try:
                if str(id_us) in  accounts_conected:
                    user=accounts_conected[str(id_us)]
                    print(f'{str(id_us)} ya se encuentra conectada')
                else: 
                                            
                    user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                                            
                    accounts_conected[str(id_us)]= user
                    accounts_conected[f'{str(id_us)}_lote']=time.time()+random.randint(300, 1000)
                    print(f'{str(id_us)} NO se encuentra conectada')
        except Exception as e:
                print("Error in resesnd _connect")
                user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                
        if not user.is_user_authorized:
            chat_id=int(id_us)
            mensaje="Su cuenta se ha desconectado por favor vuelva a conectarla"
            await bot.send_message(chat_id,mensaje,parse_mode='html')
            continue
        while True:
                    try:
                                        
                                        if not user.is_connected():
                                            await user.connect()
                                            print('Not conected.Conecting..') 
                                        break
                    except Exception as e:
                                        print(f"Error en la conexion.#critic:{e}")

                                        await asyncio.sleep(2)
        
        for id in  groups:
            if not str(id) in ids_entity:
                ids_entity[str(id)]={}
            if 'id' in ids_entity[str(id)]:
                continue
                
            group_id=int(id)
            
            username="None"
            chat_entity_title="Desconocido"
            try:
                        print(group_id)
                        chat_entity = await user.get_entity(int(group_id))
                        username=chat_entity.username
                        chat_entity_title=chat_entity.title
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
            except Exception as e:
                        print(e)
                        username="None"
                      
                        
            ids_entity[str(id)]['id']=group_id
            ids_entity[str(id)]['username']=username
            ids_entity[str(id)]['tittle']= chat_entity_title
    getentity_state="off"  
async def get_entitys():
    global getentity_state
    if getentity_state=="off":
        print('get')
        task= asyncio.create_task(get_entitys_())
        await task
                        
async def init_sessions():
    # Obtener la ruta del directorio actual
    try:
        directorio_actual = os.getcwd()

        # Obtener una lista de todos los archivos en el directorio actual
        archivos_en_directorio = os.listdir(directorio_actual)

        # Filtrar la lista para obtener solo los archivos con extensión ".session" y extraer solo los nombres sin la extensión
        archivos_session = [os.path.splitext(archivo)[0] for archivo in archivos_en_directorio if archivo.endswith(".session")]

        # Imprimir la lista de nombres de archivos sin la extensión ".session"
        print("Nombres de archivos con extensión .session en el directorio actual:")
        for archivo in archivos_session:
            try:
                print(archivo)
                id=archivo
                user = TelegramClient(archivo, api_id, api_hash)
                if user.is_user_authorized:
                    accounts_conected[str(id)]=user
                else:
                    chat_id=int(id)
                    mensaje="Su cuenta se ha desconectado por favor vuelva a conectarla"
                    await bot.send_message(chat_id,mensaje,parse_mode='html')
                    ruta_archivo = f'{archivo}.session'

                    # Verificar si el archivo existe antes de intentar eliminarlo
                    if os.path.exists(ruta_archivo):
                        # Eliminar el archivo
                        os.remove(ruta_archivo)
                        print(f"El archivo {ruta_archivo} ha sido eliminado.")
            
            except Exception as e:
                    print(f'Error en init_sessions en {archivo}: {e}')
    except Exception as e:
        print(f'Error en init_sessions: {e}')
            
     



# Iniciar sesión como usuario
#user = TelegramClient('user', api_id, a#critipi_hash)
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
    txts_=['🧩 Conectar Cuenta','💠 Conectar Canal','〽️ Agregar Grupos','⚙️ Configuración','👛 Suscripción','👁️ Remitente','⏳ Espera','🕖 Reenvío','✏️ Editar Grupos','🔰 Referidos','Siguiente ➡️','🔙 Volver','🔝 Menú principal','🧩 Más Cuentas','〽️ Más Canales','🔙 Volver','🔝 Menú principal','🚫 Cancelar','🔖 Crear Mensaje','📮 Notificaciones','🔘 Pausar Reenvío','🖲️ Compartir Suscripción']
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
    
async def send_(bot,chat_id,mensaje,event=None,keyboard=None):
    MAX_CARACTERES = 4000 # Límite de caracteres por mensaje en Telegram
    #MAX_CARACTERES=10 
    if event is None:
        if len(mensaje) <= MAX_CARACTERES:
            
            msg_send=await bot.send_message(chat_id,mensaje,buttons=keyboard,parse_mode='html')
            msg_id=[msg_send.id]
        else:
            msg_id=[]
            # Dividir el mensaje en partes de MAX_CARACTERES caracteres
            partes = [mensaje[i:i+MAX_CARACTERES] for i in range(0, len(mensaje), MAX_CARACTERES)]
            
            i=0
            # Enviar cada parte como un mensaje separado
            for parte in partes:
                i+=1
                keyboard_=keyboard
                if len(partes)!=i:
                    keyboard_=None
                try:   
                    msg_send=await bot.send_message(chat_id, parte,buttons=keyboard_,parse_mode='html')  
                    msg_id.append(msg_send.id)
                except Exception as e:
                    print("Error en send_ {e}")
                #msg_id.append(msg_send.id)
    else:
        if len(mensaje) <= MAX_CARACTERES:
        
            msg_send=await event.respond(mensaje,buttons=keyboard,parse_mode='html')
            msg_id=[msg_send.id]
        else:
            msg_id=[]
        # Dividir el mensaje en partes de MAX_CARACTERES caracteres
            partes = [mensaje[i:i+MAX_CARACTERES] for i in range(0, len(mensaje), MAX_CARACTERES)]
        
        # Enviar cada parte como un mensaje separado
            i=0
            for parte in partes:
                i+=1
                keyboard_=keyboard
                if len(partes)!=i:
                    keyboard_=None
                try:
                    msg_send=await event.respond(parte,buttons=keyboard_,parse_mode='html') 
                    msg_id.append(msg_send.id)
                except Exception as e:
                    print("Error en send_ {e}")
                    
                #msg_id.append(msg_send.id)
    return msg_id
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

def pause_subprocess_using_file(filename):
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cmdline'])
            if process_info['cmdline'] and filename in " ".join(process_info['cmdline']):
                print(f"Pausando el subproceso {process_info['name']} (PID {process_info['pid']})")
                os.kill(process_info['pid'], signal.SIGSTOP)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print('error in delete')
            pass
def resume_subprocess_using_file(filename):
    return 0
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'cmdline'])
            if process_info['cmdline'] and filename in " ".join(process_info['cmdline']):
                print(f"Reanudando el subproceso {process_info['name']} (PID {process_info['pid']})")
                os.kill(process_info['pid'], signal.SIGCONT)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def copy(ruta_original, ruta_copia):
    try:
        shutil.copyfile(ruta_original, ruta_copia)
        print("¡Archivo de sesión copiado exitosamente!")
        return ruta_copia
    except FileNotFoundError:
        print("¡Error! Archivo de sesión original no encontrado.")
    except shutil.SameFileError:
        shutil.copyfile(ruta_original, ruta_copia)
    except Exception as e:
        print(f"¡Error al copiar el archivo de sesión: {e}")
async def init_dates():
    #return 0
    global first_init
    global user_dates
    
    '''
    ac=[]
    client = TelegramClient('1721406471', api_id, api_hash)
    await client.connect()
    ac.append(client)
    print('conectado en 1')
    time.sleep(10)
    client = TelegramClient('1633521428', api_id, api_hash)
    await client.connect()
    print('conectado en 2')
    client = ac[0]
    
    if client.is_connected():
        print('Wow conectado')
    else:
        print('bad')
    '''
    if first_init:
        try:
            
            await download_db()
            await asyncio.sleep(2)
            #await upload_sessiondb()
            await download_sessiondb()
            await asyncio.sleep(2)
            await  init_sessions()
            await asyncio.sleep(2)
            #await upload_db()
            first_init=False
            user_dates=txt_to_dict('db/data')
            #print(user_dates)
            await get_entitys()
            print('Datos iniciados con exito')

        except Exception as e:
            print(e)
            
async def download_sessiondb_():
    
    global on_saving
    if not on_saving:
        on_saving=True
        ruta_original='admin.session'
        ruta_copia='cache/admin_downdbses.session'
        user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
        #user = TelegramClient(str("admin"), api_id, api_hash)
        
        
        while True:
            try:
                await user.connect()
                break
            except Exception as e:
                print(e)

                    
                try:
                    await user.disconnect()
                except:
                    print('error disconect in session db')
                await asyncio.sleep(3)
                
        print("Downloading sessions..")    
        messages =await user.get_messages(-4137258269, filter=InputMessagesFilterDocument, limit=10)

            # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
        for message in messages:
                if message.media:
                    file_path = await user.download_media(message.media,file='db/saved_sessions.zip')
        user.disconnect()  

        await asyncio.sleep(2)
        descomprimir_archivo_zip()
        on_saving=False 

async def upload_sessiondb_():
    #return 0
    comprimir_archivos_session()
    await asyncio.sleep(2)
    global on_saving
    if not on_saving:
        on_saving=True 
        print("Uploading sessions..")
        
        '''
        folder='cache'
        file_name=str(int(time.time()))+'.session'
        file_path=f'{folder}/{file_name}'
        original_file='admin.session'
        while True:
            if not Path(file_path).exists():
                print("yes")
                shutil.copyfile(original_file,file_path)
                break
            else:
                file_name=str(int(time.time()))+'.session'
                file_path=f'{folder}/{file_name}'
            '''
        dict_to_txt(user_dates,'db/data')
        ruta_original='admin.session'
        ruta_copia='cache/admin_updbses.session'
        user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
        #user = TelegramClient("admin", api_id, api_hash)
        
        while True:
            try:
                
                await user.connect()
               
                break
            except Exception as e:
                print(e)

                try:
                    
                    
                    await user.disconnect()
                    
                except:
                    print('error disconect in upload sessions')
                await asyncio.sleep(8)
        while True:
            try:
                messages =await user.get_messages(-4137258269, filter=InputMessagesFilterDocument, limit=10)
            # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
                for message in messages:
                    print(message.id)
                    await user.delete_messages(-4137258269,[message.id])
                    
                await user.send_file(-4137258269,'db/saved_sessions.zip', caption=f'saved: {str(time.time())}') 
                break
            except Exception as e:
                print("Datbase de sessions no guardada")
                print(e)

        user.disconnect() 

        #os.remove(file_path)
        on_saving=False  
   
async def upload_sessiondb():
    task = asyncio.create_task(upload_sessiondb_())
    await task
async def download_sessiondb():
    task = asyncio.create_task(download_sessiondb_())
    await task
async def download_db_():
    #return 0
    global on_saving
    if not on_saving:
        on_saving=True
        ruta_original='admin.session'
        ruta_copia='cache/admin_downdb.session'
        user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
        #user = TelegramClient(str("admin"), api_id, api_hash)
        
           
        while True:
            try:
                
                if not user.is_connected():
                    await user.connect()
                    print('Not conected.Conecting..') 
                break
            except Exception as e:
                print(f'Error en el connect del downdb{e}')

                await asyncio.sleep(3)
                
        print("Downloading db..")     
        messages =await user.get_messages(-1002000640381, filter=InputMessagesFilterDocument, limit=10)

            # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
        for message in messages:
                if message.media:
                    file_path = await user.download_media(message.media,file='db/data')
        user.disconnect()  

        on_saving=False 
   
async def upload_db_():
    #return 0
    
    global on_saving
    if not on_saving:
        on_saving=True 
        print("Uploading..")
        
        '''
        folder='cache'
        file_name=str(int(time.time()))+'.session'
        file_path=f'{folder}/{file_name}'
        original_file='admin.session'
        while True:
            if not Path(file_path).exists():
                print("yes")
                shutil.copyfile(original_file,file_path)
                break
            else:
                file_name=str(int(time.time()))+'.session'
                file_path=f'{folder}/{file_name}'
            '''
        dict_to_txt(user_dates,'db/data')
        ruta_original='admin.session'
        ruta_copia='cache/admin_updb.session'
        user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
        #user = TelegramClient("admin", api_id, api_hash)
        
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
                await asyncio.sleep(8)
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
        #os.remove(file_path)
       
        on_saving=False
    
async def upload_db():
    task = asyncio.create_task(upload_db_())
    await task
async def download_db():
    task = asyncio.create_task(download_db_())
    await task
    
@bot.on(events.NewMessage(pattern='/reset_db'))
async def reset_db(event):
    global user_dates
    user_dates={}
    user_dates['chat_ids']=[]
    await upload_db()
    
     
async def login_(event,password="not_set"):
    # Solicitar número de teléfono
    global user_dates
    global accounts_conected
    sender = await event.get_sender()
    phone=user_dates[str(sender.id)]['phone']
    user_id=str(sender.id)
    phone_code_hash_= user_dates[str(sender.id)]['phone_code_hash']
    code=user_dates[str(sender.id)]['code']
    id_chat=sender.id
    id_msg= user_dates[str(sender.id)]['connect_msg_id']
        
    
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

        
            #await bot.edit_message(id_chat, id_msg,translate(info,lg),parse_mode='html')
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
    await upload_sessiondb()
    accounts_conected[str(sender.id)]= user
    info="🐾 ¡Conexión Establecida con Éxito!\n\n🤜🤛 Gracias por elegir @Camariobot, ahora todos nuestros servicios están disponibles para usted!\n\n👣 Para comenzar a configurar su primera tarea de reenvío siga los siguientes pasos:\n \n#Paso1 - Debes agregar un canal el cual se utilizará para reenviar todas la publiciones a todos sus grupos agregados.\n\n• <b>/AddChannel</b><b>\n\n</b>#Paso2 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado.\n\n• <b>/AddGroups</b><b>\n\n</b>⚙️ Para cualquier consulta, no dude en contactar con @CamarioAdmin\n\n🦎 Manténgase Informado con las últimas actualizaciones @Camario"
    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')
    #await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
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
    global user_dates

    bot_ =await TelegramClient('bot_dep', api_id, api_hash).start(bot_token=bot_token)
    while True:
        try:
            print('-')
        
            await asyncio.sleep(10)
            for id_ in user_dates:
                if id_!='all_hashes' and id_!="chat_ids":
                    actual_time=time.time()
                        
                    if 'invitator' not in user_dates[id_]:
                            user_dates[id_]['invitator']="None"
                                                         
                    if 'saldo' not in user_dates[id_]:
                                user_dates[id_]['saldo']=0
                    if 'saldo_ref' not in user_dates[id_]:
                                user_dates[id_]['saldo_ref']=0

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
                                if user_dates[id_]['status']['cat']=='premium_shared': 
                                    sharer=user_dates[id_]['status']['sharer']
                                    if user_dates[sharer]['status']['cat']=='basic' :
                                        user_dates[id_]['status']['cat']='basic'
                                        
                                        user_dates[id_]['status']['sharer']='None'
                                          
                                        user_dates[id_]['status']['lote']=0
                                        user_dates[id_]['status']['buyed']=0
                                        
                                else:
                                     
                                    if user_dates[id_]['status']['cat']=='trial': 
                                        msg='💠 Su servicio gratis ha concluido, el precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛'
                                        user_dates[id_]['status']['cat_historial']=['trial']
                                        keyboard_inline = [Button.inline(translate('👛 Pagar',lg), data=b'buy_premium1')]
                                        print(id_)
                                        try:
                                            await bot_.send_message(int(id_), translate(msg,lg),buttons=keyboard_inline,parse_mode='html')   
                                        except Exception as e:
                                            print(e)
                                    user_dates[id_]['status']['lote']=0
                                    user_dates[id_]['status']['buyed']=0
                                    user_dates[id_]['status']['cat']='basic'  
                                
                                              
                    if 'invoice_id' in user_dates[id_] and user_dates[id_]['invoice_id']!="None":
                        
                        actual_time=time.time()
                        '''
                        if 'invitator' not in user_dates[id_]:
                            user_dates[id_]['invitator']="None"
                                                         
                        if 'saldo' not in user_dates[id_]:
                                user_dates[id_]['saldo']=0
                        if 'saldo_ref' not in user_dates[id_]:
                                user_dates[id_]['saldo_ref']=0

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
                                if user_dates[id_]['status']['cat']=='premium_shared': 
                                    sharer=user_dates[id_]['status']['sharer']
                                    if user_dates[sharer]['status']['cat']=='basic' :
                                        user_dates[id_]['status']['cat']='basic'
                                        
                                        user_dates[id_]['status']['sharer']='None'
                                          
                                        user_dates[id_]['status']['lote']=0
                                        user_dates[id_]['status']['buyed']=0
                                        
                                else:
                                     
                                    if user_dates[id_]['status']['cat']=='trial': 
                                        msg='💠 Su servicio gratis ha concluido, el precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛'
                                        user_dates[id_]['status']['cat_historial']=['trial']
                                        keyboard_inline = [Button.inline(translate('👛 Pagar',lg), data=b'buy_premium1')]
                                        await bot_.send_message(int(id_), translate(msg,lg),buttons=keyboard_inline,parse_mode='html')   
                                    user_dates[id_]['status']['lote']=0
                                    user_dates[id_]['status']['buyed']=0
                                    user_dates[id_]['status']['cat']='basic'  
                                
                        '''    
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
                                        if 'saldo_ref' not in user_dates[str(user_dates[id_]['invitator'])]:
                                            user_dates[str(user_dates[id_]['invitator'])]['saldo_ref']=0

                                        user_dates[str(user_dates[id_]['invitator'])]['saldo_ref']+=float(payed_usd)*0.25
                                    
            
                                    user_dates[id_]['invoice_id']="None"
                                   
                                    user_dates[id_]['status']['cat']='premium' 
                                    print(round(float(payed_usd)))
                                    if int(payed_usd)==5:
                                        
                                        user_dates[id_]['status']['lote']+=60*60*24*25
                                        if  user_dates[id_]['status']['buyed']==0:
                                                user_dates[id_]['status']['buyed']=time.time()
                                        user_dates[id_]['status']['sharer']='None'
                                    if int(payed_usd)==9:
                                        user_dates[id_]['status']['lote']+=60*60*24*50
                                        if  user_dates[id_]['status']['buyed']==0:
                                                user_dates[id_]['status']['buyed']=time.time()
                                        user_dates[id_]['status']['sharer']='None'
                                    if int(payed_usd)==12:
                                        user_dates[id_]['status']['lote']+=60*60*24*75
                                        if  user_dates[id_]['status']['buyed']==0:
                                            user_dates[id_]['status']['buyed']=time.time()
                                        user_dates[id_]['status']['sharer']='None'
                                    fecha = datetime.fromtimestamp(user_dates[id_]['status']['buyed']+user_dates[id_]['status']['lote'])


                                    fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                                    if  user_dates[id_]['status']['lote']==0:
                                        fecha_formateada="No premium activo"
                                        
                                     
                                    msg=f"----------PAYED-------------\nReal_recived={payed_usd}USD\nFee:{fee_usd}\nCripto:{cripto_payed}\nStatus: {user_dates[id_]['status']['cat']} \nVencimiento del premium: {fecha_formateada}"
                                    msg=f'🎉 ¡Disfrute su suscripción!\n\n• Crypto - {cripto_payed}\n• Pagado - {payed_usd} USD\n• Suscripción - {user_dates[id_]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}'  
                                    await bot_.send_message(int(id_), translate(msg,lg),parse_mode='html')
                                    await upload_db()
                                else:
                                    print("No pay")
                            else:
                                print('Error')
                            
      
                        
                      
        except Exception as e:
            print(e)
                   
            
        
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
    months=1
    if amount>5:
        months+=1
    if amount>9:
        months+=1  
    create_dates=crear_factura(amount,test_mode)
    id=create_dates['invoice_id']
    pay_url=create_dates['bot_invoice_url']
    user_dates[user_id]['invoice_id']=id
    await event.respond(translate(f'🔖 ¡<b>Factura de pago</b>!\n\n• Tipo - Crypto\n• Pago - {amount} USD\n• Tiempo - {months} Mes\n• Suscripción - Premium',lg), buttons=[(Button.url(translate('👛 Pagar Factura',lg), pay_url))],parse_mode='html')
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
    await event.respond(translate('🌏 Seleccione un Idioma:',lg),buttons=keyboard ,parse_mode='html')


async def check_subscription(user_id,channel_id):
    client_ = TelegramClient('admin_check', api_id, api_hash)
    
    while True:
            #break
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
        #user = await client_.get_entity(user_id)
        participants = await client_.get_participants(channel)
        user_ids = [participant.id for participant in participants]
        print(user_ids)
        if str(user_id) in user_ids or int(user_id) in user_ids:
            print("El usuario está suscrito al canal.")
            await client_.disconnect()
            return True 

        else:
            print("El usuario no está suscrito al canal.")
            await client_.disconnect()
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
            if 'beginner_trial' not in user_dates[str(sender.id)]:
                user_dates[str(sender.id)]['beginner_trial']=True
            if user_dates[str(sender.id)]['beginner']:

                await select_lenguage(event)
                return 0
            keyboard = [[Button.text(translate('🧩 Conectar Cuenta',user_dates[str(sender.id)]['leng']),resize=True)],[Button.text(translate('💠 Conectar Canal',user_dates[str(sender.id)]['leng']),resize=True),Button.text(translate('〽️ Agregar Grupos',user_dates[str(sender.id)]['leng']),resize=True)],[Button.text(translate('⚙️ Configuración',user_dates[str(sender.id)]['leng']),resize=True)]]
            if beginner:
                
                keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1'),Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan')]
                #await event.respond(translate('💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛\n\nPrueba Gratis ✖️ 5 Días 🎉',user_dates[str(sender.id)]['leng']), buttons=keyboard_inline,parse_mode='html')
                await event.respond(translate('🤜🤛 Gracias por elegir @Camariobot!\n\n👣 Para comenzar a configurar su cuenta siga los siguientes pasos:\n\n#Paso1 - El primero de 3 simplemente pasos a seguir será conectar su cuenta de Telegram con nuestro bot!\n\n• /ConnectAccount\n\n#Paso2 - Debes agregar un canal el cual se utilizará para reenviar todas la publicaciones a todos los grupos agregados!\n\n• /AddChannel\n\n#Paso3 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado!\n\n• /AddGroups',user_dates[str(sender.id)]['leng']), buttons=keyboard,parse_mode='html')
            else:
                await event.respond(translate('Bienvenido',user_dates[str(sender.id)]['leng']), buttons=keyboard,parse_mode='html')
    #keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1'),Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan')]     
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
    id_chat=sender.id
    id_msg= user_dates[str(sender.id)]['connect_msg_id']
    '''
    try:
        await bot.delete_messages(entity=id_chat, message_ids=[id_msg])  
    except:
        print("error in delete") 
    '''
    comand=message.split(' ')
    if len(message.split(' '))==2:
        
        phone=comand[1]
        try:
            numero = int(phone)  # Intentar convertir a entero
        except ValueError:
            info='🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555'
            msg_send=await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
            user_dates[str(sender.id)]['connect_msg_id']=msg_send.id
            return 'not_number'
 
        phone_code_hash_=await user.send_code_request(phone)
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['phone']=phone
        user_dates[str(sender.id)]['phone_code_hash']=phone_code_hash_

        info='📨 Ingrese el código de inicio de sesión enviado a la aplicación Telegram o SMS (<b>Sin espacios</b>)\n\n• <b>Ejemplo</b>:\n\nSu código de inicio de sesión es <b>123456</b>, luego ingrese <b>mycode123456</b>\n\n🧩 Por favor, introduzca el código resivido:'
        msg_send=await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
        user_dates[str(sender.id)]['connect_msg_id']=msg_send.id
        #await bot.edit_message(id_chat, id_msg,translate(info,user_dates[user_id]['leng']),parse_mode='html')  
    else:
        info='🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555'
        msg_send=await event.respond(translate(info,user_dates[user_id]['leng']),parse_mode='html')
        user_dates[str(sender.id)]['connect_msg_id']=msg_send.id
        #await bot.edit_message(id_chat, id_msg,translate(info,user_dates[user_id]['leng']),parse_mode='html')   

        
   
    
    await user.disconnect()
    
@bot.on(events.NewMessage(pattern='/delgroup'))
async def delgroup(event):
    # Solicitar número de teléfono
    global user_dates
    
    sender = await event.get_sender()
    user_id=str(sender.id)
    if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
            
    lg=user_dates[user_id]['leng']
    
    message = event.raw_text
    comand=message.split('_')
    id_chat=sender.id
    id_msg= user_dates[str(sender.id)]['edit_groups_msg_id']
    chat_nottitle=translate('Titulo desconocido',lg)
    plant1=translate('Eliminar',lg)
    
    try:
        await bot.delete_messages(entity=id_chat, message_ids=id_msg)  
    except:
        print("error in delete") 
    if len(comand)==2:
        comand.pop(0)
        if comand[0]=='all':
            
            user_dates[str(sender.id)]['group_ids']=[]

            inf="Todos los grupos han sido eliminados"
            msg=translate(inf ,user_dates[user_id]['leng'])
            await event.respond(msg,parse_mode='html')
            await upload_db()
            return 0
            
        if "-" not in comand:
                comand="-"+str(comand[0])
                
        if 'group_ids' not in user_dates[str(sender.id)] :
           return 'no_dates'

        if int(comand) in user_dates[str(sender.id)]['group_ids']:
            user_dates[str(sender.id)]['group_ids'].remove(int(comand))
            id_chat=sender.id
            id_msg= user_dates[str(sender.id)]['edit_groups_msg_id']
            '''
            user = TelegramClient(str(sender.id), api_id, api_hash)
            
            try:
                    await user.connect()
            except:
                    await user.disconnect()
                    await asyncio.sleep(1)
                    await user.connect()
            '''
            
            groups=""
            if len(user_dates[str(sender.id)]['group_ids'])==0:
                groups="No tiene grupos"
                
            for group_id in user_dates[user_id]['group_ids']:
                                chat_entity_title=chat_nottitle
                                
                                try:
                                    '''
                                    chat_entity = await user.get_entity(int(group_id))
                                    username_=chat_entity.username
                                    chat_entity_title=chat_entity.title
                                    '''
                                    
                                    username_=ids_entity[str(group_id)]['username']
                                    if ids_entity[str(group_id)]['tittle']!="Desconocido":
                                        chat_entity_title=ids_entity[str(group_id)]['tittle']
                                    
                            #res= await user(GetFullChannelRequest(int(chat.id)))
                            #username_=res.chats[0].username
                                except:
                                
                                    username_=""
                                
                                groups+=f"/delgroup_{str(group_id).replace('-','')}  {plant1}: <a href='https://t.me/{username_}'>{chat_entity_title}</a>\n"
                                #print(groups)
                    
            #await user.disconnect()

            msg=groups
            msg_id=await send_(bot,int(sender.id),msg,event=event,keyboard=None)
      
            user_dates[str(sender.id)]['edit_groups_msg_id']=msg_id
            
            await upload_db()
        else:
            return 'no_dates'
          
                
        
        
        
    
@bot.on(events.NewMessage(pattern='/get_groups'))
async def get_groups(event):
    # Solicitar número de teléfono
    global user_dates
    global accounts_conected
    
    sender = await event.get_sender()
    ruta_original=f'{str(sender.id)}.session'
    ruta_copia=f'cache/{str(sender.id)}_gg.session'
    
    user_id=str(sender.id)
    id_us=user_id
    try:
            if str(id_us) in  accounts_conected:
                user=accounts_conected[str(id_us)]
                print(f'{str(id_us)} ya se encuentra conectada')
            else: 
                                          
                user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                                        
                accounts_conected[str(id_us)]= user
                accounts_conected[f'{str(id_us)}_lote']=time.time()+random.randint(300, 1000)
                print(f'{str(id_us)} NO se encuentra conectada')
    except Exception as e:
            print("Error in resesnd _connect")
            user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
            
    if not user.is_user_authorized:
        chat_id=int(id_us)
        mensaje="Su cuenta se ha desconectado por favor vuelva a conectarla"
        await bot.send_message(chat_id,mensaje,parse_mode='html')
        return 0
    
    while True:
        try:
                                        
                                        if not user.is_connected():
                                            await user.connect()
                                            print('Not conected.Conecting..') 
                                        break
        except Exception as e:
                                        print(f"Error en la conexion.#critic:{e}")

                                        await asyncio.sleep(2)
    
    chats = await user.get_dialogs()
    info=f"{translate('Grupos',user_dates[user_id]['leng'])}:\n"



    for chat in chats:
        if chat.is_group and not chat.entity.left:
        #if chat.is_group:
            
            try:
                chanel_entity = await user.get_entity(int(chat.id))
                username_=chanel_entity.username
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
            except:
                username_=""
            try:
                title=chat.title
            except:
                title="Desconocido"
            print(chat.id)
            info+=f"<code>{str(chat.id)}</code> <a href='https://t.me/{username_}'>{title}</a>\n"
            print(f'ID del grupo: {chat.id}, Nombre del grupo: {chat.title}')
            
    keyboard = [Button.inline(translate('🗑️ Eliminar Mensaje',user_dates[user_id]['leng']), data=b'del_groups_msg')]    
    #msg_send=await event.respond(info,buttons=keyboard,parse_mode='html')
    #msg_id=msg_send.id
    msg_id=await send_(bot,int(sender.id),info,event=event,keyboard=keyboard)
    if str(sender.id) not in user_dates:
        user_dates[str(sender.id)]={}
    user_dates[str(sender.id)]['groups_msg_id']=msg_id
    message = event.raw_text
    
      
    await user.disconnect()

    await upload_db()

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
  
@bot.on(events.NewMessage(pattern='/chunk'))
async def chunk_change(event):

    global user_dates
    chat = await event.get_chat()
    sender = await event.get_sender()
    user_id=str(sender.id)
    message = event.raw_text
    global chunk_size
    comand=message.split(' ')
    if len(comand)==2:
        comand.pop(0)
        if int(comand[0])>0:
            chunk_size=int(comand[0])
            msg=f"Chunks cambiados a {chunk_size}"
            await event.respond(translate(msg,user_dates[user_id]['leng']),parse_mode='html')
            
@bot.on(events.NewMessage(pattern='/id '))
async def add_chat(event):

    global user_dates
    chat = await event.get_chat()
    sender = await event.get_sender()
    user_id=str(sender.id)
    message = event.raw_text
    '''
    id_chat=sender.id
    id_msg=user_dates[str(sender.id)]['connect_group_msg_id']
    try:
        await bot.delete_messages(entity=id_chat, message_ids=[id_msg])  
    except:
        print("error in delete") 
    '''   
    comand=message.split(' ')
    if len(comand)>1:
        comand.pop(0)
        msg='〽️ <b>Grupos Agregados</b>!\n\n• Sus grupos:\n\n'
        for id_chat in comand:
            if "-" not in id_chat:
                id_chat="-"+str(id_chat).strip()
            if 'group_ids' not in user_dates[str(sender.id)]:
               user_dates[str(sender.id)]['group_ids']=[int(id_chat)]
            else:
                if int(id_chat) not in user_dates[str(sender.id)]['group_ids']:
                    user_dates[str(sender.id)]['group_ids'].append(int(id_chat))
            
            msg+=id_chat
            msg+='\n\n'
            
        msg+='✏️ <b>Puedes editar</b>, <b>agregar</b> <b>o</b> <b>eliminar grupos desde</b>:\n\n• /Editrogroup'
        keyboard=menu_system[0]
        user_dates[str(sender.id)]['group_ids']=list(set(user_dates[str(sender.id)]['group_ids']))
        #msg_send=await event.respond(translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        info=translate(msg,user_dates[user_id]['leng'])
        msg_send=await send_(bot,int(sender.id),info,event=event,keyboard=keyboard)
        #await bot.edit_message(id_chat, id_msg,translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        #user_dates[str(sender.id)]['connect_group_msg_id']=msg_send
        await get_entitys()
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
    global user_dates
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
            
    '''       
    id_chat=sender.id
    id_msg= user_dates[str(sender.id)]['connect_chan_msg_id']
    try:
        await bot.delete_messages(entity=id_chat, message_ids=[id_msg])  
    except:
        print("error in delete") 
    '''
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
                    
                    try:
                        chanel_entity = await user.get_entity(int(user_dates[str(sender.id)]['channel_ids'][0]))
                    except:
                        chanel_entity=user_dates[str(sender.id)]['channel_ids'][0]
                        
                    if sender.id not in channel_ids_swap:
                        channel_ids_swap[sender.id]=[]
                    if len(channel_ids_swap[sender.id])==0:
                        channel_ids_swap[sender.id].append(1)
                        
                    channel_ids_swap[sender.id].pop(0)
                    channel_ids_swap[sender.id].append(int(id_channel))
                    
                    try:
                        chan_user=chanel_entity.username
                    except:
                        chan_user="a"
                    keyboard = [Button.inline(translate('〽️ Si',user_dates[user_id]['leng']) ,data=b'yes_swap_channel'),Button.inline(translate('🚫 No',user_dates[user_id]['leng']), data=b'no_swap_channel')]
                    info=f'〽️ Usted ya configuro un canal de reenvío anteriormente!\n\n• <b>Su canal</b> - <a href="https://t.me/{chan_user}">{user_dates[str(sender.id)]["channel_ids"][0]}</a>\n\n⁉️ Deseas eliminar esté canal y configurar otro:'
                    msg_send=await event.respond(translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
                    #id_chat=sender.id
                    user_dates[str(sender.id)]['connect_chan_msg_id']=msg_send.id
                    #print(f"Sender {id_chat} {id_msg}")
                    #await bot.edit_message(id_chat, id_msg,translate(info,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
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
        msg_send=await event.respond(translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
        user_dates[str(sender.id)]['connect_chan_msg_id']=msg_send.id
        #id_chat=sender.id
        #id_msg= user_dates[str(sender.id)]['connect_chan_msg_id']
        #print(f"Sender {id_chat} {id_msg}")
        #await bot.edit_message(id_chat, id_msg,translate(msg,user_dates[user_id]['leng']),buttons=keyboard,parse_mode='html')
     
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
     
   
    author=event.message.post_author
    
   
    
    print(f'Author: {author}')
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
                '''
                try:
                    entity =await bot.get_entity(int(key))
                    public_name=entity.first_name
                    if public_name==author:
                        is_configured=True
                        user_id=key
                        if user_id not in user_dates:
                    
                            user_dates[user_id]={}
                            
                        if 'pending_messages' not in user_dates[user_id]:
                    
                            user_dates[user_id]['pending_messages']=[]
                
                except Exception as e:
                    print(f'error: {e}')     
                '''   
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
                user_dates[user_id]['pending_messages']=[]
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
                '''
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
                date_in={'time':timestamp,'msg':msg,'event':'not_remitent'}
                #date_in={'time':timestamp,'msg':msg,'event':event.message}
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
                    
'''             

                user_dates[user_id]['msg_created']=msg
                
                #msg=await bot.forward_messages(-1002022055141, event.message)
                user_dates[user_id]['pending_messages']=[]
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
               # date_in={'time':timestamp,'msg':msg,'event':msg}
                date_in={'time':timestamp,'msg':'create_msg','event':event.message}
                global state
                state=False
                await asyncio.sleep(3)
                user_dates[user_id]['pending_messages'].append(date_in)
                await upload_db()
                await asyncio.sleep(1)
                state=True
                if 'notifications' not in user_dates[user_id]:
                    user_dates[user_id]['notifications']=True
                info="Mensaje creado"
                if  user_dates[user_id]['notifications']:
                    await bot.send_message(int(user_id),translate(info ,user_dates[user_id]['leng']))
#Controlador de mensajes entrantes    
@bot.on(events.NewMessage())
@private_message_handler
async def handler(event):
    global first_init
    global admins
    sender = await event.get_sender()
    user_id=str(sender.id)
    await init_dates()
    message = event.raw_text
    if "-" not in str(sender.id) and "/start" not in message :
        
        global user_dates
        if str(sender.id) not in user_dates:
            
            user_dates[str(sender.id)]={}
        if 'beginner' not in user_dates[user_id]:
            user_dates[user_id]['beginner']=True
            user_dates[user_id]['beginner_trial']=True
        if 'status' not in user_dates[user_id]:
            user_dates[user_id]['status']={} 
            user_dates[user_id]['status']['cat']='basic'    
            user_dates[user_id]['status']['lote']=0
            user_dates[user_id]['status']['buyed']=0
            
        if 'saldo' not in user_dates[str(sender.id)]:
            user_dates[str(sender.id)]['saldo']=0
        
        if 'leng' not in user_dates[user_id]:
            user_dates[user_id]['leng']='spanish'
        if 'historial_' not in user_dates[user_id]:
            user_dates[user_id]['historial_']=[]
        lg=user_dates[user_id]['leng']
            
        # Este bloque de código se ejecutará cada vez que llegue un nuevo mensaje
        chat = await event.get_chat()
    
        
        
        #user = TelegramClient(str(sender.id), api_id, api_hash)
        #await user.connect()
        if message in traduct_menu["👛 Suscripción"] or message=='/pay':

                keyboard = [[Button.inline(translate('1 Month - $5',lg), data=b'buy_premium1')],[Button.inline(translate('2 Meses - $9',lg), data=b'buy_premium2'),Button.inline(translate('3 Meses - $12',lg), data=b'buy_premium3')]] 
                info="👛 Elige un período de suscripción:"
                await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')  
                return 0
            
        all_public_option=False
        if admin_comand in message or message in traduct_menu['🧩 Conectar Cuenta'] or message=='/ConnectAccount' or  message in traduct_menu['🚫 Cancelar'] or message in traduct_menu['〽️ Agregar Grupos'] or message=='/AddGroups' or message in traduct_menu['🕖 Reenvío'] or  message in traduct_menu['🔰 Referidos'] or message=='/reff' or 'mycode' in message or 'mypass' in message or  message in traduct_menu['🔙 Volver'] or  message in traduct_menu['🔝 Menú principal'] or  message in traduct_menu['💠 Conectar Canal'] or message=='/AddChannel' or '/channel' in message or '/id' in message:
            all_public_option=True
              
        if user_dates[user_id]['status']['cat']!='basic' or (user_id in admins) or user_dates[user_id]['beginner'] or all_public_option: 
            if user_dates[user_id]['beginner_trial'] and (admin_comand not in message) and (user_id not in admins):
                keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1'),Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan')]
               
                await event.respond(translate('#💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛\n\nPrueba Gratis ✖️ 5 Días 🎉',user_dates[str(sender.id)]['leng']), buttons=keyboard_inline,parse_mode='html')
                
            if message in traduct_menu['🧩 Conectar Cuenta'] or message=='/ConnectAccount':
                user_dates[str(sender.id)]['historial_cancel']=[0]
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
                    msg_send=await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html',link_preview=False)
                    msg_id=msg_send.id
                    user_dates[str(sender.id)]['connect_msg_id']=msg_id
                    
                await user.disconnect()
        

            elif message in traduct_menu['🚫 Cancelar']:
                keyboard = await menu_action('cancel',event)
                await event.respond(translate('🚫 Cancel',lg),buttons=keyboard)
                user_dates[user_id]['historial_']=[]
            
            elif message in traduct_menu['💠 Conectar Canal'] or message=='/AddChannel':
                user_dates[str(sender.id)]['historial_cancel']=[0]
                keyboard = [Button.inline(translate('💠 Conectar Canal' ,lg),data=b'add_channel')]
                info='💠 <b>Utilice esto para forjar una conexión entre su canal y </b>@CamarioBot.\n\n• Una conexión con al menos un canal es esencial para utilizar los servicios de reenvío automático.\n\n🤖 <b>@Camariobot</b><b> deberá ser añadido como administrador en el canal configurado</b>!\n\n• Si no añade @Camariobot los servicios no funcionarán con normalidad.\n\n💡 <b>Parámetros de Conexión</b>:\n\n<code>/channel</code> (ID del Canal)\n\n• <b>Ejemplo</b>:\n\n/channel 1002065562952\n\n🔍 <b>Localice el ID de su canal utilizando </b>@ScanIDBot.\n\n• ¿No estás seguro de cómo proceder?Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n💠 <b>Conecte</b> <b>un Canal</b>:'
                msg_send=await event.respond(translate(info ,lg) ,buttons=keyboard,parse_mode='html',link_preview=False)
                msg_id=msg_send.id
                user_dates[str(sender.id)]['connect_chan_msg_id']=msg_id
            elif message in traduct_menu['〽️ Agregar Grupos'] or message=='/AddGroups':  
                user_dates[str(sender.id)]['historial_cancel']=[0]
                keyboard = [[Button.inline(translate('〽️ Agregar Grupos' ,lg),data=b'add_group')]]
                info='〽️ ¡<b>Agrega el ID de los grupos a los cuales se reenviarán las publicaciones</b>!\n\n• Deberá ser miembro de todos los grupos agregados.\n\n• No existe un límite de grupos para reenviar publicaciones.\n\n• Para editar, eliminar o agregar nuevos grupos debera dirigirse ha "⚙️Configuración".\n\n💡 <b>Parámetros de Conexión</b>:\n\n/id (ID de los grupos, separe con un espacio cada ID)\n\n• <b>Ejemplo</b>:\n\n/id 1001256118443 1001484740111\n\n• ¿No estás seguro de cómo proceder? Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n〽️ <b>Agregue los Grupos</b>:'
                msg_send=await event.respond(translate(info ,lg),buttons=keyboard,parse_mode='html',link_preview=False)
                msg_id=msg_send.id
                user_dates[str(sender.id)]['connect_group_msg_id']=msg_id
            elif message in traduct_menu['⚙️ Configuración']:
                
               
                keyboard = await get_custom_menu(event)
                user_dates[str(sender.id)]['historial']=[0]
                keyboard=keyboard[1]
                await event.respond(translate("⚙️ Configuración",lg),buttons=keyboard,parse_mode='html')
                
        
       # elif message in traduct_menu['💼 Billetera']:
       #     keyboard = [Button.inline(translate('👛 Fondos',lg), data=b'founds')]
        #    info='💷 0.00 TRX\n\n💶 0.00 USDT'
        #    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')
        #    await deposit_solicity(event,1)
        
            elif message in traduct_menu['👁️ Remitente']:
                user_dates[str(sender.id)]['historial_cancel']=[1]

                if str(sender.id) not in user_dates:
                    user_dates[str(sender.id)]={}
                if 'remitent' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['remitent']=True
                    
                
                if user_dates[str(sender.id)]['remitent']:
                   msg='📬 ¡<b>Actualmente estás mostrando el Remitente</b>!\n\n• Nota:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis premium.'  
                   keyboard = [Button.inline(translate('📫 Ocultar Reemitente',lg), data=b'off_remitent')]
                else:
                    msg='📫 ¡<b>Actualme mantienes el reemitente oculto</b>!\n\n• Nota:\n\nAl mantener el reemitente oculto el mensaje dejará de mostrar contenido relevante como emojis premium!'
                    keyboard = [Button.inline(translate('📬 Mostrar Reemitente',lg), data=b'on_remitent')]
                #msg=f'📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - {state}'
                #keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline(translate('🌑 Off',lg), data=b'off_remitent')]
                msg_send=await event.respond(translate(msg,lg), buttons=keyboard,parse_mode='html')
                msg_id=msg_send.id

                
                user_dates[str(sender.id)]['remitent_msg_id']=msg_id
                await upload_db()


            elif message in traduct_menu['⏳ Espera']:
                user_dates[str(sender.id)]['historial_cancel']=[1]
                
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
            
            elif message in traduct_menu['🕖 Reenvío']:
                user_dates[str(sender.id)]['historial_cancel']=[1]
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
            
            
            elif message in traduct_menu['✏️ Editar Grupos'] or message=='/Editrogroup':
                user_dates[str(sender.id)]['historial_cancel']=[1]
                keyboard = [Button.inline(translate('✏️ Editar Grupos',lg), data=b'edit_groups')]
                groups=""
                print(user_dates)
                if 'group_ids' in  user_dates[str(sender.id)]:
                    
                    for group_id in user_dates[str(sender.id)]['group_ids']:
                        groups+=f'{str(group_id)}\n'
                    if len(user_dates[str(sender.id)]['group_ids']) ==0:
                        groups="No hay grupos configurados\n" 
                        groups=translate(groups,lg)
                        
                else:
                    
                    groups="No hay grupos configurados\n" 
                    groups=translate(groups,lg)
                
                
                info=f'〽️ <b>Actualmente los grupos agregados son</b>:\n\n{groups}\n✏️ <b>Edita</b>, <b>agrega o elimina grupos desde el botón</b>:'
                info=translate(info,lg)
                #await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')   
                await send_(bot,int(sender.id),info,event=event,keyboard=keyboard)
                
            elif message in traduct_menu['🔰 Referidos'] or message=='/reff':
                keyboard = [Button.inline(translate('🔗 Generar Enlace',lg), data=b'generate_ref_link')]
                info=f'🔰 ¡Gane el 25% de los fondos aumentados por sus referidos!\n\n• <b>Referidos</b> - {len(tree_ref(str(sender.id))[0])}\n\n• <b>Comisiones</b> - {str(tree_ref(str(sender.id))[1])} USD\n\n👛 Los Referidos existen para brindarle la oportunidad de adquirir suscripciónes de pago gratis!'
                msg_ref_send=await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')  
              
                msg_ref_id=msg_ref_send.id
                user_dates[user_id]['ref_url_id']=msg_ref_id
            
            elif message in traduct_menu['Siguiente ➡️']:
                keyboard = await get_custom_menu(event)
                user_dates[str(sender.id)]['historial']=[1]
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
                #keyboard = await get_custom_menu(event)
                chanel_id=-1002022055141
                chanel_id=-1002017124784
                us_id=int(sender.id)
                
                resp=await check_subscription(us_id,chanel_id)
                if not resp:
                    info='💠 Suscríbase para utilizar esta opcion:\n\n👉 @CamarioForward'
                    msg=translate(info ,lg)
                    keyboard_inline = [Button.inline(translate('☑️ Listo',lg), data=b'check_subscribed_createmsg')]
                    msg_trial_send=await event.respond(translate(info,lg),buttons=keyboard_inline,parse_mode='html')
                    msg_trial_id=msg_trial_send.id
                    user_dates[user_id]['check_sub_createmsg_id']=msg_trial_id
                    
                else:    
                    user_dates[str(sender.id)]['historial_cancel']=[2]
                    user_dates[user_id]['historial_']=['🔖 Crear Mensaje']
                    keyboard = [Button.text(translate('🚫 Cancel',lg),resize=True)]
                    info='✍️ ¡<b>Escriba y envié un nuevo mensaje</b>!\n\n• También puedes Reenviar texto desde otro chat o canal:'
                    
                    await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 

            elif message in traduct_menu['📮 Notificaciones']:
                #keyboard = await get_custom_menu(event)
                user_dates[str(sender.id)]['historial_cancel']=[2]
                if str(sender.id) not in user_dates:
                    user_dates[str(sender.id)]={}
                if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
                    
                #state='🌑Apagar'
                if user_dates[str(sender.id)]['notifications']:
                    keyboard = [Button.inline(translate('📪 Dejar de Recibir',lg), data=b'off_notif')]
                    info='📨 ¿<b>Deseas dejar de recibir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
                else:
                    keyboard = [Button.inline(translate('📨 Recibir Notificaciones',lg), data=b'on_notif')]
                    info='📪 ¡<b>Actualmente no estás recibiendo notificaciones</b>!\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
                    
               
                msg_send=await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
                msg_id=msg_send.id
                user_dates[str(sender.id)]['notifications_msg_id']=msg_id
                await upload_db()
            
                        
            elif message in traduct_menu['🔘 Pausar Reenvío']:
                #keyboard = await get_custom_menu(event)
                user_dates[str(sender.id)]['historial_cancel']=[2]
                keyboard = [Button.inline(translate('⚠️ Pausar Reenvío',lg), data=b'pause_auto_send')]
                info='‼️ ¿<b>Estás seguro de pausar el reenvío de mensajes automáticos</b>?\n\n• Nota:\n\n¡Luego de pausar el reenvío podrás reanudarlo desde aquí!\n\n⚠️ <b>Pause el reenvío</b>:'
               

                
                if str(sender.id) not in user_dates:
                    user_dates[str(sender.id)]={}
                if 'resend_loop' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['resend_loop']=0
                    
                
                if user_dates[str(sender.id)]['resend_loop']==0:
                    keyboard = [Button.inline(translate('💠 Activar',lg), data=b'on_auto_resend')]
                    info='⚠️ ¡<b>Actualmente el reenvío automático está pausado</b>!\n\n• Nota:\n\n¡Aunque el reenvío este en pausa el plan de suscripción sigue contando!\n\n💠 <b>Active el reenvío</b>:'
                    
                else:
                    keyboard = [Button.inline(translate('⚠️ Pausar Reenvío',lg), data=b'pause_auto_send')]
                    info='💠 ¡<b>Actualmente el reenvío automáticos está funcionando</b>!\n\n• Nota:\n\n¡Luego de pausar el reenvío podrás reanudarlo desde aquí!\n\n⚠️ <b>Pausar el reenvío</b>:'
                    
                msg_send=await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html')     
               
                
                msg_id=msg_send.id
                user_dates[str(sender.id)]['pause_auto_msg_id']=msg_id
                await upload_db()
                
            elif message in traduct_menu['🖲️ Compartir Suscripción']:
                #keyboard = await get_custom_menu(event)
                user_dates[str(sender.id)]['historial_cancel']=[2]
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
                    id_chat=sender.id
                    id_msg= user_dates[str(sender.id)]['connect_msg_id']
        
                    await bot.edit_message(id_chat, id_msg,translate(info,lg),parse_mode='html')
                    #await event.respond(translate(info,lg),parse_mode='html') 
            
            elif message=='/help':
                info='📨 Estás presentando problemas, tienes dudas, sugerencias, contáctenos de inmediato:'
                keyboard=[[Button.url(translate('🔖 Support',lg),'https://t.me/CamarioAdmin')],[Button.url(translate('💠 Channel',lg),'https://t.me/Camario'),Button.url(translate('💭 Group',lg),'https://t.me/CamarioChat')]]

                await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
            
            elif admin_comand in message:
                comand=message.split(' ')
                info="Ascendido a administrador"
                if len(comand)>1:
                    
                    admins.append(str(comand[1]))
                await event.respond(translate(info,lg), parse_mode='html') 
            elif '/Share' in message:
                
                comand=message.split(' ')
                if len(comand)>1:
                    if len(comand)>4:
                        return 0
                    if user_dates[str(sender.id)]['status']['cat']=='premium':
                        comand.pop(0)
                        if 'share_accounts' in user_dates[str(sender.id)]:
                            for shared_ in user_dates[str(sender.id)]['share_accounts']:
                                if user_dates[str(shared_)]['status']['cat']=='premium_shared' and user_dates[str(shared_)]['status']['sharer']==str(sender.id):
                                    user_dates[str(shared_)]['status']['sharer']='None'
                                    user_dates[str(shared_)]['status']['cat']='basic'
                                    
                        user_dates[str(sender.id)]['share_accounts']=[]  
                        msg='〽️ <b>Cuentas Agregadas</b>!\n\n• Sus cuentas:\n\n'
                        for id_chat in comand:
                            id_=str(id_chat)
                            if 'status' not in user_dates[id_]:
                                user_dates[id_]['status']={} 
                                user_dates[id_]['status']['cat']='basic'    
                                user_dates[id_]['status']['lote']=0
                                user_dates[id_]['status']['buyed']=0
                            #if 'share_accounts' not in user_dates[str(sender.id)]:
                            #    user_dates[str(sender.id)]['share_accounts']=[int(id_chat)]
                            #else:
                            if   user_dates[str(id_chat)]['status']['cat']!='premium':
                                if 'sharer' not in user_dates[str(id_chat)]['status']:
                                    user_dates[str(id_chat)]['status']['sharer']='None'
                                if user_dates[str(id_chat)]['status']['sharer']=='None':
                                    msg+=id_chat
                                    user_dates[str(sender.id)]['share_accounts'].append(int(id_chat))
                                    user_dates[str(id_chat)]['status']['cat']='premium_shared'
                                    user_dates[str(id_chat)]['status']['sharer']=str(sender.id)
                                    user_dates[str(id_chat)]['beginner_trial']=False
                                else:
                                    msg+=f'{id_chat} Ya posee un plan premium compartido' 
                                    
                            else:
                                msg+=f'{id_chat} Ya posee un plan premium' 
                            
                            msg+=id_chat
                            msg+='\n\n'
                        await event.respond(translate(msg,lg),parse_mode='html')   
                        await upload_db()
                    else:
                        msg='Usted no posee un plan premium'
                        await event.respond(translate(msg,lg),parse_mode='html') 
                        
                
            elif message=='/close':
                
                keyboard=await get_custom_menu(event)
                keyboard=keyboard[0]
                
                    
                keyboard_inline=[Button.inline(translate('🔘 Desconectar',lg), data=b'close_session'),Button.inline(translate(' 🚫 Cancelar',lg), data=b'cancel_session')]
                info='⁉️ ¿Estás seguro de que deseas desconectar tu cuenta?\n\n• Ten en cuenta que perderás todos los datos.'

                msg_send=await event.respond(translate(info,lg), buttons=keyboard_inline,parse_mode='html') 
                msg_id=msg_send.id
                user_dates[str(sender.id)]['close_msg_id']=msg_id
                await upload_db()
                await upload_sessiondb()
            elif len(user_dates[user_id]['historial_'])>0:
                print('added')
                if  user_dates[user_id]['historial_'][0]=='🔖 Crear Mensaje':
                    user_dates[user_id]['historial_']=[]
                    
                    await send_anounce(event)
            print(f"ad:{user_dates[user_id]['historial_']}")       
                
        #await user.disconnect()
        else:
            keyboard = await get_custom_menu(event)
            keyboard=keyboard[1]
            keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]
            info='💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛'
            await event.respond(translate(info,lg),buttons=keyboard_inline,parse_mode='html')  
                
            
#Controlador de menu 
async def menu_action(action,event):
    sender = await event.get_sender()
    if action=='back':
        if 'historial' not in user_dates[str(sender.id)]:
            user_dates[str(sender.id)]['historial']=[0]
        if len(user_dates[str(sender.id)]['historial'])==0:
            user_dates[str(sender.id)]['historial']=[0]
        men_=await get_custom_menu(event)
        idx=user_dates[str(sender.id)]['historial'][0]
        men_ant=men_[idx]
        if idx>0:
            idx-=1
        user_dates[str(sender.id)]['historial']=[idx]
        return men_ant
        
    if action=='home':
        men_=await get_custom_menu(event)
        
        return men_[0]
        
    if action=='cancel':
        
        if 'historial_cancel' not in  user_dates[str(sender.id)]:
            user_dates[str(sender.id)]['historial_cancel']=[0]
        if len(user_dates[str(sender.id)]['historial_cancel'])==0:
            user_dates[str(sender.id)]['historial_cancel']=[0]
        men_=await get_custom_menu(event)
        
        return men_[ user_dates[str(sender.id)]['historial_cancel'][0]]
        
    
     
        
#Manejador de callbacks     
@bot.on(events.CallbackQuery)
async def callback_handler(event):
    global user_dates
    global admins
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
    
    all_public_option=False
    if event.data == b'buy_premium1' or event.data == b'buy_premium2' or b'buy_premium3' or event.data == b'check_subscribed' or event.data ==  b'trial_plan' or event.data == b'yes_auto_send_ref_link' or event.data == b'auto_send_ref_link' or event.data == b'generate_ref_link' or b'more_time' or event.data == b'connect' or event.data == b'add_group' or event.data == b'add_channel' or event.data == b'yes_swap_channel' or event.data == b'no_swap_channel' : 
        all_public_option=True
    if (user_dates[user_id]['status']['cat']=='basic' and user_id not in admins and not user_dates[str(sender.id)]['beginner'] and not  user_dates[str(sender.id)]['beginner_trial'] and not all_public_option) :
        keyboard = await get_custom_menu(event)
        keyboard=keyboard[1]
        if event.data == b'buy_premium1':
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<5:
                await deposit_solicity(event,5) 
            else:
                user_dates[user_id]['saldo_ref']-=5
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*25
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=5
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await bot.send_message(int(user_id), translate(msg,lg),parse_mode='html')
                await upload_db()
            return 0
        if event.data == b'buy_premium2': 
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<9:
                await deposit_solicity(event,9) 
            else:
                user_dates[user_id]['saldo_ref']-=9
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*50
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=9
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await bot.send_message(int(user_id), translate(msg,lg),parse_mode='html')
                await upload_db()  
            return 0
        if event.data == b'buy_premium3': 
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<12:
                await deposit_solicity(event,12) 
            else:
                user_dates[user_id]['saldo_ref']-=5
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*75
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=75
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await bot.send_message(int(user_id), translate(msg,lg),parse_mode='html')
                await upload_db()
            return 0 
        keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1')]
        info='💠 El precio para utilizar los servicios de @Camariobot es de:\n\n5 USD ✖️ 1 Mes 👛'
        await event.respond(translate(info,lg),buttons=keyboard_inline,parse_mode='html')  
        
        return 0
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
    if user_dates[user_id]['beginner_trial'] and  event.data !=  b'trial_plan' and event.data != b'check_subscribed' and user_id not in admins:
                keyboard_inline = [Button.inline(translate('👛 Pagar',user_dates[str(sender.id)]['leng']), data=b'buy_premium1'),Button.inline(translate('🎉 Pagar',user_dates[str(sender.id)]['leng']), data=b'trial_plan')]
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
        #id_chat=sender.id
        #id_msg= user_dates[str(sender.id)]['connect_msg_id']
        
        #await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
       
    
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
       
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['connect_group_msg_id']
        try:
            await bot.delete_messages(entity=id_chat, message_ids=[id_msg])  
        except:
            print("error in delete") 
            
        #await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        msg_send=await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        msg_id=msg_send.id
        user_dates[str(sender.id)]['connect_group_msg_id']=msg_id
        await upload_db() 
    if event.data == b'add_channel':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='💠 <b>Recuerde añadir a </b><b>@Camariobot</b><b> en el canal</b> <b>agregado</b>!\n\n💡 <b>Deberás ingresar el ID del canal luego del comando</b> <code>/channel</code>\n\n• Ejemplo:\n\n/channel 1001368540342\n\n🔎 <b>Ingrese el</b> ID <b>del Canal</b>:'
      
        
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['connect_chan_msg_id']

        try:
            await bot.delete_messages(entity=id_chat, message_ids=[id_msg])  
        except:
            print("error in delete") 
        #await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        
        #print(f"Sender {id_chat} {id_msg}")
        msg_send=await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        msg_id=msg_send.id
        user_dates[str(sender.id)]['connect_chan_msg_id']=msg_id
        await upload_db() 
    if event.data == b'more_accounts':
        keyboard = [Button.text(translate('🚫 Cancel',lg), resize=True)]
        info='🆔 Envié el ID de las cuentas que deseas agregar:\n\n• Utilice @ScanIDBot Para obtener el ID de sus cuentas!\n\n🧩 Solo puedes agregar un máximo de 3 cuentas!\n\n/add (ID de sus cuentas, separe con un espacio cada ID) \n\n• Ejemplo:\n\n/add 1878166234 1459865634 181862566234\n\n🚫 Tenga en cuenta que tendrás que conectar cada cuenta con @Camariobot!\n\n• Esté menú no facilita la conexión entre cuentas, simplemente compartirá su suscripción con otras cuentas.\n\n🔎 Envié el ID de las Cuentas:'
        await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
    
    if event.data == b'generate_ref_link':
        id_chat=sender.id
        id_msg=user_dates[user_id]['ref_url_id']
        keyboard = [Button.inline(translate(' ♻️ Reenvio automatico',lg), data=b'auto_send_ref_link')]
        msg=f'https://t.me/Camariobot?start={sender.id}'
        #await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        await bot.edit_message(id_chat,id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        
    if event.data == b'auto_send_ref_link':
        id_chat=sender.id
        id_msg=user_dates[user_id]['ref_url_id']
        user_id=str(sender.id)
        if user_id not in user_dates:
            
            user_dates[user_id]={}
        if 'resend_loop' not in user_dates[user_id]:
            user_dates[user_id]['resend_loop']=0
            

        
        sleep_time=user_dates[user_id]['resend_loop']
        keyboard = [Button.inline(translate('♻️ Continuar',lg), data=b'yes_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        msg=f'♻️ Reenviaras tu enlace a todos los grupos con un intervalo de reenvío de {str(sleep_time/60)} Minutos.\n\n• Está acción es gratis\n\n⁉️ Deseas continuar con el reenvío:'
        #await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        await bot.edit_message(id_chat,id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        
    if event.data == b'yes_auto_send_ref_link':
        keyboard = [Button.inline(translate('♻️ Continuar',lg), data=b'cont_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        user_id=str(sender.id)
        id_chat=sender.id
        id_msg=user_dates[user_id]['ref_url_id']
        if user_id not in user_dates:
            
            user_dates[user_id]={}
                    
        if 'pending_messages' not in user_dates[user_id]:
                
            user_dates[user_id]['pending_messages']=[]
            

            
        if 'group_ids' not in  user_dates[user_id]:
            info='🔎 Necesitas agregar grupos para reenviar automáticamente su enlace a ellos!\n\n• /AddGroups'
            #await event.respond(translate(info,lg),parse_mode='html') 
            await bot.edit_message(id_chat,id_msg,translate(info,lg),parse_mode='html')
        else:
            if len(user_dates[user_id]['group_ids'])==0:
                info='🔎 Necesitas agregar grupos para reenviar automáticamente su enlace a ellos!\n\n• /AddGroups'
                #await event.respond(translate(info,lg),parse_mode='html') 
                await bot.edit_message(id_chat,id_msg,translate(info,lg),parse_mode='html')
            else:
                timestamp=time.time()
                #date_in={timestamp:msg,'event':event.message}
                date_in={'time':timestamp,'msg':f'https://t.me/Camariobot?start={sender.id}','event':'not_remitent'}
                user_dates[user_id]['pending_messages'].append(date_in)
                await upload_db()
            
        
                
    if event.data == b'buy_premium1':
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<5:
                await deposit_solicity(event,5) 
            else:
                user_dates[user_id]['saldo_ref']-=5
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*25
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=5
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await event.respond(translate(msg,lg),parse_mode='html')
                await upload_db()
            
    if event.data == b'buy_premium2': 
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<9:
                await deposit_solicity(event,9) 
            else:
                user_dates[user_id]['saldo_ref']-=9
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*50
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=9
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await event.respond(translate(msg,lg),parse_mode='html')
                await upload_db()  
            
    if event.data == b'buy_premium3': 
            if 'status' not in user_dates[user_id]:
                user_dates[user_id]['status']={} 
                user_dates[user_id]['status']['cat']='basic'    
                user_dates[user_id]['status']['lote']=0
                user_dates[user_id]['status']['buyed']=0
            if 'saldo_ref' not in user_dates[user_id]:
                user_dates[user_id]['saldo_ref']=0
            if user_dates[user_id]['saldo_ref']<12:
                await deposit_solicity(event,12) 
            else:
                user_dates[user_id]['saldo_ref']-=5
                user_dates[user_id]['status']['cat']='premium'
                user_dates[user_id]['status']['lote']+=60*60*24*75
                if  user_dates[user_id]['status']['buyed']==0:
                    user_dates[user_id]['status']['buyed']=time.time()
                
                
                fecha = datetime.fromtimestamp(user_dates[user_id]['status']['buyed']+user_dates[user_id]['status']['lote'])


                fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')
                if  user_dates[user_id]['status']['lote']==0:
                    fecha_formateada="No premium activo"
                payed_usd=75
                                    
                                     
                msg=f'🎉 ¡Disfrute su suscripción!\n\n• Pagado - ={payed_usd} USD\n• Suscripción - {user_dates[user_id]["status"]["cat"]}\n• Vencimiento - {fecha_formateada}' 
                                    
                await event.respond(translate(msg,lg),parse_mode='html')
                await upload_db()
             
        
          
    if event.data == b'yes_swap_channel':
        
        user_dates[str(sender.id)]['channel_ids'][0]=channel_ids_swap[sender.id][0]
        keyboard=await get_custom_menu(event)
        keyboard=keyboard[0]
        await upload_db()
        info='〽️ Si\nNuevo canal configurado'
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['connect_chan_msg_id']
        #await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        
    if event.data == b'no_swap_channel':
        keyboard=menu_system[0]
        keyboard = [Button.inline(translate('🧩 Continuar',lg), data=b'cont_auto_send_ref_link'),Button.inline(translate('🚫 Cancelar',lg), data=b'can_auto_send_ref_link')]
        info='🚫 No\nNo se ha realizado ningun cambio'
        #await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['connect_chan_msg_id']
        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
    if event.data == b'del_groups_msg':
        del_list=user_dates[str(sender.id)]['groups_msg_id']
        del_list.append(del_list[0]-1)
        #await bot.delete_messages(sender.id, [user_dates[str(sender.id)]['groups_msg_id'],user_dates[str(sender.id)]['groups_msg_id']-1])
        await bot.delete_messages(sender.id, del_list)
        
    if event.data == b'on_remitent':
        keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline(translate('🌑 Off',lg), data=b'off_remitent')]
        if str(sender.id) not in user_dates:     
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['remitent']=True
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['remitent_msg_id']
        if user_dates[str(sender.id)]['remitent']:
            msg='📬 ¡<b>Actualmente estás mostrando el Remitente</b>!\n\n• Nota:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis premium.'  
            keyboard = [Button.inline(translate('📫 Ocultar Reemitente',lg), data=b'off_remitent')]
        else:
            msg='📫 ¡<b>Actualme mantienes el reemitente oculto</b>!\n\n• Nota:\n\nAl mantener el reemitente oculto el mensaje dejará de mostrar contenido relevante como emojis premium!'
            keyboard = [Button.inline(translate('📬 Mostrar Reemitente',lg), data=b'on_remitent')]
        await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'off_remitent':
        keyboard = [Button.inline(translate('🟢 On',lg), data=b'on_remitent'),Button.inline('🌑 Off', data=b'off_remitent')]
        if str(sender.id) not in user_dates:     
            user_dates[str(sender.id)]={}
            
        user_dates[str(sender.id)]['remitent']=False
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['remitent_msg_id']
        if user_dates[str(sender.id)]['remitent']:
            msg='📬 ¡<b>Actualmente estás mostrando el Remitente</b>!\n\n• Nota:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis premium.'  
            keyboard = [Button.inline(translate('📫 Ocultar Reemitente',lg), data=b'off_remitent')]
        else:
            msg='📫 ¡<b>Actualme mantienes el reemitente oculto</b>!\n\n• Nota:\n\nAl mantener el reemitente oculto el mensaje dejará de mostrar contenido relevante como emojis premium!'
            keyboard = [Button.inline(translate('📬 Mostrar Reemitente',lg), data=b'on_remitent')]
        await bot.edit_message(id_chat,id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
        
    if event.data == b'on_notif':
      
        if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}
        if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
        
        user_dates[str(sender.id)]['notifications']=True      
        if user_dates[str(sender.id)]['notifications']:
            keyboard = [Button.inline(translate('📪 Dejar de Recibir',lg), data=b'off_notif')]
            info='📨 ¿<b>Deseas dejar de recibir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
        else:
            keyboard = [Button.inline(translate('📨 Recibir Notificaciones',lg), data=b'on_notif')]
            info='📪 ¡<b>Actualmente no estás recibiendo notificaciones</b>!\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
        
        id_chat=sender.id
        id_msg= user_dates[str(sender.id)]['notifications_msg_id']
        

        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'off_notif':
      
        if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}
        if 'notifications' not in user_dates[str(sender.id)]:
                    user_dates[str(sender.id)]['notifications']=True
        
        user_dates[str(sender.id)]['notifications']=False     
        if user_dates[str(sender.id)]['notifications']:
            keyboard = [Button.inline(translate('📪 Dejar de Recibir',lg), data=b'off_notif')]
            info='📨 ¿<b>Deseas dejar de recibir notificaciones</b>?\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
        else:
            keyboard = [Button.inline(translate('📨 Recibir Notificaciones',lg), data=b'on_notif')]
            info='📪 ¡<b>Actualmente no estás recibiendo notificaciones</b>!\n\n• Nota:\n\nSi dejas de recibir notificaciones no sabrás si su cuenta o el reenvío automático deja de funcionar por algún motivo.'
        
        id_chat=sender.id
        id_msg= user_dates[str(sender.id)]['notifications_msg_id']
        

        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        await upload_db()
        
    if event.data == b'pause_auto_send':
        keyboard = [Button.inline(translate('💠 Activar',lg), data=b'on_auto_resend')]
        info='⚠️ ¡<b>Actualmente el reenvío automático está pausado</b>!\n\n• Nota:\n\n¡Aunque el reenvío este en pausa el plan de suscripción sigue contando!\n\n💠 <b>Active el reenvío</b>:'
        user_id=str(sender.id)
        user_dates[user_id]['resend_loop_old']=user_dates[user_id]['resend_loop']
        user_dates[user_id]['resend_loop']=0
        user_dates[user_id]['pending_messages']=[]
        #await event.respond(translate(info,lg),buttons=keyboard,parse_mode='html')
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['pause_auto_msg_id']
        

        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        await upload_db()           
                    

    if event.data ==b'on_auto_resend':
        id_chat=sender.id
        id_msg=user_dates[str(sender.id)]['pause_auto_msg_id']
        if 'resend_loop_old' not in user_dates[user_id]:
            info='⚠️No hay un tiempo previo configurado'
            await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
            return 0
        user_dates[user_id]['resend_loop']=user_dates[user_id]['resend_loop_old']
        keyboard = [Button.inline(translate('⚠️ Pausar Reenvío',lg), data=b'pause_auto_send')]
        info='El reenvío de mensajes automáticos ha sido reanudado.Puede volver a pausarlo desde aqui</b>?\n\n• Nota:\n\n¡Luego de pausar el reenvío podrás reanudarlo desde aquí!\n\n⚠️ <b>Pause el reenvío</b>:'
        info='💠 ¡<b>Actualmente el reenvío automáticos está funcionando</b>!\n\n• Nota:\n\n¡Luego de pausar el reenvío podrás reanudarlo desde aquí!\n\n⚠️ <b>Pausar el reenvío</b>:'
        #await event.respond(translate(info,lg), buttons=keyboard,parse_mode='html') 
        

        await bot.edit_message(id_chat, id_msg,translate(info,lg),buttons=keyboard,parse_mode='html')
        await upload_db() 
    if event.data ==  b'edit_groups':
            print(user_dates)
            user_id=str(sender.id)
            chat_nottitle=translate('Titulo desconocido',lg)
            plant1=translate('Eliminar',lg)
            groups=""

            if str(sender.id) not in user_dates:
                user_dates[str(sender.id)]={}

            if 'group_ids' in  user_dates[str(sender.id)]:
                if len(user_dates[str(sender.id)]['group_ids'])==0:
                    groups="No tiene grupos"
                '''
                ruta_original=f'{str(sender.id)}.session'
                ruta_copia=f'cache/{str(sender.id)}_edit_g.session'
                
                user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                #user = TelegramClient(str(sender.id), api_id, api_hash)

            
                while True:
                    try:
                                        
                                        if not user.is_connected():
                                            await user.connect()
                                            print('Not conected.Conecting..') 
                                        break
                    except Exception as e:
                                        print(f"Error en la conexion.#critic:{e}")

                                        await asyncio.sleep(2)
                
                '''
                for group_id in user_dates[user_id]['group_ids']:
                    chat_entity_title=chat_nottitle
                    
                    try:
                        '''
                        chat_entity = await user.get_entity(int(group_id))
                        username_=chat_entity.username
                        chat_entity_title=chat_entity.title
                        '''
                        
                        username_=ids_entity[str(group_id)]['username']
                        if ids_entity[str(group_id)]['tittle']!="Desconocido":
                            chat_entity_title=ids_entity[str(group_id)]['tittle']
                        
                #res= await user(GetFullChannelRequest(int(chat.id)))
                #username_=res.chats[0].username
                    except:
                       
                        username_=""
                    
                    groups+=f"/delgroup_{str(group_id).replace('-','')}  {plant1}: <a href='https://t.me/{username_}'>{chat_entity_title}</a>\n"
                    #print(groups)
                    
                #await user.disconnect()
                    
            else:
               groups=translate("No hay grupos configurados\n",lg) 
               
            #msg_send=await event.respond(translate(groups,lg),parse_mode='html')
            #msg_id=msg_send.id
            info=groups
            msg_id=await send_(bot,int(sender.id),info,event=event,keyboard=None)
      
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
    if event.data==b'cancel_session':
        msg=f'Cancelado' 
        id_chat=sender.id
        id_msg= user_dates[str(sender.id)]['close_msg_id']
    
        await bot.edit_message(id_chat, id_msg,translate(msg,lg),parse_mode='html')
    if event.data==b'close_session': 
                user_id=str(sender.id)
                file=f'{user_id}.session'
                keyboard=await get_custom_menu(event)
                keyboard=keyboard[0]
                if os.path.exists(file):
                    os.remove(file)
                    print("El archivo ha sido eliminado.")
               
                  
                    user_dates[user_id]['group_ids']=[]
                    user_dates[user_id]['pending_messages']=[]
                    user_dates[user_id]['sleep_time']=1
                    user_dates[user_id]['wait_time']=1
                    user_dates[user_id]['notifications']=True
                    user_dates[user_id]['resend_loop']=0
                    user_dates[user_id]['channel_ids']=[]
                    msg='‼️ ¡Cuenta Desconecta!\n\n• Precine el siguiente botón para reconectar su cuenta:'
                    id_chat=sender.id
                    id_msg= user_dates[str(sender.id)]['close_msg_id']
                    keyboard = [Button.inline(translate('🧩 Conectar Cuenta',lg), data=b'connect')]
                    await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
                    user_dates[str(sender.id)]['connect_msg_id']=id_msg
                    await upload_db()
                else:
                    print("El archivo no existe.")
                    msg='No posee cuenta conectada' 
                    id_chat=sender.id
                    id_msg= user_dates[str(sender.id)]['close_msg_id']
    
                    await bot.edit_message(id_chat, id_msg,translate(msg,lg),buttons=keyboard,parse_mode='html')
    if event.data ==  b'trial_plan':
        chanel_id=-1002065562952
        us_id=int(sender.id)
        id_=str(sender.id)
        resp=await check_subscription(us_id,chanel_id)
        
        if resp:
            if 'status' not in user_dates[id_]:
                    user_dates[id_]['status']={} 
                    user_dates[id_]['status']['cat']='basic'    
                    user_dates[id_]['status']['lote']=0
                    user_dates[id_]['status']['buyed']=0
            if user_dates[str(sender.id)]['beginner_trial']:

                    user_dates[str(sender.id)]['status']['cat']='trial' 
                    user_dates[str(sender.id)]['status']['lote']+=60*60*24*5
                    if  user_dates[user_id]['status']['buyed']==0:
                        user_dates[user_id]['status']['buyed']=time.time()
                    user_dates[str(sender.id)]['beginner_trial']=False
                    info='El plan de prueba vence en 5 dias'
                    msg=translate(info ,lg)
                    #id_chat=sender.id
                    #id_msg= user_dates[user_id]['check_sub_trial_id']
                    
                    #await bot.edit_message(id_chat,id_msg,msg,parse_mode='html')
                    user_dates[str(sender.id)]['beginner_trial']=False
                    #await upload_db()  
                    msg_trial_send=await event.respond(msg,parse_mode='html')
                    msg_trial_id=msg_trial_send.id
                    user_dates[user_id]['check_sub_trial_id']=msg_trial_id
                    

        else:
         
            info='💠 Suscríbase para utilizar nuestros servicios gratis:\n\n👉 @Camario'
            msg=translate(info ,lg)
            keyboard_inline = [Button.inline(translate('☑️ Listo',lg), data=b'check_subscribed')]
            msg_trial_send=await event.respond(translate(info,lg),buttons=keyboard_inline,parse_mode='html')
            msg_trial_id=msg_trial_send.id
            user_dates[user_id]['check_sub_trial_id']=msg_trial_id
        await upload_db()  
    if event.data == b'check_subscribed':
        chanel_id=-1002065562952
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
                    if  user_dates[user_id]['status']['buyed']==0:
                        user_dates[user_id]['status']['buyed']=time.time()
                    user_dates[str(sender.id)]['beginner_trial']=False
                    info='El plan de prueba vence en 5 dias'
                    msg=translate(info ,lg)
                    id_chat=sender.id
                    id_msg= user_dates[user_id]['check_sub_trial_id']
                    
                    await bot.edit_message(id_chat,id_msg,msg,parse_mode='html')
                    user_dates[str(sender.id)]['beginner_trial']=False
                    await upload_db()
                    
        else:
            
            info='⚠️ Suscríbase para utilizar nuestros servicios gratis:\n\n👉 @Camario'
            msg=translate(info ,lg)
            id_chat=sender.id
            id_msg= user_dates[user_id]['check_sub_trial_id']
            keyboard_inline = [Button.inline(translate('✔️ Listo',lg), data=b'check_subscribed')]
            await bot.edit_message(id_chat,id_msg,msg,buttons=keyboard_inline,parse_mode='html')

    if event.data == b'check_subscribed_createmsg':   
        chanel_id=-1002022055141
        chanel_id=-1002017124784
        us_id=int(sender.id)
                
        resp=await check_subscription(us_id,chanel_id)
        id_chat=sender.id
        id_msg= user_dates[user_id]['check_sub_createmsg_id']
                    
        if resp:
            info='Ya puede usar el servicio'
            msg=translate(info ,lg)

            await bot.edit_message(id_chat,id_msg,msg,parse_mode='html')
        else:
            info='⚠️ Suscríbase para utilizar esta opcion:\n\n👉 @CamarioForward'
            msg=translate(info ,lg)
            keyboard_inline = [Button.inline(translate('☑️ Listo',lg), data=b'check_subscribed_createmsg')]
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
        global accounts_conected
        bot_ =await TelegramClient('bot_', api_id, api_hash).start(bot_token=bot_token)
        while True:
            try:
                global user_dates
                
                
                print('.')
                if state:
                    
                    for id_us in  user_dates:
                        if id_us!='all_hashes' and id_us!="chat_ids":
                            '''
                            if f'{str(id_us)}_resend' in  accounts_conected:
                                if accounts_conected[f'{str(id_us)}_lote']<time.time():
                                                                          

                                    u_=accounts_conected[f'{str(id_us)}_resend']
                                    try:
                                            if u_.is_connected():
                                                await u_.disconnect()
                                                print(f'{str(id_us)} ha sido desconectada')
                                        
                                    except Exception as e:
                                            print(f"Error en la conexion en simulate desconexion.#critic:{e}")
                                        
                                        
                                        
                                    accounts_conected.pop(f'{str(id_us)}_resend')
                                    accounts_conected.pop(f'{str(id_us)}_lote')
                            '''          
                                        
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
                                    user_dates[id_us]['sleep_time']=5
                        
                                sleep_time= user_dates[id_us]['sleep_time']
                    
                                if 'wait_time' not in user_dates[id_us]:
                                    user_dates[id_us]['wait_time']=1
                        
                                wait_time= user_dates[id_us]['wait_time'] 
                                if 'resend_loop' not in user_dates[id_us]:
                                    user_dates[id_us]['resend_loop']=0
                                if 'notifications' not in user_dates[id_us]:
                                    user_dates[id_us]['notifications']=True
                                resend_loop= user_dates[id_us]['resend_loop']

                                #user = TelegramClient(str(id_us), api_id, api_hash)
                                ruta_original=f'{str(id_us)}.session'
                                ruta_copia=f'cache/{str(id_us)}_resend.session'
                                try:
                                    if str(id_us) in  accounts_conected:
                                        user=accounts_conected[str(id_us)]
                                        print(f'{str(id_us)} ya se encuentra conectada')
                                    else: 
                                          
                                        user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                                        
                                        accounts_conected[str(id_us)]= user
                                        accounts_conected[f'{str(id_us)}_lote']=time.time()+random.randint(300, 1000)
                                        print(f'{str(id_us)} NO se encuentra conectada')
                                except Exception as e:
                                    print("Error in resesnd _connect")
                                    user = TelegramClient(copy(ruta_original,ruta_copia), api_id, api_hash)
                                if not user.is_user_authorized:
                                    chat_id=int(id_us)
                                    mensaje="Su cuenta se ha desconectado por favor vuelva a conectarla"
                                    await bot.send_message(chat_id,mensaje,parse_mode='html')
                                    continue
                                while True:
                                    try:
                                        
                                        if not user.is_connected():
                                            await user.connect()
                                            print('Not conected.Conecting..') 
                                        break
                                    except Exception as e:
                                        print(f"Error en la conexion.#critic:{e}")

                                        await asyncio.sleep(2)
                                '''
                                while True:
                                    try:
                                        await user.connect()
                                        break
                                    except Exception as e:
                                        print(f"Error en la conexion.#critic:{e}")

                    
                                        try:
                                            await user.disconnect()
                                        except:
                                            print('error disconect')
                                        await asyncio.sleep(2)
                                
                                '''
                                msg_dates= user_dates[id_us]['pending_messages']
                                index=0
                                desv=0 
                                for msg_date in msg_dates:
                                    try:
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
                                                    error_groups=[]
                                                    #numeros_aleatorios = list(range(len(user_dates[id_us]['group_ids'])))
       
                                                    #random.shuffle(numeros_aleatorios)
                                                    #numeros_aleatorios = numeros_aleatorios[:len(user_dates[id_us]['group_ids'])]
                                                    #print(numeros_aleatorios)
                                                    #for group_id in user_dates[id_us]['group_ids']:
                                                    init_proc=time.time()
                                                    user_dates[id_us]['group_ids']=list(set(user_dates[id_us]['group_ids']))
                                                    
                                                    random.shuffle(user_dates[id_us]['group_ids'])
                                                    #chunk_size = 10
                                                    global chunk_size
                                                    for idx_ in range(0,len(user_dates[id_us]['group_ids']),chunk_size):
                                                        chunk =user_dates[id_us]['group_ids'][idx_:idx_+ chunk_size]
                                                       # camuf_idx=numeros_aleatorios[idx_]
                                                        print(f'idx{idx_}')
                                                        #group_id=user_dates[id_us]['group_ids'][camuf_idx]
                                                        #print(group_id)
                                                        try:
                                                            
                                                            if user_dates[id_us]['remitent'] and event_message!='not_remitent' and msg!='create_msg':
                                                                
                                                                await enviar_mensajes_concurrentes(chunk, "None", error_groups,user,event_message)
                                                            else:
                                                                if event_message=='not_remitent':
                                                                    #await user.send_message(int(group_id), msg,parse_mode='html')
                                                                    await enviar_mensajes_concurrentes(chunk, msg, error_groups,user,event_message)
                                                                else:
                                                                   
                                                                    
                                                                    msg_=await bot_.forward_messages(resend_channel,event_message)
                                                                    try:
                                                                        mes_= await enviar_mensajes_concurrentes(chunk, "None", error_groups,user,msg_)
                                                                    except Exception as e:
                                                                        print(f'Error {e}')
                                                                        not_errors=False
                                        
                                                                        
                                                                        try:
                                                                            #chanel_entity = await user.get_entity(int(group_id))
                                                                            #username_=chanel_entity.username
                                                                            username_=""
                                                                            #res= await user(GetFullChannelRequest(int(chat.id)))
                                                                            #username_=res.chats[0].username
                                                                        except:
                                                                            username_=""
                                                                        #error_groups+=f"<a href='https://t.me/{username_}'>{group_id}</a>\n"
                                                                        #error_groups+=f"{str(group_id)}\n"
                                                                        print(f"resend_error:{e}")
                                                                    er_id=0
                                                                    while True:
                                                                        er_id+=1
                                                                        if er_id==20:
                                                                            break
                                                                        try:
                                                                            await msg_.delete()
                                                                            break
                                                                        except:
                                                                            print('error in delete')
                                                            print('send')
                                                            
                                                            
                                                        except Exception as e:
                                                            not_errors=False
                             
                                                            
                                                            try:
                                                                #chanel_entity = await user.get_entity(int(group_id))
                                                                #username_=chanel_entity.username
                                                                username_=""
                                                                #res= await user(GetFullChannelRequest(int(chat.id)))
                                                                #username_=res.chats[0].username
                                                            except:
                                                                username_=""
                                                            #error_groups+=f"<a href='https://t.me/{username_}'>{group_id}</a>\n"
                                                            #error_groups+=f"{str(group_id)}\n"
                                                            print(f"resend_error:{e}")
                                                            
                                                       # await asyncio.sleep(sleep_time)
                                                    if len(error_groups)>0:
                                                        not_errors=False
                                                    if not_errors:
                                                        if user_dates[id_us]['notifications']:
                                                            await bot_.send_message(int(id_us),translate(f"Mensaje reenviado en : {time.time()-init_proc} segundos",lg),parse_mode='html')
                                                        if  resend_loop==0:
                                                            msg_dates.pop(index-desv)
                                                            desv+=1
                                                             
                                                        else:
                                                            print('loop_resend')
                                                            msg_date['time']=actual_time+resend_loop
                                                            
                                                    else:
                                                        if user_dates[id_us]['notifications']:
                                                            error_groups_=""
                                                            #for g in error_groups:
                                                             #  error_groups_+=str(g)
                                                            #   error_groups_+='\n' 
                                                            for group_id in error_groups:
                                                                
                                                                
                                                                try:

                                                                    
                                                                    username_=ids_entity[str(group_id)]['username']

                                                                    
                                                            #res= await user(GetFullChannelRequest(int(chat.id)))
                                                            #username_=res.chats[0].username
                                                                except:
                                                                
                                                                    username_=""
                                                                
                                                                error_groups_+=f"<a href='https://t.me/{username_}'>{str(group_id)}</a>\n"
                                                            #await bot_.send_message(int(id_us), f"{translate('Error en el reenvio en',lg)} :\n {error_groups}")
                                                            info_=f"{translate('Error en el reenvio en',lg)} :\n {error_groups_} \n\nTerminado en :{time.time()-init_proc} segundos.\nCantidad de grupos: {len(user_dates[id_us]['group_ids'])}"
                                                            await send_(bot_,int(id_us),info_,event=None,keyboard=None)
                                                            print(info_)
                                                        #msg_dates.pop(index-desv)
                                                        if  resend_loop==0:
                                                            msg_dates.pop(index-desv)
                                                            desv+=1
                                                             
                                                        else:
                                                            print('loop_resend')
                                                            msg_date['time']=actual_time+resend_loop
                                                        #desv+=1


                                                    await upload_db() 
                                            
                                            
                                                index+=1
                                                
                                    except Exception as e:
                                        print(f'Schedule error: {e}')
                                        msg_dates.pop(index-desv)
                                        desv+=1
                                        await upload_db() 
                                         
                                                
                                
                                             
                                
                                #await user.disconnect()   
                                 
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
    #if True:
    
        
        loop1.run_until_complete(deposit_check())
    except Exception as e:
    #else:
        loop1.close()
        print(f"main exception1 :{e}")
        threading.Thread(target=main_).start()
        
       

    


    
# Crea un nuevo bucle de eventos
threading.Thread(target=main).start()
threading.Thread(target=main_).start()

with bot:
   bot.run_until_disconnected()
# Iniciar el bot

     
