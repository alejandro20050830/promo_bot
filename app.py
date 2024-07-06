keep_alive()
print_to_web("finish alive")
from testing import *
print_to_web("finish testin")
from trading_simulate_ import *
print_to_web("finish trading simulate")
import threading
import sys
new_user_msg = []
callback_handler_semaforo = asyncio.Semaphore(100)
handler_semaforo = asyncio.Semaphore(100)
db_semaforo = asyncio.Semaphore(6)
cryptobot_semaphore = asyncio.Semaphore(1)
Admin_List = [1633521428,1795223610]
# db
user_dates = {}
request = {}
first_init = True
on_saving = False
# Cripto
Test = False
conc = True
ref_value = 0.01
# menu
bet_sel_keyb = [
    [Button.inline("USDT", data=b"USDT_crypcas")],
    [Button.inline("TON", data=b"TON_crypcas")],
    [Button.inline("BTC", data=b"BTC_crypcas")],
    [Button.inline("LTC", data=b"LTC_crypcas")],
    [Button.inline("ETH", data=b"ETH_crypcas")],
    [Button.inline("BNB", data=b"BNB_crypcas")],
    [Button.inline("TRX", data=b"TRX_crypcas")],
    [Button.inline("🔙 Back", data=b"back")],
]
cripto_infos_with_net = {
    "USDT_TRC20": "TRON – TRC20 ",
    "USDT_TON": "The Open Network – TON",
    "USDT_ERC20": "Ethereum – ERC20",
    "USDT_BEP20": "BNB Smart Chain – BEP20",
    "TRX": "TRON – TRC20",
    "BNB": "BNB Smart Chain – BEP20",
    "BTC": "Bitcoin – BTC",
    "LTC": "Litecoin – LTC",
    "ETH": "Ethereum – ERC20",
    "TON": "The Open Network – TON",
    "NOT": "Notcoin – TON",
    "USDC_ERC20": "Ethereum – ERC20",
    "USDC_BEP20": "BNB Smart Chain – BEP20",
}

criptos_idx = {
    "USDT_cr": 0,
    "TON_cr": 1,
    "GRAM_cr": 2,
    "BTC_cr": 3,
    "LTC_cr": 4,
    "ETH_cr": 5,
    "BNB_cr": 6,
    "TRX_cr": 7,
    "USDC_cr": 8,
}
if not Test:
    criptos_idx = {
        "USDT_cr": 0,
        "TON_cr": 1,
        "GRAM_cr": 2,
        "NOT_cr": 3,
        "BTC_cr": 4,
        "LTC_cr": 5,
        "ETH_cr": 6,
        "BNB_cr": 7,
        "TRX_cr": 8,
        "USDC_cr": 9,
    }


conc_cr = False


# Sub_check
CHANNEL_ID = ["@UniSwapTips", -1002089285594]

# CHANNEL_ID = [-1002089285594]

print_to_web("finish variables")
def private_message_handler(func):
    async def wrapper(event):
        if event.is_private and event.sender_id != await get_bot_id():
            await func(event)

    return wrapper


async def get_bot_id():
    me = await bot.get_me()
    return me.id


