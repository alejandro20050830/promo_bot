from telethon import TelegramClient, events
from telethon.tl import functions, types
from telethon import events, Button
import telegram
from keep_alive import keep_alive
import time
import threading
keep_alive()
state=True
import telethon
import asyncio
api_id = '16620070'
api_hash = 'dbf692cdc9b6fb2977dda29fb1691df4'
group_ids = {}
channel_ids={}
chat_ids=[]
channel_ids_swap={}
pending_messages = {}
admins=[]
bot_token = '6395817457:AAH1YxFN6h1arYwu70ESTtavNxFsGqoy7nc'
bot_token = '5850221861:AAEg7MPNSUkK2nYm0YPCk2hBQzNmD_EAnds'
user_dates={}
menu_system=[
    [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('💠 Conectar Canal',resize=True),Button.text('〽️ Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]],
    [[Button.text('💼 Billetera',resize=True)],[Button.text('👁️ Remitente',resize=True),Button.text('⏳ Espera',resize=True)],[Button.text('🕖 Reenvío',resize=True),Button.text('✏️ Editar Grupos',resize=True)],[Button.text('🔰 Referidos',resize=True),Button.text('Siguiente ➡️',resize=True)],[Button.text('🔙 Back',resize=True),Button.text('🔝 Main Menu',resize=True)]],      
    [[Button.text('🧩 Más Cuentas',resize=True)],[Button.text('〽️ Más Canales',resize=True)],[Button.text('🔙 Back',resize=True),Button.text('🔝 Main Menu',resize=True)]]       
             ]
menu_history={}
# Iniciar sesión como bot
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
phone_code_hash_=""
# Iniciar sesión como usuario
#user = TelegramClient('user', api_id, api_hash)


async def login_(event,password="not_set"):
    # Solicitar número de teléfono
    global user_dates
    sender = await event.get_sender()
    phone=user_dates[sender.id]['phone']
    phone_code_hash_= user_dates[sender.id]['phone_code_hash']
    code=user_dates[sender.id]['code']
    
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
    await user.connect()
    chat = await event.get_chat()
    
    message = event.raw_text

 

    
    # Iniciar sesión con el número de teléfono y el código
    if password=="not_set":
        try:
            

            await user.sign_in(phone,code=code,phone_code_hash=phone_code_hash_.phone_code_hash)
                
        except telethon.errors.SessionPasswordNeededError:

            await event.respond('‼️La verificación en dos pasos está habilitada y se requiere una contraseña.Agreguela de la siguiente manera:\n\n• <b>Ejemplo</b>:\n\nSu contraseña es <b>123456</b>, luego ingrese <b>mypass123456</b>\n\n🧩 Por favor, introduzca su contraseña:',parse_mode='html')
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
        
    keyboard = [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('💠 Conectar Canal',resize=True),Button.text('〽️ Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]]       
    await event.respond("'🐾 ¡Conexión Establecida con Éxito!\n\n🤜🤛 Gracias por elegir @Camariobot, ahora todos nuestros servicios están disponibles para usted!\n\n👣 Para comenzar a configurar su primera tarea de reenvío siga los siguientes pasos:\n \n#Paso1 - Debes agregar un canal el cual se utilizará para reenviar todas la publiciones a todos sus grupos agregados.\n\n• <b>/AgregarCanal</b><b>\n\n</b>#Paso2 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado.\n\n• <b>/AgregarGrupos</b><b>\n\n</b>⚙️ Para cualquier consulta, no dude en contactar con @CamarioAdmin\n\n🦎 Manténgase Informado con las últimas actualizaciones @Camario'", buttons=keyboard,parse_mode='html')
    await user.disconnect()
    return 0




#Comands
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
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
    message = event.raw_text
    chat_username = chat.username
    print(f"Nuevo mensaje de {sender.id} en el chat {chat.id}")
    print(f"Mensaje: {message}")
    
    markup = event.client.build_reply_markup([
        [Button.text('First button')],
        [Button.text('Second button')]
    ])
    if sender.id not in user_dates:
        
            
        user_dates[sender.id]={}
        await event.respond('🤜🤛 Gracias por elegir @Camariobot!\n\n👣 Para comenzar a configurar su cuenta siga los siguientes pasos:\n\n#Paso1 - El primero de 3 simplemente pasos a seguir será conectar su cuenta de Telegram con nuestro bot!\n\n• /ConectarCuenta\n\n#Paso2 - Debes agregar un canal el cual se utilizará para reenviar todas la publicaciones a todos los grupos agregados!\n\n• /AgregarCanal\n\n#Paso3 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado!\n\n• /AgregarGrupos', buttons=keyboard,parse_mode='html')
    else :  
        await event.respond('Bienvenido', buttons=keyboard,parse_mode='html')
        
        
    await event.respond('• Manténgase Actualizado:', buttons=[(Button.url('🦎 Camario', 'http://t.me/Camario'))],parse_mode='html')


@bot.on(events.NewMessage(pattern='/connect'))
async def send_code(event):
    # Solicitar número de teléfono
    global user_dates
    sender = await event.get_sender()
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
    await user.connect()
    chat = await event.get_chat()
    
    message = event.raw_text
    comand=message.split(' ')
    if len(message.split(' '))==2:
        
        phone=comand[1]
        try:
            numero = int(phone)  # Intentar convertir a entero
        except ValueError:
            
            await event.respond('🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555',parse_mode='html')
            return 'not_number'
 
        phone_code_hash_=await user.send_code_request(phone)
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
        user_dates[sender.id]['phone']=phone
        user_dates[sender.id]['phone_code_hash']=phone_code_hash_

       
        await event.respond('📨 Ingrese el código de inicio de sesión enviado a la aplicación Telegram o SMS (<b>Sin espacios</b>)\n\n• <b>Ejemplo</b>:\n\nSu código de inicio de sesión es <b>123456</b>, luego ingrese <b>mycode123456</b>\n\n🧩 Por favor, introduzca el código resivido:',parse_mode='html')
    else:
        await event.respond('🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555',parse_mode='html')
        
    
    await user.disconnect()

@bot.on(events.NewMessage(pattern='/get_groups'))
async def get_groups(event):
    # Solicitar número de teléfono
    global user_dates
    
    sender = await event.get_sender()
    
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
    await user.connect()
    
    chats = await user.get_dialogs()
    info="Grupos:\n"



    for chat in chats:
        if chat.is_group:
            info+=str(chat.id)+" "+chat.title+'\n'
            print(f'ID del grupo: {chat.id}, Nombre del grupo: {chat.title}')
            
    keyboard = [Button.inline('🗑️ Eliminar Mensaje', data=b'del_groups_msg')]    
    msg_send=await event.respond(info,buttons=keyboard,parse_mode='html')
    msg_id=msg_send.id
    if sender.id not in user_dates:
        user_dates[sender.id]={}
    user_dates[sender.id]['groups_msg_id']=msg_id
    message = event.raw_text
    
      
    await user.disconnect()



@bot.on(events.NewMessage(pattern='/login'))
async def login(event):
    # Solicitar número de teléfono
    global phone_code_hash_
    sender = await event.get_sender()
    user = TelegramClient(str(sender.id), api_id, api_hash)
    
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
    message = event.raw_text
    comand=message.split(' ')
    if len(comand)>1:
        comand.pop(0)
        msg="Grupos agregados:\n"
        for id_chat in comand:
            if "-" not in id_chat:
                id_chat="-"+str(id_chat)
            if sender.id not in group_ids:
                group_ids[sender.id]=[int(id_chat)]
            else:
                group_ids[sender.id].append(int(id_chat))
            
            msg+=id_chat
            msg+="\n"
            
        await event.respond(msg)
    
@bot.on(events.NewMessage(pattern='/channel '))
async def add_channel(event):
    # Solicitar número de teléfono
    print (chat_ids)
    print(channel_ids)
    chat = await event.get_chat()
    sender = await event.get_sender()
    message = event.raw_text
    comand=message.split(' ')
    if len(comand)==2:
        comand.pop(0)
        msg="Canal agregado:\n"
        for id_channel in comand:
            if "-" not in id_channel:
                id_channel="-"+str(id_channel)
            chat_ids.append(int(id_channel))
            if sender.id not in channel_ids:
                channel_ids[sender.id]=[]
            
            if sender.id not in admins:
                if len(channel_ids[sender.id])>0:
                    chanel_entity = await bot.get_entity(int(channel_ids[sender.id][0]))
                    if sender.id not in channel_ids_swap:
                        channel_ids_swap[sender.id]=[]
                    if len(channel_ids_swap[sender.id])==0:
                        channel_ids_swap[sender.id].append(1)
                        
                    channel_ids_swap[sender.id].pop(0)
                    channel_ids_swap[sender.id].append(int(id_channel))
                    
                    keyboard = [Button.inline('〽️ Si', data=b'yes_swap_channel'),Button.inline('🚫 No', data=b'no_swap_channel')]
                    await event.respond(f'〽️ Usted ya configuro un canal de reenvío anteriormente!\n\n• <b>Su canal</b> - (ID del canal, con un enlace al canal de usuario, por ejemplo <a href="https://t.me/{chanel_entity.username}">{channel_ids[sender.id][0]}</a>)\n\n⁉️ Deseas eliminar esté canal y configurar otro:',buttons=keyboard,parse_mode='html')
                    return 'not admin'
                else:
                    channel_ids[sender.id].append(int(id_channel))
                    
            else:
                channel_ids[sender.id].append(int(id_channel))
            

            
            msg+=id_channel
            msg+="\n"
            
        await event.respond(msg)
     
@bot.on(events.NewMessage(pattern='/time'))
async def time_(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    if len(comand)==2:
        time=int(comand[1])
    
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
            
        user_dates[sender.id]['sleep_time']=time
        
            
        await event.respond(f'Tiempo de reenvio modiificado a {time} seg entre cada menaje')
        
@bot.on(events.NewMessage(pattern='/ree'))
async def resend_time_(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    if len(comand)==2:
        time_=int(comand[1])*60
    
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
            
        user_dates[sender.id]['resend_loop']=time_
        
            
        await event.respond(f'Tiempo de reenvio automatico modiificado a {time_} seg entre cada menaje,para desctivar reenvio automatico establezca el valor en 0')
        
        
@bot.on(events.NewMessage(pattern='/wait'))
async def wait(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    message = event.raw_text
    comand=message.split(' ')
    global user_dates
    if len(comand)==2:
        w_time=int(comand[1])
    
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
            
        user_dates[sender.id]['wait_time']=w_time
        
            
        await event.respond(f'Tiempo de retraso reenvio modiificado a {w_time} seg entre cada menaje')



@bot.on(events.NewMessage(pattern='/send_anounce'))
async def send_anounce(event):
    global user_dates
    
   
    sender = await event.get_sender()
    user = TelegramClient(str(sender.id), api_id, api_hash)
    await user.connect()
    chat = await event.get_chat()
    if sender.id not in user_dates:
            
            user_dates[sender.id]={}
    if 'sleep_time' not in user_dates[sender.id]:
        user_dates[sender.id]['sleep_time']=1
        
    sleep_time= user_dates[sender.id]['sleep_time']
    message = event.raw_text
    comand=message.split('->')
    if len(comand)==2:
        msg=comand[1]
    

    
        if sender.id not in group_ids:
            await event.respond('No tiene chats agregados') 
        # Enviar un mensaje como usuario
        else:
            for group_id in group_ids[sender.id]:
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
    print(sender.id)
        
    user_id=sender.id
    

            


   
    if chat_id in chat_ids:
        
        print(f"Nuevo mensaje en el canal ._. {event.chat.title}: {event.text}")


        print(chat_id)
        print(f"Nuevo mensaje en el canal {event.chat.title}: {event.text}")
        for key in channel_ids:
            if chat_id in channel_ids[key]:
                user_id=key
                if user_id not in user_dates:
            
                    user_dates[user_id]={}
                    
                if user_id not in pending_messages:
            
                    pending_messages[user_id]=[]

        user = TelegramClient(str(user_id), api_id, api_hash)
        
        
        if 'sleep_time' not in user_dates[user_id]:
            user_dates[user_id]['sleep_time']=1
        
        sleep_time= user_dates[user_id]['sleep_time']
    
        if 'wait_time' not in user_dates[user_id]:
            user_dates[user_id]['wait_time']=1
        
        wait_time= user_dates[user_id]['wait_time']
        
        
        await user.connect()
        chat = await event.get_chat()
    
        msg = event.raw_text
        
        # Enviar un mensaje como usuario
        if user_id not in group_ids:
            await event.respond('No tiene chats agregados') 
        else:
            
            timestamp=time.time()
            #date_in={timestamp:msg,'event':event.message}
            date_in={'time':timestamp,'msg':msg,'event':event.message}
            global state
            state=False
            await asyncio.sleep(3)
            pending_messages[user_id].append(date_in)
            await asyncio.sleep(1)
            state=True
           
            
            
            #for group_id in group_ids[user_id]:
                
            #    try:
            #        await user.forward_messages(int(group_id),event.message)
                    #await user.send_message(int(group_id), msg)
            #        await asyncio.sleep(sleep_time)
             #   except Exception as e:
            #        print(e)
                
            await bot.send_message(int(user_id), "Mensaje agregado")
            
        user.disconnect()
    else:
        print("Mensaje de un canal no registrado. ._.")
        


#Controlador de mensajes entrantes    
@bot.on(events.NewMessage)
async def handler(event):
    global user_dates

    # Este bloque de código se ejecutará cada vez que llegue un nuevo mensaje
    chat = await event.get_chat()
    sender = await event.get_sender()
    message = event.raw_text
    user = TelegramClient(str(sender.id), api_id, api_hash)
    await user.connect()
    
    if message=='🧩 Conectar Cuenta' or message=='/ConectarCuenta':

        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
             menu_history[sender.id].append(message)
             
             
        if await user.is_user_authorized():
            keyboard = [Button.inline('🧩 Conectar Cuenta', data=b'connect')]
            await event.respond("🧩 Su cuenta actualmente está conectada con @Camariobot!", buttons=keyboard,parse_mode='html',link_preview=False)
            
            
        else:
            keyboard = [Button.inline('🧩 Conectar Cuenta', data=b'connect')]
            await event.respond('🧩 <b>Menú de Conectividad</b>:\n\n• Utilice esto para forjar una conexión entre su cuenta y @CamarioBot.\n\n• Una conexión con al menos una cuenta es esencial para utilizar los servicios.\n\n• Ingrese el número de teléfono asociado a la cuenta de Telegram, incluya el prefijo de país, elimine el espacio entre el prefijo y el número.\n\n💡 <b>Parámetros de Conexión</b>:\n\n<code>/connect</code> (Número de teléfono completo sin espacios)\n\n• <b>Ejemplo</b>: su número es <b>+84 55555</b>, debes enviar\n\n/connect +8455555\n\n🌐 <b>Descubre el prefijo de cada país visitando este </b><b><a href="https://countrycode.org/">Enlace</a></b>\n\n• No estás seguro de cómo proceder, contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n🧩 <b>Conecte su Cuenta</b>:', buttons=keyboard,parse_mode='html',link_preview=False)

    if message=='🚫 Cancel':
        keyboard = await menu_action('cancel',event)
        await event.respond("🚫 Cancel",buttons=keyboard)
    
    if message=='💠 Conectar Canal' or message=='/AgregarCanal':
        keyboard = [Button.inline('〽️ Conectar Canal',data=b'add_channel')]
       
        await event.respond('💠 <b>Utilice esto para forjar una conexión entre su canal y </b>@CamarioBot.\n\n• Una conexión con al menos un canal es esencial para utilizar los servicios de reenvío automático.\n\n🤖 <b>@Camariobot</b><b> deberá ser añadido como administrador en el canal configurado</b>!\n\n• Si no añade @Camariobot los servicios no funcionarán con normalidad.\n\n💡 <b>Parámetros de Conexión</b>:\n\n<code>/channel</code> (ID del Canal)\n\n• <b>Ejemplo</b>:\n\n/channel 1002065562952\n\n🔍 <b>Localice el ID de su canal utilizando </b>@ScanIDBot.\n\n• ¿No estás seguro de cómo proceder?Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n💠 <b>Conecte</b> <b>un Canal</b>:',buttons=keyboard,parse_mode='html',link_preview=False)
        
    if message=='〽️ Agregar Grupos' or message=='/AgregarGrupos':  
        keyboard = [[Button.inline('〽️ Agregar Grupos',data=b'add_group')]]
        
        await event.respond('〽️ ¡<b>Agrega el ID de los grupos a los cuales se reenviarán las publicaciones</b>!\n\n• Deberá ser miembro de todos los grupos agregados.\n\n• No existe un límite de grupos para reenviar publicaciones.\n\n• Para editar, eliminar o agregar nuevos grupos debera dirigirse ha "⚙️Configuración".\n\n💡 <b>Parámetros de Conexión</b>:\n\n/id (ID de los grupos, separe con un espacio cada ID)\n\n• <b>Ejemplo</b>:\n\n/id 1001256118443 1001484740111\n\n• ¿No estás seguro de cómo proceder? Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>.\n\n〽️ <b>Agregue los Grupos</b>:',buttons=keyboard,parse_mode='html',link_preview=False)

    if message=='⚙️ Configuración':
        keyboard = menu_system[1]
        await event.respond("⚙️ Configuración",buttons=keyboard,parse_mode='html')
        
    
    if message=='💼 Billetera':
        keyboard = [Button.inline('👛 Fondos', data=b'founds')]
        await event.respond('💷 0.00 TRX\n\n💶 0.00 USDT', buttons=keyboard,parse_mode='html')
    
    if message=='👁️ Remitente':
        keyboard = [Button.inline('🟢 On', data=b'on_remitent'),Button.inline('🌑 Off_remitent', data=b'off_remitent')]
        await event.respond('📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - On', buttons=keyboard,parse_mode='html')


    if message=='⏳ Espera':
        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
             menu_history[sender.id].append(message)
             
        if 'wait_time' not in user_dates[sender.id]:
            user_dates[sender.id]['wait_time']=1
        
        wait_time= user_dates[sender.id]['wait_time']
        keyboard = [Button.inline('⏳ Modificar Espera', data=b'resend_time')]
        await event.respond(f'⏳ Espera PreEnvío.\n\n• Tiempo: {wait_time} Segundos \n\n💡 La espera previa al reenvío te permite establecer un retraso entre el envío de la publicación en el canal y el reenvío en los grupos dentro de los cuales puedes editar el mensaje o eliminarlo.\n\n• Tenga en cuenta que el tiempo de espera no transcurre entre las distintas publicaciones, sino solo entre la recepción y el reenvío de ese único mensaje.', buttons=keyboard,parse_mode='html')
      
    if message=='🕖 Reenvío':
        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
            menu_history[sender.id].append(message)
        
        if 'sleep_time' not in user_dates[sender.id]:
            user_dates[sender.id]['sleep_time']=1
        
        sleep_time= user_dates[sender.id]['sleep_time']
        keyboard = [Button.inline('🕖 Aumentar Tiempo', data=b'more_time')]
        await event.respond(f'🕖 Tiempo entre Reenvíos.\n\n• Tiempo: {sleep_time} Segundos\n\n💡 Desde aquí podrás configurar el tiempo que transcurre entre un reenvío y otro. Manteniendo el contador en 0 Minutos optas por un solo reenvío de la publicación.\n\n• Tenga en cuenta que el tiempo de reenvío transcurre entre la repetición del reenvío del último mensaje enviado al canal.', buttons=keyboard,parse_mode='html')  
     
     
    if message=='✏️ Editar Grupos':
       
        await event.respond('✏️ Editar Grupos',parse_mode='html')   
    
    if message== '🔰 Referidos':
        keyboard = [Button.inline('♻️ Generar Enlace', data=b'generate_ref_link')]
        await event.respond('🔰 ¡Gane el 25% de los fondos aumentados por sus referidos!\n\n• <b>Referidos</b> - 0\n\n• <b>Comisiones</b> - 0 USD\n\n👛 Los Referidos existen para brindarle la oportunidad de adquirir suscripciónes de pago gratis!', buttons=keyboard,parse_mode='html')  
    
    if message=='Siguiente ➡️':
        keyboard = menu_system[2]
        await event.respond("Siguiente ➡️",buttons=keyboard,parse_mode='html')
    
    if message=='🧩 Más Cuentas':
        keyboard = [Button.inline('➕ Agregar Cuentas', data=b'more_accounts')]
        await event.respond('🧩 Para evitar pagar múltiples pagos, desde este menú podrás agregar hasta un máximo de 3 cuentas!\n\n• Una vez caducada la suscripción de está cuenta las cuentas agregadas también perderán todos los beneficios.',buttons=keyboard,parse_mode='html')   
    
    if message=='〽️ Más Canales':
       
        await event.respond('〽️ Más Canales',parse_mode='html')     
    
    if message== '🔙 Back':
        keyboard=await menu_action('back',event)
        await event.respond('🔙 Back', buttons=keyboard,parse_mode='html')  
        
    if message== '🔝 Main Menu':
        keyboard=await menu_action('home',event)
        await event.respond('🔝 Main Menu', buttons=keyboard,parse_mode='html') 
    
    if 'mycode' in message:
        
        code=message.replace('mycode','')
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
        user_dates[sender.id]['code']=code
        await login_(event)
            
    
    if 'mypass' in message:
        password=message.replace('mypass','')
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
        user_dates[sender.id]['password']=password
        respond=await login_(event,password)
        if respond!=0:
            await event.respond('Error',parse_mode='html') 
    
    await user.disconnect()
        
            
#Controlador de menu 
async def menu_action(action,event):
    sender = await event.get_sender()
    if action=='back':
        return menu_system[0]
        
    if action=='home':
        return menu_system[0]
    if action=='cancel':
        
        return menu_system[0]
    
     
        
#Manejador de callbacks     
@bot.on(events.CallbackQuery)
async def callback_handler(event):
    global user_dates
    chat_id = event.chat_id
    sender = await event.get_sender()
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
    if event.data == b'connect':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🧩 Por favor, Ingrese su número de teléfono asociado a la cuenta de Telegram.(Sin el +)\n\n• <b>Ejemplo</b>, su número es +84 55555 colocará:\n\n/connect 8455555',buttons=keyboard,parse_mode='html')
    
    if event.data == b'resend_time':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🕖 El tiempo máximo de espera es de 2 minutos (120 segundos)\n\n• <b>Ejemplo</b>, el tiempo que deseas agregar es de 60 segundos enviarás:\n\n/wait 60\n\n⏳ Envía ahora el número de segundos que deben pasar antes de reenviar:',buttons=keyboard,parse_mode='html')
    
    if event.data == b'more_time':

        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('⏰ El tiempo mínimo de espera entre reenvíos es de (30 minutos)\n\n• Si deseas agregar un intervalo de reenvío de 60 minutos el formato correcto es:\n\n/ree 60\n\n⏱️ Envía el número de minutos que deben pasar entre cada reenvío, recuerde utilizar el comando <code>/ree</code>:',buttons=keyboard,parse_mode='html')
    
    
    if event.data == b'add_group':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🔘 <b>Recibe en un mensaje el ID de todos sus grupos enviando el comando</b>:\n\n• /get_groups\n\n💡 <b>Utilize un espacio para separar un ID de otro</b>.\n\n• Ejemplo:\n\n/id 1001256118443 1001484740111 1001368540342\n\n🔎 <b>Ingrese el</b> ID <b>de los Grupos</b>:',buttons=keyboard,parse_mode='html')
    if event.data == b'add_channel':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('💠 <b>Recuerde añadir a </b><b>@Camariobot</b><b> en el canal</b> <b>agregado</b>!\n\n💡 <b>Deberás ingresar el ID del canal luego del comando</b> <code>/chanel</code>\n\n• Ejemplo:\n\n/chanel 1001368540342\n\n🔎 <b>Ingrese el</b> ID <b>del Canal</b>:',buttons=keyboard,parse_mode='html')
    
    if event.data == b'more_accounts':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🆔 Envié el ID de las cuentas que deseas agregar:\n\n• Utilice @ScanIDBot Para obtener el ID de sus cuentas!\n\n🧩 Solo puedes agregar un máximo de 3 cuentas!\n\n/add (ID de sus cuentas, separe con un espacio cada ID) \n\n• Ejemplo:\n\n/add 1878166234 1459865634 181862566234\n\n🚫 Tenga en cuenta que tendrás que conectar cada cuenta con @Camariobot!\n\n• Esté menú no facilita la conexión entre cuentas, simplemente compartirá su suscripción con otras cuentas.\n\n🔎 Envié el ID de las Cuentas:',buttons=keyboard,parse_mode='html')
    
    if event.data == b'generate_ref_link':

        
        keyboard = [Button.inline('🧩 Reenvio automatico', data=b'auto_send_ref_link')]
        await event.respond(f'https://t.me/Camariobot?start={sender.id}',buttons=keyboard,parse_mode='html')
        
    if event.data == b'auto_send_ref_link':
        user_id=sender.id
        if user_id not in user_dates:
            
            user_dates[user_id]={}
        if 'resend_loop' not in user_dates[user_id]:
            user_dates[user_id]['resend_loop']=0
            

        
        sleep_time=user_dates[user_id]['resend_loop']
        keyboard = [Button.inline('🧩 Continuar', data=b'yes_auto_send_ref_link'),Button.inline('🚫 Cancelar', data=b'can_auto_send_ref_link')]
        await event.respond(f'🧩 Reenviaras tu enlace a todos los grupos con un intervalo de reenvío de {str(sleep_time/60)} Minutos.\n\n• Está acción es gratis\n\n⁉️ Deseas continuar con el reenvío:',buttons=keyboard,parse_mode='html')
    if event.data == b'yes_auto_send_ref_link':
        keyboard = [Button.inline('🧩 Continuar', data=b'cont_auto_send_ref_link'),Button.inline('🚫 Cancelar', data=b'can_auto_send_ref_link')]
        user_id=sender.id

        if user_id not in user_dates:
            
            user_dates[user_id]={}
                    
        if user_id not in pending_messages:
            
            pending_messages[user_id]=[]
            

            
        if user_id not in group_ids:
            await event.respond('🔎 Necesitas agregar grupos para reenviar automáticamente su enlace a ellos!\n\n• /AgregarGrupos',parse_mode='html') 
        else:
            
            timestamp=time.time()
            #date_in={timestamp:msg,'event':event.message}
            date_in={'time':timestamp,'msg':f'https://t.me/Camariobot?start={sender.id}','event':'not_remitent'}
            pending_messages[user_id].append(date_in)
            
        
                
                
        
          
    if event.data == b'yes_swap_channel':
        
        channel_ids[sender.id][0]=channel_ids_swap[sender.id][0]
        await event.respond('〽️ Si\nNuevo canal configurado',parse_mode='html')
        
    if event.data == b'no_swap_channel':
        keyboard = [Button.inline('🧩 Continuar', data=b'cont_auto_send_ref_link'),Button.inline('🚫 Cancelar', data=b'can_auto_send_ref_link')]
        await event.respond('🚫 No\nNo se ha realizado ningun cambio',parse_mode='html')
    
    if event.data == b'del_groups_msg':
        await bot.delete_messages(sender.id, [user_dates[sender.id]['groups_msg_id']])
        
    if event.data == b'on_remitent':
        if sender.id not in user_dates:     
            user_dates[sender.id]={}
            
        user_dates[sender.id]['remitent']=True
        
        await event.respond('Se ha activado el remitente',parse_mode='html')
    if event.data == b'off_remitent':
        if sender.id not in user_dates:     
            user_dates[sender.id]={}
            
        user_dates[sender.id]['remitent']=False
        
        await event.respond('Se ha desactivado el remitente',parse_mode='html')
    
   
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
        
        while state:
            try:
                global user_dates
                bot_ = await TelegramClient('bot_', api_id, api_hash).start(bot_token=bot_token)
                await asyncio.sleep(1)
                print('.')
                if len(pending_messages)>0:
                    for id_us in pending_messages:
                        
                        if id_us not in user_dates:     
                            user_dates[id_us]={}
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
                
                        resend_loop= user_dates[id_us]['resend_loop'] 
                        user = TelegramClient(str(id_us), api_id, api_hash)
                        
                        await user.connect()
                        

                        msg_dates=pending_messages[id_us]
                        index=0
                        desv=0 
                        for msg_date in msg_dates:
                                        
                                        programed_time=msg_date['time']
                                #for programed_time in msg_date:
                                #   if programed_time!='event':
                                        event_message=msg_date['event']
                                        msg=msg_date['msg']

                                        actual_time = time.time()
                                        

                                        if float(actual_time)>=float(programed_time):
                                            await asyncio.sleep(wait_time)
                                            for group_id in group_ids[int(id_us)]:
                                                    print(group_id)
                                                #try:
                                                    if user_dates[id_us]['remitent'] and event_message!='not_remitent':
                                                        
                                                        await user.forward_messages(int(group_id),event_message)
                                                    else:
                                                        await user.send_message(int(group_id), msg,parse_mode='html')
                                                    print('send')
                                                    
                                                    await asyncio.sleep(sleep_time)
                                                #except Exception as e:
                                                    #print()
                                                
                                    
                                            await bot_.send_message(int(id_us), "Mensaje reenviado")
                                        
                                            if  resend_loop==0:
                                                msg_dates.pop(index-desv)
                                                desv+=1
                                            else:
                                                print('loop_resend')
                                                msg_date['time']=programed_time+resend_loop
                                            
                                    
                                    
                                        index+=1
                                        
                                        
                                        
                        
                                        
                                
                        await user.disconnect()       
            except Exception as e:
        #threading.Thread(target=main).start()
                print(f'error{e}')
        
    
 
def main():

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(schedule_messages())
    finally:
        loop.close()

    


    
# Crea un nuevo bucle de eventos
threading.Thread(target=main).start()

with bot:
   bot.run_until_disconnected()
# Iniciar el bot

     
