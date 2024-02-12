from telethon import TelegramClient, events
from telethon.tl import functions, types
from telethon import events, Button
import telegram
from keep_alive import keep_alive
#keep_alive()

import telethon
import asyncio
api_id = '16620070'
api_hash = 'dbf692cdc9b6fb2977dda29fb1691df4'
group_ids = {}
channel_ids={}
chat_ids=[-1002122725303]
sleep_time={}
bot_token = '6395817457:AAH1YxFN6h1arYwu70ESTtavNxFsGqoy7nc'
user_dates={}
menu_system=[
    [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('〽️ Agregar Canal',resize=True),Button.text('🔎 Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]],
    [[Button.text('💼 Billetera',resize=True)],[Button.text('👁️ Remitente',resize=True),Button.text('⏳ Espera',resize=True)],[Button.text('🕖 Reenvío',resize=True),Button.text('✏️ Editar Grupos',resize=True)],[Button.text('🔰 Referidos',resize=True)],[Button.text('🔙 Back',resize=True),Button.text('🔝 Main Menu',resize=True)]]      
             
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
        
    keyboard = [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('〽️ Agregar Canal',resize=True),Button.text('🔎 Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]]       
    await event.respond("'🐾 ¡Conexión Establecida con Éxito!\n\n🤜🤛 Gracias por elegir @Camariobot, ahora todos nuestros servicios están disponibles para usted!\n\n👣 Para comenzar a configurar su primera tarea de reenvío siga los siguientes pasos:\n \n#Paso1 - Debes agregar un canal el cual se utilizará para reenviar todas la publiciones a todos sus grupos agregados.\n\n• <b>/AgregarCanal</b><b>\n\n</b>#Paso2 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado.\n\n• <b>/AgregarGrupos</b><b>\n\n</b>⚙️ Para cualquier consulta, no dude en contactar con @CamarioAdmin\n\n🦎 Manténgase Informado con las últimas actualizaciones @Camario'", buttons=keyboard,parse_mode='html')
    await user.disconnect()
    return 0


# Evento para manejar los mensajes entrantes
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Crear un "InlineKeyboardButton" para el "Online Button"
    online_button = types.KeyboardButtonCallback(text='Online', data=b'online')

# Crear un "KeyboardButton" para el "Keyboard Button"
    keyboard_button = telegram.KeyboardButton(text='Keyboard Button')
    

# Crear un teclado con los botones
    #keyboard = types.ReplyKeyboardMarkup([Button.text('Mi Botón')], resize=True,persistent=True)
    keyboard = [[Button.text('🧩 Conectar Cuenta',resize=True)],[Button.text('〽️ Agregar Canal',resize=True),Button.text('🔎 Agregar Grupos',resize=True)],[Button.text('⚙️ Configuración',resize=True)]]
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
    await event.respond("'🐾 ¡Conexión Establecida con Éxito!\n\n🤜🤛 Gracias por elegir @Camariobot, ahora todos nuestros servicios están disponibles para usted!\n\n👣 Para comenzar a configurar su primera tarea de reenvío siga los siguientes pasos:\n \n#Paso1 - Debes agregar un canal el cual se utilizará para reenviar todas la publiciones a todos sus grupos agregados.\n\n• <b>/AgregarCanal</b><b>\n\n</b>#Paso2 - Es tan simple que solamente te falta agregar las ID de los grupos a los cuales se reenviarán los mensajes recibidos en el canal previamente configurado.\n\n• <b>/AgregarGrupos</b><b>\n\n</b>⚙️ Para cualquier consulta, no dude en contactar con @CamarioAdmin\n\n🦎 Manténgase Informado con las últimas actualizaciones @Camario'", buttons=keyboard,parse_mode='html')


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
        phone_code_hash_=await user.send_code_request(phone)
        if sender.id not in user_dates:
            
            user_dates[sender.id]={}
            
        user_dates[sender.id]['phone']=phone
        user_dates[sender.id]['phone_code_hash']=phone_code_hash_

       
        await event.respond('📨 Ingrese el código de inicio de sesión enviado a la aplicación Telegram o SMS (<b>Sin espacios</b>)\n\n• <b>Ejemplo</b>:\n\nSu código de inicio de sesión es <b>123456</b>, luego ingrese <b>mycode123456</b>\n\n🧩 Por favor, introduzca el código resivido:',parse_mode='html')
    else:
         await event.respond('🚫 <b>Formato incorrecto</b>!\n\n☑️ Por favor envié su número de teléfono en el formato correcto!\n\n• Su número fuera +84 555555 tendría que enviar:\n\n/connect 84555555',parse_mode='html')
        
    
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
    
    chat = await event.get_chat()
    sender = await event.get_sender()
    message = event.raw_text
    comand=message.split(' ')
    if len(comand)==2:
        comand.pop(0)
        msg="Canal agregado:\n"
        for id_channel in comand:
            chat_ids.append(int(id_channel))
            channel_ids[sender.id]=[int(id_channel)]

            
            msg+=id_channel
            msg+="\n"
            
        await event.respond(msg)
     
   
    

@bot.on(events.NewMessage(chats=chat_ids))
async def handle_channels_new_message(event):

    sender = await event.get_sender()
    print(sender.id)
    chat_id = event.chat_id
    user_id=sender.id
    print(chat_id)
    print(f"Nuevo mensaje en el canal {event.chat.title}: {event.text}")
    for key in channel_ids:
        if chat_id in channel_ids[key]:
            user_id=key
    user = TelegramClient(str(user_id), api_id, api_hash)
    await user.connect()
    chat = await event.get_chat()
   
    msg = event.raw_text
     
    # Enviar un mensaje como usuario
    if user_id not in group_ids:
       await event.respond('No tiene chats agregados') 
    else:
        
        for group_id in group_ids[user_id]:
            
            try:
                
                await user.send_message(int(group_id), msg)
                #await asyncio.sleep(sleep_time)
            except Exception as e:
                print(e)
            
        await event.respond('Mensajes reenviados.')
    user.disconnect()

@bot.on(events.NewMessage(pattern='/send_anounce'))
async def send_anounce(event):
    sender = await event.get_sender()
    user = TelegramClient(str(sender.id), api_id, api_hash)
    await user.connect()
    chat = await event.get_chat()
    
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
        
        
@bot.on(events.NewMessage)
async def handler(event):
    global user_dates
    # Este bloque de código se ejecutará cada vez que llegue un nuevo mensaje
    chat = await event.get_chat()
    sender = await event.get_sender()
    message = event.raw_text
    if message=='🧩 Conectar Cuenta':
        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
             menu_history[sender.id].append(message)
        keyboard = [Button.inline('🧩 Conectar Cuenta', data=b'connect')]
        await event.respond("'🔘 Menú de Conectividad:\n\n• Utilice esto para forjar una conexión entre su cuenta y @CamarioBot.\n\n☑️ Una conexión con al menos una cuenta es esencial para utilizar los servicios.\n\n• Ingrese el número de teléfono asociado a la cuenta de Telegram, incluido el código de país.\n\n♻️ Parámetros de Conexión:\n\n<b>/connect</b> (Número de Teléfono)\n\n• <b>Ejemplo</b>:\n\n<b>/connect</b> +84 5555555\n\n🌐 Descubre el prefijo de cada país visitando este <b><a href='https://countrycode.org/'>Enlace</a></b>\n\n• ¿No estás seguro de cómo proceder?\n\n⚙️ Contacte con <b><a href='http://t.me/CamarioAdmin'>Soporte</a></b>\n\n🧩 Conecte su cuenta y comience a disfrutar:'", buttons=keyboard,parse_mode='html',link_preview=False)

    if message=='🚫 Cancel':
        keyboard = await menu_action('cancel',event)
        await event.respond("🚫 Cancel",buttons=keyboard)
    
    if message=='〽️ Agregar Canal':
        keyboard = [Button.inline('〽️ Conectar Canal',data=b'add_channel')]
       
        await event.respond('〽️ Menú de Conectividad:\n\n• Utilice esto para forjar una conexión entre su canal y @CamarioBot.\n\n☑️ Una conexión con un canal es esencial para utilizar los servicios de reenvío automático.\n\n• Debes ser miembro del canal agregado, actualmente solamente se permite agregar un canal de reenvío.\n\n♻️ Parámetros de Conexión:\n\n/channel (ID del canal utilizado como sede de reenvío)\n\n• <b>Ejemplo</b>:\n\n/channel 1002065562952\n\n🔍 Localice el ID de su canal utilizando @ScanIDBot.\n\n• ¿No estás seguro de cómo proceder?\n\n⚙️ Contacte con <a href="http://t.me/CamarioAdmin">Soporte</a>\n\n〽️ Conecte su Canal:',buttons=keyboard,parse_mode='html',link_preview=False)
        
    if message=='🔎 Agregar Grupos':  
        keyboard = [[Button.inline('🔎 Agregar Grupos',data=b'add_group')]]
        
        await event.respond('🆔 Agrege el ID de los grupos a los cuales se reenviarán las publicaciones.\n\n• Debes ser miembro de todos los grupos agregados.\n\n♻️ Parámetros de Conexión:\n\n/id (ID de sus grupos, separe con un espacio cada ID)\n\n• Ejemplo:\n\n/id 1001256118443 1001484740111\n\n🔍 Localice el ID de sus grupos utilizando @ScanIDBot.\n\n• ¿No estás seguro de cómo proceder?\n\n⚙️ Contacte con <b><a href="@CamarioAdmin">Soporte\n\n</a></b>🔎 Agregue grupos y comienze a crecer:',buttons=keyboard,parse_mode='html')

    if message=='⚙️ Configuración':
        keyboard = [[Button.text('💼 Billetera',resize=True)],[Button.text('👁️ Remitente',resize=True),Button.text('⏳ Espera',resize=True)],[Button.text('🕖 Reenvío',resize=True),Button.text('✏️ Editar Grupos',resize=True)],[Button.text('🔰 Referidos',resize=True)],[Button.text('🔙 Back',resize=True),Button.text('🔝 Main Menu',resize=True)]]
        await event.respond("⚙️ Configuración",buttons=keyboard,parse_mode='html')
        
    
    if message=='💼 Billetera':
        keyboard = [Button.inline('👛 Fondos', data=b'founds')]
        await event.respond('💷 0.00 TRX\n\n💶 0.00 USDT', buttons=keyboard,parse_mode='html')
    
    if message=='👁️ Remitente':
        keyboard = [Button.inline('🟢 On', data=b'on'),Button.inline('🌑 Off', data=b'off')]
        await event.respond('📬 ¿Deseas mostrar el remitente en tus mensajes?\n\n• <b>Nota</b>:\n\nSi posees una suscripción premium y mantienes el remitente oculto tus mensajes no mostrarán emojis animados.\n\n🔘 Actualmente - On', buttons=keyboard,parse_mode='html')


    if message=='⏳ Espera':
        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
             menu_history[sender.id].append(message)
        keyboard = [Button.inline('⏳ Modificar Espera', data=b'mod_time')]
        await event.respond('⏳ Espera PreEnvío.\n\n• Tiempo: 0 \n\n💡 La espera previa al reenvío te permite establecer un retraso entre el envío de la publicación en el canal y el reenvío en los grupos dentro de los cuales puedes editar el mensaje o eliminarlo.\n\n• Tenga en cuenta que el tiempo de espera no transcurre entre las distintas publicaciones, sino solo entre la recepción y el reenvío de ese único mensaje.', buttons=keyboard,parse_mode='html')
      
    if message=='🕖 Reenvío':
        if sender.id not in menu_history:
            menu_history[sender.id]=[message]
        else:
             menu_history[sender.id].append(message)
        
        keyboard = [Button.inline('🕖 Aumentar Tiempo', data=b'more_time')]
        await event.respond('🕖 Tiempo entre Reenvíos.\n\n• Tiempo: 0 Minutos\n\n💡 Desde aquí podrás configurar el tiempo que transcurre entre un reenvío y otro. Manteniendo el contador en 0 Minutos optas por un solo reenvío de la publicación.\n\n• Tenga en cuenta que el tiempo de reenvío transcurre entre la repetición del reenvío del último mensaje enviado al canal.', buttons=keyboard,parse_mode='html')  
     
     
    if message=='✏️ Editar Grupos':
       
        await event.respond('✏️ Editar Grupos',parse_mode='html')   
    
    if message== '🔰 Referidos':
        keyboard = [Button.inline('♻️ Generar Enlace', data=b'referreals')]
        await event.respond('🔰 ¡Gane el 25% de los fondos aumentados por sus referidos!\n\n• <b>Referidos</b> - 0\n\n• <b>Comisiones</b> - 0 USD\n\n👛 Los Referidos existen para brindarle la oportunidad de adquirir suscripciónes de pago gratis!', buttons=keyboard,parse_mode='html')  
    
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
    
    
        
            
    
        
       
        
         
   
        
    
    
async def menu_action(action,event):
    sender = await event.get_sender()
    if action=='back':
        return menu_system[0]
        
    if action=='home':
        return menu_system[0]
    if action=='cancel':
        
        return menu_system[0]
    
        
        
@bot.on(events.CallbackQuery)
async def connect(event):
    # Aquí puedes agregar el código que quieras ejecutar cuando se presione el botón
    if event.data == b'connect':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🧩 Por favor, Ingrese su número de teléfono asociado a la cuenta de Telegram.(Sin el +)\n\n• <b>Ejemplo</b>, su número es +84 55555 colocará:\n\n/connect 8455555',buttons=keyboard,parse_mode='html')
    
    if event.data == b'mod_time':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🕖 El tiempo máximo de espera es de 2 minutos (120 segundos)\n\n• Envía ahora el número de segundos que deben pasar antes de reenviar:',buttons=keyboard,parse_mode='html')
    
    if event.data == b'more_time':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('🕖 El tiempo máximo de espera es de 2 minutos (120 segundos)\n\n• <b>Ejemplo</b>, el tiempo que deseas agregar es de 60 segundos enviarás:\n\n/time 60\n\n⏳ Envía ahora el número de segundos que deben pasar antes de reenviar:',buttons=keyboard,parse_mode='html')
    
    
    if event.data == b'add_group':
        keyboard = [Button.text('🚫 Cancel', resize=True)]
        await event.respond('💡 No existe un límite de grupos para reenviar publicaciones, utilize un espacio para separar un ID de otro.\n\n📡 @ScanIDBot Encuéntra el ID de grupos!\n\n• <b>Ejemplo</b>:\n\n/id 1001256118443 1001484740111 1001368540342\n\n🔎 Ingrese el ID de los Grupos:',buttons=keyboard,parse_mode='html')
  
   
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
 
 

# Iniciar el bot
with bot:
    
    bot.run_until_disconnected()