# Menu funcs
async def menu_action(event, action):

    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    lg = user_dates[user_id]["leng"]

    if "historial" not in user_dates[str(sender.id)]:
        user_dates[str(sender.id)]["historial"] = "/main"
        info = copy.deepcopy(menu_system[user_dates[str(sender.id)]["historial"]].back_())
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        return 0

    if action == "back":
        event_ = MyEvent(event)

        if user_dates[str(sender.id)]["historial"] != "/main/casino/dado/game/bet_size":
            user_dates[user_id]["apuesta_cord"] = None
            user_dates[user_id]["typing"] = "off"

        info = copy.deepcopy(menu_system[user_dates[str(sender.id)]["historial"]].back_())
        # if 'rules' in user_dates[str(sender.id)]['historial']:
        #    info=info.back_()
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[str(sender.id)]["historial"] = info.route
        
        if "/main/wallet/swap/coin1/coin2/am" == info.route:
            event_.data = f"{user_dates[user_id]['swap-coin2']}_swap1-cr".encode(
                "utf-8"
            )

            await callback_handler(event_)
            return 0
        if "/main/settings" == info.route:
            event_.data = b"settings"
            await callback_handler(event_)
            return 0
        if "/main/settings" == info.route:
            event_.data = b"settings"
            await callback_handler(event_)
            return 0
        
        if "/main/unicorn" == info.route:
            event_.data = b"unicorn"
            await callback_handler(event_)
            return 0
        if "/main/unicorn/feed_pet" == info.route:
            event_.data = b"unicorn-feed_pet"
            await callback_handler(event_)
            return 0
        if "/main/free_uni/referrals" == info.route:
            event_.data = b"f_uni-refer"
            await callback_handler(event_)
            return 0
        if "/main/free_uni/task/channel" == info.route:
            event_.data = b"f_uni-channels"
            await callback_handler(event_)
            return 0
        
        if "/main/free_uni/task/group" == info.route:
            event_.data = b"f_uni-group"
            await callback_handler(event_)
            return 0
        if "/main/free_uni/task/bot" == info.route:
            event_.data = b"f_uni-bots"
            await callback_handler(event_)
            return 0
        if "/main/wallet/swap/coin1/coin2" == info.route:
            event_.data = f"{user_dates[user_id]['swap-coin1']}_swap-cr".encode("utf-8")
            await callback_handler(event_)
            return 0
        
        if "/main/wallet/deposit/net" == info.route:
            event_.data = b"USDT_cr"
            await callback_handler(event_)
            return 0
        if "/main/wallet/deposit/amount" == info.route:

            event_.data = f"´{user_dates[user_id]['dep_cripto']}_cr"

            await callback_handler(event_)
            return 0
        if "/main/wallet" == info.route:

            event_.data = b"wallet"
            print_to_web("yea")
            await callback_handler(event_)
            return 0
        if "/main/casino" in info.route and "/game" in info.route:
            await sel_game(event)
            return 0

        if "/main/grid/manage/bot" == info.route:
            idx = user_dates[user_id]["bot_sel"]
            bot_dates = user_dates[user_id]["bots"][str(idx)]
            cripto = bot_dates["cripto"]
            cripto_price = get_price(cripto)

            lvg = bot_dates["lvg"]
            sl = bot_dates["sl"]
            tp = bot_dates["tp"]
            ords_today = bot_dates["ord_today"]
            ords_total = bot_dates["ord_total"]
            shorts = bot_dates["shorts"]
            longs = bot_dates["longs"]
            invest = bot_dates["usd_am"]
            perc_profittoday = bot_dates["prof_today"]
            brute_profittoday = round((perc_profittoday / 100) * invest, 6)
            perc_profittotal = bot_dates["prof_total"]
            brute_profittotal = round((perc_profittotal / 100) * invest, 6)

            perc_apr = round(
                1
                + ((perc_profittotal / invest) * 100)
                * (365 / ((time.time() - bot_dates["date"]) / (3600 * 24)))
                - 1,
                6,
            )

            brute_apr = round((perc_apr / 100) * invest, 6)

            # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
            text = Template(text)
            text = text.substitute(
                cripto=cripto,
                cripto_in_usd=cripto_price,
                leverage=lvg,
                SL=sl,
                TP=tp,
                orders_today=ords_today,
                orders_total=ords_total,
                longs=longs,
                shorts=shorts,
                invest=invest,
                profit_today=perc_profittoday,
                profit_today_brute=brute_profittoday,
                profit_total=perc_profittotal,
                profit_total_brute=brute_profittotal,
                apr=perc_apr,
                apr_brute=brute_apr,
            )

        if "/main/grid/manage" == info.route:
            keyboard = []

            if "bots" not in user_dates[user_id]:
                user_dates[user_id]["bots"] = {}

            for key in user_dates[user_id]["bots"]:
                bot_name = f'{color_crypto[user_dates[user_id]["bots"][key]["cripto"]]} {user_dates[user_id]["bots"][key]["cripto"]}'

                keyboard.append([Button.inline(bot_name, data=f"gdbot_id:{str(key)}")])
            keyboard.append([Button.inline("< Back", data=b"back")])

            if len(user_dates[user_id]["bots"]) == 0:
                info = copy.deepcopy(menu_system["/main/grid/manage_0"])
                info.custom(lg)
                text = info.text

        if "/main/grid/new_grid_cripto/new_grid_am_ok" == info.route:
            info = copy.deepcopy(menu_system["/main/grid/new_grid_cripto/new_grid_am_ok"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            cripto = user_dates[user_id]["grid_cryp"]
            text = Template(text)
            text = text.substitute(
                cripto_info=f"{color_crypto[cripto]} {cripto}/USDT ≈ {str(amount)}"
            )
        if "/main/grid/copy" == info.route:
            copy_bots = []
            for uid in user_dates:
                if "launched" in user_dates[uid]:
                    for id_ in user_dates[uid]["launched"]:
                        # copy_bots_=user_dates[uid]['launched'][id_]
                        copy_bots_ = user_dates[uid]["bots"][id_]
                        copy_bots_["idx"] = id_
                        copy_bots_["uid"] = uid
                        copy_bots.append(copy_bots_)
            if not "copy_idx" in user_dates[user_id]:
                user_dates[user_id]["copy_idx"] = 0
            idx_sel = user_dates[user_id]["copy_idx"]
            copy_opt = copy_bots[idx_sel]
            uid = copy_opt["uid"]
            id_ = copy_opt["idx"]

            # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}

            cripto = copy_opt["cripto"]
            cripto_price = "{:.9f}".format(get_price(cripto))
            lvg = copy_opt["lvg"]
            sl = copy_opt["sl"]
            tp = copy_opt["tp"]
            ords_today = copy_opt["ord_today"]
            ords_total = copy_opt["ord_total"]
            shorts = copy_opt["shorts"]
            longs = copy_opt["longs"]
            invest = copy_opt["usd_am"]
            perc_profittoday = copy_opt["prof_today"]
            brute_profittoday = round((perc_profittoday / 100) * invest, 6)
            perc_profittotal = copy_opt["prof_total"]
            brute_profittotal = round((perc_profittotal / 100) * invest, 6)

            perc_apr = round(
                1
                + ((perc_profittotal / invest) * 100)
                * (
                    365
                    / (
                        (time.time() - user_dates[uid]["launched"][id_]["time"])
                        / (3600 * 24)
                    )
                )
                - 1,
                6,
            )

            brute_apr = round((perc_apr / 100) * invest, 6)

            # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
            text = Template(text)
            text = text.substitute(
                cripto=f"{color_crypto[cripto]} {cripto}",
                cripto_in_usd=cripto_price,
                leverage=lvg,
                SL=sl,
                TP=tp,
                orders_today=ords_today,
                orders_total=ords_total,
                longs=longs,
                shorts=shorts,
                profit_today=perc_profittoday,
                profit_today_brute=brute_profittoday,
                profit_total=perc_profittotal,
                profit_total_brute=brute_profittotal,
                days_online=str(
                    int(
                        (time.time() - user_dates[uid]["launched"][id_]["time"])
                        / 3600
                        / 24
                    )
                ),
                apr=perc_apr,
                apr_brute=brute_apr,
            )

        if "/main/grid/manage/bot/conf" == info.route:

            # cripto = user_dates[user_id]["grid_cryp"]
            idx = user_dates[user_id]["bot_sel"]
            bot_dates = user_dates[user_id]["bots"][str(idx)]
            cripto = bot_dates["cripto"]
            text = Template(text)
            text = text.substitute(cripto=f"{color_crypto[cripto]} {cripto}")

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
        user_dates[user_id]["apuesta"] = None

    if action == "home":
        user_dates[str(sender.id)]["historial"] = "/main"
        info =  copy.deepcopy(menu_system[user_dates[str(sender.id)]["historial"]].back_())
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )



# Cripto_funcs
async def deposit_check():
    global user_dates

    bot_ = await TelegramClient("bot_criptodep_", api_id, api_hash).start(
        bot_token=bot_token
    )
    admin_ = TelegramClient("admin_dep", api_id, api_hash)
    while True:
        try:
            # if True:
            print_to_web("Checking deposit...")

            await asyncio.sleep(300)
            
            await upload_db(admin_)
            for id_ in user_dates:

                user_id = id_
                if "leng" not in user_dates[user_id]:
                    user_dates[user_id]["leng"] = "english"
                lg = user_dates[user_id]["leng"]
                if "balance" not in user_dates[user_id]:
                    user_dates[user_id]["balance"] = {}

                if "USDT" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["USDT"] = 0
                if "USDC" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["USDC"] = 0
                if "BTC" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["BTC"] = 0
                if "LTC" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["LTC"] = 0
                if "ETH" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["ETH"] = 0
                if "BNB" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["BNB"] = 0
                if "UNI" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["UNI"] = 0
                if "TRX" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["TRX"] = 0
                if "TON" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["TON"] = 0
                if "NOT" not in user_dates[user_id]["balance"]:
                    user_dates[user_id]["balance"]["NOT"] = 0

                if (
                    "invoice_id" in user_dates[id_]
                    and user_dates[id_]["invoice_id"] != "None"
                ):

                    id = user_dates[id_]["invoice_id"]
                    #print_to_web(f"Comprobacion de {id} para {id_}")
                    verify_resp = verificar_pago(int(id), Test)
                    if verify_resp:
                        if len(verify_resp["result"]["items"]) > 0:
                            factura_status = verify_resp["result"]["items"][0]["status"]

                            if factura_status == "paid":
                                payed_usd = verify_resp["result"]["items"][0]["amount"]
                                fee_usd = verify_resp["result"]["items"][0][
                                    "fee_in_usd"
                                ]
                                cripto_payed = verify_resp["result"]["items"][0][
                                    "paid_asset"
                                ]

                                user_dates[id_]["invoice_id"] = "None"
                                dep_in_crip = float(payed_usd) / get_price(
                                    user_dates[id_]["dep_cripto"]
                                )
                                user_dates[id_]["balance"][
                                    user_dates[id_]["dep_cripto"]
                                ] += dep_in_crip

                                # msg = f"----------PAYED-------------\nReal_recived={payed_usd}USD\nFee:{fee_usd}\nCripto:{cripto_payed}"
                                msg = f"🎉 Deposito completado\n\n• Crypto - {cripto_payed}\n• Pagado - {payed_usd} USD"
                                msg = f"👛 Coins deposited successfully. You received <b>{payed_usd}  {cripto_payed}</b>."
                                msg = my_text_db.translate(msg, lg)

                                await bot_.send_message(
                                    int(id_), msg, parse_mode="html"
                                )
                                #admin_ = TelegramClient("admin_dep", api_id, api_hash)
                                #await upload_db(admin_)

                            else:
                                pass
                                #print_to_web("No pay")
                        else:pass
                            #print_to_web("Error")

        except Exception as e:
            # else:
            print_to_web(f"Error en checkeo de deposito: {e}")


async def process_withdraw(user_id, amount, wallet_add,root = None):
    global conc_cr
    await cryptobot_semaphore.acquire()
    #if conc_cr == False:
    try:
        conc_cr = True
        chat_id = "@CryptoTestnetBot"
        if not Test:
            chat_id = "@CryptoBot"
        await client.connect()
        await client.send_message(chat_id, "/wallet")
        await asyncio.sleep(3)
        try:
            if not root:
                root = user_dates[user_id]["with_root"]
            
            resp = await press_inline_button_with(
                chat_id, user_id, amount, wallet_add,root
            )
            conc_cr = False
            return 0
        except Exception as e:
            print_to_web(e)
            conc_cr = False
            client.send_message(int(user_id), "Ha ocurrido un error")
            return 0
    except:pass
    cryptobot_semaphore.release()
    await client.disconnect()
    conc_cr = False
    return resp


async def press_inline_button_with(chat_id, user_id, amount, wallet_add, id_button=[]):
    global user_dates
    global conc
    print_to_web("----------------------------------------------------------------------")
    print_to_web(user_id)

    clave_string = ["Coin:", "Network:"]
    alert_text = ""
    await asyncio.sleep(3)
    event = await get_last_message_and_event(chat_id)
    button = await event.get_buttons()
    await asyncio.sleep(2)
    if Test:
        await button[0][1].click()
    else:
        await button[1][1].click()

    await asyncio.sleep(3)
    if "leng" not in user_dates[user_id]:
        user_dates[user_id]["leng"] = "english"
    if not "typing" in user_dates[user_id]:
        user_dates[user_id]["typing"] = "off"
    lg = user_dates[user_id]["leng"]
    event = await get_last_message_and_event(chat_id)
    button = await event.get_buttons()
    if "Choose a cryptocurrency" not in event.text:
        await process_withdraw(user_id, amount, wallet_add)
        print_to_web("recursivity")
        event = await get_last_message_and_event(chat_id)
        button = await event.get_buttons()
        return 0
    print_to_web("Encontrado")
    # Encuentra el botón inline en el mensaje
    event = await get_last_message_and_event(chat_id)
    button = await event.get_buttons()
    print_to_web(button)
    if button:
        print_to_web(get_keyboard(button))
        # print_to_web(button[0][0].data)
        for id_btn in id_button:
            # if id_button:
            print_to_web(id_button)

            if button:
                print_to_web(f"Iteration.............................................{id_btn}")
                await button[id_btn][0].click()
                await asyncio.sleep(2)
                event = await get_last_message_and_event(chat_id)

                if "Enter a wallet address" in event.text:
                    await client.send_message(chat_id, wallet_add)
                    await asyncio.sleep(3)
                    event = await get_last_message_and_event(chat_id)

                    if (
                        "Enter an amount of" in event.text
                        and "Min" in event.text
                        and "Your balance" in event.text
                    ):
                        enlace_pattern = r"\[.*?\]\((.*?)\)"
                        msg = event.text
                        enlaces = re.findall(enlace_pattern, msg)
                        print_to_web(enlaces)
                        address = user_dates[user_id]["withdraw_address"]
                        send_am = user_dates[user_id]["withdraw_amount"]
                        info = copy.deepcopy(menu_system["/main/wallet/withdraw/wait"])
                        info.custom(lg)
                        text = info.text
                        keyboard = info.keyboard
                        text = Template(text)
                        if user_dates[user_id]["with_cripto"] == "USDT":
                            key = f'USDT_{user_dates[user_id]["with_net"]}'
                        else:
                            key = user_dates[user_id]["with_cripto"]

                        net_info = cripto_infos_with_net[key]
                        address = user_dates[user_id]["withdraw_address"]
                        address_url = enlaces[0]
                        address_abv = f"{address[:7]}...{address[-7:]}"
                        fee = criptos[user_dates[user_id]["with_cripto"]]["fee"]
                        send_am = user_dates[user_id]["withdraw_amount"] - fee
                        cripto = user_dates[user_id]["with_cripto"]
                        text = text.substitute(
                            net_info=net_info,
                            address=address_url,
                            address_abv=address_abv,
                            send_am=send_am,
                            cripto=cripto,
                            fee_am=fee,
                            total_am=user_dates[user_id]["withdraw_amount"],
                        )
                        user_dates[user_id]["msg_id"] = await edit_msg(
                            bot, int(user_id), text, user_dates, keyboard
                        )
                        await client.send_message(chat_id, str(amount))
                        await asyncio.sleep(2)
                        event = await get_last_message_and_event(chat_id)
                        button = await event.get_buttons()
                        if (
                            "Confirmation" in event.text
                            and "Network" in event.text
                            and "Address" in event.text
                            and "You send" in event.text
                            and "Are you sure you want to send these coins to the address"
                            in event.text
                        ):

                            await button[0][0].click()
                            await asyncio.sleep(2)
                            event = await get_last_message_and_event(chat_id)

                            if "Would you like to save the address" in event.text:
                                event = await get_last_message_and_event(chat_id)
                                await asyncio.sleep(2)

                            break
                            # user_dates[user_id]["msg_id"] = msg.id
                        else:
                            msg_ = (
                                "Saldo insufuciente en la billetera de retiro principal"
                            )
                            msg = await bot.send_message(int(user_id), msg_)
                            return 0
                    else:
                        msg_ = "ERROR AL PROCESAR LA DIRECCION DE BILLETERA"
                        msg = await bot.send_message(int(user_id), msg_)
                        return 0

                event = await get_last_message_and_event(chat_id)
                button = await event.get_buttons()

        event = await get_last_message_and_event(chat_id)
        msg = event.text
        print_to_web(msg)

        """
        if 'Choose a cryptocurrency' not in msg and 'Choose a network' not in msg and "Enter an amount of" not in msg and "Enter a wallet address" not in msg :
            print_to_web('entry++++++++++++++++++++++++++++++++++++++++++++')
            info = copy.deepcopy(menu_system["/main/wallet/withdraw/wait"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            text = Template(text) 
            if user_dates[user_id]["with_cripto"] == 'USDT':
                key=f'USDT_{user_dates[user_id]["with_net"]}'
            else:
                key=user_dates[user_id]["with_cripto"]
                
            net_info = cripto_infos_with_net[key]
            address = user_dates[user_id]["withdraw_address"]
            address_abv = f'{address[:7]}...{address[-7:]}'
            fee = criptos[user_dates[user_id]["with_cripto"]]['fee']
            send_am = user_dates[user_id]["withdraw_amount"] - fee
            cripto = user_dates[user_id]["with_cripto"]
            text = text.substitute(net_info = net_info,address = address,address_abv=address_abv,send_am=send_am,cripto=cripto,fee_am=fee,total_am = user_dates[user_id]["withdraw_amount"])
            user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, int(user_id), text, user_dates, keyboard
                )
         """
        if "sent" not in msg or "successfully" not in msg:
            await asyncio.sleep(5)
            event = await get_last_message_and_event(chat_id)
            msg = event.text

        if "sent" not in msg or "successfully" not in msg:

            msg_ = "Saldo insufuciente en la billetera de retiro principal"
            msg = await bot.send_message(int(user_id), msg_)
            return 0
        enlace_pattern = r"\[.*?\]\((.*?)\)"
        enlaces = re.findall(enlace_pattern, msg)
        print_to_web(enlaces)
        keyboard = [[Button.inline("< Back", data=b"back")]]

        info = copy.deepcopy(menu_system["/main/wallet/complete"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[0][0].url = enlaces[0]
        text = Template(text)
        if user_dates[user_id]["with_cripto"] == "USDT":
            key = f'USDT_{user_dates[user_id]["with_net"]}'
        else:
            key = user_dates[user_id]["with_cripto"]

        net_info = cripto_infos_with_net[key]
        address = user_dates[user_id]["withdraw_address"]
        adress_url = enlaces[1]
        address_abv = f"{address[:7]}...{address[-7:]}"
        fee = criptos[user_dates[user_id]["with_cripto"]]["fee"]
        send_am = user_dates[user_id]["withdraw_amount"] - fee
        cripto = user_dates[user_id]["with_cripto"]
        text = text.substitute(
            net_info=net_info,
            address=address_url,
            address_abv=address_abv,
            send_am=send_am,
            cripto=cripto,
            fee_am=fee,
            total_am=user_dates[user_id]["withdraw_amount"],
        )
        """
        await bot.delete_messages(
            entity=int(user_id),
            message_ids=[
                #user_dates[user_id]["msg_id"],
                #user_dates[user_id]["msg_id"] - 1,
            ],
        )
        """
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, int(user_id), text, user_dates, keyboard
        )
        return 1

        # msg = await bot.send_message(int(user_id), msg, buttons=keyboard)
        # user_dates[user_id]["msg_id"] = msg.id


async def press_inline_button(chat_id, user_id, id_invoice, amount, id_button=[]):

    global user_dates
    global conc
    clave_string = ["Coin:", "Network:"]

    event = await get_last_message_and_event(chat_id)
    print_to_web("Encontrado")
    # Encuentra el botón inline en el mensaje
    button = await event.get_buttons()
    print_to_web(button)
    if button:
        print_to_web(get_keyboard(button))
        # print_to_web(button[0][0].data)
        for id_btn in id_button:
            # if id_button:

            if button:
                await button[id_btn][0].click()
                await asyncio.sleep(2)
                event = await get_last_message_and_event(chat_id)
                button = await event.get_buttons()
                for btn in button:

                    btn_txt = btn[0].text
                    print_to_web(btn_txt)

                    if alert_text in btn_txt:
                        await swap_all(id_button)
                        await process_get_wallet(user_id, id_invoice, amount)
                        return 0

                    if (
                        "💳 Pay Now" in btn_txt
                        or "Are you sure you want to pay this invoice?" in event.text
                    ):
                        await button[0][0].click()
                        await asyncio.sleep(2)
                        print_to_web("yes")
                        # await bot.send_message(1633521428,event.text,parse_mode='html')
                        event = await get_last_message_and_event(chat_id)
                        button = await event.get_buttons()
                        if (
                            not "Coin:" in event.text
                            and not "Choose a network" in event.text
                        ):
                            await bot.delete_messages(
                                entity=int(user_id),
                                message_ids=[
                                    user_dates[user_id]["msg_id"],
                                    user_dates[user_id]["msg_id"] - 1,
                                ],
                            )
                            keyboard = [[Button.inline("< Back", data=b"back")]]
                            msg = "ERROR IN GET DEPOSIT ADDRESS"
                            msg = await bot.send_message(
                                int(user_id), msg, buttons=keyboard
                            )

                            user_dates[user_id]["msg_id"] = msg.id
                            return 0
                            conc = False
                            user_dates[user_id]["invoice_id"] = "None"

                            # verify_resp=verificar_pago(int(id_invoice),Test)
                            # amount=verify_resp['result']['items'][0]['amount']
                            await swap_all(id_button)
                            # verify_resp=verificar_pago(int(id_invoice),Test)
                            # amount=verify_resp['result']['items'][0]['amount']
                            create_dates = crear_factura(amount, Test)
                            id__ = create_dates["invoice_id"]

                            user_dates[user_id]["invoice_id"] = id__
                            pay_url = create_dates["bot_invoice_url"]
                            id_ = pay_url.split("=")[1]
                            await process_get_wallet(user_id, id_, amount)
                            # await process_get_wallet(user_id,id_invoice)
                            # user_dates[user_id]['invoice_id']="None"
                            conc = True
                            return 0

                        break
        event = await get_last_message_and_event(chat_id)
        if not "Coin:" in event.text:
            await bot.delete_messages(
                entity=int(user_id),
                message_ids=[
                    user_dates[user_id]["msg_id"],
                    user_dates[user_id]["msg_id"] - 1,
                ],
            )
            keyboard = [[Button.inline("< Back", data=b"back")]]
            msg = "ERROR IN GET DEPOSIT ADDRESS"
            msg = await bot.send_message(int(user_id), msg, buttons=keyboard)

            user_dates[user_id]["msg_id"] = msg.id
            return 0
        msg = event.text.split("Coin:")

        msg = f"👛 Use the address below to deposit coins.\n\nCoin:{msg[1]}"
        keyboard = [[Button.inline("< Back", data=b"back")]]
        # user_dates[user_id]["msg_id"] = await edit_msg(bot, int(user_id), msg, user_dates, keyboard)

        await bot.delete_messages(
            entity=int(user_id),
            message_ids=[
                user_dates[user_id]["msg_id"],
                user_dates[user_id]["msg_id"] - 1,
            ],
        )
        msg = await bot.send_message(int(user_id), msg, buttons=keyboard)
        user_dates[user_id]["msg_id"] = msg.id


async def get_keyboard_():
    event = await get_last_message_and_event("@CryptoBot")
    button = await event.get_buttons()
    print_to_web(get_keyboard(button))


def get_keyboard(brute_buttons):
    btns = []

    idx = 0
    for btn in brute_buttons:

        btn_txt = btn[0].text
        btn_comp = [f"Button.inline({btn_txt}, data=b'idx_{idx}')"]
        btns.append(btn_comp)
        idx += 1
    return btns


async def process_get_wallet(user_id, id_invoice, amount):
    global conc_cr
    await cryptobot_semaphore.acquire()
    #if conc_cr == False:
    try:
        conc_cr = True
        chat_id = "@CryptoTestnetBot"
        if not Test:
            chat_id = "@CryptoBot"

        await client.connect()
        await client.send_message(chat_id, f"/start {id_invoice}")
        await asyncio.sleep(2)
        try:
            await press_inline_button(
                chat_id, user_id, id_invoice, amount, user_dates[user_id]["dep_root"]
            )
        except Exception as e:
            print_to_web(e)
            conc_cr = False
            await client.send_message(
                int(user_id),
                "Un error ha ocurrido al intentar obtener la direccion de deposito",
            )
    except:pass

    cryptobot_semaphore.release()
    await client.disconnect()
    conc_cr = False


async def callback_handler_cripto(event):

    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    decoded = event.data.decode("utf-8")
    """
    if  'idx' in event.data.decode('utf-8'):
        idx=event.data.decode('utf-8').split('_')[1]
        print_to_web(idx)
        user_dates[user_id].append((int(idx)))
     """
    lg = user_dates[user_id]["leng"]
    if event.data == b"wall_dep":

        info = copy.deepcopy(menu_system["/main/wallet/deposit"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"USDT_cr":

        info = copy.deepcopy(menu_system["/main/wallet/deposit/net"])
        info.custom(lg)
        text = info.text
        text = Template(text)

        text = text.substitute(cripto="USDT")

        keyboard = info.keyboard
        user_dates[user_id]["dep_root"] = [criptos_idx[decoded]]
        user_dates[user_id]["dep_cripto"] = decoded.replace("_cr", "")
        cripto_info = decoded.replace("_cr", "")
        user_dates[user_id]["cripto_info"] = cripto_info

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route

        # await bot.send_message(sender.id,'Selecciona la red',buttons=net_sel_keyb)

        return 0
    if event.data == b"USDC_cr":

        info = copy.deepcopy(menu_system["/main/wallet/deposit/net"])
        info.custom(lg)
        text = info.text
        text = Template(text)

        text = text.substitute(cripto="USDC")

        keyboard = info.keyboard
        keyboard.pop(0)

        user_dates[user_id]["dep_root"] = [criptos_idx[decoded]]
        user_dates[user_id]["dep_cripto"] = decoded.replace("_cr", "")
        cripto_info = decoded.replace("_cr", "")
        user_dates[user_id]["cripto_info"] = cripto_info

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route

        # await bot.send_message(sender.id,'Selecciona la red',buttons=net_sel_keyb)

        return 0

    """
    if "cr" == decoded[-2:]:
        idx = criptos_idx[decoded]
        
        keyb = cripto_sel_keyb.copy()
        keyb[idx] = [Button.inline(f"•{decoded.replace('_cr','')}", data=event.data)]
        user_dates[user_id]["dep_root"] = [criptos_idx[decoded]]
        keyboard = [[Button.inline("🧩Confirmar", data=b"confirm_dp")]]
        id_chat = sender.id
        id_msg = user_dates[user_id]["msg_id"]
        info = "Confirma tu opcion"
        info = my_text_db.translate(info, lg)
        # await bot.edit_message(id_chat, id_msg,info,buttons=keyb+keyboard,parse_mode='html')
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, info, user_dates, keyb + keyboard
        )
    if "net" in decoded:

        id_chat = sender.id
        id_msg = user_dates[user_id]["msg_id"]
        info = "Confirma tu eleccion:"
        info = my_text_db.translate(info, lg)
        idx = net_idx[decoded]
        keyb = net_sel_keyb.copy()
        print_to_web(net_sel_keyb)
        keyb[idx] = [Button.inline(f"•{decoded.replace('_net','')}", data=event.data)]
        keyboard = [[Button.inline("🧩Confirmar", data=b"confirm_dp")]]
        if (
            len(user_dates[user_id]["dep_root"]) == 0
            or len(user_dates[user_id]["dep_root"]) == 2
        ):
            # await bot.send_message(sender.id,'Selecciona cripto',buttons=cripto_sel_keyb)
            # await bot.edit_message(id_chat, id_msg,'Selecciona cripto',buttons=cripto_sel_keyb,parse_mode='html')
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates, cripto_sel_keyb
            )
            return 0
        # await bot.edit_message(id_chat, id_msg,info,buttons=keyb+keyboard,parse_mode='html')
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, info, user_dates, keyb + keyboard
        )
        user_dates[user_id]["dep_root"].append(net_idx[decoded])
    """
    if ("_cr" in decoded and "crypcas" not in decoded) or "_net" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/deposit/amount"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_info = ""

        if "cr" == decoded[-2:]:

            user_dates[user_id]["dep_root"] = [criptos_idx[decoded]]
            user_dates[user_id]["dep_cripto"] = decoded.replace("_cr", "")
            cripto_info += decoded.replace("_cr", "")
            user_dates[user_id]["cripto_info"] = cripto_info
            print_to_web(user_dates[user_id]["cripto_info"])

        if "_net" in decoded:

            idx = net_idx[decoded]

            if user_dates[user_id]["dep_cripto"] == "USDC":
                idx -= 2
                if idx < 0:
                    idx = 0

            user_dates[user_id]["dep_root"].append(idx)
            cripto_info = user_dates[user_id]["cripto_info"]
            cripto_info += f" – {decoded.replace('_net','')}"
            user_dates[user_id]["cripto_info"] = cripto_info
            if (
                len(user_dates[user_id]["dep_root"]) == 0
                or len(user_dates[user_id]["dep_root"]) == 3
            ):

                # await bot.send_message(sender.id,'Selecciona cripto',buttons=cripto_sel_keyb)
                # await bot.edit_message(id_chat, id_msg,'Selecciona cripto',buttons=cripto_sel_keyb,parse_mode='html')
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, info, user_dates, cripto_sel_keyb
                )
                return 0

        text = text.substitute(cripto_info=cripto_info)

        keyboard = info.keyboard
        print_to_web(min_dep[user_dates[user_id]["dep_cripto"]])
        amount_ = min_dep[user_dates[user_id]["dep_cripto"]]
        if isinstance(amount_, int):
            keyboard[0][1].text = str(amount_)
        else:
            keyboard[0][1].text = str("{:.9f}".format(amount_))
        user_dates[user_id]["dep_amount_sel"] = amount_
        user_dates[user_id]["dep_amount_sel_usd"] = (
            get_price(user_dates[user_id]["dep_cripto"])
            * user_dates[user_id]["dep_amount_sel"]
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"dep-":

        info = copy.deepcopy(menu_system["/main/wallet/deposit/amount"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_info = user_dates[user_id]["cripto_info"]
        text = text.substitute(cripto_info=cripto_info)
        user_dates[user_id]["dep_amount_sel_usd"] -= 1
        amount_sel = user_dates[user_id]["dep_amount_sel"]
        final_amount = amount_sel - usdt_to_cryp(user_dates[user_id]["dep_cripto"], 1)
        keyboard = info.keyboard

        keyboard[0][1].text = str("{:.9f}".format(final_amount))
        user_dates[user_id]["dep_amount_sel"] = final_amount

        if float(keyboard[0][1].text) <= min_dep[user_dates[user_id]["dep_cripto"]]:
            return 0
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"dep+":

        info = copy.deepcopy(menu_system["/main/wallet/deposit/amount"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_info = user_dates[user_id]["cripto_info"]
        text = text.substitute(cripto_info=cripto_info)
        amount_sel = user_dates[user_id]["dep_amount_sel"]
        user_dates[user_id]["dep_amount_sel_usd"] += 1
        final_amount = amount_sel + usdt_to_cryp(user_dates[user_id]["dep_cripto"], 1)
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(final_amount))
        user_dates[user_id]["dep_amount_sel"] = final_amount
        max_dep_ = max_dep[user_dates[user_id]["dep_cripto"]]
        if float(keyboard[0][1].text) >= max_dep_:
            return 0
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"dep_min":

        info = copy.deepcopy(menu_system["/main/wallet/deposit/amount"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_info = user_dates[user_id]["cripto_info"]
        text = text.substitute(cripto_info=cripto_info)

        keyboard = info.keyboard

        final_amount = min_dep[user_dates[user_id]["dep_cripto"]]
        keyboard[0][1].text = str("{:.9f}".format(final_amount))
        user_dates[user_id]["dep_amount_sel"] = final_amount
        user_dates[user_id]["dep_amount_sel_usd"] = (
            get_price(user_dates[user_id]["dep_cripto"])
            * user_dates[user_id]["dep_amount_sel"]
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"dep_conf":
        msg = await bot.send_message(-1002168522436, f"Deposito solicitado por:{user_id}")
        amount = user_dates[user_id]["dep_amount_sel_usd"]
        create_dates = crear_factura(amount, Test)

        pay_url = create_dates["bot_invoice_url"]
        id_ = pay_url.split("=")[1]
        await process_get_wallet(user_id, id_, amount)

        id = create_dates["invoice_id"]

        user_dates[user_id]["invoice_id"] = id

    if event.data == b"dep_bal":
        info = copy.deepcopy(menu_system["/main/wallet/deposit/amount/but_bal"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        await event.answer(text, alert=True)
        """
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
        """
    if event.data == b"wall_with":

        info = copy.deepcopy(menu_system["/main/wallet/withdraw"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"USDT_with-cr":

        info = copy.deepcopy(menu_system["/main/wallet/withdraw/net"])
        info.custom(lg)
        text = info.text
        text = Template(text)

        text = text.substitute(cripto="USDT")

        keyboard = info.keyboard
        user_dates[user_id]["with_root"] = [
            criptos_idx[f'{decoded.replace("_with-cr", "")}_cr']
        ]
        user_dates[user_id]["with_cripto"] = decoded.replace("_with-cr", "")
        cripto_info = decoded.replace("_with-cr", "")
        user_dates[user_id]["cripto_info_with"] = cripto_info

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route

        # await bot.send_message(sender.id,'Selecciona la red',buttons=net_sel_keyb)

        return 0
    if event.data == b"USDC_with-cr":

        info = copy.deepcopy(menu_system["/main/wallet/withdraw/net"])
        info.custom(lg)
        text = info.text
        text = Template(text)

        text = text.substitute(cripto="USDC")

        keyboard = info.keyboard
        keyboard.pop(0)
        user_dates[user_id]["with_root"] = [
            criptos_idx[f'{decoded.replace("_with-cr", "")}_cr']
        ]
        user_dates[user_id]["with_cripto"] = decoded.replace("_with-cr", "")
        cripto_info = decoded.replace("_with-cr", "")
        user_dates[user_id]["cripto_info_with"] = cripto_info

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route

        # await bot.send_message(sender.id,'Selecciona la red',buttons=net_sel_keyb)

        return 0
    if "with-cr" in decoded or "with-net" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/withdraw/address"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_info = ""

        if "with-cr" in decoded:

            user_dates[user_id]["with_root"] = [
                criptos_idx[f'{decoded.replace("_with-cr", "")}_cr']
            ]
            user_dates[user_id]["with_cripto"] = decoded.replace("_with-cr", "")
            cripto_info += decoded.replace("with-cr", "")
            user_dates[user_id]["cripto_info_with"] = cripto_info
            if "USDT" not in decoded:
                user_dates[user_id]["with_root"].append(0)

        if "with-net" in decoded:
            idx = net_idx[f'{decoded.replace("_with-net", "")}_net']
            if user_dates[user_id]["dep_cripto"] == "USDC":
                idx -= 2
                if idx < 0:
                    idx = 0
            user_dates[user_id]["with_root"].append(idx)
            cripto_info = user_dates[user_id]["cripto_info_with"]
            cripto_info += f" – {decoded.replace('with-net','')}"
            user_dates[user_id]["cripto_info_with"] = cripto_info
            user_dates[user_id]["with_net"] = decoded.replace("_with-net", "")
            if (
                len(user_dates[user_id]["with_root"]) == 0
                or len(user_dates[user_id]["with_root"]) > 2
            ):
                info = copy.deepcopy(menu_system["/main/wallet/withdraw"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                # await bot.send_message(sender.id,'Selecciona cripto',buttons=cripto_sel_keyb)
                # await bot.edit_message(id_chat, id_msg,'Selecciona cripto',buttons=cripto_sel_keyb,parse_mode='html')
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                return 0

        if user_dates[user_id]["with_cripto"] == "USDT" and "with-net" in decoded:
            key = f"USDT_{decoded.replace('_with-net','')}"
        else:
            key = user_dates[user_id]["with_cripto"]
        cripto_info = cripto_infos_with_net[key]

        text = text.substitute(
            cripto_info=cripto_info, cripto=user_dates[user_id]["with_cripto"]
        )
        keyboard = info.keyboard

        user_dates[user_id]["typing"] = "wallet_address"

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"with-amount":

        info = copy.deepcopy(menu_system["/main/wallet/withdraw/amount"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        if user_dates[user_id]["with_cripto"] == "USDT":
            key = f'USDT_{user_dates[user_id]["with_net"]}'
        else:
            key = user_dates[user_id]["with_cripto"]

        cripto_info = user_dates[user_id]["cripto_info_with"]
        cripto_info = cripto_infos_with_net[key]
        text = text.substitute(cripto_info=cripto_info)
        user_dates[user_id]["typing"] = "withdraw_amount"

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"with-confirm":
  

        info = copy.deepcopy(menu_system["/main/wallet/withdraw/confirm"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        if user_dates[user_id]["with_cripto"] == "USDT":
            key = f'USDT_{user_dates[user_id]["with_net"]}'
        else:
            key = user_dates[user_id]["with_cripto"]

        net_info = cripto_infos_with_net[key]
        address = user_dates[user_id]["withdraw_address"]
        address_abv = f"{address[:7]}...{address[-7:]}"
        fee = criptos[user_dates[user_id]["with_cripto"]]["fee"]
        send_am = user_dates[user_id]["withdraw_amount"] - fee
        cripto = user_dates[user_id]["with_cripto"]
        text = text.substitute(
            net_info=net_info,
            address=address,
            address_abv=address_abv,
            send_am=send_am,
            cripto=cripto,
            fee_am=fee,
            total_am=user_dates[user_id]["withdraw_amount"],
        )
        user_dates[user_id]["typing"] = "withdraw_amount"

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"with-confirm_fin":
        address = user_dates[user_id]["withdraw_address"]
        send_am = user_dates[user_id]["withdraw_amount"]
        info = copy.deepcopy(menu_system["/main/wallet/withdraw/wait"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        if user_dates[user_id]["with_cripto"] == "USDT":
            key = f'USDT_{user_dates[user_id]["with_net"]}'
        else:
            key = user_dates[user_id]["with_cripto"]

        net_info = cripto_infos_with_net[key]
        address = user_dates[user_id]["withdraw_address"]
        address_abv = f"{address[:7]}...{address[-7:]}"
        fee = criptos[user_dates[user_id]["with_cripto"]]["fee"]
        send_am = user_dates[user_id]["withdraw_amount"] - fee
        cripto = user_dates[user_id]["with_cripto"]
        text = text.substitute(
            net_info=net_info,
            address=address,
            address_abv=address_abv,
            send_am=send_am,
            cripto=cripto,
            fee_am=fee,
            total_am=user_dates[user_id]["withdraw_amount"],
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, int(user_id), text, user_dates, keyboard
        )
        if "pending_withdraws" not in user_dates[user_id]:
            user_dates[user_id]["pending_withdraws"] = {}
        user_dates[user_id]["pending_withdraws"][str(len(user_dates[user_id]["pending_withdraws"]))] = {
                "address": address,
                "amount":send_am ,
                "root":user_dates[user_id]["with_root"],
                "cripto":cripto  
        }
        username = str(await get_username_from_id(int(user_id)))
        await bot.send_message(-1002168522436,f"Retiro solicitado por: @{username}\n\n{text}\n\n\nConfirmacion: /confirm_withdraw {str(len(user_dates[user_id]['pending_withdraws'])-1)} {user_id}",parse_mode="html")
        return 0
        resp = await process_withdraw(str(sender.id), send_am, address,root)
        
        if resp == 1:
                print_to_web(cripto)
                print_to_web("rebaja..............")
                user_dates[user_id]["balance"][cripto] -= user_dates[user_id][
                    "withdraw_amount"
                ]
               
                await upload_db()

    # FEES
    if event.data == b"wall_fees":

        info = copy.deepcopy(menu_system["/main/wallet/fees"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "fee-cr" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/fees/info"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        user_dates[user_id]["fee_cr"] = decoded.replace("_fee-cr", "")

        if "USDT" in decoded:

            info = copy.deepcopy(menu_system["/main/wallet/fees/usdt-net"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route
            return 0
        if "USDC" in decoded:

            info = copy.deepcopy(menu_system["/main/wallet/fees/usdc-net"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route
            return 0

        text = text.substitute(
            cripto=decoded.replace("_fee-cr", ""),
            cripto_info=cripto_infos_with_net[decoded.replace("_fee-cr", "")],
            fee_with=str(criptos[decoded.replace("_fee-cr", "")]["fee"]),
            min_with=str(criptos[decoded.replace("_fee-cr", "")]["min_withdraw"]),
        )
        keyboard = info.keyboard
        if criptos[decoded.replace("_fee-cr", "")]["min_deposit"]:
            info = copy.deepcopy(menu_system["/main/wallet/fees/info2"])
            info.custom(lg)
            text = info.text
            text = Template(text)
            text = text.substitute(
                cripto=decoded.replace("_fee-cr", ""),
                cripto_info=cripto_infos_with_net[decoded.replace("_fee-cr", "")],
                fee_with=str(criptos[decoded.replace("_fee-cr", "")]["fee"]),
                min_with=str(criptos[decoded.replace("_fee-cr", "")]["min_withdraw"]),
                min_dep=str(criptos[decoded.replace("_fee-cr", "")]["min_deposit"]),
            )

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "fee-net" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/fees/info"])

        info.custom(lg)
        text = info.text
        text = Template(text)
        sel_cr = user_dates[user_id]["fee_cr"]
        sel_cr_ = f'{sel_cr}_{decoded.replace("_fee-net","")}'

        text = text.substitute(
            cripto=sel_cr,
            cripto_info=cripto_infos_with_net[sel_cr_],
            fee_with=str(criptos[sel_cr]["fee"][decoded.replace("_fee-net", "")]),
            min_with=str(
                criptos[sel_cr]["min_withdraw"][decoded.replace("_fee-net", "")]
            ),
        )
        keyboard = info.keyboard
        if criptos[sel_cr]["min_deposit"]:
            info = copy.deepcopy(menu_system["/main/wallet/fees/info2"])
            info.custom(lg)
            text = info.text
            text = Template(text)
            text = text.substitute(
                cripto=sel_cr,
                cripto_info=cripto_infos_with_net[sel_cr],
                fee_with=str(criptos[sel_cr]["fee"]),
                min_with=str(
                    criptos[sel_cr]["min_withdraw"][decoded.replace("_fee-net", "")]
                ),
                min_dep=str(
                    criptos[sel_cr]["min_deposit"][decoded.replace("_fee-net", "")]
                ),
            )

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"wall_swap":
        info = copy.deepcopy(menu_system["/main/wallet/swap"])
        info.custom(lg)
        text = info.text

        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"swap-referrals":

        if "ref_swaped" not in user_dates[str(sender.id)]:
            user_dates[str(sender.id)]["ref_swaped"] = 0
        info = copy.deepcopy(menu_system["/main/wallet/swap/ref"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        referrals = get_ref(user_dates, user_id)
        ref_swaped = user_dates[user_id]["ref_swaped"]
        if len(referrals["lvl1"]) - ref_swaped <= 0:
            info = copy.deepcopy(menu_system["/main/wallet/swap/ref0"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
        else:
            text = text.substitute(ref=str(len(referrals["lvl1"]) - ref_swaped))
            user_dates[user_id]["typing"] = "ref_swap_amount"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"swap-exchange_refs":
        swap_am = user_dates[user_id]["swap_am_sel_ref"]
        info = copy.deepcopy(menu_system["/main/ok"])
        user_dates[user_id]["ref_swaped"] += swap_am
        user_dates[user_id]["balance"]["USDT"] += ref_value * swap_am
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text.substitute(amount=str(swap_amount), cripto="USDT")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"swap-coin":

        info = copy.deepcopy(menu_system["/main/wallet/swap/coin1"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "swap-cr" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/swap/coin1/coin2"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        user_dates[user_id]["swap-coin1"] = decoded.replace("_swap-cr", "")

        text = text.substitute(cripto=user_dates[user_id]["swap-coin1"])
        keyboard = info.keyboard
        stop = False
        for x in range(len(keyboard)):
            print_to_web(len(keyboard))

            for y in range(len(keyboard[x])):
                print_to_web(len(keyboard[x]))
                print_to_web(f"err in {x} {y}")
                if user_dates[user_id]["swap-coin1"] in keyboard[x][y].text:

                    keyboard[x].pop(y)
                    stop = True
                    break
            if stop:
                break
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "swap1-cr" in decoded:

        info = copy.deepcopy(menu_system["/main/wallet/swap/coin1/coin2/am"])
        info.custom(lg)
        text = info.text
        text = Template(text)
        user_dates[user_id]["swap-coin2"] = decoded.replace("_swap1-cr", "")
        text = text.substitute(
            cripto1=user_dates[user_id]["swap-coin1"],
            cripto2=user_dates[user_id]["swap-coin2"],
        )
        keyboard = info.keyboard

        user_dates[user_id]["typing"] = "cripto_swap_amount"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"swap_exchange":
        amount = user_dates[user_id]["swap_am_sel_cripto"]
        cripto1 = user_dates[user_id]["swap-coin1"]
        cripto2 = user_dates[user_id]["swap-coin2"]
        print_to_web(cripto1)
        print_to_web(cripto2)
        cripto2_swap = ((amount * get_price(cripto1)) / get_price(cripto2)) * 0.98
        user_dates[user_id]["balance"][cripto1] -= amount
        user_dates[user_id]["balance"][cripto2] += cripto2_swap

        info = copy.deepcopy(menu_system["/main/ok"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(amount=str(cripto2_swap), crypto=cripto2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route


async def casino_cripto(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    decoded = event.data.decode("utf-8")
    """
    if  'idx' in event.data.decode('utf-8'):
        idx=event.data.decode('utf-8').split('_')[1]
        print_to_web(idx)
        user_dates[user_id].append((int(idx)))
     """
    if "leng" not in user_dates[user_id]:
        user_dates[user_id]["leng"] = "english"
    lg = user_dates[user_id]["leng"]

    # Seleccionar cripto para apo
    # star
    if "crypcas" in decoded:
        """
        game = user_dates[user_id]["game_sel"]
        idx = criptos_idx_casino[decoded.replace("crypcas", "cr")]
        keyb = bet_sel_keyb.copy()
        keyb[idx] = [
            Button.inline(f"•{decoded.replace('_crypcas','')}", data=event.data)
        ]
        """
        user_dates[user_id]["bet_cryp"] = decoded.replace("_crypcas", "")
        user_dates[user_id]["bet_size"] = criptos[user_dates[user_id]["bet_cryp"]]["min_amount"]
        """
        info = "Menu"
        info = my_text_db.translate(info, lg)

        ]
        keyboard = [
            [
                Button.inline("-", data=b"-cas"),
                Button.inline("change", data=b"wallet"),
                Button.inline("+", data=b"+cas"),
            ],
            [
                Button.inline("Min.", data=b"min_cas"),
                Button.inline("Double", data=b"doub_cas"),
                Button.inline("Max.", data=b"max_cas"),
            ],
            [Button.inline("< Back", data=b"back")],
        ]
        """
        await sel_game(event)

    # Comandos de bet size
    if event.data == b"-cas":
        await apost(event, "-")
    if event.data == b"+cas":
        await apost(event, "+")

    if event.data == b"min_cas":
        await apost(event, "min")
    if event.data == b"max_cas":
        await apost(event, "max")
    if event.data == b"doub_cas":
        await apost(event, "2x")
    if event.data == b"back_to_game":

        await sel_game(event)

    if event.data == b"bet_size":
        user_dates[user_id]["bet_size"] = criptos[user_dates[user_id]["bet_cryp"]][
            "min_amount"
        ]
        user_dates[user_id]["typing"] = "bet"
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        info = copy.deepcopy(menu_system["/main/casino/dado/game/bet_size"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    # Juegos

    if event.data == b"dice":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["game_sel"] = "dice"
        info = copy.deepcopy(menu_system["/main/casino/dado"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"no_apuesta":
        user_dates[str(sender.id)]["historial"] = "/main/casino/dado/game/er"
        await menu_action(event, "back")
    if event.data == b"rules":
        game = user_dates[user_id]["game_sel"]
        if game == "dice":

            info = copy.deepcopy(menu_system["/main/casino/dado/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        if game == "basket":

            info = copy.deepcopy(menu_system["/main/casino/basketball/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        if game == "darts":

            info = copy.deepcopy(menu_system["/main/casino/dardos/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        if game == "bowlling":

            info = copy.deepcopy(menu_system["/main/casino/bolos/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        if game == "football":

            info = copy.deepcopy(menu_system["/main/casino/football/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        if game == "slot_machine":

            info = copy.deepcopy(menu_system["/main/casino/slots/rules"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"basket":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["apuesta"] = "4-5"
        user_dates[user_id]["game_sel"] = "basket"
        info = copy.deepcopy(menu_system["/main/casino/basketball"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"darts":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["apuesta"] = 6
        user_dates[user_id]["game_sel"] = "darts"

        info = copy.deepcopy(menu_system["/main/casino/dardos"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"bowlling":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["apuesta"] = "5-6"
        user_dates[user_id]["game_sel"] = "bowlling"

        info = copy.deepcopy(menu_system["/main/casino/bolos"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"football":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["apuesta"] = "3-4-5"
        user_dates[user_id]["game_sel"] = "football"

        info = copy.deepcopy(menu_system["/main/casino/football"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"slot_machine":
        user_dates[user_id]["lost_count"] = 0
        user_dates[user_id]["apuesta"] = "3-4-5"
        user_dates[user_id]["game_sel"] = "slot_machine"

        info = copy.deepcopy(menu_system["/main/casino/slots"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    # Menus de juegos
    if event.data == b"play":
        # user_dates[user_id]['typing']='off'
        await azar_msg(event)
        # await sel_game(event)

    if "dice_" in decoded:

        apues = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            apues = float(apues)
        except:
            apues = apues

        user_dates[user_id]["apuesta"] = apues
        user_dates[user_id]["apuesta_cord"] = cords
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        info = copy.deepcopy(menu_system["/main/casino/dado/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        keyboard[0][
            0
        ].text = f"{keyboard[0][0].text} {str('{:.9f}'.format(user_dates[user_id]['bet_size']))}"
        await sel_game(event)
        # user_dates[user_id]['msg_id']=await edit_msg(bot,sender.id,text,user_dates,keyboard)
        # user_dates[user_id]['historial']=info.route

    """
    if b'bet_size'==event.data:
        keyboard=[[Button.inline('-', data=b'-cas'),Button.inline(str('{:.9f}'.format(user_dates[user_id]['bet_size'])), data=b'wallet'),Button.inline('+' ,data=b'+cas')],
                  [Button.inline('Min.', data=b'min_cas'),Button.inline('Double', data=b'doub_cas'),Button.inline('Max.', data=b'max_cas')],
                  [Button.inline('< Back', data=b'back'),Button.inline('Play', data=b'play')]
                  ]
        info='Menu'
        info=my_text_db.translate(info,lg)
        user_dates[user_id]['msg_id']=await edit_msg(bot,sender.id,info,user_dates,keyboard)
    """
    # if event.data==b'play':


async def grid_cripto(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    decoded = event.data.decode("utf-8")

    if not user_id in user_dates:
        user_dates[user_id] = {}

    if "leng" not in user_dates[user_id]:
        user_dates[user_id]["leng"] = "english"
    lg = user_dates[user_id]["leng"]

    # Seleccionar cripto para apostar
    if "_crypgrid" in decoded:
        user_dates[user_id]["typing"] = "grid"
        cryp = decoded.replace("_crypgrid", "")
        user_dates[user_id]["grid_cryp"] = cryp
        cripto = cryp
        info = menu_system["/main/grid/new_grid_cripto/new_grid_am"]
        info.custom(lg)
        text = info.text
        text = Template(text)
        cripto_price = "{:.9f}".format(get_price(cripto))
        text = text.substitute(
            cripto=f"{color_crypto[cripto]} {cripto}",
            cripto_info=f"≈ {str(cripto_price)} USDT",
        )
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "lev_" in decoded and "man_grid" not in decoded:
        lev = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            lev = float(lev)
        except:
            lev = lev

        user_dates[user_id]["grid_lev"] = lev
        user_dates[user_id]["lev_cord"] = cords

        info = copy.deepcopy(menu_system["/main/grid/manual/leverage"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "minords_" in decoded and "man_grid" not in decoded:
        min = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            min = int(min)
        except:
            min = min

        user_dates[user_id]["grid_minords"] = min
        user_dates[user_id]["minords_cord"] = cords

        info = copy.deepcopy(menu_system["/main/grid/manual/day_ords/min_ords"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "maxords_" in decoded and "man_grid" not in decoded:
        max = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            max = int(max)
        except:
            max = max

        user_dates[user_id]["grid_maxords"] = max
        user_dates[user_id]["maxords_cord"] = cords

        info = copy.deepcopy(menu_system["/main/grid/manual/day_ords/max_ords"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "sl_" == decoded[0:3] and "man_grid" not in decoded:
        sl = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            sl = float(sl)
        except:
            sl = sl

        user_dates[user_id]["grid_sl"] = sl
        user_dates[user_id]["sl_cord"] = cords

        info = copy.deepcopy(menu_system["/main/grid/manual/sl"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        text = Template(text)
        text = text.substitute(sl=f"{str(sl)}%")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "tp_" in decoded and "man_grid" not in decoded:
        tp = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            tp = float(tp)
        except:
            tp = tp

        user_dates[user_id]["grid_tp"] = tp
        user_dates[user_id]["tp_cord"] = cords

        info = copy.deepcopy(menu_system["/main/grid/manual/tp"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        tp = keyboard[x][y].text
        text = Template(text)
        text = text.substitute(tp=tp)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"create_auto_grid":
        info = copy.deepcopy(
            menu_system["/main/grid/new_grid_cripto/new_grid_am_ok/automatic"]
        )
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        if "bots" not in user_dates[user_id]:
            user_dates[user_id]["bots"] = {}
        idx = 1
        for key in user_dates[user_id]["bots"]:
            idx += 1

        user_dates[user_id]["bots"][str(idx)] = {
            "cripto": user_dates[user_id]["grid_cryp"],
            "usd_am": user_dates[user_id]["grid_amount"],
            "tp": 20,
            "sl": 20,
            "min_ords": 5,
            "lvg": 10,
            "date": time.time(),
            "ord_today": 0,
            "ord_total": 0,
            "shorts": 0,
            "longs": 0,
            "prof_today": 0,
            "prof_total": 0,
        }
        """
        msg_to_del = []
        msg_ = await bot.send_message(
            sender.id, "🤖 Creating Bot...", parse_mode="html"
        )
        msg_to_del.append(msg_)
        msg_ = await bot.send_message(
            sender.id, "☁️ Uploading Data....", parse_mode="html"
        )
        msg_to_del.append(msg_)
        msg_ = await bot.send_message(sender.id, "🎉 🎉 🎉", parse_mode="html")

        msg_to_del.append(msg_)
        await asyncio.sleep(1)
        await bot.delete_messages(entity=sender.id, message_ids=msg_to_del)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        """
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "🤖 Creating Bot...", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "☁️ Uploading Data....", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(bot, sender.id, "🎉", user_dates)
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route
        await upload_db()

    if "lvgmanag_" in decoded:
        lev = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            lev = float(lev)
        except:
            lev = lev
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        user_dates[user_id]["bots"][str(idx)]["lvg"] = lev
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/leverage"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "slmanag_" in decoded:
        sl = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            sl = float(sl)
        except:
            sl = sl

        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        user_dates[user_id]["bots"][str(idx)]["sl"] = sl

        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/sl"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        text = Template(text)
        text = text.substitute(sl=f"{str(sl)}%")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if "tpmanag_" in decoded and "man_grid" not in decoded:
        tp = decoded.split("{")[0].split("_")[1]
        cords = decoded.split("{")[1].split(",")
        x = int(cords[0])
        y = int(cords[1])

        try:
            tp = float(tp)
        except:
            tp = tp

        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        user_dates[user_id]["bots"][str(idx)]["tp"] = tp

        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/tp"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        text = Template(text)
        text = text.substitute(tp=f"{str(tp)}%")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"create_manual_grid":
        info = copy.deepcopy(
            menu_system["/main/grid/new_grid_cripto/new_grid_am_ok/manual"]
        )
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"leverage_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/leverage"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        if not "lev_cord" in user_dates[user_id]:
            user_dates[user_id]["lev_cord"] = None
        cords = user_dates[user_id]["lev_cord"]
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"dailyords_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/day_ords"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"minords_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/day_ords/min_ords"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        if not "minords_cord" in user_dates[user_id]:
            user_dates[user_id]["minords_cord"] = None
        cords = user_dates[user_id]["minords_cord"]
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"maxords_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/day_ords/max_ords"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        if "maxords_cord" not in user_dates[user_id]:
            user_dates[user_id]["maxords_cord"] = None
        cords = user_dates[user_id]["maxords_cord"]
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"sl_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/sl"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        if not "sl_cord" in user_dates[user_id]:
            user_dates[user_id]["sl_cord"] = None
        cords = user_dates[user_id]["sl_cord"]
        sl = "--"
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
            sl = keyboard[x][y].text
        text = Template(text)
        text = text.substitute(sl=sl)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"tp_man_grid":
        info = copy.deepcopy(menu_system["/main/grid/manual/tp"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        if not "tp_cord" in user_dates[user_id]:
            user_dates[user_id]["tp_cord"] = None
        cords = user_dates[user_id]["tp_cord"]
        tp = "--"
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
            tp = keyboard[x][y].text
        text = Template(text)
        text = text.substitute(tp=tp)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"done_create_man_gd":
        info = copy.deepcopy(menu_system["/main/grid/done"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        if "bots" not in user_dates[user_id]:
            user_dates[user_id]["bots"] = {}
        idx = 1
        for key in user_dates[user_id]["bots"]:
            idx += 1
        tp = 20
        sl = 20
        min_ords = 5

        if "grid_tp" in user_dates[user_id]:
            tp = user_dates[user_id]["grid_tp"]
        if "grid_sl" in user_dates[user_id]:
            sl = user_dates[user_id]["grid_sl"]

        if "grid_minords" in user_dates[user_id]:
            min_ords = user_dates[user_id]["grid_minords"]

        if "lvg" in user_dates[user_id]:
            lvg = user_dates[user_id]["grid_lev"]

        user_dates[user_id]["bots"][str(idx)] = {
            "cripto": user_dates[user_id]["grid_cryp"],
            "usd_am": user_dates[user_id]["grid_amount"],
            "tp": tp,
            "sl": sl,
            "min_ords": min_ords,
            "lvg": lvg,
            "date": time.time(),
            "ord_today": 0,
            "ord_total": 0,
            "shorts": 0,
            "longs": 0,
            "prof_today": 0,
            "prof_total": 0,
        }
        """
        msg_to_del = []
        msg_ = await bot.send_message(
            sender.id, "🤖 Creating Bot...", parse_mode="html"
        )
        msg_to_del.append(msg_)
        msg_ = await bot.send_message(
            sender.id, "☁️ Uploading Data....", parse_mode="html"
        )
        msg_to_del.append(msg_)
        msg_ = await bot.send_message(sender.id, "🎉 🎉 🎉", parse_mode="html")

        msg_to_del.append(msg_)
        await asyncio.sleep(1)
        await bot.delete_messages(entity=sender.id, message_ids=msg_to_del)
        """

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "🤖 Creating Bot...", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "☁️ Uploading Data....", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(bot, sender.id, "🎉", user_dates)
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route
        await upload_db()

    if event.data == b"manage_done" or event.data == b"manage_gd":
        info = copy.deepcopy(menu_system["/main/grid/manage"])
        info.custom(lg)
        text = info.text

        keyboard = []

        if "bots" not in user_dates[user_id]:
            user_dates[user_id]["bots"] = {}

        for key in user_dates[user_id]["bots"]:
            bot_name = f'{color_crypto[user_dates[user_id]["bots"][key]["cripto"]]} {user_dates[user_id]["bots"][key]["cripto"]}'
            keyboard.append([Button.inline(bot_name, data=f"gdbot_id:{str(key)}")])
            print_to_web(key)
        keyboard.append([Button.inline("< Back", data=b"back")])
        if len(user_dates[user_id]["bots"]) == 0:
            info = copy.deepcopy(menu_system["/main/grid/manage_0"])
            info.custom(lg)
            text = info.text

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if "gdbot_id:" in decoded:

        print_to_web("Yes")
        info = copy.deepcopy(menu_system["/main/grid/manage/bot"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        idx = decoded.split(":")[1]
        print_to_web(idx)
        print_to_web(user_dates[user_id]["bots"])
        user_dates[user_id]["bot_sel"] = str(idx)
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        cripto = bot_dates["cripto"]
        cripto_price = "{:.9f}".format(get_price(cripto))
        lvg = bot_dates["lvg"]
        sl = bot_dates["sl"]
        tp = bot_dates["tp"]
        ords_today = bot_dates["ord_today"]
        ords_total = bot_dates["ord_total"]
        shorts = bot_dates["shorts"]
        longs = bot_dates["longs"]
        invest = bot_dates["usd_am"]
        perc_profittoday = bot_dates["prof_today"]
        brute_profittoday = round((perc_profittoday / 100) * invest, 6)
        perc_profittotal = bot_dates["prof_total"]
        brute_profittotal = round((perc_profittotal / 100) * invest, 6)
        print_to_web(bot_dates["prof_total"])
        perc_apr = round(
            1
            + ((perc_profittotal / invest) * 100)
            * (365 / ((time.time() - bot_dates["date"]) / (3600 * 24)))
            - 1,
            6,
        )

        brute_apr = round((perc_apr / 100) * invest, 6)

        # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
        text = Template(text)
        text = text.substitute(
            cripto=f"{color_crypto[cripto]} {cripto}",
            cripto_in_usd=cripto_price,
            leverage=lvg,
            SL=sl,
            TP=tp,
            orders_today=ords_today,
            orders_total=ords_total,
            longs=longs,
            shorts=shorts,
            invest=invest,
            profit_today=perc_profittoday,
            profit_today_brute=brute_profittoday,
            profit_total=perc_profittotal,
            profit_total_brute=brute_profittotal,
            apr=perc_apr,
            apr_brute=brute_apr,
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"manage_botgd":
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        cripto = bot_dates["cripto"]
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        text = Template(text)

        text = text.substitute(cripto=f"{color_crypto[cripto]} {cripto}")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"share_botgd":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/share"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"botgd_sl":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/sl"])
        info.custom(lg)

        text = info.text
        keyboard = info.keyboard
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        sl = str(int(bot_dates["sl"])).replace("%", "")
        print_to_web(sl)
        if keyboard:
            for x in range(len(keyboard)):

                for y in range(len(keyboard[x])):
                    print_to_web(str(keyboard[x][y].text).replace("%", ""))
                    if str(keyboard[x][y].text).replace("%", "") == sl:

                        try:
                            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
                        except Exception as e:
                            print_to_web(e)
        text = Template(text)
        text = text.substitute(sl=f"{str(sl)}%")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"botgd_tp":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/tp"])
        info.custom(lg)

        text = info.text
        keyboard = info.keyboard
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        tp = str(int(bot_dates["tp"])).replace("%", "")

        if keyboard:
            for x in range(len(keyboard)):

                for y in range(len(keyboard[x])):
                    print_to_web(str(keyboard[x][y].text).replace("%", ""))
                    if str(keyboard[x][y].text).replace("%", "") == tp:

                        try:
                            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
                        except Exception as e:
                            print_to_web(e)

        text = Template(text)
        text = text.substitute(tp=f'{str(bot_dates["tp"])}%')
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"leverage_botgd":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/leverage"])
        info.custom(lg)

        text = info.text
        keyboard = info.keyboard
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        lev = str(int(bot_dates["lvg"])).replace("x", "")

        if keyboard:
            for x in range(len(keyboard)):

                for y in range(len(keyboard[x])):
                    print_to_web(str(keyboard[x][y].text).replace("x", ""))
                    if str(keyboard[x][y].text).replace("x", "") == lev:

                        try:
                            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
                        except Exception as e:
                            print_to_web(e)

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"delete_botgd":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/delete"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"increase_botgd":
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        am = str(int(bot_dates["usd_am"]))
        user_dates[user_id]["typing"] = "increase_am"
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/increase_found"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(invest=f"{am} USDT")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"decrease_botgd":
        idx = user_dates[user_id]["bot_sel"]
        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
        bot_dates = user_dates[user_id]["bots"][str(idx)]
        am = str(int(bot_dates["usd_am"]))
        user_dates[user_id]["typing"] = "decrease_am"
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/decrease_found"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(invest=f"{am} USDT")
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    if event.data == b"yes_deletebot":
        idx = user_dates[user_id]["bot_sel"]
        user_dates[user_id]["bots"].pop(idx)

        info = copy.deepcopy(menu_system["/main/grid/manage/deleted"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"del_nope" or event.data == b"del_no":
        await menu_action(event, "back")
    if event.data == b"share_launch":
        idx = user_dates[user_id]["bot_sel"]
        if not "launched" in user_dates[user_id]:
            user_dates[user_id]["launched"] = {}
        user_dates[user_id]["launched"][idx] = {
            "copiers": [],
            "copiers_out": 0,
            "last_earn": 0,
            "total_earn": 0,
            "time": time.time(),
            "apr": 0,
            "profit_tod": 0,
            "profit_total": 0,
        }
        text = "🚀"
        user_dates[user_id]["msg_id"] = await edit_msg(bot, sender.id, text, user_dates)
        await asyncio.sleep(1)
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/share/launch"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"share_statics":
        info = copy.deepcopy(menu_system["/main/grid/manage/bot/conf/share/statics"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        idx = user_dates[user_id]["bot_sel"]
        dates = user_dates[user_id]["launched"][idx]
        text = Template(text)
        # user_dates[user_id]['launched'][idx]={'copiers':0,'copiers_out':0,'last_earn':0,'total_earn':0,'time':time.time(),'apr':0,'profit_tod':0,'profit_total':0}
        text = text.substitute(
            copiers=len(dates["copiers"]),
            copiers_out=dates["copiers_out"],
            earn_yest=dates["last_earn"],
            earn_total=dates["total_earn"],
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"copy_grid":
        copy_bots = []
        for uid in user_dates:
            if "launched" in user_dates[uid]:
                for id_ in user_dates[uid]["launched"]:
                    # copy_bots_=user_dates[uid]['launched'][id_]
                    copy_bots_ = user_dates[uid]["bots"][id_]
                    copy_bots_["idx"] = id_
                    copy_bots_["uid"] = uid
                    copy_bots.append(copy_bots_)
        if not "copy_idx" in user_dates[user_id]:
            user_dates[user_id]["copy_idx"] = 0
        idx_sel = user_dates[user_id]["copy_idx"]

        if len(copy_bots) == 0:
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 bots", user_dates, keyboard
            )
            return 0
        copy_opt = copy_bots[idx_sel]
        uid = copy_opt["uid"]
        id_ = copy_opt["idx"]
        info = copy.deepcopy(menu_system["/main/grid/copy"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}

        cripto = copy_opt["cripto"]
        cripto_price = "{:.9f}".format(get_price(cripto))
        lvg = copy_opt["lvg"]
        sl = copy_opt["sl"]
        tp = copy_opt["tp"]
        ords_today = copy_opt["ord_today"]
        ords_total = copy_opt["ord_total"]
        shorts = copy_opt["shorts"]
        longs = copy_opt["longs"]
        invest = copy_opt["usd_am"]
        perc_profittoday = copy_opt["prof_today"]
        brute_profittoday = round((perc_profittoday / 100) * invest, 6)
        perc_profittotal = copy_opt["prof_total"]
        brute_profittotal = round((perc_profittotal / 100) * invest, 6)

        perc_apr = round(
            1
            + ((perc_profittotal / invest) * 100)
            * (
                365
                / (
                    (time.time() - user_dates[uid]["launched"][id_]["time"])
                    / (3600 * 24)
                )
            )
            - 1,
            6,
        )

        brute_apr = round((perc_apr / 100) * invest, 6)

        # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
        text = Template(text)
        text = text.substitute(
            cripto=f"{color_crypto[cripto]} {cripto}",
            cripto_in_usd=cripto_price,
            leverage=lvg,
            SL=sl,
            TP=tp,
            orders_today=ords_today,
            orders_total=ords_total,
            longs=longs,
            shorts=shorts,
            profit_today=perc_profittoday,
            profit_today_brute=brute_profittoday,
            profit_total=perc_profittotal,
            profit_total_brute=brute_profittotal,
            days_online=str(
                int(
                    (time.time() - user_dates[uid]["launched"][id_]["time"]) / 3600 / 24
                )
            ),
            apr=perc_apr,
            apr_brute=brute_apr,
        )

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"ant_copy":
        copy_bots = []
        idx_sel = user_dates[user_id]["copy_idx"]
        for uid in user_dates:
            if "launched" in user_dates[uid]:
                for id_ in user_dates[uid]["launched"]:
                    # copy_bots_=user_dates[uid]['launched'][id_]
                    copy_bots_ = user_dates[uid]["bots"][id_]
                    copy_bots_["idx"] = id_
                    copy_bots_["uid"] = uid
                    copy_bots.append(copy_bots_)
        if not "copy_idx" in user_dates[user_id]:
            user_dates[user_id]["copy_idx"] = 0

        if idx_sel <= 0:

            user_dates[user_id]["copy_idx"] = len(copy_bots) - 1
        else:
            user_dates[user_id]["copy_idx"] -= 1

        idx_sel = user_dates[user_id]["copy_idx"]

        copy_opt = copy_bots[idx_sel]
        uid = copy_opt["uid"]
        id_ = copy_opt["idx"]
        info = copy.deepcopy(menu_system["/main/grid/copy"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}

        cripto = copy_opt["cripto"]
        cripto_price = "{:.9f}".format(get_price(cripto))
        lvg = copy_opt["lvg"]
        sl = copy_opt["sl"]
        tp = copy_opt["tp"]
        ords_today = copy_opt["ord_today"]
        ords_total = copy_opt["ord_total"]
        shorts = copy_opt["shorts"]
        longs = copy_opt["longs"]
        invest = copy_opt["usd_am"]
        perc_profittoday = copy_opt["prof_today"]
        brute_profittoday = round((perc_profittoday / 100) * invest, 6)
        perc_profittotal = copy_opt["prof_total"]
        brute_profittotal = round((perc_profittotal / 100) * invest, 6)

        perc_apr = round(
            1
            + ((perc_profittotal / invest) * 100)
            * (
                365
                / (
                    (time.time() - user_dates[uid]["launched"][id_]["time"])
                    / (3600 * 24)
                )
            )
            - 1,
            6,
        )

        brute_apr = round((perc_apr / 100) * invest, 6)

        # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
        text = Template(text)
        text = text.substitute(
            cripto=f"{color_crypto[cripto]} {cripto}",
            cripto_in_usd=cripto_price,
            leverage=lvg,
            SL=sl,
            TP=tp,
            orders_today=ords_today,
            orders_total=ords_total,
            longs=longs,
            shorts=shorts,
            profit_today=perc_profittoday,
            profit_today_brute=brute_profittoday,
            profit_total=perc_profittotal,
            profit_total_brute=brute_profittotal,
            days_online=str(
                int(
                    (time.time() - user_dates[uid]["launched"][id_]["time"]) / 3600 / 24
                )
            ),
            apr=perc_apr,
            apr_brute=brute_apr,
        )

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"post_copy":
        copy_bots = []
        idx_sel = user_dates[user_id]["copy_idx"]
        for uid in user_dates:
            if "launched" in user_dates[uid]:
                for id_ in user_dates[uid]["launched"]:
                    # copy_bots_=user_dates[uid]['launched'][id_]
                    copy_bots_ = user_dates[uid]["bots"][id_]
                    copy_bots_["idx"] = id_
                    copy_bots_["uid"] = uid
                    copy_bots.append(copy_bots_)
        if not "copy_idx" in user_dates[user_id]:
            user_dates[user_id]["copy_idx"] = 0
        if idx_sel >= len(copy_bots) - 1:

            user_dates[user_id]["copy_idx"] = 0
        else:
            user_dates[user_id]["copy_idx"] += 1
        idx_sel = user_dates[user_id]["copy_idx"]
        copy_opt = copy_bots[idx_sel]
        uid = copy_opt["uid"]
        id_ = copy_opt["idx"]
        info = copy.deepcopy(menu_system["/main/grid/copy"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}

        cripto = copy_opt["cripto"]
        cripto_price = "{:.9f}".format(get_price(cripto))
        lvg = copy_opt["lvg"]
        sl = copy_opt["sl"]
        tp = copy_opt["tp"]
        ords_today = copy_opt["ord_today"]
        ords_total = copy_opt["ord_total"]
        shorts = copy_opt["shorts"]
        longs = copy_opt["longs"]
        invest = copy_opt["usd_am"]
        perc_profittoday = copy_opt["prof_today"]
        brute_profittoday = round((perc_profittoday / 100) * invest, 6)
        perc_profittotal = copy_opt["prof_total"]
        brute_profittotal = round((perc_profittotal / 100) * invest, 6)

        perc_apr = round(
            1
            + ((perc_profittotal / invest) * 100)
            * (
                365
                / (
                    (time.time() - user_dates[uid]["launched"][id_]["time"])
                    / (3600 * 24)
                )
            )
            - 1,
            6,
        )

        brute_apr = round((perc_apr / 100) * invest, 6)

        # info='$cipto/USDT\n• 1 $cripto ≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leveragex\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📈 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Compras - $shorts Ventas)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Anualizado)\n•$apr% ≈ $apr_brute USDT'
        text = Template(text)
        text = text.substitute(
            cripto=f"{color_crypto[cripto]} {cripto}",
            cripto_in_usd=cripto_price,
            leverage=lvg,
            SL=sl,
            TP=tp,
            orders_today=ords_today,
            orders_total=ords_total,
            longs=longs,
            shorts=shorts,
            profit_today=perc_profittoday,
            profit_today_brute=brute_profittoday,
            profit_total=perc_profittotal,
            profit_total_brute=brute_profittotal,
            days_online=str(
                int(
                    (time.time() - user_dates[uid]["launched"][id_]["time"]) / 3600 / 24
                )
            ),
            apr=perc_apr,
            apr_brute=brute_apr,
        )

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    if event.data == b"copy_bot":
        copy_bots = []
        for uid in user_dates:
            if "launched" in user_dates[uid]:
                for id_ in user_dates[uid]["launched"]:
                    # copy_bots_=user_dates[uid]['launched'][id_]
                    copy_bots_ = copy.deepcopy(user_dates[uid]["bots"][id_])
                    copy_bots_["idx"] = id_
                    copy_bots_["uid"] = uid
                    copy_bots.append(copy_bots_)
        if not "copy_idx" in user_dates[user_id]:
            user_dates[user_id]["copy_idx"] = 1

        if "bots" not in user_dates[user_id]:
            user_dates[user_id]["bots"] = {}

        idx_sel = user_dates[user_id]["copy_idx"]

        copy_opt = copy_bots[idx_sel]
        uid = copy_opt["uid"]
        id_ = copy_opt["idx"]
        info = copy.deepcopy(menu_system["/main/grid/copy/copy_sel_am"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["typing"] = "copy_am"

        idx = 1
        for key in user_dates[user_id]["bots"]:
            idx += 1
        user_dates[user_id]["bot_sel"] = idx

        # user_dates[user_id]['bots'][str(idx)]={'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}

        # user_dates[user_id]['launched'][idx]={'copiers':0,'copiers_out':0,'last_earn':0,'total_earn':0,'time':time.time(),'apr':0,'profit_tod':0,'profit_total':0}
        user_dates[uid]["launched"][id_]["copiers"].append(user_id)
        user_dates[user_id]["bots"][str(idx)] = copy.deepcopy(
            user_dates[uid]["bots"][id_]
        )
        user_dates[user_id]["bots"][str(idx)]["user_copied"] = uid
        user_dates[user_id]["bots"][str(idx)]["bot_copied"] = id_
        user_dates[user_id]["bots"][str(idx)]["usd_am"] = 0
        user_dates[user_id]["bots"][str(idx)]["ord_today"] = 0
        user_dates[user_id]["bots"][str(idx)]["ord_total"] = 0
        user_dates[user_id]["bots"][str(idx)]["shorts"] = 0
        user_dates[user_id]["bots"][str(idx)]["longs"] = 0
        user_dates[user_id]["bots"][str(idx)]["prof_today"] = 0
        user_dates[user_id]["bots"][str(idx)]["prof_total"] = 0
        user_dates[user_id]["bots"][str(idx)]["date"] = time.time()
        # user_dates[user_id]['bots'][str(idx)]['copied']=True
        """
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "🤖 Creating Bot...", user_dates
        )
        await asyncio.sleep(1)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "☁️ Uploading Data....", user_dates
        )
        await asyncio.sleep(1)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "🎉", user_dates
        )
        await asyncio.sleep(1)
        """
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )


# DB FUNCS
async def download_db_():
    # return 0
    global on_saving
    if not on_saving:
        on_saving = True
        ruta_original = "admin.session"
        ruta_copia = "cache/admin_downdb.session"
        user = admin
        # user = TelegramClient(str("admin"), api_id, api_hash)

        while True:
            try:

                if not user.is_connected():
                    await user.connect()
                    print_to_web("Not conected.Conecting..")
                break
            except Exception as e:
                print_to_web(f"Error en el connect del downdb{e}")

                await asyncio.sleep(3)

        print_to_web("Downloading db..")
        messages = await user.get_messages(
            -4154626193, filter=InputMessagesFilterDocument, limit=10
        )

        # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
        for message in messages:
            if message.media:
                file_path = await user.download_media(message.media, file="db/data")
        user.disconnect()

        on_saving = False


async def upload_db_(account=None):
    # return 0

    global on_saving
    if not on_saving:
        on_saving = True
        print_to_web("Uploading..")

        """
        folder='cache'
        file_name=str(int(time.time()))+'.session'
        file_path=f'{folder}/{file_name}'
        original_file='admin.session'
        while True:
            if not Path(file_path).exists():
                print_to_web("yes")
                shutil.copyfile(original_file,file_path)
                break
            else:
                file_name=str(int(time.time()))+'.session'
                file_path=f'{folder}/{file_name}'
            """
        dict_to_txt(user_dates, "db/data")
        ruta_original = "admin.session"
        ruta_copia = "cache/admin_.session"

        user = admin
        if account:
            user = account

        for i in range(10):

            try:

                if not user.is_connected():
                    await user.connect()
                    print_to_web("Not conected.Conecting..")
                break
            except Exception as e:
                print_to_web(f"Error en la conexion.#critic:{e}")

                await asyncio.sleep(2)
        for i in range(10):
            try:
                messages = await user.get_messages(
                    -4154626193, filter=InputMessagesFilterDocument, limit=10
                )
                # Itera sobre los mensajes para encontrar y descargar archivos adjuntos
                for message in messages:
                    print_to_web(message.id)
                    await user.delete_messages(-4154626193, [message.id])

                await user.send_file(
                    -4154626193, "db/data", caption=f"saved: {str(time.time())}"
                )
                break
            except Exception as e:
                print_to_web("Datbase no guardada")
                print_to_web(e)

        user.disconnect()
        # os.remove(file_path)

        on_saving = False


async def upload_db(account=None):
    global first_init
    await db_semaforo.acquire()
    try:
        if not first_init:
            task = asyncio.create_task(upload_db_(account))
            await task
    except Exception as e:
        print_to_web(e)
    db_semaforo.release()


async def download_db():
    await db_semaforo.acquire()
    try:
        task = asyncio.create_task(download_db_())
        await task
    except Exception as e:
        print_to_web(e)
    db_semaforo.release() 

async def send_massive(msg=None,users = None,info_ = None):
        lg = "en"
        msg =msg
        keyb = None
        info =  copy.deepcopy(menu_system[info_])
        if info:
            info.custom(lg)
            msg =info.text
            keyb = info.keyboard
        if users:
            for uid in users:
                try:
                    await bot.send_message(int(uid),msg,buttons=keyb,parse_mode="html",link_preview=False) 
                    
                except:pass    
                return 0 
        users = []
        for uid in user_dates:
            users.append(uid)
        for uid in users:
            
            try:
                await bot.send_message(int(uid),msg,buttons=keyb,parse_mode="html",link_preview=False)
                
                print(f"enviado a {uid}-->{await get_username_from_id(int(uid))} ")
            except:pass
            
async def init_dates():
    print_to_web("init dates")

    global first_init
    global user_dates

    if first_init:
        try:

            await download_db()
            await asyncio.sleep(2)
            # await upload_sessiondb()

            # await upload_db()

            user_dates = txt_to_dict("db/data")
            # print_to_web(user_dates)

            print_to_web("Datos iniciados con exito")
            first_init = False
            if "admin_settings" not in user_dates["1633521428"]:
                user_dates["1633521428"]["admin_settings"] = {"temporizer_date":0}
            
            #await send_massive(info_ = "/main")
        except Exception as e:
            print_to_web(e)


# Apuesta
async def azar_msg(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    game = user_dates[user_id]["game_sel"]
    apuesta = user_dates[user_id]["apuesta"]
    ganance = user_dates[user_id]["bet_size"]
    lg = user_dates[user_id]["leng"]

    if not apuesta and game == "dice":
        info = copy.deepcopy(menu_system["/main/casino/dado/game/er"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[str(sender.id)]["historial"] = info.route
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        return 0
    
    if not "lost_count" in user_dates[user_id]:
        user_dates[user_id]["lost_count"] = 0
    if  user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] < user_dates[user_id]["bet_size"]:
        return 0
    try:

        await bot.delete_messages(
            entity=int(user_id), message_ids=user_dates[user_id]["msg_id_"]
        )

    except Exception as e:
        print_to_web(f"error in delete {e}")
        
    user_dates[user_id]["msg_id_"] = []
    msg_1 = await bot.send_message(sender.id, "🍀 Good Luck!", parse_mode="html")
    user_dates[user_id]["msg_id_"] = [msg_1.id]

    initial_balance = user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]]
    if game == "dice":

        result = bot_pytel.send_dice(chat_id=sender.id, emoji="🎲")
        msg_id = result.message_id

        # user_dates[user_id]['msg_id_'].append(int(msg_id))
        print_to_web(user_dates[user_id]["msg_id"])
        result = [result.dice.value]
        result_ = result[0]

        num_emoji = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣"}
        paridad = "even"
        duo = result_ - 0.5
        if result_ % 2 != 0:
            paridad = "odd"
            duo = result_ + 0.5

        result.append(paridad)
        result.append(duo)

        ganance_rate = {result_: 5, duo: 2.7, paridad: 1.8}
        info = f"{num_emoji[result_]} - {paridad}"
        msg_perd = ["😖 Bad luck", "😉 Try again", "😉 Try again", "😉 Try again"]
        al_num = random.randint(0, 3)

        if apuesta in result:
            info += f'\n\n✅ You won {str("{:.9f}".format(ganance*ganance_rate[apuesta]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[apuesta] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            info += f"\n\n{msg_perd[al_num]}"
            user_dates[user_id]["lost_count"] += 1
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] -= ganance

    if game == "basket":

        result = bot_pytel.send_dice(chat_id=sender.id, emoji="🏀")
        msg_id = result.message_id
        # user_dates[user_id]['msg_id_'].append(msg_id)
        result = result.dice.value
        ganance_rate = {
            4: {"ratio": 2.5, "msg": "🤑 SPLAAAAASH 🤑"},
            5: {"ratio": 1.5, "msg": "💪 GOOD SHOT 💪"},
        }
        msg_perd = ["😵 Stuck", "😏 Nice try", "👌 Very close", "😉 Try again"]
        al_num = random.randint(0, 3)
        info = msg_perd[al_num]

        if result in ganance_rate:
            info = ganance_rate[result]["msg"]
            info += f'\n\n✅️ You won {str("{:.9f}".format(ganance*ganance_rate[result]["ratio"]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[result]["ratio"] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            user_dates[user_id]["lost_count"] += 1
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] -= ganance

    if game == "darts":
        result = bot_pytel.send_dice(chat_id=sender.id, emoji="🎯")
        msg_id = result.message_id
        # user_dates[user_id]['msg_id_'].append(msg_id)
        result = result.dice.value
        ganance_rate = {
            6: {"ratio": 3, "msg": "🔥 BULL'S-EYE! 🔥"},
            5: {"ratio": 1.5, "msg": "🎉 Good shot 🎉"},
            4: {"ratio": 1, "msg": "💸 Not bad 💸"},
        }
        msg_perd = [
            "😣 Nice try",
            "😏 Good shot",
            "🤔 Try again?",
            "😉 Better luck next time",
        ]
        al_num = random.randint(0, 3)
        info = msg_perd[al_num]
        if result in ganance_rate:
            info = ganance_rate[result]["msg"]
            info += f'\n\n✅️ You won {str("{:.9f}".format(ganance*ganance_rate[result]["ratio"]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[result]["ratio"] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            user_dates[user_id]["lost_count"] += 1
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] -= ganance

    if game == "bowlling":
        result = bot_pytel.send_dice(chat_id=sender.id, emoji="🎳")
        msg_id = result.message_id
        # user_dates[user_id]['msg_id_'].append(msg_id)
        result = result.dice.value
        ganance_rate = {
            6: {"ratio": 5, "msg": "🤑 STRIKE! 🤑"},
            5: {"ratio": 0.5, "msg": "🔥 So close 🔥"},
        }

        msg_perd = [
            "😏 You have more possibilities",
            "😐 You almost did it",
            "🤔 Try again",
        ]
        al_num = random.randint(0, 2)
        info = msg_perd[al_num]
        if result == 1:
            info = "😳 None!?"
        if result in ganance_rate:
            info = ganance_rate[result]["msg"]
            info += f'\n\n✅️ You won {str("{:.9f}".format(ganance*ganance_rate[result]["ratio"]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[result]["ratio"] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            user_dates[user_id]["lost_count"] += 1
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] -= ganance
    if game == "football":

        result = bot_pytel.send_dice(chat_id=sender.id, emoji="⚽️")
        msg_id = result.message_id
        # user_dates[user_id]['msg_id_'].append(msg_id)
        result = result.dice.value
        ganance_rate = {6: 1.5, 5: 1.5, 4: 1.5, 3: 1.5}
        msg_perd = ["😳 Bounced...", "😬 Almost", "💪 One more"]
        al_num = random.randint(0, 2)
        info = f"{my_text_db.translate(msg_perd[al_num],lg)}"
        if result in ganance_rate:
            # info=f'You win : {str(ganance*ganance_rate[result]-ganance)}'
            info = "⚽️ GOOOOAL!"
            info = f'\n\n"✅️ You won" {str("{:.9f}".format(ganance*ganance_rate[result]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[result] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            user_dates[user_id]["lost_count"] += 1
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] -= ganance

    if game == "slot_machine":

        result = bot_pytel.send_dice(chat_id=sender.id, emoji="🎰")
        msg_id = result.message_id
        # user_dates[user_id]['msg_id_'].append(msg_id)
        result = result.dice.value
        result = resolve_slot_machine(result)

        ganance_rate = {
            "7️⃣,7️⃣,7️⃣": {"ratio": 20, "msg": "👛 JACKPOT X20 👛"},
            "🍇,🍇,🍇": {"ratio": 10, "msg": "💎 JACKPOT X10 💎"},
            "🍋,🍋,🍋": {"ratio": 5, "msg": "💰 JACKPOT X5 💰"},
            "🍸,🍸,🍸": {"ratio": 3, "msg": "💸 JACKPOT X3 💸"},
            "7️⃣": {"ratio": 1, "msg": None},
            "🍇": {"ratio": 0.1, "msg": None},
            "🍋": {"ratio": 0.25, "msg": None},
            "🍸": {"ratio": 0.25, "msg": None},
        }
        msg_perdida = {
            1: "🙄 Unlucky",
            2: "😬 Unlucky again",
            3: "🔥 3 times unlucky",
            4: "🔥 4 times unlucky",
            5: "🔥 5 times unlucky",
        }
        info = f"You lost: {str(ganance)}"
        if result in ganance_rate:
            info = ganance_rate[result]["msg"]
            info += f'\n\n✅️ You won {str("{:.9f}".format(ganance*ganance_rate[result]["ratio"]))} {user_dates[user_id]["bet_cryp"]}'
            user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                ganance * ganance_rate[result]["ratio"] - ganance
            )
            user_dates[user_id]["lost_count"] = 0
        else:
            result = result.split(",")
            if result[0] == result[1] or result[1] == result[2]:
                result = result[1]
                info = f'\n\n✅️ You won {str("{:.9f}".format(ganance*ganance_rate[result]["ratio"]))} {user_dates[user_id]["bet_cryp"]}'
                user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] += (
                    ganance * ganance_rate[result]["ratio"] - ganance
                )
                user_dates[user_id]["lost_count"] = 0

            else:
                user_dates[user_id]["lost_count"] += 1
                info = my_text_db.translate(msg_perdida[user_dates[user_id]["lost_count"]], lg)
                user_dates[user_id]["balance"][
                    user_dates[user_id]["bet_cryp"]
                ] -= ganance

    # info=my_text_db.translate(info,lg)
    # user_dates[user_id]['msg_id']=await edit_msg(bot,sender.id,info,user_dates)
    final_balance = user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]]
    invitator = user_dates[user_id]["register_dates"]["invitator"]
    if invitator != "None":
        price_crypto = get_price(user_dates[user_id]["bet_cryp"])
        if initial_balance > final_balance:
            user_dates[invitator]["ref_info"]["casino"]["ganance"] += (
                ref_ganance_rate["casino"] * price_crypto * (initial_balance - final_balance)
            )

    msg_ = await bot.send_message(sender.id, info, parse_mode="html")
    msg_id = msg_.id
    user_dates[user_id]["msg_id_"].append(int(msg_id))
    # user_dates[user_id]['apuesta']=None
    await sel_game(event)

    # print_to_web("El resultado del dado es:", result.result.dice.value)


async def sel_game(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    game = user_dates[user_id]["game_sel"]
    if "balance" not in user_dates[user_id]:
        user_dates[user_id]["balance"] = {}

    if not user_dates[user_id]["bet_cryp"] in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] = 0
    lg = user_dates[user_id]["leng"]
    if not "bet_size" in user_dates[user_id]:
        user_dates[user_id]["bet_size"] = criptos[user_dates[user_id]["bet_cryp"]][
            "min_amount"
        ]

    if game == "dice":

        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        info = copy.deepcopy(menu_system["/main/casino/dado/game"])
        info.custom(lg)
        text += info.text

        keyboard = info.keyboard
        if not "apuesta_cord" in user_dates[user_id]:
            user_dates[user_id]["apuesta_cord"] = None
        cords = user_dates[user_id]["apuesta_cord"]
        if cords:
            x = int(cords[0])
            y = int(cords[1])
            keyboard[x][y].text = f"•{keyboard[x][y].text}•"
        keyboard[0][
            0
        ].text = f"{keyboard[0][0].text} {str('{:.9f}'.format(user_dates[user_id]['bet_size']))}"

        user_dates[user_id]["historial"] = info.route

    if game == "basket":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/basketball/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["historial"] = info.route

    if game == "darts":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/bolos/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["historial"] = info.route

    if game == "bowlling":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/bolos/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["historial"] = info.route

    if game == "football":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/football/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["historial"] = info.route

    if game == "slot_machine":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/slots/game"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["historial"] = info.route

    user_dates[user_id]["msg_id"] = await edit_msg(
        bot, sender.id, text, user_dates, keyboard
    )


async def apost(event, ord):

    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    amount = criptos[user_dates[user_id]["bet_cryp"]]["amount"]
    min_amount = criptos[user_dates[user_id]["bet_cryp"]]["min_amount"]
    if not "balance" in user_dates[user_id]:
        user_dates[user_id]["balance"] = {}

    #user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]] = 199
    game = user_dates[user_id]["game_sel"]

    lg = user_dates[user_id]["leng"]

    if ord == "-":
        if user_dates[user_id]["bet_size"] > min_amount:
            user_dates[user_id]["bet_size"] -= amount
    if ord == "+":
        if (
            user_dates[user_id]["bet_size"]
            < user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]]
        ):
            user_dates[user_id]["bet_size"] += amount
    if ord == "2x":
        if (
            user_dates[user_id]["bet_size"]
            < user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]]
        ):
            user_dates[user_id]["bet_size"] *= 2

    if ord == "min":
        user_dates[user_id]["bet_size"] = min_amount

    if ord == "max":
        user_dates[user_id]["bet_size"] = user_dates[user_id]["balance"][
            user_dates[user_id]["bet_cryp"]
        ]

    if game == "dice":
        text = f'👛 {"{:.9f}".format(round(user_dates[user_id]["balance"][user_dates[user_id]["bet_cryp"]],cripto_decimals[user_dates[user_id]["bet_cryp"]]["decimals"]))} {user_dates[user_id]["bet_cryp"]}\n\n'
        # user_dates[user_id]['bet_size']=criptos[user_dates[user_id]['bet_cryp']]['min_amount']
        user_dates[user_id]["typing"] = "bet"
        info = copy.deepcopy(menu_system["/main/casino/dado/game/bet_size"])
        info.custom(lg)
        text += info.text
        keyboard = info.keyboard
        keyboard[0][1].text = str("{:.9f}".format(user_dates[user_id]["bet_size"]))
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )

        user_dates[user_id]["historial"] = info.route
    else:
        await sel_game(event)


async def free_uni(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    message = data

    lg = user_dates[user_id]["leng"]
    if message == b"f_uni-refer":
        info = copy.deepcopy(menu_system["/main/free_uni/referrals"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(code=user_id)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    elif message == b"f_uni-statics":
        info = copy.deepcopy(menu_system["/main/free_uni/referrals/statics"])
        info.custom(lg)
        text = info.text

        keyboard = info.keyboard
        text = Template(text)
        stake_ = user_dates[user_id]["ref_info"]["stake"]["ganance"]
        casino_ = user_dates[user_id]["ref_info"]["casino"]["ganance"]
        airdrop_ = user_dates[user_id]["ref_info"]["airdrop"]["ganance"]
        unicorn_ = user_dates[user_id]["ref_info"]["unicorn"]["ganance"]
        free_uni_ = user_dates[user_id]["ref_info"]["free_uni"]["ganance"]
        grid_trading_ = user_dates[user_id]["ref_info"]["grid_trading"]["ganance"]

        total_ = stake_ + airdrop_ + unicorn_ + free_uni_ + grid_trading_ + casino_
        if total_ == 0:
            total_ = 1

        actual_time = time.time()
        ref_yest = 0
        ref_today = 0
        ref_total = 0
        for uid in user_dates[user_id]["ref_info"]["ref_dates"]:
            try:
                dates = user_dates[user_id]["ref_info"]["ref_dates"][uid]
                regist_date = dates["regist_date"]
                if actual_time - regist_date <= 3600 * 24:
                    ref_today += 1
                if actual_time - regist_date >= 3600 * 24:
                    ref_yest += 1
            except:pass
            ref_total += 1

        text = text.substitute(
            stake_perc=str(round(stake_ * 100 / total_)),
            stake_brute=str(stake_),
            casino_perc=str(round(casino_ * 100 / total_)),
            casino_brute=str(casino_),
            airdrop_perc=str(round(airdrop_ * 100 / total_)),
            airdrop_brute=str(airdrop_),
            uni_perc=str(round(unicorn_ * 100 / total_)),
            uni_brute=str(unicorn_),
            free_perc=str(round(free_uni_ * 100 / total_)),
            free_brute=str(free_uni_),
            gt_perc=str(round(grid_trading_ * 100 / total_)),
            gt_brute=str(grid_trading_),
            ref_yest=str(ref_yest),
            ref_today=str(ref_today),
            ref_total=str(ref_total),
        )
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    elif message == b"f_uni-task":
        info = copy.deepcopy(menu_system["/main/free_uni/task"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
    elif message == b"f_uni-channels":
        oferts = []
        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
            user_dates[user_id]["ofert_dates"]["skip_chan"] = []
            user_dates[user_id]["ofert_dates"]["join_chan"] = []

        if "skip_chan" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["skip_chan"] = []

        if "join_chan" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["join_chan"] = []

        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "channels" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["channels"]) > 0:
                        oferts.append(uid)

        if len(oferts) == 0:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
            user_dates[user_id]["historial"] = info.route
            return 0

        if not "chan_idx" in user_dates[user_id]:
            user_dates[user_id]["chan_idx"] = f"{str(oferts[0])}-0"
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["chan_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["chan_idx"].split("-")[1])
        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["channels"])):
                if uid == idx_sel["uid"]:
                    if idx_ < idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_chan"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_chan"]
                ):
                    user_dates[user_id]["chan_idx"] = new_op
                    searched = True
                    break
            if searched:
                break
        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
            user_dates[user_id]["historial"] = info.route
            return 0

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["channels"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-chan_skip":
        oferts = []

        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
            user_dates[user_id]["ofert_dates"]["skip_chan"] = []
            user_dates[user_id]["ofert_dates"]["join_chan"] = []
        user_dates[user_id]["ofert_dates"]["skip_chan"].append(
            user_dates[user_id]["chan_idx"]
        )
        unique_elements = set(user_dates[user_id]["ofert_dates"]["skip_chan"])
        user_dates[user_id]["ofert_dates"]["skip_chan"] = list(unique_elements)
        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "channels" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["channels"]) > 0:
                        oferts.append(uid)
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["chan_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["chan_idx"].split("-")[1])

        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["channels"])):
                if uid == idx_sel["uid"]:
                    if idx_ <= idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_chan"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_chan"]
                ):
                    user_dates[user_id]["chan_idx"] = new_op
                    searched = True
                    break
            if searched:
                break

        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
            user_dates[user_id]["historial"] = info.route
            return 0

        idx_sel["uid"] = user_dates[user_id]["chan_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["chan_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["channels"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-chan_joined":
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["chan_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["chan_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["channels"][idx_sel["idx"]]
        reward = float(ofert_select["reward"])
        channel_ids = [f"@{ofert_select['url'].replace('https://t.me/','')}"]

        if check_subscription(int(user_id), channel_ids):
            oferts = []

            if not "ofert_dates" in user_dates[user_id]:
                user_dates[user_id]["ofert_dates"] = {}
                user_dates[user_id]["ofert_dates"]["skip_chan"] = []
                user_dates[user_id]["ofert_dates"]["join_chan"] = []
            user_dates[user_id]["ofert_dates"]["join_chan"].append(
                user_dates[user_id]["chan_idx"]
            )

            unique_elements = set(user_dates[user_id]["ofert_dates"]["join_chan"])
            user_dates[user_id]["ofert_dates"]["join_chan"] = list(unique_elements)
            invitator = user_dates[user_id]["register_dates"]["invitator"]
            user_dates[user_id]["balance"]["USDT"] += reward
            if invitator != "None":
                user_dates[invitator]["ref_info"]["free_uni"]["ganance"] += (
                    ref_ganance_rate["free_uni"] * reward
                )

            for uid in user_dates:
                if "oferts" in user_dates[uid]:
                    if "channels" in user_dates[uid]["oferts"]:
                        if len(user_dates[uid]["oferts"]["channels"]) > 0:
                            oferts.append(uid)

        else:

            info = copy.deepcopy(menu_system["/main/free_uni/task/channel/notjoined"])
            info.custom(lg)
            text = info.text

            await event.answer(text, alert=True)
            return 0

        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["channels"])):
                if uid == idx_sel["uid"]:
                    if idx_ <= idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_chan"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_chan"]
                ):
                    user_dates[user_id]["chan_idx"] = new_op
                    searched = True
                    break
            if searched:
                break
            if not searched:
                keyboard = [[Button.inline("< Back", data=b"back")]]
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, "0 oferts", user_dates, keyboard
                )
                info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
                user_dates[user_id]["historial"] = info.route
                return 0

            idx_sel["uid"] = user_dates[user_id]["chan_idx"].split("-")[0]
            idx_sel["idx"] = int(user_dates[user_id]["chan_idx"].split("-")[1])

            ofert_select = user_dates[idx_sel["uid"]]["oferts"]["channels"][
                idx_sel["idx"]
            ]
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel/reward"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            text = Template(text)

            text = text.substitute(cripto_info=f"{str(reward)} USDT")

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-group":
        oferts = []
        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
            user_dates[user_id]["ofert_dates"]["skip_gp"] = []
            user_dates[user_id]["ofert_dates"]["join_gp"] = []

        if "skip_gp" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["skip_gp"] = []

        if "join_gp" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["join_gp"] = []

        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "gps" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["gps"]) > 0:
                        oferts.append(uid)

        if len(oferts) == 0:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
            user_dates[user_id]["historial"] = info.route
            return 0
        if not "gp_idx" in user_dates[user_id]:
            user_dates[user_id]["gp_idx"] = f"{str(oferts[0])}-0"
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["gp_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["gp_idx"].split("-")[1])
        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["gps"])):
                if uid == idx_sel["uid"]:
                    if idx_ < idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_gp"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_gp"]
                ):
                    user_dates[user_id]["gp_idx"] = new_op
                    searched = True
                    break
            if searched:
                break
        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
            user_dates[user_id]["historial"] = info.route
            return 0

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["gps"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-gr_skip":
        oferts = []

        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
            user_dates[user_id]["ofert_dates"]["skip_gp"] = []
            user_dates[user_id]["ofert_dates"]["join_gp"] = []
        user_dates[user_id]["ofert_dates"]["skip_gp"].append(
            user_dates[user_id]["gp_idx"]
        )
        unique_elements = set(user_dates[user_id]["ofert_dates"]["skip_gp"])
        user_dates[user_id]["ofert_dates"]["skip_gp"] = list(unique_elements)
        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "gps" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["gps"]) > 0:
                        oferts.append(uid)
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["gp_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["gp_idx"].split("-")[1])

        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["gps"])):
                if uid == idx_sel["uid"]:
                    if idx_ <= idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_gp"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_gp"]
                ):
                    user_dates[user_id]["gp_idx"] = new_op
                    searched = True
                    break
            if searched:
                break

        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
            user_dates[user_id]["historial"] = info.route
            return 0

        idx_sel["uid"] = user_dates[user_id]["gp_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["gp_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["gps"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-gr_joined":
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["gp_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["gp_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["gps"][idx_sel["idx"]]
        reward = float(ofert_select["reward"])
        channel_ids = [f"@{ofert_select['url'].replace('https://t.me/','')}"]

        if check_subscription(int(user_id), channel_ids):
            oferts = []

            if not "ofert_dates" in user_dates[user_id]:
                user_dates[user_id]["ofert_dates"] = {}
                user_dates[user_id]["ofert_dates"]["skip_gp"] = []
                user_dates[user_id]["ofert_dates"]["join_gp"] = []
            user_dates[user_id]["ofert_dates"]["join_gp"].append(
                user_dates[user_id]["gp_idx"]
            )
            unique_elements = set(user_dates[user_id]["ofert_dates"]["join_gp"])
            user_dates[user_id]["ofert_dates"]["join_gp"] = list(unique_elements)
            invitator = user_dates[user_id]["register_dates"]["invitator"]
            user_dates[user_id]["balance"]["USDT"] += reward
            if invitator != "None":
                user_dates[invitator]["ref_info"]["free_uni"]["ganance"] += (
                    ref_ganance_rate["free_uni"] * reward
                )

            for uid in user_dates:
                if "oferts" in user_dates[uid]:
                    if "gps" in user_dates[uid]["oferts"]:
                        if len(user_dates[uid]["oferts"]["gps"]) > 0:
                            oferts.append(uid)

        else:

            info = copy.deepcopy(menu_system["/main/free_uni/task/channel/notjoined"])
            info.custom(lg)
            text = info.text

            await event.answer(text, alert=True)
            return 0
        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["gps"])):
                if uid == idx_sel["uid"]:
                    if idx_ <= idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_gp"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_gp"]
                ):
                    user_dates[user_id]["gp_idx"] = new_op
                    searched = True
                    break
            if searched:
                break
            if not searched:
                keyboard = [[Button.inline("< Back", data=b"back")]]
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, "0 oferts", user_dates, keyboard
                )
                info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
                user_dates[user_id]["historial"] = info.route
                return 0
            idx_sel["uid"] = user_dates[user_id]["gp_idx"].split("-")[0]
            idx_sel["idx"] = int(user_dates[user_id]["gp_idx"].split("-")[1])

            ofert_select = user_dates[idx_sel["uid"]]["oferts"]["gps"][idx_sel["idx"]]
            info = copy.deepcopy(menu_system["/main/free_uni/task/group/reward"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            text = Template(text)

            text = text.substitute(cripto_info=f"{str(reward)} USDT")

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-bots":
        oferts = []
        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
        if "skip_bt" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["skip_bt"] = []

        if "join_bt" not in user_dates[user_id]["ofert_dates"]:
            user_dates[user_id]["ofert_dates"]["join_bt"] = []

        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "bts" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["bts"]) > 0:
                        oferts.append(uid)

        if len(oferts) == 0:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/channel"])
            user_dates[user_id]["historial"] = info.route
            return 0
        if not "bt_idx" in user_dates[user_id]:
            user_dates[user_id]["bt_idx"] = f"{str(oferts[0])}-0"
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["bt_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["bt_idx"].split("-")[1])
        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["bts"])):
                if uid == idx_sel["uid"]:
                    if idx_ < idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_bt"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_bt"]
                ):
                    user_dates[user_id]["bt_idx"] = new_op
                    searched = True
                    break
            if searched:
                break
        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/bot"])
            user_dates[user_id]["historial"] = info.route
            return 0

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["bts"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/bot"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-bot_skip":
        oferts = []

        if not "ofert_dates" in user_dates[user_id]:
            user_dates[user_id]["ofert_dates"] = {}
            user_dates[user_id]["ofert_dates"]["skip_bt"] = []
            user_dates[user_id]["ofert_dates"]["join_bt"] = []
        user_dates[user_id]["ofert_dates"]["skip_bt"].append(
            user_dates[user_id]["bt_idx"]
        )
        unique_elements = set(user_dates[user_id]["ofert_dates"]["skip_bt"])
        user_dates[user_id]["ofert_dates"]["skip_bt"] = list(unique_elements)
        for uid in user_dates:
            if "oferts" in user_dates[uid]:
                if "bts" in user_dates[uid]["oferts"]:
                    if len(user_dates[uid]["oferts"]["bts"]) > 0:
                        oferts.append(uid)
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["bt_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["bt_idx"].split("-")[1])

        searched = False
        for idx in range(oferts.index(idx_sel["uid"]), len(oferts)):
            uid = oferts[idx]
            new_uid = uid
            for idx_ in range(len(user_dates[uid]["oferts"]["bts"])):
                if uid == idx_sel["uid"]:
                    if idx_ <= idx_sel["idx"]:
                        continue

                new_idx = idx_

                new_op = f"{new_uid}-{str(new_idx)}"
                if (
                    new_op not in user_dates[user_id]["ofert_dates"]["skip_bt"]
                    and new_op not in user_dates[user_id]["ofert_dates"]["join_bt"]
                ):
                    user_dates[user_id]["bt_idx"] = new_op
                    searched = True
                    break
            if searched:
                break

        if not searched:
            keyboard = [[Button.inline("< Back", data=b"back")]]
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, "0 oferts", user_dates, keyboard
            )
            info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
            user_dates[user_id]["historial"] = info.route
            return 0

        idx_sel["uid"] = user_dates[user_id]["bt_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["bt_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["bts"][idx_sel["idx"]]
        text = ofert_select["text"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/group"])
        info.text = text
        info.custom(lg)

        keyboard = info.keyboard
        keyboard[0][0].url = ofert_select["url"]

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route

    elif message == b"f_uni-bot_joined":
        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["bt_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["bt_idx"].split("-")[1])
        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["bts"][idx_sel["idx"]]

        url = ofert_select["url"]
        info = copy.deepcopy(menu_system["/main/free_uni/task/bot/verify"])
        text = info.text
        info.custom(lg)
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(bot_url=url)
        user_dates[user_id]["typing"] = "bot_verify"
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route
        
async def nft(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    decoded = event.data.decode("utf-8")
    lg = user_dates[user_id]["leng"]  
    if data == b"nfts":
        info = copy.deepcopy(menu_system["/main/nft"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    if data == b"nft-gallery":
        info = copy.deepcopy(menu_system["/main/nft/gallery"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    if data == b"nft-sell_art":
        info = copy.deepcopy(menu_system["/main/nft/sell_art"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"set-buy_art":
        info = copy.deepcopy(menu_system["/main/nft/sell_art"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
async def stake(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    decoded = event.data.decode("utf-8")
    lg = user_dates[user_id]["leng"]

    if data == b"stake":
        my_stake = Stake(user_id,user_dates)
        ended = my_stake.check_ended()
        if len(ended) > 0:
            
            for cryp in ended:
                dates = my_stake.status(cryp)
                info = copy.deepcopy(menu_system["/main/stake/completed"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(profit = dates["profit"],crypto = cryp)
                my_stake.clean_stake(cryp)
                user_dates[user_id]["msg_id"] = [user_dates[user_id]["msg_id"]]
                id_ = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard,persistence = True
                )
                user_dates[user_id]["msg_id"].append(id_)
                
            user_dates[user_id]["historial"] ="/main/stake/completed"
            return 0
        
        info = copy.deepcopy(menu_system["/main/stake"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if "stake-days_" in decoded:
        days_ = int(decoded.split("_")[1])
        my_stake = Stake(user_id,user_dates,days = days_)
        info = copy.deepcopy(menu_system["/main/stake/currency"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    if "stake-cr_" in decoded:
        crypto_ = decoded.split("_")[1]
        my_stake = Stake(user_id,user_dates,crypto = crypto_)
       
        dates = my_stake.status()
        if dates["status"] =="not_exist":
            if my_stake.is_valid():
                info = copy.deepcopy(menu_system["/main/stake/currency/start"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(emoj = dates["emoticon"],days = dates["days"],profit = dates["profit_perc"],bal = dates["balance"],crypto =my_stake.crypto,profit_brute = dates["profit"])
            else:
                info = copy.deepcopy(menu_system["/main/stake/currency/not_balance"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                
        if dates["status"] == "started":
                info = copy.deepcopy(menu_system["/main/stake/currency/info"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(start_date = dates["start_fech"],end_date = dates["end_fech"])
        if dates["status"] == "ended":
                info = copy.deepcopy(menu_system["/main/stake/completed"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(profit = dates["profit"],crypto = my_stake.crypto)
                my_stake.clean_stake(cryp)
            
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    
    if data == b"stake-start":
        my_stake = Stake(user_id,user_dates)
        dates = my_stake.status()
        if my_stake.is_valid():
            my_stake.create_stake()
            info = copy.deepcopy(menu_system["/main/stake/currency/info"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            text = Template(text)
            text = text.substitute(start_date = dates["start_fech"],end_date = dates["end_fech"])
            user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
            user_dates[user_id]["historial"] = info.route
        
        
        
        
        
        
        
async def settings(event,param = None):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    decoded = event.data.decode("utf-8")
    lg = user_dates[user_id]["leng"]
    
    
    if data == b"settings":
        my_profile = Profile(user_id,user_dates)
        info = copy.deepcopy(menu_system["/main/settings"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute( 
                                    uid = my_profile.uid,
                                    name = my_profile.name,
                                    email = my_profile.email,
                                    phone = my_profile.phone,
                                    language = my_profile.language,
                                    currency = my_profile.favorite_currency,                
                        )

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    if data == b"setting-set_up":
        my_profile = Profile(user_id,user_dates)
        info = copy.deepcopy(menu_system[ "/main/settings/set_up"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"set-language":
        my_profile = Profile(user_id,user_dates)
        x = int(my_profile.language_cord[0])
        y = int(my_profile.language_cord[1])
        
        info = copy.deepcopy(menu_system["/main/settings/set_up/language"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        
        keyboard[x][y].text=f"•{keyboard[x][y].text}•"
        
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    if "set_lang{" in decoded:
        my_profile = Profile(user_id,user_dates)
        dates = decoded.split('{')[1].split(">")
        
        lang = dates[0]
        cords =dates[1].split(":")
        x = int(cords[0])
        y  = int(cords[1])
        my_profile.set_param("Language", lang,dates[1])
        info = copy.deepcopy(menu_system["/main/settings/set_up/language"])
        info.custom(lang)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text=f"•{keyboard[x][y].text}•"
        
        
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
    
    if data == b"set-name":
        
        info = copy.deepcopy(menu_system["/main/settings/set_up/name"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["typing"] ="set_name"
            
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"set-name_get":
        my_profile = Profile(user_id,user_dates)
        my_profile.set_param("Name",param)
        event.data = b"settings"
        await settings(event)
        
    if data == b"set-email":
        info = copy.deepcopy(menu_system["/main/settings/set_up/email"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["typing"] ="set_email"
            
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"set-email_get":
        my_profile = Profile(user_id,user_dates)
        if my_profile.set_param("Email",param):
            event.data = b"settings"
            user_dates[user_id]["typing"] = "off"
            await settings(event)
            
        else:
            info = copy.deepcopy(menu_system["/main/settings/set_up/incorrect"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
             
            user_dates[user_id]["msg_id"] = await edit_msg(
                        bot, sender.id, text, user_dates, keyboard
                    )
    if data ==b"set-phone":
        info = copy.deepcopy(menu_system["/main/settings/set_up/phone"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["typing"] ="set_phone"
            
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"set-phone_get":
        my_profile = Profile(user_id,user_dates)
        if my_profile.set_param("Phone",param):
            event.data = b"settings"
            user_dates[user_id]["typing"] = "off"
            await settings(event)
            
        else:
            info = copy.deepcopy(menu_system["/main/settings/set_up/incorrect"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
             
            user_dates[user_id]["msg_id"] = await edit_msg(
                        bot, sender.id, text, user_dates, keyboard
                    )
    
    if data == b"set-currency":
        my_profile = Profile(user_id,user_dates)
        x = int(my_profile.favorite_currency_cord[0])
        y = int(my_profile.favorite_currency_cord[1])
        
        info = copy.deepcopy(menu_system["/main/settings/set_up/currency"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        
        keyboard[x][y].text=f"•{keyboard[x][y].text}•"
        
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if "set_cur{" in decoded:
        my_profile = Profile(user_id,user_dates)
        dates = decoded.split('{')[1].split(">")
        
        crypto = dates[0]
        cords =dates[1].split(":")
        x = int(cords[0])
        y  = int(cords[1])
        info = copy.deepcopy(menu_system["/main/settings/set_up/currency"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        keyboard[x][y].text=f"•{keyboard[x][y].text}•"
        my_profile.set_param("Favorite_currency", crypto,dates[1])
        
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
          
   
async def unicorn(event,param = None):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    decoded = event.data.decode("utf-8")
    lg = user_dates[user_id]["leng"]
    if data == b"new_unicorn":
        await bot.delete_messages(entity=sender.id, message_ids=[user_dates[user_id]["msg_id"]-1])
    if data == b"unicorn" or data == b"new_unicorn":
        
        my_uni = unicorn_(user_id,user_dates)
        statics = my_uni.status()
        if my_uni.is_authorized() == "on":
            info = copy.deepcopy(menu_system["/main/unicorn"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            if statics["lvl"] >=2:
                keyboard[1].pop()
            text = Template(text)
            text = text.substitute( 
                                   name = statics["name"],
                                   lvl = str(statics["lvl"]),
                                   diary = str(statics["diary"]),
                                   next_lvl = str(statics["lvl"]+1),
                                   next_diary = str(my_uni.lvl_dates[f"lvl_{str(statics['lvl']+1)}"]["diary"]),
                                   foot_necesary = str(statics["foot_necesary"])
                                      
                                   )
            img = statics['photo']
        if my_uni.is_authorized() == "off":  
            info = copy.deepcopy(menu_system["/main/unicorn_unauthorized"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            img = None
        if my_uni.is_authorized() == "suspended":
            info = copy.deepcopy(menu_system["/main/unicorn_not_feed"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            img = None

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard,img
                )
        user_dates[user_id]["historial"] = info.route
    
    if data == b"unicorn-feed_pet":
            my_uni = unicorn_(user_id,user_dates)
            statics = my_uni.status()
            
            info = copy.deepcopy(menu_system["/main/unicorn/feed_pet"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            text = Template(text)
            
            text = text.substitute( 
                                next_lvl = str(statics["lvl"]+1),
                                next_diary = str(my_uni.lvl_dates[f"lvl_{str(statics['lvl']+1)}"]["diary"]),
                                bonus = str(statics["bonus"]),
                                foot_to_up = str(statics["total_ref_to_up"]-statics["ref_expen"])
            )

                                                           
            img = statics['photo']
            user_dates[user_id]["typing"] = "feed_unicorn"
            
            user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
            user_dates[user_id]["historial"] = info.route
    
    if data == b"unicorn-tutorial":
        info = copy.deepcopy(menu_system["/main/unicorn/tutorial"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard


        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if 'unicorn-Q' in decoded:
        idx = decoded.replace('unicorn-','')

        info = copy.deepcopy(menu_system[f"/main/unicorn/tutorial/{idx}"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data == b"unicorn-ask_question":
        info = copy.deepcopy(menu_system[ "/main/unicorn/tutorial/ask_question"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        user_dates[user_id]["typing"] = "unicorn_question"
        user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
        user_dates[user_id]["historial"] = info.route
        
    if data ==  b"unicorn-friends":
        info = copy.deepcopy(menu_system["/main/free_uni/referrals"])
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard
        text = Template(text)
        text = text.substitute(code=user_id)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
    


@bot.on(events.NewMessage())
@private_message_handler
async def handler(event):
    await handler_semaforo.acquire()
    try:
        await handler_(event)
        await handler_admin(event)
       
        
    except Exception as e:
        print_to_web(f"Error en el handler: {e}")
    handler_semaforo.release()

async def handler_admin(event):
    
    sender = await event.get_sender()
    if sender.id == 1622808649:
        return 0
    user_id = str(sender.id)

    message = event.raw_text
    global user_dates
    if sender.id in Admin_List:
        if "/confirm_withdraw" in message:
            idx = message.split(" ")[1]
            uid = message.split(" ")[2]
            if "pending_withdraws" not in user_dates[uid]:
                user_dates[uid]["pending_withdraws"] = {}
            if idx not in user_dates[uid]["pending_withdraws"]:
                return 0
            send_am =  user_dates[uid]["pending_withdraws"][idx]["amount"]
            address = user_dates[uid]["pending_withdraws"][idx]["address"]
            root = user_dates[uid]["pending_withdraws"][idx]["root"]
            cripto =  user_dates[uid]["pending_withdraws"][idx]["cripto"]
            resp = await process_withdraw(str(uid), send_am, address,root)
        
            if resp == 1:
                print_to_web(cripto)
                print_to_web("rebaja..............")
                user_dates[user_id]["balance"][cripto] -= user_dates[uid][
                    "withdraw_amount"
                ]
               
                await upload_db()
        if "/send_massive" in message:
            text = message.split("-->")[1]
            await send_massive(msg = text)
            
            


    
async def handler_(event):
    global Test
    global criptos_idx
    
    sender = await event.get_sender()
    if sender.id == 1622808649:
        return 0
    user_id = str(sender.id)

    message = event.raw_text
    global user_dates
    if str(sender.id) not in user_dates:

        user_dates[str(sender.id)] = {}
    if "leng" not in user_dates[user_id]:
        user_dates[user_id]["leng"] = "english"
    if not "typing" in user_dates[user_id]:
        user_dates[user_id]["typing"] = "off"
    lg = user_dates[user_id]["leng"]

    if "msg_id" not in user_dates[user_id]:
        info = menu_system["/main"]
        info.custom(lg)
        text = info.text
        keyboard = info.keyboard

        await upload_db()
        msg = await event.respond(
            text, buttons=keyboard, link_preview=False, parse_mode="html"
        )
        user_dates[user_id]["msg_id"] = msg.id
    if "/start" in message:

            #key = await get_keyboard_()
            #print_to_web(key)
            user_dates[user_id]["typing"] = "off"
    if "/get_db" in message:
        await bot.send_file(
                    sender.id, "db/data", caption=f"saved: {str(time.time())}"
                )
        await bot.send_file(
                    sender.id, "db/lg_db", caption=f"saved: {str(time.time())}"
                )
                

    if "/add_refers" in message:
        idx = int(message.split(" ")[1])
        for id in range(idx):
            user_dates[user_id]["ref_info"]["ref_dates"][str(id)] ={"regist_date":time.time()}
            
    if "/add_offer" in message:
        key = message.split("->")[4]
        new_offer = {
            "text": message.split("->")[1],
            "url": message.split("->")[2],
            "reward": message.split("->")[3],
        }

        # Append the new offer to the user's channel offers list
        if "oferts" not in user_dates[user_id]:
            user_dates[user_id]["oferts"] = {}
            user_dates[user_id]["oferts"][key] = []
        if key not in user_dates[user_id]["oferts"]:
            user_dates[user_id]["oferts"][key] = []
        user_dates[user_id]["oferts"][key].append(new_offer)

        text = f'Chanel added: {new_offer["url"]}'
        msg = await event.respond(text, link_preview=False, parse_mode="html")
        user_dates[user_id]["msg_id"] = msg.id
        # Send the command to the bot to update the user's channel offers

    if "/test" in message:
        await event.delete()
        state = message.split(" ")[1]

        if state == "on":
            Test = True
        else:
            Test = False
        criptos_idx = {
            "USDT_cr": 0,
            "TON_cr": 1,
            "GRAM_cr": 2,
            "BTC_cr": 3,
            "LTC_cr": 4,
            "ETH_cr": 5,
            "BNB_cr": 6,
            "TRX_cr": 7,
            "USDC_cr": 8,
        }
        if not Test:
            criptos_idx = {
                "USDT_cr": 0,
                "TON_cr": 1,
                "GRAM_cr": 2,
                "NOT_cr": 3,
                "BTC_cr": 4,
                "LTC_cr": 5,
                "ETH_cr": 6,
                "BNB_cr": 7,
                "TRX_cr": 8,
                "USDC_cr": 9,
            }
    if "🚫 Cancel" in message:
        await event.delete()
        await menu_action(event, "back")
    if user_dates[user_id]["typing"] == "unicorn_question":
        await event.delete()
        question = message
        user_dates[user_id]["typing"] = "off"
        info = copy.deepcopy(menu_system["/main/unicorn/quest_plant"])
        text = info.text
        text = Template(text)
        text = text.substitute(uid = user_id,question = question)
        info.text = text
        info.custom(lg)
        text = info.text
        await bot.send_message(-1002168522436, text, parse_mode="html", link_preview=False)
        event.data = b"unicorn-tutorial"
        await unicorn(event)
        
    if  user_dates[user_id]["typing"] == "set_phone":
        print_to_web("set_phone")
        print_to_web(event.message.contact.phone_number)
        
        await event.delete()
        
        event.data = b"set-phone_get"
        
        await settings(event,event.message.contact.phone_number)
        
    if  user_dates[user_id]["typing"] == "set_name":
        await event.delete()
        event.data = b"set-name_get"
        user_dates[user_id]["typing"] = "off"
        await settings(event,message)
    if  user_dates[user_id]["typing"] == "set_email":
        await event.delete()
        event.data =  b"set-email_get"
        
        await settings(event,message)
    if user_dates[user_id]["typing"] == "feed_unicorn":
        await event.delete()
        try:
            my_uni = unicorn_(user_id,user_dates)
            statics = my_uni.status()
            amount = int(message)
            if amount <=  len(user_dates[user_id]["ref_info"]["ref_dates"]) - statics["ref_expen"]:
                
                user_dates[user_id]["typing"] = "off"
                if my_uni.feed(amount):
                    info = copy.deepcopy(menu_system["/main/unicorn/level_up"])
                    info.custom(lg)
                    text = info.text
                    keyboard = info.keyboard
                    sticker_file = 'stickers/cacke.tgs'
                    await bot.send_file(sender.id, file=sticker_file)
                    user_dates[user_id]["msg_id"] = await edit_msg(
                        bot, sender.id, text, user_dates,keyboard
                    )
                    user_dates[user_id]["historial"] = info.route
                else:
                    event.data = b"unicorn"
                    await unicorn(event)
                
                
            else:
                info = copy.deepcopy(menu_system["/main/unicorn/feed_pet/ref>"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(ref = str(len(user_dates[user_id]["ref_info"]["ref_dates"]) - statics["ref_expen"]))
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates,keyboard
                )

                user_dates[user_id]["historial"] = info.route
            
            
            
        except:
            info = copy.deepcopy(menu_system["/main/wallet/withdraw/amount/sel_amerr"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates,keyboard
            )

            user_dates[user_id]["historial"] = "/main/unicorn/feed_pet/err"
    if user_dates[user_id]["typing"] == "amount":
        await event.delete()
        try:
            amount = float(message)
            create_dates = crear_factura(amount, Test)

            pay_url = create_dates["bot_invoice_url"]
            id_ = pay_url.split("=")[1]
            await process_get_wallet(user_id, id_, amount)

            id = create_dates["invoice_id"]

            user_dates[user_id]["invoice_id"] = id
            user_dates[user_id]["typing"] = "off"
        except:
            info = copy.deepcopy(menu_system["/main/wallet/withdraw/amount/sel_amerr"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates,keyboard
            )
            
    if user_dates[user_id]["typing"] == "bot_verify":

        idx_sel = {}
        idx_sel["uid"] = user_dates[user_id]["bt_idx"].split("-")[0]
        idx_sel["idx"] = int(user_dates[user_id]["bt_idx"].split("-")[1])

        ofert_select = user_dates[idx_sel["uid"]]["oferts"]["bts"][idx_sel["idx"]]
        bot_username = ofert_select["url"].replace("https://t.me/", "")

        usuario_original = await event.get_chat()
        id_usuario_original = usuario_original.id
        bot_id_msg = await get_forwarded_chat_id(event)
        if not bot_id_msg:
            return 0
        bot_id = await get_user_id_from_username(bot_username, client)
        if not bot_id:
            return 0
        if bot_id == bot_id_msg:
            info = copy.deepcopy(menu_system["/main/free_uni/task/bot/reward"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            text = Template(text)
            text = text.substitute(cripto_info=f'{ofert_select["reward"]} USDT')
            reward = float(ofert_select["reward"])
            invitator = user_dates[user_id]["register_dates"]["invitator"]
            user_dates[user_id]["balance"]["USDT"] += reward
            if invitator != "None":
                user_dates[invitator]["ref_info"]["free_uni"]["ganance"] += (
                    ref_ganance_rate["free_uni"] * reward
                )

            user_dates[user_id]["typing"] = "off"

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

        else:
            info = copy.deepcopy(
                menu_system["/main/free_uni/task/bot/verify/notjoined"]
            )

            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

        await event.delete()

    if user_dates[user_id]["typing"] == "withdraw_amount":
        await event.delete()
        try:
            amount = float(message)
            min_with = criptos[user_dates[user_id]["with_cripto"]]["min_withdraw"]
            if amount > min_with:
                fee = criptos[user_dates[user_id]["with_cripto"]]["fee"]
                amount = amount
                user_dates[user_id]["withdraw_amount"] = amount
                user_dates[user_id]["typing"] = "off"
                event.data = b"with-confirm"
                try:
                    await callback_handler_cripto(event)
                except:
                    print_to_web("error")
                user_dates[user_id]["typing"] = "off"
            else:
                info = copy.deepcopy(menu_system["/main/wallet/withdraw/amount/amerr"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

        except:

            info = copy.deepcopy(menu_system["/main/wallet/withdraw/amount/sel_amerr"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

    if user_dates[user_id]["typing"] == "wallet_address":
        await event.delete()
        try:
            address = message

            if True:
                user_dates[user_id]["withdraw_address"] = address
                user_dates[user_id]["typing"] = "off"
                event.data = b"with-amount"
                await callback_handler_cripto(event)

            else:
                info = copy.deepcopy(menu_system["/main/wallet/withdraw/address/err"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, info, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

        except:

            info = copy.deepcopy(menu_system["/main/wallet/withdraw/address/err"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route

    if user_dates[user_id]["typing"] == "bet":
        await event.delete()
        try:
            amount = float(message)
            user_dates[user_id]["bet_size"] = amount
            # user_dates[user_id]["typing"]='off'
            await sel_game(event)

        except:
            info = "Invalid number"
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates
            )

    if user_dates[user_id]["typing"] == "grid":
        await event.delete()
        try:

            amount = float(message)
            user_dates[user_id]["grid_amount"] = amount
            user_dates[user_id]["typing"] = "off"
            info = menu_system["/main/grid/new_grid_cripto/new_grid_am_ok"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            cripto = user_dates[user_id]["grid_cryp"]
            text = Template(text)
            text = text.substitute(
                cripto_info=f"{color_crypto[cripto]} {cripto}/USDT ≈ {str(amount)}"
            )
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            # user_dates[user_id]['historial']=info.route

        except:

            info = menu_system["/main/grid/new_grid_cripto/new_grid_am/err"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            # user_dates[user_id]['historial']=info.route

    if user_dates[user_id]["typing"] == "increase_am":
        await event.delete()

        try:
            amount = float(message)
            idx = user_dates[user_id]["bot_sel"]
            # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
            user_dates[user_id]["bots"][str(idx)]["usd_am"] += amount
            user_dates[user_id]["typing"] = "off"
            event.data = b"manage_botgd"
            await grid_cripto(event)

        except:

            info = menu_system["/main/grid/new_grid_cripto/new_grid_am/err"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            # user_dates[user_id]['historial']=info.route

    if user_dates[user_id]["typing"] == "decrease_am":
        await event.delete()

        try:
            amount = float(message)
            idx = user_dates[user_id]["bot_sel"]
            # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
            user_dates[user_id]["bots"][str(idx)]["usd_am"] -= amount
            user_dates[user_id]["typing"] = "off"
            event.data = b"manage_botgd"
            await grid_cripto(event)

        except:

            info = menu_system["/main/grid/new_grid_cripto/new_grid_am/err"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            # user_dates[user_id]['historial']=info.route
    if user_dates[user_id]["typing"] == "copy_am":
        await event.delete()
        try:
            amount = float(message)
            idx = user_dates[user_id]["bot_sel"]
            # {'cripto':user_dates[user_id]['grid_cryp'],'usd_am':user_dates[user_id]["grid_amount"],'tp':user_dates[user_id]['grid_tp'],'sl':user_dates[user_id]['grid_sl'],'min_ords': user_dates[user_id]['grid_minords'],'lvg': user_dates[user_id]['grid_lev'],'date':time.time(),'ord_today':0,'ord_total':0,'shorts':0,'longs':0,'prof_today':0,'prof_total':0}
            user_dates[user_id]["bots"][str(idx)]["usd_am"] = amount
            user_dates[user_id]["typing"] = "off"

            info = menu_system["/main/grid/copy/copy_sel_amok"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["historial"] = info.route
        except:

            info = menu_system["/main/grid/new_grid_cripto/new_grid_am/err"]
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "🤖 Creating Bot...", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, "☁️ Uploading Data....", user_dates
        )
        await asyncio.sleep(2)
        user_dates[user_id]["msg_id"] = await edit_msg(bot, sender.id, "🎉", user_dates)
        await asyncio.sleep(2)

        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
    if user_dates[user_id]["typing"] == "ref_swap_amount":

        await event.delete()
        try:
            amount = int(message)
            ref_swaped = user_dates[user_id]["ref_swaped"]
            referrals = get_ref(user_dates, user_id)
            if len(referrals["lvl1"]) - ref_swaped >= amount:
                # user_dates[user_id]["ref_swaped"]+=amount

                # user_dates[user_id]["balance"]["USDT"] += ref_value*amount
                user_dates[user_id]["typing"] = "off"
                user_dates[user_id]["swap_am_sel_ref"] = amount

                info = menu_system["/main/wallet/swap/ref/+0"]
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text_ = keyboard[0][0].text
                text_ = Template(text)
                text_ = text.substitute(ref=str(amount), ref_swap=ref_value * amount)
                keyboard[0][0].text = text_
                user_dates[user_id]["historial"] = info.route
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )

            else:
                info = copy.deepcopy(
                    menu_system["/main/wallet/swap/coin1/coin2/am/<am"]
                )
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(amount=str(len(referrals["lvl1"]) - ref_swaped))
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

        except:

            info = copy.deepcopy(menu_system["/main/wallet/swap/am_err"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route
    if user_dates[user_id]["typing"] == "cripto_swap_amount":

        await event.delete()
        try:

            amount = float(message)
            cripto1 = user_dates[user_id]["swap-coin1"]
            cripto2 = user_dates[user_id]["swap-coin2"]
            balance = user_dates[user_id]["balance"][cripto1]
            if balance >= amount and amount > 0:

                user_dates[user_id]["typing"] = "off"
                user_dates[user_id]["swap_am_sel_cripto"] = amount

                info = menu_system["/main/wallet/swap/coin1/coin2/am/conf"]
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                cripto2_swap = (
                    (amount * get_price(cripto1)) / get_price(cripto2)
                ) * 0.98

                text = Template(text)
                text = text.substitute(
                    cripto1_am=str(amount),
                    crypto1=cripto1,
                    cripto2_am=str(cripto2_swap),
                    crypto2=cripto2,
                )

                user_dates[user_id]["historial"] = info.route
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )

            else:
                info = copy.deepcopy(
                    menu_system["/main/wallet/swap/coin1/coin2/am/<am"]
                )
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(amount=str(balance))
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

        except Exception as e:

            print_to_web(e)

            info = copy.deepcopy(menu_system["/main/wallet/swap/am_err"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route
    if check_subscription(sender.id, CHANNEL_ID):
        if "/start" in message:

            #key = await get_keyboard_()
            #print_to_web(key)
            user_dates[user_id]["typing"] = "off"
            info =  copy.deepcopy(menu_system["/main"])
            info.custom(lg)
            text = info.text
            keyboard = info.keyboard

            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, text, user_dates, keyboard
            )
            user_dates[user_id]["historial"] = info.route
            await event.delete()
            
            if str(sender.id) not in user_dates:

                user_dates[str(sender.id)] = {}

                user_dates[str(sender.id)]["register_dates"] = {}
                user_dates[str(sender.id)]["register_dates"]["time"] = time.time()
                user_dates[str(sender.id)]["register_dates"]["init_bonus"] = True

                if len(message.split(" ")) == 2:
                    code = message.split("-")[1]

                    user_dates[str(sender.id)]["register_dates"]["invitator"] = code
                    user_dates[code]["ref_info"]["ref_dates"][str(sender.id)] = {
                        "regist_date": time.time()
                    }

                else:
                    user_dates[str(sender.id)]["register_dates"]["invitator"] = "None"
            else:
                if "register_dates" not in user_dates:
                    user_dates[str(sender.id)]["register_dates"] = {}
                    user_dates[str(sender.id)]["register_dates"]["time"] = time.time()
                if "init_bonus" not in user_dates[str(sender.id)]["register_dates"]:
                    user_dates[str(sender.id)]["register_dates"]["init_bonus"] = True
            if "invitator" not in user_dates[str(sender.id)]["register_dates"]:
                user_dates[str(sender.id)]["register_dates"]["invitator"] = "None"
            if user_dates[str(sender.id)]["register_dates"]["init_bonus"]:
                user_dates[str(sender.id)]["register_dates"]["init_bonus"] = False
                info =  copy.deepcopy(menu_system["/main/gift"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard

                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route
                  
            await upload_db()

        if "/simulate" in message:
            teading_simulate_final()
        if "/reset_db" in message:
            user_dates = {}
            await upload_db()
        if "/add_money" in message:
            cripto = message.split(" ")[1]
            amount = message.split(" ")[2]
            if not "balance" in user_dates[user_id]:
                user_dates[user_id]["balance"] = {}

            user_dates[user_id]["balance"][cripto] = float(amount)
    else:
        info = copy.deepcopy(menu_system["/sub"])
        info.custom(lg)
        text = f"💠 {info.text}"
        keyboard = info.keyboard
        user_dates[user_id]["msg_id"] = await edit_msg(
            bot, sender.id, text, user_dates, keyboard
        )
        user_dates[user_id]["historial"] = info.route


@bot.on(events.CallbackQuery)
async def callback_handler(event):
    await callback_handler_semaforo.acquire()
    try:
        sender = await event.get_sender()
        
        print_to_web(f"{event.data} {str(time.time())} {str(sender.id)}")
        await callback_handler_(event)
        print_to_web(f"{event.data} {str(time.time())}")
    except Exception as e:
        print_to_web(f"Error en el handler: {e}")
    callback_handler_semaforo.release()
async def callback_handler_(event):
    global user_dates
    sender = await event.get_sender()
    user_id = str(sender.id)
    data = event.data
    message = data
    global user_dates
    if str(sender.id) not in user_dates:

        user_dates[str(sender.id)] = {}
    if  'unicron' not in user_dates[user_id]:
            user_dates[user_id]['unicron'] = {
                "lvl":1,
                "ref_expen":0,
                "expen_history":{},
                "state":"off",
                "update_time":None,
                "profit_time":0,
                "total_profit":0
            }
    if "balance" not in user_dates[str(sender.id)]:
        user_dates[user_id]["balance"] = {}

    if "ref_info" not in user_dates[str(sender.id)]:
        user_dates[user_id]["ref_info"] = {"ref_dates": {}}
        user_dates[user_id]["ref_info"]["stake"] = {"ganance": 0}
        user_dates[user_id]["ref_info"]["casino"] = {"ganance": 0}
        user_dates[user_id]["ref_info"]["airdrop"] = {"ganance": 0}
        user_dates[user_id]["ref_info"]["unicorn"] = {"ganance": 0}
        user_dates[user_id]["ref_info"]["free_uni"] = {"ganance": 0}
        user_dates[user_id]["ref_info"]["grid_trading"] = {"ganance": 0}

    if "USDT" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["USDT"] = 0
    if "BTC" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["BTC"] = 0
    if "LTC" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["LTC"] = 0
    if "ETH" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["ETH"] = 0
    if "BNB" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["BNB"] = 0
    if "UNI" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["UNI"] = 0
    if "TRX" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["TRX"] = 0
    if "TON" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["TON"] = 0
    if "NOT" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["NOT"] = 0
    if "USDC" not in user_dates[user_id]["balance"]:
        user_dates[user_id]["balance"]["USDC"] = 0

    if "leng" not in user_dates[user_id]:
        
        user_dates[user_id]["leng"] = "en"
        
    if user_dates[user_id]["leng"] not in lenguage:
        user_dates[user_id]["leng"] = "en"
    if "bet_size" not in user_dates[user_id]:
        user_dates[user_id]["bet_size"] = 0

    if not user_id in request:
        request[user_id] = {}
        request[user_id]["pending"] = False

    lg = user_dates[user_id]["leng"]

    try:

        # if request[user_id]['pending']:
        #   return 0
        request[user_id]["pending"] = True

        if message == b"back":
            await menu_action(event, "back")
        await unicorn(event)
        await free_uni(event)
        await callback_handler_cripto(event)
        await casino_cripto(event)
        await grid_cripto(event)
        await settings(event)
        await stake(event)
        await nft(event)
        if message == b"check_sub":
            if check_subscription(sender.id, CHANNEL_ID):
                info = menu_system["/main"]
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

            else:

                info = copy.deepcopy(menu_system["/sub"])
                info.custom(lg)
                text = f"⚠️ {info.text}"
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route
            # return 0

        # if check_subscription(sender.id,CHANNEL_ID):
        if True:
            if message == b"wallet":

                usdt = user_dates[user_id]["balance"]["USDT"]

                btc = user_dates[user_id]["balance"]["BTC"]

                ltc = user_dates[user_id]["balance"]["LTC"]

                eth = user_dates[user_id]["balance"]["ETH"]

                bnb = user_dates[user_id]["balance"]["BNB"]

                uni = user_dates[user_id]["balance"]["UNI"]

                trx = user_dates[user_id]["balance"]["TRX"]
                ton = user_dates[user_id]["balance"]["TON"]
                not_ = user_dates[user_id]["balance"]["NOT"]

                usdc = user_dates[user_id]["balance"]["USDC"]
                usd_total = (
                    usdt
                    + get_price("BTC") * btc
                    + get_price("LTC") * ltc
                    + get_price("ETH") * eth
                    + get_price("BNB") * bnb
                    + get_price("UNI") * uni
                    + get_price("TRX") * trx
                    + get_price("TON") * ton
                    + get_price("NOT") * not_
                    + get_price("USDC") * usdc
                )
                uni_total = usdt_to_cryp("UNI", usd_total)
                info = copy.deepcopy(menu_system["/main/wallet"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(
                    usdt=usdt,
                    ton=ton,
                    btc=btc,
                    ltc=ltc,
                    eth=eth,
                    bnb=bnb,
                    uni=uni,
                    tron=trx,
                    uni_total=uni_total,
                    uni_total_to_usd=usd_total,
                    not_=not_,
                    usdc=usdc,
                )
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route
            elif message == b"get_initgift":
                if len(user_dates[user_id]["ref_info"]["ref_dates"]) >= 3:  
                    info = copy.deepcopy(menu_system["/main/authorized_gift"])
                    user_dates[user_id]["balance"]["UNI"] += 0.05
                else:
                    info = copy.deepcopy(menu_system["/main/gift/unauthorized_gift"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard

                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route
            elif message == b"initgift_invite":
                info = copy.deepcopy(menu_system["/main/free_uni/referrals"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                text = Template(text)
                text = text.substitute(code=user_id)
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )

            elif message == b"profile":
                return 0

                info = "ID: <code>1038737191</code>\n\n👨 Jorge King\n\n• Número telefónico:\n\n+1 102983727\n\n• Lenguaje:\n🇺🇸 English\n\n• Moneda favorita:\n\nBTC/USD ≈ 718.19828 USD"
                info = my_text_db.translate(info, lg)
                # keyboard=[[Button.inline(my_text_db.translate('✏️ Editar perfil',lg), data=b'profile_edit')],[Button.inline(my_text_db.translate('🔙 Back',lg), data=b'back')]]
                keyboard = await get_custom_menu(event)[3]
                user_dates[user_id]["historial"] = [1]
                # await event.respond(info,buttons=keyboard,parse_mode='html')
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, info, user_dates, keyboard
                )
            elif message == b"services":
                return 0
                keyboard = [
                    [Button.inline(my_text_db.translate("-", lg), data=b"aliment")],
                    [Button.inline(my_text_db.translate("🔙 Back", lg), data=b"back")],
                ]
                chat_id = sender.id

                info = "Info"
                info = my_text_db.translate(info, lg)
                media = "2.jpg"
                # await bot.send_file(chat_id, file=media,caption=info, buttons=keyboard,parse_mode='html')
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, info, user_dates, keyboard, media
                )
            elif message == b"subsc":

                keyboard = [
                    [
                        Button.url(
                            my_text_db.translate("UniSwap News", lg), "http://t.me/UniSwapNew"
                        )
                    ],
                    [
                        Button.url(
                            my_text_db.translate("UniSwap Chat", lg), "http://t.me/uniswaptips"
                        )
                    ],
                    [
                        Button.inline(
                            my_text_db.translate("✅I am joined,Continue>", lg), data=b"check_sub"
                        )
                    ],
                ]
                keyboard = await get_custom_menu(event)[4]
                user_dates[user_id]["historial"] = [1]
                info = '💠 Join our <a href="http://t.me/uniswapnew">channel</a> and <a href="http://t.me/uniswaptips">chat</a> to stay tuned for new features and other updates from <a href="http://t.me/uniswapbot">UniSwap Bot</a>.'
                info = my_text_db.translate(info, lg)
                # await event.respond(info,buttons=keyboard,parse_mode='html',link_preview=False)
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, info, user_dates, keyboard
                )
            # Grid
            elif message == b"grid":
                info = copy.deepcopy(menu_system["/main/grid"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

            elif message == b"new_grid":
                info = copy.deepcopy(menu_system["/main/grid/new_grid_cripto"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route

            elif message == b"casino":

                info = copy.deepcopy(menu_system["/main/casino"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route
            elif message == b"free_uni":
                info = copy.deepcopy(menu_system["/main/free_uni"])
                info.custom(lg)
                text = info.text
                keyboard = info.keyboard
                user_dates[user_id]["msg_id"] = await edit_msg(
                    bot, sender.id, text, user_dates, keyboard
                )
                user_dates[user_id]["historial"] = info.route


        else:
            keyboard = [
                [Button.url(my_text_db.translate("UniSwap News", lg), "http://t.me/UniSwapNew")],
                [Button.url(my_text_db.translate("UniSwap Chat", lg), "http://t.me/uniswaptips")],
                [
                    Button.inline(
                        my_text_db.translate("✅I am joined,Continue>", lg), data=b"check_sub"
                    )
                ],
            ]
            keyboard = await get_custom_menu(event)
            keyboard = keyboard[4]
            user_dates[user_id]["historial"] = [1]
            info = '⚠️ Join our <a href="http://t.me/uniswapnew">channel</a> and <a href="http://t.me/uniswaptips">chat</a> to stay tuned for new features and other updates from <a href="http://t.me/uniswapbot">UniSwap Bot</a>.'
            info = my_text_db.translate(info, lg)
            # await event.respond(info,buttons=keyboard,parse_mode='html',link_preview=False)
            user_dates[user_id]["msg_id"] = await edit_msg(
                bot, sender.id, info, user_dates, keyboard
            )
        request[user_id]["pending"] = False
    except Exception as e:
        print_to_web(f"Error in callback: {e}")
        request[user_id]["pending"] = False


def teading_simulate_final():
    global user_dates

    for uid in user_dates:
        if "bots" in user_dates[uid]:

            for id_ in user_dates[uid]["bots"]:
                if "user_copied" in user_dates[uid]["bots"][id_]:
                    continue
                # copy_bots_=user_dates[uid]['launched'][id_]
                bot_dates = user_dates[uid]["bots"][id_]
                cripto = bot_dates["cripto"]
                lvg = bot_dates["lvg"]
                sl = bot_dates["sl"]
                tp = bot_dates["tp"]
                time_ = bot_dates["date"]
                min_ords = bot_dates["min_ords"]
                invest = bot_dates["usd_am"]
                if lvg == 0:
                    lvg = 1
                data = get_price_history(cripto)

                register = trading_simulate(data, min_ords, lvg)
                oper_register = register["operations"]
                print_to_web(
                    "----------------------------------------RESUMEN---------------------------------"
                )
                print_to_web(register["result"])
                result = 0
                shorts = 0
                longs = 0

                oper_report = ""
                if "state" not in user_dates[uid]["bots"][id_]:
                    user_dates[uid]["bots"][id_]["state"] = "on"

                if user_dates[uid]["bots"][id_]["state"] != "off":
                    for oper in oper_register:

                        dates = oper.info
                        print_to_web(dates)

                        open_time = dates["open_time"]
                        close_time = dates["close_time"]
                        ganance = dates["ganance"]
                        oper = dates["oper"]

                        open_price = dates["open_price"]
                        close_price = dates["close_price"]

                        # if open_time.timestamp() < time_:
                        #    continue

                        result += ganance

                        if oper == "LONG":
                            longs += 1
                        else:
                            shorts += 1
                        if (
                            user_dates[uid]["bots"][id_]["prof_total"] + result * lvg
                            >= tp
                        ):
                            user_dates[uid]["bots"][id_]["state"] = "off"
                            result = (
                                tp - user_dates[uid]["bots"][id_]["prof_total"]
                            ) / lvg
                            close_price = "----"
                            break
                        if (
                            user_dates[uid]["bots"][id_]["prof_total"] + result * lvg
                            <= sl * -1
                        ):
                            user_dates[uid]["bots"][id_]["state"] = "off"
                            result = (
                                (sl - abs(user_dates[uid]["bots"][id_]["prof_total"]))
                                / lvg
                            ) * -1
                            close_price = "----"
                            break

                    print_to_web(result)
                    print_to_web(lvg)

                    total_ganance = result * lvg

                    user_dates[uid]["bots"][id_]["prof_total"] += total_ganance
                    user_dates[uid]["bots"][id_]["prof_today"] = total_ganance
                    user_dates[uid]["bots"][id_]["ord_today"] = longs + shorts
                    user_dates[uid]["bots"][id_]["ord_total"] += longs + shorts
                    user_dates[uid]["bots"][id_]["shorts"] += shorts
                    user_dates[uid]["bots"][id_]["longs"] += longs
                ref_ganance = 0
                if "launched" in user_dates[uid] and id_ in user_dates[uid]["launched"]:
                    copiers = user_dates[uid]["launched"][id_]["copiers"]
                    print_to_web("copiers")
                    if isinstance(copiers, (str, int, float)):
                        user_dates[uid]["launched"][id_]["copiers"] = [
                            str(user_dates[uid]["launched"][id_]["copiers"])
                        ]

                    copiers = user_dates[uid]["launched"][id_]["copiers"]
                    for copier_id in copiers:
                        copier_bot_dates = user_dates[copier_id]["bots"]
                        for bot_id in copier_bot_dates:

                            if (
                                "user_copied" in copier_bot_dates[bot_id]
                                and user_dates[copier_id]["bots"][bot_id]["state"]
                                != "off"
                            ):

                                user_copied = copier_bot_dates[bot_id]["user_copied"]
                                bot_copied = copier_bot_dates[bot_id]["bot_copied"]
                                if uid == user_copied and bot_copied == id_:
                                    result = 0
                                    shorts = 0
                                    longs = 0

                                    time_ = user_dates[copier_id]["bots"][bot_id][
                                        "date"
                                    ]
                                    for oper in oper_register:

                                        dates = oper.info

                                        open_time = dates["open_time"]
                                        close_time = dates["close_time"]
                                        ganance = dates["ganance"]
                                        oper = dates["oper"]

                                        open_price = dates["open_price"]
                                        close_price = dates["close_price"]

                                        # if open_time.timestamp() < time_:
                                        #   continue

                                        result += ganance
                                        if oper == "LONG":
                                            longs += 1
                                        else:
                                            shorts += 1
                                        if (
                                            user_dates[copier_id]["bots"][bot_id][
                                                "prof_total"
                                            ]
                                            + result * lvg
                                            >= tp
                                        ):
                                            user_dates[copier_id]["bots"][bot_id][
                                                "state"
                                            ] = "off"
                                            result = (
                                                tp
                                                - user_dates[copier_id]["bots"][bot_id][
                                                    "prof_total"
                                                ]
                                            ) / lvg
                                            close_price = "----"
                                            break
                                        if (
                                            user_dates[copier_id]["bots"][bot_id][
                                                "prof_total"
                                            ]
                                            + result * lvg
                                            <= sl * -1
                                        ):
                                            user_dates[copier_id]["bots"][bot_id][
                                                "state"
                                            ] = "off"
                                            result = (
                                                (
                                                    sl
                                                    - abs(
                                                        user_dates[copier_id]["bots"][
                                                            bot_id
                                                        ]["prof_total"]
                                                    )
                                                )
                                                / lvg
                                            ) * -1
                                            close_price = "----"
                                            break
                                    total_ganance_copied = result * lvg
                                    total_brute_ganance_copied = (
                                        (result * lvg) / 100
                                    ) * user_dates[copier_id]["bots"][bot_id]["usd_am"]
                                    ref_ganance += total_brute_ganance_copied * (
                                        15 / 100
                                    )
                                    user_dates[copier_id]["bots"][bot_id][
                                        "ord_today"
                                    ] = (longs + shorts)
                                    user_dates[copier_id]["bots"][bot_id][
                                        "ord_total"
                                    ] += (longs + shorts)
                                    user_dates[copier_id]["bots"][bot_id][
                                        "shorts"
                                    ] += shorts
                                    user_dates[copier_id]["bots"][bot_id][
                                        "longs"
                                    ] += longs
                                    user_dates[copier_id]["bots"][bot_id][
                                        "prof_today"
                                    ] = total_ganance_copied
                                    user_dates[copier_id]["bots"][bot_id][
                                        "prof_total"
                                    ] += total_ganance_copied
                                    user_dates[uid]["launched"][id_][
                                        "last_earn"
                                    ] = ref_ganance
                                    user_dates[uid]["launched"][id_][
                                        "total_earn"
                                    ] += ref_ganance

                print_to_web(f"---------------------FINAL---------------\n{result}")

@bot.on(events.ChatAction())
async def handle_new_user(event):
    global new_user_msg
    await handler_semaforo.acquire()
    sender = event.user_id
    username = await get_username_from_id(int(sender))
    welcome_messages = [
        '👋 <b>Hi $freq</b> $name. Did you know that UniSwapBot developed a 🎰 <b>Casino</b> directly on Telegram! <a href="https://t.me/UniSwapBot?start=Casino">Try it now »</a>',
        '👋 <b>Welcome  $freq</b> $name. Did you know that UniSwapBot developed a 🎰 Casino directly on Telegram! <a href="https://t.me/UniSwapBot?start=Casino">Try it now »</a>',
        '👋 <b>Hi $freq</b> $name. Do you know what a 📈 <b>Grid Trading</b> is? Now it is possible to use them directly in Telegram! <a href="https://t.me/UniSwapBot?start=GridTrading">Try it now »</a>',
        '👊 Hello $freq $name , Get a free 🦄 <b>Unicorn</b> right now and start earning $UNI Free. <a href="https://t.me/UniSwapBot?start=Unicorn">Get now »</a>'  ,
        '👋 Welcome $freq $name , get a 🎁 <b>Free gift</b> where you can win up to 5 UNI. <a href="https://t.me/UniSwapBot?start=FreeGift">Get now »</a>',
        'Welcome $freq $name.Our 👛Wallet system currently supports more than 10 deposit and 📤Withdrawal methods. <a href="https://t.me/UniSwapBot?start=Wallet">Try it now »</a>'             
    ]
    msg = random.choice(welcome_messages)
    msg = Template(msg)
    
    if event.user_joined:
        msg = msg.substitute(name = f"@{str(username)}",freq = ",")
    if event.user_added:
        msg = msg.substitute(name = f"@{str(username)}",freq = "again,")
    if not event.user_joined and not event.user_added:
        return 0
    msg_send = await bot.send_message(event.chat_id, msg,parse_mode="html",link_preview = False)
    new_user_msg.append(msg_send.id)
    if len(new_user_msg) >= 6:
     
        try:
            
            
            await bot.delete_messages(entity=event.chat_id, message_ids=[new_user_msg[0:3]])
            new_user_msg.pop(0,1,2)
        except:
            print_to_web("error in delete")
            new_user_msg = []
    
    handler_semaforo.release()
def unicorn_simulate():
    for uid in user_dates:
        my_uni = unicorn_(uid,user_dates)
        if my_uni.is_authorized() == "on":
            my_uni.get_profit()
        
def stake_simulate():
    for uid in user_dates:
        my_stake = Stake(uid,user_dates)
        my_stake.get_profit()
       
 

        
def temporizer():
    ready = True
    ready_ = True
    while True:
        #print_to_web("-")
        ahora = datetime.now()
        if ahora.hour%6 == 0:
            if ready_:
                ready_ = False
                stake_simulate()
                unicorn_simulate()
                
        else:
            ready_ = True
            
                
        
             
            
        if ahora.hour == 23:
            if ready:
                ready = False
                teading_simulate_final()
                
                
        else:
            ready = True

        time.sleep(10 * 60)


def main_():

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    if True:

        loop.run_until_complete(deposit_check())
    # except Exception as e:
    """
    else:
        loop.close()
        #print_to_web(f"main exception1 :{e}")
        threading.Thread(target=main_).start()
    """


# Crea un nuevo bucle de eventos

#my_text_db.db_lg()
print_to_web("init_bot")

with bot:

    loop = bot.loop
    loop.create_task(init_dates())
    threading.Thread(target=main_).start()
    #db_lg_ = threading.Thread(target=my_text_db.db_lg())
    
    #db_lg_.start()
    trad_temp = threading.Thread(target=temporizer).start()
   
    bot.run_until_disconnected()
