from telethon import TelegramClient, events, sync
from telethon.tl import functions, types
from telethon import events, Button
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
import random
from telethon.tl.functions.messages import EditMessageRequest
import time
import re
import threading
import copy
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.types import UpdateShortMessage
from telethon.tl.types import PeerUser, PeerChannel
from telethon.tl.types import Message
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipant
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.types import InputMediaPhoto
from string import Template
import asyncio
from threading import Thread
import requests
import json
import time
from db_tools import *
from keep_alive import*
import time
import requests
from datetime import datetime, timedelta
from translate_api_2 import *

api_id = "16620070"
api_hash = "dbf692cdc9b6fb2977dda29fb1691df4"
bot_token = "5850221861:AAFfZUP2HYaeaNE6vxBq8FSwN7n8n6dyrfI"
bot_token = "6918635120:AAGzJbgs4PYqiCtToXype-IqK_6ck8DJhsU"
from telegram import Bot

lenguage = ["ru", "es", "en", "zh-CN", "ar", "hi", "pt", "ja", "fr", "bn"]

bot_pytel = Bot(bot_token)

bot = TelegramClient("app", api_id, api_hash).start(bot_token=bot_token)
client_ = TelegramClient("admin_check", api_id, api_hash)
admin = TelegramClient("admin", api_id, api_hash)
client = TelegramClient("1633521428", api_id, api_hash)

ref_ganance_rate = {
    "unicorn": 0.05,
    "stake": 0.04,
    "casino": 0.15,
    "grid_trading": 0.05,
    "airdrop": 0.08,
    "free_uni": 0.1,
}
alert_text = "💸 Send Payment to Recipient"
min_amount = 0.1
cripto_decimals = {
    "USDT": {"red": ["TRC20", "ERC20", "BEP20"], "decimals": 6},
    "TON": {"red": [], "decimals": 6},
    #'GRAM':{'red':[],'min_amount':usdt_to_cryp('GRAM',min_amount),'amount':usdt_to_cryp('GRAM',min_amount)},
    "BTC": {"red": [], "decimals": 9},
    "LTC": {"red": [], "decimals": 6},
    "ETH": {"red": [], "decimals": 9},
    "BNB": {"red": [], "decimals": 6},
    "TRX": {"red": [], "decimals": 6},
    "UNI": {"red": [], "decimals": 6},
    "NOT": {"red": [], "decimals": 6},
    "USDC": {"red": ["ERC20", "BEP20"], "decimals": 6},
}

cripto_prices = {}
search_crypt = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "BNB": "binancecoin",
    "UNI": "uniswap",
    "SHIB": "shiba-inu",
    "DOGE": "dogecoin",
    "TRX": "tron",
    "LTC": "litecoin",
    "MATIC": "matic-network",
    "ADA": "cardano",
    "SOL": "solana",
    "XRP": "ripple",
    "TON": "toncoin",
    "BCH": "bitcoin-cash",
    "FLOKI": "floki-inu",
    "SUSHI": "sushi",
    "CAKE": "pancakeswap-token",
    "DASH": "dash",
    "NOT": "notcoin",
    "USDC": "usdc",
}
min_dep = {
    "USDT": 5,
    "USDC": 5,
    "TRX": 25,
    "BTC": 0.000085,
    "TON": 2,
    "BNB": 0.0085,
    "ETH": 0.0015,
    "LTC": 0.05,
    "NOT": 1,
}
fees = {
    "USDT": 1,
    "USDC": 5,
    "TRX": 25,
    "BTC": 0.000085,
    "TON": 0.1,
    "BNB": 0.0085,
    "ETH": 0.0015,
    "LTC": 0.05,
    "NOT": 200,
}
min_dep_usd = {
    "USDT": 5,
    "USDC": 5,
    "TRX": 25,
    "BTC": 0.000085,
    "TON": 2,
    "BNB": 0.0085,
    "ETH": 0.0015,
    "LTC": 0.05,
}

max_dep = {
    "USDT": 1000,
    "USDC": 1000,
    "TRX": 10000,
    "BTC": 10000,
    "TON": 10000,
    "BNB": 10000,
    "ETH": 10000,
    "LTC": 10000,
    "NOT": 1000000,
}





async def get_user_id_from_username(username):
    try:
        input_entity = await client_.get_input_entity(user_id)
        user = await client_.get_entity(input_entity)
        user = await client.get_entity(username)
        return user.id
    except:
        return None


# api_id = '16620070'
# api_hash = 'dbf692cdc9b6fb2977dda29fb1691df4'
def cripto_dates(criptomoneda):
    for i in range(30):
        try:
            moneda = "USD"
            criptomoneda = criptomoneda.replace(" ", "")
            url = f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={criptomoneda}&tsyms={moneda}"
            response = requests.get(url)

            if response.status_code == 200:
                resultadoJson = response.json()
                cotizacion = resultadoJson["RAW"][criptomoneda][moneda]
                return cotizacion
                # También puedes imprimir el resultado DISPLAY aquí si es necesario
                # print_to_web(resultadoJson["DISPLAY"][criptomoneda][moneda])
            else:
                print_to_web(f"Error al consultar la API: {response.status_code}")

        except Exception as e:
            print_to_web(f"error {e}")
    return None


def get_price_(crypto):

    for i in range(30):
        try:
            crypto = search_crypt[crypto]
            url = "https://api.coingecko.com/api/v3/simple/price"

            params = {
                "ids": crypto,  # Aquí va el identificador de la criptomoneda
                "vs_currencies": "usd",  # Aquí va la moneda en la que quieres el precio
            }
            response = requests.get(url, params=params)
            data = response.json()
            if response.status_code == 200:
                data = response.json()
                cripto_price = data[crypto]["usd"]
                if isinstance(cripto_price, (int, float)):
                    return cripto_price

            else:

                print_to_web("No se pudo obtener los datos de la API")
                return None
        except Exception as e:

            print_to_web(e)
            return None


def get_price(criptomoneda):

    print_to_web(f"getting price: {criptomoneda}")
    decimals = cripto_decimals[criptomoneda]["decimals"]

    try:
        if criptomoneda == "NOT":
            if criptomoneda not in cripto_prices:
                cripto_prices[criptomoneda] = {}
                resp = round(get_price_(criptomoneda), decimals)
                cripto_prices[criptomoneda]["price"] = resp
                cripto_prices[criptomoneda]["update_hour"] = time.time()
                return resp
            if time.time() - cripto_prices[criptomoneda][
                "update_hour"
            ] <= 300 and isinstance(cripto_prices[criptomoneda]["price"], (float, int)):
                return cripto_prices[criptomoneda]["price"]

            resp = round(get_price_(criptomoneda), decimals)

            if not isinstance(resp, (int, float)):
                return cripto_prices[criptomoneda]["price"]
            cripto_prices[criptomoneda]["price"] = resp
            cripto_prices[criptomoneda]["update_hour"] = time.time()
            return resp

        if criptomoneda not in cripto_prices:
            cripto_prices[criptomoneda] = {}
            resp = round(cripto_dates(criptomoneda)["PRICE"], decimals)
            cripto_prices[criptomoneda]["price"] = resp
            cripto_prices[criptomoneda]["update_hour"] = time.time()
            return resp
        if time.time() - cripto_prices[criptomoneda][
            "update_hour"
        ] <= 300 and isinstance(cripto_prices[criptomoneda]["price"], (float, int)):
            return cripto_prices[criptomoneda]["price"]

        resp = round(cripto_dates(criptomoneda)["PRICE"], decimals)
        if not isinstance(resp, (int, float)):
            return cripto_prices[criptomoneda]["price"]
        cripto_prices[criptomoneda]["price"] = resp
        cripto_prices[criptomoneda]["update_hour"] = time.time()
        return resp
    except:
        print_to_web("error in get_price")


def usdt_to_cryp(criptomoneda, amount):
    cryp_value = get_price(criptomoneda)
    resp = amount / cryp_value
    decimals = cripto_decimals[criptomoneda]["decimals"]
    return round(resp, decimals)


criptos = {
    "USDT": {
        "red": ["TRC20", "ERC20", "BEP20"],
        "min_amount": min_amount,
        "amount": min_amount,
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": {"TON": 1, "TRC20": 1, "ERC20": 0.01, "BEP20": 1},
        "fee": {"TON": 0.5, "TRC20": 3.5, "ERC20": 15.5, "BEP20": 3},
    },
    "TON": {
        "red": [],
        "min_amount": usdt_to_cryp("TON", min_amount),
        "amount": usdt_to_cryp("TON", min_amount),
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": 0.001,
        "fee": 0.1,
    },
    #'GRAM':{'red':[],'min_amount':usdt_to_cryp('GRAM',min_amount),'amount':usdt_to_cryp('GRAM',min_amount)},
    "BTC": {
        "red": [],
        "min_amount": usdt_to_cryp("BTC", min_amount),
        "amount": usdt_to_cryp("BTC", min_amount),
        "decimals": 9,
        "min_deposit": 0.00002,
        "min_withdraw": 0.001,
        "fee": 0.00275,
    },
    "LTC": {
        "red": [],
        "min_amount": usdt_to_cryp("LTC", min_amount),
        "amount": usdt_to_cryp("LTC", min_amount),
        "decimals": 6,
        "min_deposit": 0.0001,
        "min_withdraw": 0.01,
        "fee": 0.0125,
    },
    "ETH": {
        "red": [],
        "min_amount": usdt_to_cryp("ETH", min_amount),
        "amount": usdt_to_cryp("ETH", min_amount),
        "decimals": 9,
        "min_deposit": None,
        "min_withdraw": 0.001,
        "fee": 0.008,
    },
    "BNB": {
        "red": [],
        "min_amount": usdt_to_cryp("BNB", min_amount),
        "amount": usdt_to_cryp("BNB", min_amount),
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": 0.001,
        "fee": 0.005,
    },
    "TRX": {
        "red": [],
        "min_amount": usdt_to_cryp("TRX", min_amount),
        "amount": usdt_to_cryp("TRX", min_amount),
        "decimals": 6,
        "min_deposit": 10,
        "min_withdraw": 20,
        "fee": 10,
    },
    "NOT": {
        "red": [],
        "min_amount": usdt_to_cryp("TRX", min_amount),
        "amount": usdt_to_cryp("TRX", min_amount),
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": 1,
        "fee": 200,
    },
    "USDC": {
        "red": [],
        "min_amount": usdt_to_cryp("TRX", min_amount),
        "amount": usdt_to_cryp("TRX", min_amount),
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": {"ERC20": 0.01, "BEP20": 1.5},
        "fee": {"ERC20": 8.5, "BEP20": 0.01},
    },
    "UNI": {
        "red": [],
        "min_amount": usdt_to_cryp("UNI", min_amount),
        "amount": usdt_to_cryp("UNI", min_amount),
        "decimals": 6,
        "min_deposit": None,
        "min_withdraw": {"ERC20": 0.01, "BEP20": 1.5},
        "fee": {"ERC20": 8.5, "BEP20": 0.01},
    },
    
}


def is_valid_add(criptomoneda, direccion, net=None):
    resultado = coinaddrvalidator.validate(criptomoneda, direccion)
    valid = False
    if resultado.valid:
        valid = True
        if net:
            if net != resultado.network:
                valid = False
    return valid


def resolve_slot_machine(value):
    map_ = [
        0,
        1,
        2,
        3,
        "7️⃣",
        "🍸",
        "🍇",
        "🍋",
        8,
        9,
        "7️⃣",
        "🍸",
        "🍇",
        "🍋",
        14,
        15,
        "7️⃣",
        "🍸",
        "🍇",
        "🍋",
    ]

    map = [1, 2, 3, 0]
    s1 = 4 + map[(value - 1) & 3]
    s2 = 10 + map[((value - 1) >> 2) & 3]
    s3 = 16 + map[((value - 1) >> 4) & 3]

    return f"{map_[s1]},{map_[s2]},{map_[s3]}"


def get_ref(user_dates, user_id):
    lvl1 = []
    lvl2 = []
    lvl3 = []

    for uid in user_dates:
        if "register_dates" not in user_dates[uid]:
            user_dates[uid]["register_dates"] = {}
            user_dates[uid]["register_dates"]["invitator"] = "None"
        if user_dates[uid]["register_dates"]["invitator"] == user_id:
            lvl1.append(uid)

    for user_id in lvl1:

        for uid in user_dates:
            if user_dates[uid]["register_dates"]["invitator"] == user_id:
                lvl2.append(uid)

    for user_id in lvl2:
        for uid in user_dates:
            if user_dates[uid]["register_dates"]["invitator"] == user_id:
                lvl3.append(uid)
    return {"lvl1": lvl1, "lvl2": lvl2, "lvl3": lvl3}


async def get_last_message_and_event(chat_id):
    await client.connect()
    async for message in client.iter_messages(chat_id, limit=1):
        return message


async def check_subscription_(user_id, channel_ids):

    await client_.connect()

    async with client_:
        for channel_id in channel_ids:
            channel = await client_.get_entity(channel_id)
            # user = await client_.get_entity(user_id)
            participants = await client_.get_participants(channel)
            user_ids = [participant.id for participant in participants]
            print_to_web(user_ids)
            if str(user_id) in user_ids or int(user_id) in user_ids:
                print_to_web("El usuario está suscrito al canal.")
                # await client_.disconnect()
                # return True

            else:
                print_to_web("El usuario no está suscrito al canal.")
                # await client_.disconnect()
                return False
        return True


async def get_username_from_id(user_id):

    try:
        await client_.connect()
        input_entity = await client_.get_input_entity(user_id)
        user = await client_.get_entity(input_entity)
        if user.username:
            return user.username
        else:
            return user_id
    except ValueError:
        return user_id


async def get_forwarded_chat_id(event):
    if event.message.fwd_from:
        fwd_header = event.message.fwd_from

        # Obtener el ID del remitente original (si está disponible)
        if isinstance(fwd_header.from_id, PeerUser):
            original_author_id = fwd_header.from_id.user_id
            return original_author_id
        if isinstance(fwd_header.from_id, PeerChannel):
            fwd_channel_id = fwd_header.from_id.channel_id
            original_chat = await client_.get_entity(fwd_channel_id)
            return original_chat
    else:
        return None


def check_subscription(user_id, channel_ids):

    for channel_id in channel_ids:
        member = bot_pytel.get_chat_member(channel_id, user_id)

        if member.status == "member" or member.status == "administrator":

            print_to_web("El usuario está suscrito al canal.")
        else:
            print_to_web(member.status)
            return False
    return True


async def edit_msg(bot, user_id, txt, db, buttons_=None, img=None, persistence=False):

    msg_id = db[str(user_id)]["msg_id"]
    # while True:

    if not persistence:
        try:
            if isinstance(msg_id, list):
                await bot.delete_messages(entity=user_id, message_ids=msg_id)

            else:
                await bot.delete_messages(entity=user_id, message_ids=[msg_id])

        except:
            print_to_web("error in delete")
    if img:
        msg = await bot.send_file(
            user_id, file=img, caption=txt, buttons=buttons_, parse_mode="html"
        )
        return msg.id
    msg = await bot.send_message(
        user_id, txt, buttons=buttons_, parse_mode="html", link_preview=False
    )
    return msg.id


class MyEvent:
    def __init__(self, event):
        # Copiar atributos básicos del evento original
        self.original_update = event
        self.chat_id = getattr(event, "chat_id", None)
        self.message = getattr(event, "message", None)

        self.raw_text = getattr(self.message, "raw_text", None)
        self.data = getattr(event, "data", None)  # Agregar atributo data

        # ... (agregar más atributos según tus necesidades)

    def __getattr__(self, name):
        # Acceder a atributos del evento original si no existen en MyEvent
        return getattr(self.original_update, name)

    def get_sender(self):
        return self.original_update.get_sender()


class Stake:
    def __init__(self, uid, db, days=None, crypto=None):
        self.day_perc = {
            "5": 0.04,
            "15": 0.07,
            "20": 0.1,
            "30": 0.14,
            "50": 0.2,
            "75": 0.4,
        }
        self.emoticon = {
            "5": "📙",
            "15": "📗",
            "20": "📘",
            "30": "📕",
            "50": "📔",
            "75": "📓",
        }

        self.user_dates = db
        self.uid = uid
        self.balance = self.user_dates[self.uid]["balance"]
        self.usdt_ref = self.user_dates[self.uid]["ref_info"]["stake"]["ganance"]
        +self.user_dates[self.uid]["ref_info"]["casino"]["ganance"]
        +self.user_dates[self.uid]["ref_info"]["airdrop"]["ganance"]
        +self.user_dates[self.uid]["ref_info"]["unicorn"]["ganance"]
        +self.user_dates[self.uid]["ref_info"]["free_uni"]["ganance"]
        +self.user_dates[self.uid]["ref_info"]["grid_trading"]["ganance"]
        self.usdt_total = self.user_dates[self.uid]["balance"]["USDT"] + self.usdt_ref

        if "stake_dates" not in self.user_dates[self.uid]:
            self.user_dates[self.uid]["stake_dates"] = {"days": None, "crypto": None}

        if "stake" not in self.user_dates[self.uid]:
            self.user_dates[self.uid]["stake"] = {}
        """
                                                        "crypto" : None,
                                                        "balance" : None,
                                                        "days" : None,
                                                        "start_date" : None,
        """
        if days:
            self.user_dates[self.uid]["stake_dates"]["days"] = days
        if crypto:
            self.user_dates[self.uid]["stake_dates"]["crypto"] = crypto
        self.days = self.user_dates[self.uid]["stake_dates"]["days"]
        self.crypto = self.user_dates[self.uid]["stake_dates"]["crypto"]

    def status(self, crypto=None):
        """
        0 not exist
        1 started
        2 ended
                        "balance" : None,
                        "days" : None,
                        "start_date" : None,
                        "start_fech"
                        "end_fech"
                        "profit"
                        "profit_perc"
                        "emoticon"
        """

        if not crypto:
            crypto = self.crypto
        dates = {}

        dates["balance"] = self.user_dates[self.uid]["balance"][crypto]
        dates["days"] = self.days
        dates["start_date"] = time.time()

        tiempo_estructurado = time.localtime(dates["start_date"])
        # Formatear la tupla de tiempo a "día/mes/año"
        fecha_formateada = time.strftime("%d/%m/%Y", tiempo_estructurado)
        dates["start_fech"] = fecha_formateada
        tiempo_estructurado = time.localtime(
            dates["start_date"] + dates["days"] * 3600 * 24
        )
        fecha_formateada = time.strftime("%d/%m/%Y", tiempo_estructurado)
        dates["end_fech"] = fecha_formateada

        profit = dates["balance"] + self.day_perc[str(dates["days"])] * dates["balance"]
        dates["profit"] = profit
        dates["profit_perc"] = self.day_perc[str(dates["days"])] * 100
        dates["emoticon"] = self.emoticon[str(dates["days"])]
        if crypto in self.user_dates[self.uid]["stake"]:
            dates["days"] = self.user_dates[self.uid]["stake"][crypto]["days"]
            dates["start_date"] = self.user_dates[self.uid]["stake"][crypto][
                "start_date"
            ]
            dates["balance"] = self.user_dates[self.uid]["stake"][crypto]["balance"]
            tiempo_estructurado = time.localtime(dates["start_date"])
            fecha_formateada = time.strftime("%d/%m/%Y", tiempo_estructurado)
            dates["start_fech"] = fecha_formateada
            tiempo_estructurado = time.localtime(
                dates["start_date"] + dates["days"] * 3600 * 24
            )
            fecha_formateada = time.strftime("%d/%m/%Y", tiempo_estructurado)
            dates["end_fech"] = fecha_formateada
            profit = (
                dates["balance"] + self.day_perc[str(dates["days"])] * dates["balance"]
            )
            dates["profit"] = profit
            dates["profit_perc"] = self.day_perc[str(dates["days"])] * 100
            dates["emoticon"] = self.emoticon[str(dates["days"])]
            if self.user_dates[self.uid]["stake"][crypto]["status"] == "started":

                dates["status"] = "started"
            else:
                dates["status"] = "ended"
        else:
            dates["status"] = "not_exist"

        return dates

    def is_valid(self, crypto=None, days=None):
        if not crypto:
            crypto = self.crypto
        if not days:
            days = self.days
        if crypto in self.user_dates[self.uid]["stake"]:
            if self.user_dates[self.uid]["status"] == "started":
                return False
        if crypto in self.user_dates[self.uid]["balance"]:

            if crypto == "USDT" and self.usdt_total > 0:
                return True
            if self.user_dates[self.uid]["balance"][crypto] > 0:
                return True
        return False

    def create_stake(self, crypto=None, days=None):
        if not crypto:
            crypto = self.crypto
        if not days:
            days = self.days
        if self.is_valid(crypto, days):
            bal = self.user_dates[self.uid]["balance"][crypto]
            if crypto == "USDT":
                bal = self.usdt_total
            self.user_dates[self.uid]["stake"][crypto] = {
                "balance": bal,
                "days": days,
                "start_date": time.time(),
                "status": "started",
            }
            self.user_dates[self.uid]["balance"][crypto] = 0
            return True
        return False

    def get_profit(self):
        for crypto in self.user_dates[self.uid]["stake"]:

            bal = self.user_dates[self.uid]["stake"][crypto]["balance"]
            days = self.user_dates[self.uid]["stake"][crypto]["days"]
            start = self.user_dates[self.uid]["stake"][crypto]["start_date"]
            if (
                time.time() - self.user_dates[self.uid]["stake"][crypto]["start_date"]
                >= 3600 * 24 * self.user_dates[self.uid]["stake"][crypto]["days"]
            ) and (self.user_dates[self.uid]["stake"][crypto]["status"] == "started"):
                self.user_dates[self.uid]["stake"][crypto]["status"] = "ended"
                if crypto == "USDT":
                    bal = bal - self.usdt_ref
                profit = self.day_perc[str(days)] * bal

                self.user_dates[self.uid]["balance"][crypto] += bal + profit
                invitator = self.user_dates[self.uid]["register_dates"]["invitator"]
                if invitator != "None":
                    self.user_dates[invitator]["ref_info"]["stake"]["ganance"] += (
                        ref_ganance_rate["stake"] * get_price(crypto) * profit
                    )

    def check_ended(self):
        ended = []
        for crypto in self.user_dates[self.uid]["stake"]:

            if self.user_dates[self.uid]["stake"][crypto]["status"] == "ended":
                ended.append(crypto)
        return ended

    def clean_stake(self, crypto):
        self.user_dates[self.uid]["stake"].pop(crypto)


class Profile:
    def __init__(self, uid, db):
        self.lg_abbrev = {
            "ru": "🇷🇺Русский",
            "es": "🇪🇸Español",
            "en": "🇺🇸English",
            "zh-CN": "🇨🇳普通话",
            "ar": "🇸🇦العربية",
            "hi": "🇮🇳हिन्दी",
            "pt": "🇵🇹Português",
            "ja": "🇯🇵日本語",
            "fr": "🇫🇷Français",
            "bn": "🇧🇩বাংলা",
        }
        self.user_dates = db
        self.uid = uid

        if "profile" not in self.user_dates[self.uid]:
            self.user_dates[self.uid]["profile"] = {
                "ID": self.uid,
                "Name": None,
                "Email": None,
                "Phone": None,
                "Language": {"lg": "en", "cords": "1:0"},
                "Favorite_currency": {"curr": "USDT", "cords": "0:0"},
            }
        self.profile = self.user_dates[self.uid]["profile"]
        self.name = self.profile["Name"]
        self.email = self.profile["Email"]
        self.phone = self.profile["Phone"]
        self.language = self.lg_abbrev[self.profile["Language"]["lg"]]
        self.language_cord = self.profile["Language"]["cords"].split(":")

        self.favorite_currency = self.profile["Favorite_currency"]["curr"]
        self.favorite_currency_cord = self.profile["Favorite_currency"]["cords"].split(
            ":"
        )

    def set_param(self, param, value, cords=None):
        """
        Parameters:
         {
            "ID":self.uid,
            "Name" : None,
            "Email" : None,
            "Phone": None,
            "Language": {"lg":"en","cords":"1_0"},
            "Favorite_currency": None

        }

        """
        if param == "Email":
            if not self.is_email(value):
                return False
        if param == "Phone":
            if not self.is_phone_number(value):
                return False
            value = value.replace("+", "")
            value = f"+{value}"
        if param == "Language":
            self.user_dates[self.uid]["leng"] = value
            self.profile[param]["lg"] = value
            self.profile[param]["cords"] = cords
            return True

        if param == "Favorite_currency":

            self.profile[param]["curr"] = value
            self.profile[param]["cords"] = cords
            return True

        self.profile[param] = value
        return True

    def is_email(self, email):
        if "@" in email and ".com" in email and email.islower():
            for caracter in email:
                if not (caracter.isalnum() or caracter == "." or caracter == "@"):
                    return False
            return True
        return False

    def is_phone_number(self, phone):
        for caracter in phone:
            if not (caracter.isdigit() or caracter == "+"):
                return False

        return True


class unicorn_:

    def __init__(self, uid, db):

        self.user_dates = db
        self.uid = uid

        self.lvl_dates = {
            "lvl_1": {
                "name": "BabyUni",
                "diary": 0.005,
                "bonus": 0.05,
                "foot_necesary": 1,
                "foot_to_up": 8,
                "bonus_tasks": 0,
                "new_uni": True,
            },
            "lvl_2": {
                "name": "Rebel",
                "diary": 0.0075,
                "bonus": 0.05,
                "foot_necesary": 5,
                "foot_to_up": 15,
                "bonus_tasks": 0,
                "new_uni": False,
            },
            "lvl_3": {
                "name": "Rebel",
                "diary": 0.0085,
                "bonus": 0.05,
                "foot_necesary": 10,
                "foot_to_up": 25,
                "bonus_tasks": 10,
                "new_uni": True,
            },
            "lvl_4": {
                "name": "HardUni",
                "diary": 0.01,
                "bonus": 0.08,
                "foot_necesary": 25,
                "foot_to_up": 40,
                "bonus_tasks": 10,
                "new_uni": False,
            },
            "lvl_5": {
                "name": "HardUni",
                "diary": 0.02,
                "bonus": 0.08,
                "foot_necesary": 40,
                "foot_to_up": 50,
                "bonus_tasks": 20,
                "new_uni": False,
            },
            "lvl_6": {
                "name": "Gladiator",
                "diary": 0.04,
                "bonus": 0.1,
                "foot_necesary": 50,
                "foot_to_up": 100,
                "bonus_tasks": 50,
                "new_uni": True,
            },
            "lvl_7": {
                "name": None,
                "diary": 0.05,
                "bonus": 0.1,
                "foot_necesary": 50,
                "foot_to_up": 100,
                "bonus_tasks": 50,
                "new_uni": False,
            },
        }

    def is_authorized(self):
        if len(self.user_dates[self.uid]["ref_info"]["ref_dates"]) >= 5:
            self.user_dates[self.uid]["unicron"]["state"] = "on"
            if not self.user_dates[self.uid]["unicron"]["update_time"]:
                self.user_dates[self.uid]["unicron"]["update_time"] = time.time()
                return "on"
            total_ref = 0
            lvl_actual = self.user_dates[self.uid]["unicron"]["lvl"]

            for key in self.user_dates[self.uid]["unicron"]["expen_history"]:
                value = self.user_dates[self.uid]["unicron"]["expen_history"][key]
                total_ref += value

            foot_necesary = self.lvl_dates[f"lvl_{str(lvl_actual)}"]["foot_necesary"]

            if (
                time.time() - self.user_dates[self.uid]["unicron"]["update_time"]
                >= 3600 * 24 * 20
            ):
                if total_ref < foot_necesary:
                    self.user_dates[self.uid]["unicron"]["state"] = "suspended"
                    self.user_dates[self.uid]["unicron"]["expen_history"] = {}
                    return "suspended"

                else:
                    self.user_dates[self.uid]["unicron"]["update_time"] = time.time()
                    if self.user_dates[self.uid]["unicron"]["state"] == "suspended":
                        self.user_dates[self.uid]["unicron"]["state"] = "on"
                    else:
                        self.user_dates[self.uid]["unicron"]["expen_history"] = {}

            return "on"
        else:
            return "off"

    def level_up(self):
        total_ref_necesary = {}
        total_ref = 0
        lvl_ = 1
        for lvl in self.lvl_dates:
            lvl_dates = self.lvl_dates[lvl]
            foot_to_up = lvl_dates["foot_to_up"]
            total_ref += foot_to_up
            total_ref_necesary[str(lvl_)] = total_ref
            lvl_ += 1

        lvl_actual = self.user_dates[self.uid]["unicron"]["lvl"]

        while (
            self.user_dates[self.uid]["unicron"]["ref_expen"]
            >= total_ref_necesary[str(lvl_actual)]
        ):
            self.user_dates[self.uid]["unicron"]["lvl"] += 1
            lvl_actual = self.user_dates[self.uid]["unicron"]["lvl"]
            if (
                self.user_dates[self.uid]["unicron"]["ref_expen"]
                < total_ref_necesary[str(lvl_actual)]
            ):

                self.get_profit(self.lvl_dates[f"lvl_{str(lvl_actual)}"]["bonus"])
                self.user_dates[self.uid]["unicron"]["state"] = "on"
                self.user_dates[self.uid]["unicron"]["update_time"] = time.time()
                self.user_dates[self.uid]["unicron"]["expen_history"] = {
                    str(time.time()): self.user_dates[self.uid]["unicron"]["ref_expen"]
                    - total_ref_necesary[str(lvl_actual - 1)]
                }
                return True
        return False

    def feed(self, num):
        self.user_dates[self.uid]["unicron"]["ref_expen"] += num
        self.user_dates[self.uid]["unicron"]["expen_history"][str(time.time())] = num
        upped = self.level_up()
        if self.user_dates[self.uid]["unicron"]["state"] != "on":
            self.is_authorized()
        return upped

    def get_profit(self, bonus=None):
        if bonus:
            profit = bonus

            self.user_dates[self.uid]["unicron"]["total_profit"] += profit
            self.user_dates[self.uid]["balance"]["UNI"] += profit
            invitator = self.user_dates[self.uid]["register_dates"]["invitator"]

            if invitator != "None":
                self.user_dates[invitator]["ref_info"]["unicorn"]["ganance"] += (
                    ref_ganance_rate["unicorn"] * profit
                )

        if (
            time.time() - self.user_dates[self.uid]["unicron"]["profit_time"]
            >= 3600 * 24
            and self.user_dates[self.uid]["unicron"]["state"] == "on"
        ):

            lvl_actual = self.user_dates[self.uid]["unicron"]["lvl"]

            profit = self.lvl_dates[f"lvl_{str(lvl_actual)}"]["diary"]

            self.user_dates[self.uid]["unicron"]["profit_time"] = time.time()
            self.user_dates[self.uid]["unicron"]["total_profit"] += profit
            self.user_dates[self.uid]["balance"]["UNI"] += profit
            invitator = self.user_dates[self.uid]["register_dates"]["invitator"]

            if invitator != "None":
                self.user_dates[invitator]["ref_info"]["unicorn"]["ganance"] += (
                    ref_ganance_rate["unicorn"] * profit
                )

    def total_ref_necesary_(self, Lvl):
        total_ref_necesary = {}
        total_ref = 0
        lvl_ = 1
        for lvl in self.lvl_dates:
            lvl_dates = self.lvl_dates[lvl]
            foot_to_up = lvl_dates["foot_to_up"]
            total_ref += foot_to_up
            total_ref_necesary[str(lvl_)] = total_ref
            lvl_ += 1
        return total_ref_necesary[str(Lvl)]

    def status(self):
        """
        "lvl":1,
        "ref_expen":0,
        "expen_history":{},
        "state":"off",
        "update_time":None,
        "profit_time":0,
        "total_profit":0
        "name"
        "diary"
        "bonus"
        "foot_necesary"
        "foot_to_up"
        "bonus_tasks"
        "new_uni"
        'total_ref_to_up'
        'photo'
        """

        lvl_actual = self.user_dates[self.uid]["unicron"]["lvl"]
        statics = self.lvl_dates[f"lvl_{str(lvl_actual)}"]
        statics.update(self.user_dates[self.uid]["unicron"])
        statics["photo"] = f"img/unicorn/levels/{str(lvl_actual)}.jpg"
        statics["total_ref_to_up"] = self.total_ref_necesary_(lvl_actual)
        return statics

    def search_info(self, lvl):
        """
        "name"
        "diary"
        "bonus"
        "foot_necesary"
        "foot_to_up"
        "bonus_tasks"
        "new_uni"

        """
        key = f"lvl_{str(lvl)}"
        return self.lvl_dates[key]


class info:
    def __init__(self, route=None, text=None, keyboard=None):

        self.route = route
        self.text = text
        self.keyboard = keyboard

    def back_(self):
        if self.route == "/main":
            return self.route
        back = self.route.split("/")
        back.pop()
        back = "/".join(back)
        return menu_system[back]

    def custom(self, lg):
        self.text = my_text_db.translate(self.text, lg)
        if self.keyboard:
            for x in range(len(self.keyboard)):
                for y in range(len(self.keyboard[x])):
                    try:
                        self.keyboard[x][y].text = my_text_db.translate(
                            self.keyboard[x][y].text, lg
                        )
                    except Exception as e:
                        print_to_web(e)


class User_db:
    def __init__(self, route=None):

        self.route = route


color_crypto = {
    "BTC": "🟠",
    "ETH": "🔵",
    "BNB": "🟠",
    "UNI": "🔴",
    "SHIB": "🔴",
    "DOGE": "🟡",
    "TRX": "🔴",
    "LTC": "🔵",
    "MATIC": "🟣",
    "ADA": "⚪️",
    "SOL": "🟣",
    "XRP": "⚫️",
    "TON": "🔵",
    "BCH": "🟢",
    "FLOKI": "🟠",
    "SUSHI": "🟣",
    "CAKE": "🟠",
    "DASH": "🔵",
}


menu_system = {
    "/main/gift": info(
        "/main/gift",
        "Thank you for joining!!.Claim your welcome bonus now.",
        [
            [Button.inline("🎁 Get Gift", data=b"get_initgift")],
        ],
    ),
    "/main/gift/unauthorized_gift": info(
        "/main/gift/unauthorized_gift",
        "‼️ You must have at least 3 Referral to Claim this Gift.",
        [
            [Button.inline("🔖 Invite Now", data=b"initgift_invite")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/authorized_gift": info(
        "/main/authorized_gift",
        "👛 You received 0.05 UNI in your Wallet.",
        [
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    
    # Suscripcion
    
    "/sub": info(
        "/main",
        'Join our <a href="http://t.me/uniswapnew">channel</a> and <a href="http://t.me/uniswaptips">chat</a> to stay tuned for new features and other updates from <a href="http://t.me/uniswapbot">UniSwap Bot</a>.',
        [
            [
                Button.url("UniSwap News", "http://t.me/UniSwapNew"),
                Button.url("UniSwap Chat", "http://t.me/uniswaptips"),
            ],
            [Button.inline("✅ I`ve joined,Continue>", data=b"check_sub")],
        ],
    ),
    # Main menu
    "/main": info(
        "/main",
        '👛 Receive, send, store, play and win with cryptocurrencies at any time. <a href="https://t.me/UniSwapNew/18">Learn more ›</a>\n\nJoin <a href="http://t.me/UniSwapNew">our channel</a> and <a href="http://t.me/UniSwaptips">our chat</a>.',
        [
            [
                Button.inline("👛 Wallet", data=b"wallet"),
                # Button.inline("💠 Services", data=b"services"),
                Button.inline("🦄 Unicorn", data=b"unicorn"),
            ],
            [
                Button.inline("🔖 Promotion", data=b"promotion"),
                Button.inline("🦋 Stake", data=b"stake"),
            ],
            [
                Button.inline("🍥 Free UNI", data=b"free_uni"),
                Button.inline("📈 Grid Trading", data=b"grid"),
                # Button.inline("📊 Infinity Grid", data=b"grid"),
                # Button.inline("🎰 Casino", data=b"casino"),
            ],
            [
                Button.inline("👾 NFTs", data=b"nfts"),
                Button.inline("🎰 Casino", data=b"casino"),
            ],
            [
                Button.inline("🎈Airdrop", data=b"tokens"),
                Button.inline("⚙️ Settings", data=b"settings"),
            ],
        ],
    ),
    # Grid
    "/main/grid": info(
        "/main/grid",
        "📊 Manage, Copy and Create new Grid Trading Bot.",
        [
            [Button.inline("📈 New Grid BOT", data=b"new_grid")],
            [
                Button.inline("🔖 Copy Grid BOT", data=b"copy_grid"),
                Button.inline("⚙️ Manage Grid BOT", data=b"manage_gd"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/new_grid_cripto": info(
        "/main/grid/new_grid_cripto",
        "📈 Select the coin your Trading Grid Bot will operate.",
        [
            [
                Button.inline(f"{color_crypto['BTC']}BTC/USDT", data=b"BTC_crypgrid"),
                Button.inline(f"{color_crypto['ETH']}ETH/USDT", data=b"ETH_crypgrid"),
            ],
            [
                Button.inline(f"{color_crypto['BNB']}BNB/USDT", data=b"BNB_crypgrid"),
                Button.inline(f"{color_crypto['UNI']}UNI/USDT", data=b"UNI_crypgrid"),
            ],
            [
                Button.inline(
                    f"{color_crypto['SHIB']}SHIB/USDT", data=b"SHIB_crypgrid"
                ),
                Button.inline(
                    f"{color_crypto['DOGE']}DOGE/USDT", data=b"DOGE_crypgrid"
                ),
            ],
            [
                Button.inline(f"{color_crypto['TRX']}TRX/USDT", data=b"TRX_crypgrid"),
                Button.inline(f"{color_crypto['LTC']}LTC/USDT", data=b"LTC_crypgrid"),
            ],
            [
                Button.inline(
                    f"{color_crypto['MATIC']}MATIC/USDT", data=b"MATIC_crypgrid"
                ),
                Button.inline(f"{color_crypto['ADA']}ADA/USDT", data=b"ADA_crypgrid"),
            ],
            [
                Button.inline(f"{color_crypto['SOL']}SOL/USDT", data=b"SOL_crypgrid"),
                Button.inline(f"{color_crypto['XRP']}XRP/USDT", data=b"XRP_crypgrid"),
            ],
            [
                Button.inline(f"{color_crypto['TON']}TON/USDT", data=b"TON_crypgrid"),
                Button.inline(f"{color_crypto['BCH']}BCH/USDT", data=b"BCH_crypgrid"),
            ],
            [
                Button.inline(
                    f"{color_crypto['FLOKI']}FLOKI/USDT", data=b"FLOKI_crypgrid"
                ),
                Button.inline(
                    f"{color_crypto['SUSHI']}SUSHI/USDT", data=b"SUSHI_crypgrid"
                ),
            ],
            [
                Button.inline(
                    f"{color_crypto['CAKE']}CAKE/USDT", data=b"CAKE_crypgrid"
                ),
                Button.inline(
                    f"{color_crypto['DASH']}DASH/USDT", data=b"DASH_crypgrid"
                ),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/new_grid_cripto/new_grid_am": info(
        "/main/grid/new_grid_cripto/new_grid_am",
        "$cripto/USDT\n$cripto_info\n\n• Indicate the Amount of USDT your Grid Bot will use to Trade:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/grid/new_grid_cripto/new_grid_am/err": info(
        "/main/grid/new_grid_cripto/new_grid_am/err",
        "‼️ Wrong format, just numbers!",
        [[Button.inline("OK", data=b"back")]],
    ),
    "/main/grid/new_grid_cripto/new_grid_am_ok": info(
        "/main/grid/new_grid_cripto/new_grid_am_ok",
        "$cripto_info\n\nSelect an option to continue.",
        [
            [
                Button.inline("🧠 Create Automatic ", data=b"create_auto_grid"),
                Button.inline("🧑‍💻 Create Manual", data=b"create_manual_grid"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/new_grid_cripto/new_grid_am_ok/automatic": info(
        "/main/grid/new_grid_cripto/new_grid_am_ok/automatic",
        "📊 Your new Trading Grid Bot is operational and working.",
        [
            [Button.inline("Manage", data=b"manage_done")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/new_grid_cripto/new_grid_am_ok/manual": info(
        "/main/grid/new_grid_cripto/new_grid_am_ok/manual",
        "Set up your new Trading Grid.",
        [
            [
                Button.inline("🕹️ Leverage", data=b"leverage_man_grid"),
                Button.inline("🔆 Daily Orders", data=b"dailyords_man_grid"),
            ],
            [
                Button.inline("🔴 Stop Loss", data=b"sl_man_grid"),
                Button.inline("🟢 Take Profit", data=b"tp_man_grid"),
            ],
            [Button.inline("✅ I'm done, Create...", data=b"done_create_man_gd")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/leverage": info(
        "/main/grid/manual/leverage",
        "The risk of using leverage is extremely high, please be careful.\n\n🕹️ Select the leverage your Grid Bot.",
        [
            [
                Button.inline("0x", data=b"lev_0{0,0"),
                Button.inline("5x", data=b"lev_5{0,1"),
                Button.inline("10x", data=b"lev_10{0,2"),
            ],
            [
                Button.inline("15x", data=b"lev_15{1,0"),
                Button.inline("20x", data=b"lev_20{1,1"),
                Button.inline("25x", data=b"lev_25{1,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/day_ords": info(
        "/main/grid/manual/day_ords",
        "🔆  Set a maximum and minimum daily orders.",
        [
            [
                Button.inline("Minimum Orders", data=b"minords_man_grid"),
                Button.inline("Maximum Orders", data=b"maxords_man_grid"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/day_ords/min_ords": info(
        "/main/grid/manual/day_ords/min_ords",
        "🔅 Select the minimum number of orders your Grid Bot will process per day",
        [
            [
                Button.inline("1", data=b"minords_1{0,0"),
                Button.inline("5", data=b"minords_5{0,1"),
                Button.inline("10", data=b"minords_10{0,2"),
            ],
            [
                Button.inline("15", data=b"minords_15{1,0"),
                Button.inline("20", data=b"minords_20{1,1"),
                Button.inline("25", data=b"minords_25{1,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/day_ords/max_ords": info(
        "/main/grid/manual/day_ords/max_ords",
        "🔅 Select the maximum number of orders your Grid Bot will process per day.",
        [
            [
                Button.inline("25", data=b"maxords_25{0,0"),
                Button.inline("30", data=b"maxords_30{0,1"),
                Button.inline("35", data=b"maxords_35{0,2"),
            ],
            [
                Button.inline("40", data=b"maxords_40{1,0"),
                Button.inline("45", data=b"maxords_45{1,1"),
                Button.inline("50", data=b"maxords_50{1,2"),
            ],
            [
                Button.inline("55", data=b"maxords_55{2,0"),
                Button.inline("60", data=b"maxords_60{2,1"),
                Button.inline("65", data=b"maxords_65{2,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/sl": info(
        "/main/grid/manual/sl",
        "🔴 When you reach a loss of $sl your Grid Bot will stop automatically.",
        [
            [
                Button.inline("1%", data=b"sl_1{0,0"),
                Button.inline("5%", data=b"sl_5{0,1"),
                Button.inline("10%", data=b"sl_10{0,2"),
            ],
            [
                Button.inline("15%", data=b"sl_15{1,0"),
                Button.inline("25%", data=b"sl_25{1,1"),
                Button.inline("30%", data=b"sl_30{1,2"),
            ],
            [
                Button.inline("35%", data=b"sl_35{2,0"),
                Button.inline("40%", data=b"sl_40{2,1"),
                Button.inline("55%", data=b"sl_55{2,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manual/tp": info(
        "/main/grid/manual/tp",
        "🟢 When you reach a profit of $tp your Grid Bot will stop automatically.",
        [
            [
                Button.inline("5%", data=b"tp_5{0,0"),
                Button.inline("15%", data=b"tp_15{0,1"),
                Button.inline("20%", data=b"tp_20{0,2"),
            ],
            [
                Button.inline("25%", data=b"tp_25{1,0"),
                Button.inline("35%", data=b"tp_35{1,1"),
                Button.inline("40%", data=b"tp_40{1,2"),
            ],
            [
                Button.inline("70%", data=b"tp_70{2,0"),
                Button.inline("80%", data=b"tp_80{2,1"),
                Button.inline("90%", data=b"tp_90{2,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/done": info(
        "/main/grid/done",
        "✅ I'm done, Create...",
        [
            [Button.inline("Manage", data=b"manage_done")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage": info(
        "/main/grid/manage", "⚙️ Manage and configure your Grid Trading"
    ),
    "/main/grid/manage_0": info(
        "/main/grid/manage_0", "😔 Actualmente no dispones de ningún Grid Trading Bot."
    ),
    "/main/grid/manage/bot": info(
        "/main/grid/manage/bot",
        "$cripto/USDT\n≈$cripto_in_usd USDT\n\n🕹 Leverage:\n• $leverage x\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📊 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Buys - $shorts Sales)\n\n💰 Investiment\n• $invest USDT\n\n🔆 Profit today:\n• $profit_today% ≈ $profit_today_brute USDT\n\n👛 Total profit:\n• $profit_total% ≈ $profit_total_brute USDT\n\n〽️ APR (Annualized)\n•$apr% ≈ $apr_brute USDT",
        [
            [Button.inline("⚙️ Manage", data=b"manage_botgd")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf": info(
        "/main/grid/manage/bot/conf",
        "$cripto/USDT\n\n• Manage you Grid Bot.",
        [
            [Button.inline("〽️ Compartir", data=b"share_botgd")],
            [
                Button.inline("🔴 Stop Loss", data=b"botgd_sl"),
                Button.inline("🟢 Take Profit", data=b"botgd_tp"),
            ],
            [
                Button.inline("🕹️ Leverage", data=b"leverage_botgd"),
                Button.inline("‼️ Delete", data=b"delete_botgd"),
            ],
            [
                Button.inline("📊 Increase Funds", data=b"increase_botgd"),
                Button.inline("📉 Decrease Funds", data=b"decrease_botgd"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/increase_found": info(
        "/main/grid/manage/bot/conf/increase_found",
        "• Investment $invest\n\n📊 Send the amount you will increase:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/grid/manage/bot/conf/decrease_found": info(
        "/main/grid/manage/bot/conf/decrease_found",
        "• Investment $invest\n\n📉 Send the amount you will decrease:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/grid/manage/bot/conf/leverage": info(
        "/main/grid/manage/bot/conf/leverage",
        "The risk of using leverage is extremely high, please be careful.\n\n🕹️ Select the leverage your Grid Bot.",
        [
            [
                Button.inline("0x", data=b"lvgmanag_0{0,0"),
                Button.inline("5x", data=b"lvgmanag_5{0,1"),
                Button.inline("10x", data=b"lvgmanag_10{0,2"),
            ],
            [
                Button.inline("15x", data=b"lvgmanag_15{1,0"),
                Button.inline("20x", data=b"lvgmanag_20{1,1"),
                Button.inline("25x", data=b"lvgmanag_25{1,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/sl": info(
        "/main/grid/manage/bot/conf/sl",
        "🔴 When you reach a loss of $sl your Grid Bot will stop automatically.",
        [
            [
                Button.inline("1%", data=b"slmanag_1{0,0"),
                Button.inline("5%", data=b"slmanag_5{0,1"),
                Button.inline("10%", data=b"slmanag_10{0,2"),
            ],
            [
                Button.inline("15%", data=b"slmanag_15{1,0"),
                Button.inline("25%", data=b"slmanag_25{1,1"),
                Button.inline("30%", data=b"slmanag_30{1,2"),
            ],
            [
                Button.inline("35%", data=b"slmanag_35{2,0"),
                Button.inline("40%", data=b"slmanag_40{2,1"),
                Button.inline("55%", data=b"slmanag_55{2,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/tp": info(
        "/main/grid/manage/bot/conf/tp",
        "🟢 When you reach a profit of $tp your Grid Bot will stop automatically.",
        [
            [
                Button.inline("5%", data=b"tpmanag_5{0,0"),
                Button.inline("15%", data=b"tpmanag_15{0,1"),
                Button.inline("20%", data=b"tpmanag_20{0,2"),
            ],
            [
                Button.inline("25%", data=b"tpmanag_25{1,0"),
                Button.inline("35%", data=b"tpmanag_35{1,1"),
                Button.inline("40%", data=b"tpmanag_40{1,2"),
            ],
            [
                Button.inline("70%", data=b"tpmanag_70{2,0"),
                Button.inline("80%", data=b"tpmanag_80{2,1"),
                Button.inline("90%", data=b"tpmanag_90{2,2"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/delete": info(
        "/main/grid/manage/bot/conf/delete",
        "‼️ You are about to delete your Grid Bot. Is that correct?",
        [
            [Button.inline("Yes, delete the bot", data=b"yes_deletebot")],
            [Button.inline("No!", data=b"del_no")],
            [Button.inline("Nope, nevermind", data=b"del_nope")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/deleted": info(
        "/main/grid/manage/deleted",
        "‼️ You have deleted your Grid Bot.",
        [
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/share": info(
        "/main/grid/manage/bot/conf/share",
        "• You will earn 15% of the profits your copiers receive.\n\n〽️ Launch your Grid Bot and win.",
        [
            [
                Button.inline("🚀 Launch", data=b"share_launch"),
                Button.inline("📊 Statistics", data=b"share_statics"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/manage/bot/conf/share/launch": info(
        "/main/grid/manage/bot/conf/share/launch",
        "🚀 Congratulations, your Grid Bot is now public and anyone can copy it.",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/grid/manage/bot/conf/share/statics": info(
        "/main/grid/manage/bot/conf/share/statics",
        "👤 Copiers:\n• $copiers People\n\n👥 Copiers out:\n• $copiers_out People\n\n🔅 Earned yesterday:\n• $earn_yest USDT\n\n💰 Total earned:\n•  $earn_total USDT",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/grid/copy": info(
        "/main/grid/copy",
        "$cripto/USDT\n≈ $cripto_in_usd USDT\n\n🕹 Leverage:\n• $leverage x\n\n🔴 Stop loss\n• $SL%\n\n🟢 Take profit\n• $TP%\n\n📊 Orders today:\n• +$orders_today Orders\n\n📊 Total orders:\n• $orders_total Orders ($longs Buys - $shorts Sales)\n\n🔆 Profit today:\n• $profit_today %\n\n👛 Total profit:\n• $profit_total %\n\n🚀 Days online:\n • $days_online Days\n\n〽️ APR (Annualized)\n•$apr% ≈ $apr_brute USDT",
        [
            [Button.inline("〽️ Copy Grid Bot", data=b"copy_bot")],
            [
                Button.inline("«", data=b"ant_copy"),
                Button.inline("» ", data=b"post_copy"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/grid/copy/copy_sel_am": info(
        "/main/grid/copy/copy_sel_am",
        "〽️ Send the amount in USDT that you want to add to your new Grid Bot:",
        [[Button.text("🚫 Cancel", resize=True, single_use=True)]],
    ),
    "/main/grid/copy/copy_sel_amerr": info(
        "/main/grid/copy/copy_sel_amerr",
        "‼️ Wrong format, just numbers!",
        [[Button.inline("OK", data=b"back")]],
    ),
    "/main/grid/copy/copy_sel_amok": info(
        "/main/grid/copy/copy_sel_amok",
        "📊 Your new Grid Trading Bot is operational and working.",
        [[Button.inline("< Back", data=b"back")]],
    ),
    # Casino
    "/main/casino": info(
        "/main/casino",
        "🕹️ Select a Game.",
        [
            [
                Button.inline("🎰 Slots", data=b"slot_machine"),
                Button.inline("🎲️ Dice", data=b"dice"),
            ],
            [
                Button.inline("🏀 Basket", data=b"basket"),
                Button.inline("🎯 Darts", data=b"darts"),
            ],
            [
                Button.inline("🎳️ Bowling", data=b"bowlling"),
                Button.inline("⚽️ Football", data=b"football"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    # Slots
    "/main/casino/slots": info(
        "/main/casino/slots",
        "🎰️ Spin and knock out a winning combination.\n\nSelect a Coin",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/slots/rules": info(
        "/main/casino/slots/rules",
        '🎰️ Slots rules.\n\nSpin and knock out a winning combination:\n\n7️⃣7️⃣7️⃣ — 20x\n🍇🍇🍇 — 10x\n🍋🍋🍋 — 5x\n🍸🍸🍸 — 3x\n7️⃣7️⃣ — 1x\n🍇🍇 — 0.5x\n🍋🍋 — 0.25x\n🍸🍸 — 0.25x\n\n<b>Bet Size:</b>\n• <i>Min. bet size: 0.1 USD\n• Max bet size: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations in the emoji is determined by </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can affect his choice, except your luck.</i>\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/slots/game": info(
        "/main/casino/slots/game",
        "Send a bet amount and choose the outcome:",
        [
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
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("🔄 Spin", data=b"play"),
            ],
        ],
    ),
    # Dado
    "/main/casino/dado": info(
        "/main/casino/dado",
        "🎲️ Roll dice and try your luck.\n\nSelect a Coin:",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/dado/rules": info(
        "/main/casino/dado/rules",
        '🎲️️ Dice<b> </b>rules.\n\nRoll the die and guess the lucky number, the interval, or an even/odd number. If you guessed it, you win!\n\n<b>Multipliers:</b>\n• <i>Exact number: 5x\n• Interval: 2.7x\n• Even/Odd number: 1.8x</i>\n\n<b>Bet Size:</b>\n• <i>Min. bet size: 0.1 USD\n• Max bet size: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations in the emoji is determined by </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can affect his choice, except your luck.</i>\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/dado/game": info(
        "/main/casino/dado/game",
        "Send a bet amount and choose the outcome:",
        [
            [Button.inline("⚙️", data=b"bet_size")],
            [
                Button.inline("1", data=b"dice_1{1,0"),
                Button.inline("2", data=b"dice_2{1,1"),
                Button.inline("3", data=b"dice_3{1,2"),
                Button.inline("4", data=b"dice_4{1,3"),
                Button.inline("5", data=b"dice_5{1,4"),
                Button.inline("6", data=b"dice_6{1,5"),
            ],
            [
                Button.inline("1-2", data=b"dice_1.5{2,0"),
                Button.inline("3-4", data=b"dice_3.5{2,1"),
                Button.inline("5-6", data=b"dice_5.5{2,2"),
            ],
            [
                Button.inline("Even", data=b"dice_even{3,0"),
                Button.inline("Odd", data=b"dice_odd{3,1"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("🎲️ Roll", data=b"play"),
            ],
        ],
    ),
    "/main/casino/dado/game/er": info(
        "/main/casino/dado/game/er",
        "❌ You have not chosen an outcome for a bet",
        [[Button.inline("Ok", data=b"no_apuesta")]],
    ),
    "/main/casino/dado/game/bet_size": info(
        "/main/casino/dado/game/bet_size",
        "💶Send a bet amount and choose the outcome:",
        [
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
        ],
    ),
    # Basket
    "/main/casino/basketball": info(
        "/main/casino/basketball",
        "🏀 Shoot the ball into the basket to win.\n\nSelect a Coin:",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/basketball/rules": info(
        "/main/casino/basketball/rules",
        '🏀 Basket rules.\n\nShoot the ball into the basket to win. The size of the winning depends on the quality of the shot!\n\n<b>Multipliers:</b>\n• <i>Splash shot — 2.5x\n• Shot — 1.5x</i>\n\nBet Size:\n• <i>Min. bet size: 0.1 USD\n• Max bet size: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations in the emoji is determined by </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can affect his choice, except your luck.</i>\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/basketball/game": info(
        "/main/casino/basketball/game",
        "Send or select a size for your bet:",
        [
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
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("🏀 Shoot", data=b"play"),
            ],
        ],
    ),
    # Dardos
    "/main/casino/dardos": info(
        "/main/casino/dardos",
        "🎯 Shoot dart into the target to win.\n\nSelect a Coin:",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/dardos/rules": info(
        "/main/casino/dardos/rules",
        '🎯 Darts rules.\n\nShoot the dart into the center of the target to win. The size of the winning depends on the quality of the shot!\n\n<b>Multipliers:</b>\n<i>• Into the centre — 3x\n• 1 circle from the centre — 1.5x\n• 2 circle from the centre — 1x</i>\n\n<b>Bet size:</b>\n<i>• Minimum bet: 0.1 USD\n• Maximum bet: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations in the emoji is determined by </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can affect his choice, except your luck.</i>\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/dardos/game": info(
        "/main/casino/dardos/game",
        "Send or select a size for your bet:",
        [
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
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("🎯 Shoot", data=b"play"),
            ],
        ],
    ),
    # Bolos
    "/main/casino/bolos": info(
        "/main/casino/bolos",
        "🎳️ Knock out a strike and win x5 of the bet.\n\nSelect a Coin:",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/bolos/rules": info(
        "/main/casino/bolos/rules",
        '🎳 Bowling<b> </b>rules.\n\nKnock down all pins (strike) and win x5 of your bet!\n\n<b>Multipliers:</b>\n• <i>Strike — 5x\n• One pin left — 0.5x</i>\n\n<b>Betting Size:</b>\n• <i>Min bet size: 0.1 USD\n• Max bet size: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations falling out in the emoji is determined by the </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can influence its choice, except your luck</i>.\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/bolos/game": info(
        "/main/casino/bolos/game",
        "Send or select a size for your bet:",
        [
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
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("🎳️ Throw", data=b"play"),
            ],
        ],
    ),
    # Football
    "/main/casino/football": info(
        "/main/casino/football",
        "⚽️ Score a goal and win x1.5 of the bet.\n\nSelect a Coin:",
        [
            [
                Button.inline("TON", data=b"TON_crypcas"),
                Button.inline("UNI", data=b"UNI_crypcas"),
            ],
            [
                Button.inline("LTC", data=b"LTC_crypcas"),
                Button.inline("BNB", data=b"BNB_crypcas"),
            ],
            [
                Button.inline("ETH", data=b"ETH_crypcas"),
                Button.inline("BTC", data=b"BTC_crypcas"),
            ],
            [
                Button.inline("TRX", data=b"TRX_crypcas"),
                Button.inline("USDT", data=b"USDT_crypcas"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Rules >", data=b"rules"),
            ],
        ],
    ),
    "/main/casino/football/rules": info(
        "/main/casino/football/rules",
        '⚽ Football rules.\n\nThere are more winning combinations than losing ones!\n\n<b>Multipliers:</b>\n<i>Score a goal and win x1.5 of the bet.</i>\n\n<b>Betting Size:</b>\n• <i>Min bet size: 0.1 USD\n• Max bet size: 500 USD</i>\n\n<b>Provably fair:</b>\n• <i>The outcome of the combinations falling out in the emoji is determined by the </i><i><a href="http://core.telegram.org/api/dice">Telegram API</a></i><i>, no one can influence its choice, except your luck</i>.\n\n🍀 <b>Have fun playing</b>!',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/casino/football/game": info(
        "/main/casino/football/game",
        "Send or select a size for your bet:",
        [
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
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("⚽️ Kick", data=b"play"),
            ],
        ],
    ),
    # WALLET
    "/main/wallet": info(
        "/main/wallet",
        '👛 <b>Wallet</b>\n\n• <i><a href="https://tether.to/">Tether</a></i>: $usdt USDT\n\n• <i><a href="https://ton.org/">Toncoin</a></i><i>: </i>$ton TON\n\n• <i><a href="https://notco.in/">Notcoin</a></i><i>: </i>$not_ NOT\n\n• <i><a href="https://bitcoin.org/">Bitcoin</a></i>:$btc BTC\n\n• <i><a href="https://litecoin.org/">Litecoin</a></i>: $ltc LTC\n\n• <i><a href="https://ethereum.org/">Ethereum</a></i>: $eth ETH\n\n• <i><a href="https://binance.org/">Binance</a></i>: $bnb BNB\n\n• <i><a href="https://uniswap.org/">Uniswap</a></i>: $uni UNI\n\n• <i><a href="https://tron.network/">TRON</a></i>: $tron TRX\n\n• <i><a href="https://www.centre.io/usdc">USD Coin</a></i>: $usdc USDC\n\n≈ $uni_total UNI ($uni_total_to_usd)',
        [
            [
                Button.inline("👛 Deposit", data=b"wall_dep"),
                Button.inline("📤 Withdraw", data=b"wall_with"),
            ],
            [
                Button.inline("💱 Swap", data=b"wall_swap"),
            ],
            [
                Button.inline("🔖 Fees & Limits", data=b"wall_fees"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/wallet/deposit": info(
        "/main/wallet/deposit",
        "👛 Choose a cryptocurrency you want to deposit.",
        [
            [
                Button.inline("USDT", data=b"USDT_cr"),
                Button.inline("TRX", data=b"TRX_cr"),
            ],
            [
                Button.inline("BNB", data=b"BNB_cr"),
                Button.inline("BTC", data=b"BTC_cr"),
            ],
            [
                Button.inline("LTC", data=b"LTC_cr"),
                Button.inline("ETH", data=b"ETH_cr"),
            ],
            [
                Button.inline("TON", data=b"TON_cr"),
                Button.inline("NOT", data=b"NOT_cr"),
            ],
            [Button.inline("USDC", data=b"USDC_cr")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/deposit/net": info(
        "/main/wallet/deposit/net",
        "👛 Choose a network to deposit $cripto.",
        [
            [
                Button.inline("TRC20", data=b"TRC20_net"),
                Button.inline("TON", data=b"TON_net"),
            ],
            [
                Button.inline("ERC20", data=b"ERC20_net"),
                Button.inline("BEP20", data=b"BEP20_net"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/deposit/amount": info(
        "/main/wallet/deposit/amount",
        "👛 Coin ≈ $cripto_info\n\n• Choose the amount to deposit.",
        [
            [
                Button.inline("-", data=b"dep-"),
                Button.inline("0", data=b"dep_bal"),
                Button.inline("+", data=b"dep+"),
            ],
            [Button.inline("Minimum", data=b"dep_min")],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("📥 Deposit", data=b"dep_conf"),
            ],
        ],
    ),
    "/main/wallet/deposit/amount/but_bal": info(
        "/main/wallet/deposit/amount/but_bal",
        "USDT - 5\n\nUSDC - 5\n\nTRX - 25\n\nBTC - 0.000085\n\nTON - 2\n\nBNB - 0.0085\n\nETH - 0.0015\n\nLTC - 0.05",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/wallet/withdraw": info(
        "/main/wallet/withdraw",
        "📤 Choose a cryptocurrency you want to withdraw.",
        [
            [
                Button.inline("USDT", data=b"USDT_with-cr"),
                Button.inline("TRX", data=b"TRX_with-cr"),
            ],
            [
                Button.inline("BNB", data=b"BNB_with-cr"),
                Button.inline("BTC", data=b"BTC_with-cr"),
            ],
            [
                Button.inline("LTC", data=b"LTC_with-cr"),
                Button.inline("ETH", data=b"ETH_with-cr"),
            ],
            [
                Button.inline("TON", data=b"TON_with-cr"),
                Button.inline("NOT", data=b"NOT_with-cr"),
            ],
            [Button.inline("USDC", data=b"USDC_with-cr")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/withdraw/net": info(
        "/main/wallet/withdraw/net",
        "👛 Choose a network to withdraw $cripto.",
        [
            [
                Button.inline("TRC20", data=b"TRC20_with-net"),
                Button.inline("TON", data=b"TON_with-net"),
            ],
            [
                Button.inline("ERC20", data=b"ERC20_with-net"),
                Button.inline("BEP20", data=b"BEP20_with-net"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/withdraw/address": info(
        "/main/wallet/withdraw/address",
        "Network: <b>$cripto_info</b> ‼️\n\n📤 Enter a wallet address to send $cripto.",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/wallet/withdraw/address/err": info(
        "/main/wallet/withdraw/address/err",
        "😔 Apparently the address entered is incorrect. Please try again.",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/wallet/withdraw/amount": info(
        "/main/wallet/withdraw/amount",
        "📤 Coin ≈ $cripto_info\n\n• Send the amount to Withdraw.",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/wallet/withdraw/confirm": info(
        "/main/wallet/withdraw/confirm",
        '👛 <b>Confirmation</b>\n\n<b>Network</b>: $net_info ‼️\n<b>Address</b>: <a href="$address">$address_abv</a>\n\n• <b>You send</b>: $send_am $cripto\n\n• <b>Fee</b>: $fee_am $cripto\n\n• <b>Total amount</b>: $total_am $cripto\n\nAre you sure you want to send these coins to the address <a href="$address">$address_abv</a>?',
        [
            [
                Button.inline("✅ Confirm", data=b"with-confirm_fin"),
                Button.inline(" 🚫 Cancel", data=b"with-cancel"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/withdraw/wait": info(
        "/main/wallet/withdraw/wait",
        '👛 <b>Confirmation</b>\n\n<b>Network</b>: $net_info ‼️\n<b>Address</b>: <a href="$address">$address_abv</a>\n\n• <b>You send</b>: $send_am $cripto\n\n• <b>Fee</b>: $fee_am $cripto\n\n• <b>Total amount</b>: $total_am $cripto\n\n💸 Waiting for sending.',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/wallet/complete": info(
        "/main/wallet/complete",
        '👛 <b>Confirmation</b>\n\n<b>Network</b>: $net_info ‼️\n<b>Address</b>: <a href="$address">$address_abv</a>\n\n• <b>You send</b>: $send_am $cripto\n\n• <b>Fee</b>: $fee_am $cripto\n\n• <b>Total amount</b>: $total_am $cripto\n\n✅ Withdrawal was sent.',
        [
            [Button.url("View Transaction", "http://t.me/UniSwapNew")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/withdraw/amount/sel_amerr": info(
        "/main/wallet/withdraw/amount/sel_amerr",
        "‼️ Wrong format, just numbers!",
        [[Button.inline("OK", data=b"back")]],
    ),
    "/main/wallet/withdraw/amount/amerr": info(
        "/main/wallet/withdraw/amount/amerr",
        "Invalid amount",
        [[Button.inline("OK", data=b"back")]],
    ),
    "/main/wallet/fees": info(
        "/main/wallet/fees",
        "🔎Choose a cryptocurrency to view fees and limits.",
        [
            [
                Button.inline("USDT", data=b"USDT_fee-cr"),
                Button.inline("TRX", data=b"TRX_fee-cr"),
            ],
            [
                Button.inline("BNB", data=b"BNB_fee-cr"),
                Button.inline("BTC", data=b"BTC_fee-cr"),
            ],
            [
                Button.inline("LTC", data=b"LTC_fee-cr"),
                Button.inline("ETH", data=b"ETH_fee-cr"),
            ],
            [
                Button.inline("TON", data=b"TON_fee-cr"),
                Button.inline("NOT", data=b"NOT_fee-cr"),
            ],
            [Button.inline("USDC", data=b"USDC_fee-cr")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/fees/usdt-net": info(
        "/main/wallet/fees/usdt-net",
        "🔎Choose a network to view fees and limits for USDT.",
        [
            [
                Button.inline("TRC20", data=b"TRC20_fee-net"),
                Button.inline("TON", data=b"TON_fee-net"),
            ],
            [
                Button.inline("ERC20", data=b"ERC20_fee-net"),
                Button.inline("BEP20", data=b"BEP20_fee-net"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/fees/usdc-net": info(
        "/main/wallet/fees/usdc-net",
        "🔎Choose a network to view fees and limits for USDC",
        [
            [
                Button.inline("ERC20", data=b"ERC20_fee-net"),
                Button.inline("BEP20", data=b"BEP20_fee-net"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/fees/info": info(
        "/main/wallet/fees/info",
        "👀 Here you can view fees and limits for $cripto in the network $cripto_info.\n\n•\xa0Withdrawal fee for $cripto –  $fee_with $cripto\n\n•\xa0For withdrawals – from $min_with $cripto",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/wallet/fees/info2": info(
        "/main/wallet/fees/info2",
        "👀 Here you can view fees and limits for $cripto in the network $cripto_info.\n\n•\xa0Withdrawal fee for $cripto –  $fee_with $cripto\n\n\n•\xa0For deposits – from $min_dep $cripto\n\n•\xa0For withdrawals – from $min_with $cripto",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/wallet/swap": info(
        "/main/wallet/swap",
        "💱 Select an option to continue.",
        [
            [
                Button.inline("Referrals", data=b"swap-referrals"),
                Button.inline("Coin", data=b"swap-coin"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/swap/ref": info(
        "/main/wallet/swap/ref",
        "<b>Referrals</b> ≈ <code>$ref</code> Ref\n\n• Indicate the amount of referrals you want to exchange for USDT.",
        [[[Button.text("🚫 Cancel", resize=True)]]],
    ),
    "/main/wallet/swap/ref0": info(
        "/main/wallet/swap/ref0",
        "‼️ You do not have enough referrals to exchange for USDT.",
        [
            [Button.inline("🤑 Start Earning", data=b"swap-earn")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/swap/ref/+0": info(
        "/main/wallet/swap/ref/+0",
        "💱 Swap!",
        [
            [Button.inline("$ref Ref - ≈ - $ref_swap USDT", data=b"swap-ref_select")],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("✅ Exchange Now »", data=b"swap-exchange_refs"),
            ],
        ],
    ),
    "/main/wallet/swap/ref/+0/exchange": info(
        "/main/wallet/swap/ref/+0/exchange",
        "👛 Coins Received. You received <b>$ref_swap USDT</b>",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/wallet/swap/coin1": info(
        "/main/wallet/swap/coin1",
        "💱 Select a Coin  to Continue.",
        [
            [
                Button.inline("USDT", data=b"USDT_swap-cr"),
                Button.inline("TRX", data=b"TRX_swap-cr"),
            ],
            [
                Button.inline("BNB", data=b"BNB_swap-cr"),
                Button.inline("BTC", data=b"BTC_swap-cr"),
            ],
            [
                Button.inline("LTC", data=b"LTC_swap-cr"),
                Button.inline("ETH", data=b"ETH_swap-cr"),
            ],
            [
                Button.inline("TON", data=b"TON_swap-cr"),
                Button.inline("NOT", data=b"NOT_swap-cr"),
            ],
            [Button.inline("USDC", data=b"USDC_swap-cr")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/swap/coin1/coin2": info(
        "/main/wallet/swap/coin1/coin2",
        "• $cripto ≈ ¿?\n\n💡 Select the currency you will exchange your <b>$cripto</b> for.",
        [
            [
                Button.inline("USDT", data=b"USDT_swap1-cr"),
                Button.inline("TRX", data=b"TRX_swap1-cr"),
            ],
            [
                Button.inline("BNB", data=b"BNB_swap1-cr"),
                Button.inline("BTC", data=b"BTC_swap1-cr"),
            ],
            [
                Button.inline("LTC", data=b"LTC_swap1-cr"),
                Button.inline("ETH", data=b"ETH_swap1-cr"),
            ],
            [
                Button.inline("TON", data=b"TON_swap1-cr"),
                Button.inline("NOT", data=b"NOT_swap1-cr"),
            ],
            [Button.inline("USDC", data=b"USDC_swap1-cr")],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/wallet/swap/coin1/coin2/am": info(
        "/main/wallet/swap/coin1/coin2/am",
        "• $cripto1 ≈ $cripto2\n\n💱 Send the amount of <b>$cripto1</b> you want to exchange for <b>$cripto2</b>.",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/wallet/swap/coin1/coin2/am/conf": info(
        "/main/wallet/swap/coin1/coin2/am/conf",
        "$cripto1_am $crypto1 - ≈ - $cripto2_am $crypto2",
        [
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("✅ Exchange Now »", data=b"swap_exchange"),
            ]
        ],
    ),
    "/main/ok": info(
        "/main/ok",
        "👛 Coins Received. You received <b>$amount $crypto</b>",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/wallet/swap/coin1/coin2/am/<am": info(
        "/main/wallet/swap/coin1/coin2/am/<am",
        "💡 You must send an amount equal to or greater than $amount.",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/wallet/swap/am_err": info(
        "/main/wallet/swap/am_err",
        "‼️ Incorrect Format. Only Numbers!",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/free_uni": info(
        "/main/free_uni",
        "💰 Select an option to Continue.",
        [
            [
                Button.inline("🔖 Tasks", data=b"f_uni-task"),
                Button.inline("〽️ Rewards", data=b"f_uni-rewards"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("👥 Referrals", data=b"f_uni-refer"),
            ],
        ],
    ),
    "/main/free_uni/referrals": info(
        "/main/free_uni/referrals",
        '💰 Invite <b>active users</b> and earn rewards in cryptocurrency.\n\nYou can earn these rewards by inviting users:\n\n• <b>5%</b> of what you earn from your referrals in the 🦄 <a href="https://t.me/UniSwapBot?start=Unicorn">Unicorn</a>.\n• <b>4%</b> for each coin that your referrals keep in 🦋 <a href="https://t.me/UniSwapBot?start=Stake">Stake</a>.\n• <b>5%</b> of the profits earned by your referrals in the 📈 <a href="https://t.me/UniSwapBot?start=GridTrading">Grid Trading</a>.\n•\xa0<b>15%</b> for every loss that your referrals have in the 🎰 <a href="https://t.me/UniSwapBot?start=Casino">Casino</a>.\n• <b>8%</b> of what your referrals spend on campaigns 🎈<a href="https://t.me/UniSwapBot?start=Airdrop">Airdrop</a>.\n•\xa0<b>10%</b> of the profits that your referrals earn by earning 🍥 <a href="https://t.me/UniSwapBot?start=FreeUNI">Free UNI</a>.\n\nUse these links below to invite new users:\n\n•\xa0t.me/UniSwapBot?start=r-$code\n•\xa0t.me/UniSwapBot?start=r-$code-Exchange\n• t.me/UniSwapBot?start=r-$code-GridTrading',
        [
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("♨️ Statistics", data=b"f_uni-statics"),
            ]
        ],
    ),
    "/main/free_uni/referrals/statics": info(
        "/main/free_uni/referrals/statics",
        '👥 <b>Referral</b> ~ <b>Statistics</b>.\n\n💰 Total earnings collected from your referrals:\n\n<b>$stake_perc%</b> 🦋 <a href="https://t.me/UniSwapBot?start=Stake">Stake</a> ≈ $stake_brute\n<b>$casino_perc%</b> 🎰 <a href="https://t.me/UniSwapBot?start=Casino">Casino</a> ≈ $casino_brute\n<b>$airdrop_perc%</b> 🎈<a href="https://t.me/UniSwapBot?start=Airdrop">Airdrop</a> ≈ $airdrop_brute\n<b>$uni_perc%</b> 🦄 <a href="https://t.me/UniSwapBot?start=Unicorn">Unicorn</a> ≈ $uni_brute\n<b>$free_perc%</b> 🍥 <a href="https://t.me/UniSwapBot?start=FreeUNI">Free UNI</a> ≈\xa0 $free_brute\n<b>$gt_perc%</b> 📈 <a href="https://t.me/UniSwapBot?start=GridTrading">Grid Trading</a> ≈ $gt_brute\n\n👥 <b>Referrals</b>:\n\n$ref_yest Referred yesterday.\n$ref_today Referred today.\n$ref_total Referred in total.',
        [
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("♻️ Refresh", data=b"f_uni-refresh"),
            ]
        ],
    ),
    "/main/free_uni/task": info(
        "/main/free_uni/task",
        "👛 Select an option to start Earning.",
        [
            [
                Button.inline("👁️ Messages", data=b"f_uni-msg"),
                Button.inline("💭 Groups", data=b"f_uni-group"),
            ],
            [
                Button.inline("🤖 Bots", data=b"f_uni-bots"),
                Button.inline("📣 Channels", data=b"f_uni-channels"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/free_uni/task/channel": info(
        "/main/free_uni/task/channel",
        "Text",
        [
            [Button.url("📢Join the Channel📢", "http://t.me/UniSwapNew")],
            [
                Button.inline("➡️Skip", data=b"f_uni-chan_skip"),
                Button.inline("✅Joined", data=b"f_uni-chan_joined"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/free_uni/task/channel/joined": info(
        "/main/free_uni/task/channels/joined",
        "✅ Promotion has been completed successfully",
    ),
    "/main/free_uni/task/channel/notjoined": info(
        "/main/free_uni/task/channel/notjoined", "Join frist"
    ),
    "/main/free_uni/task/channel/reward": info(
        "/main/free_uni/task/channel/reward",
        "✅ Promotion has been completed successfully\n⚡ Congratulations! You've earned $cripto_info",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/free_uni/task/group": info(
        "/main/free_uni/task/group",
        "Text",
        [
            [Button.url("📢Join the Group📢", "http://t.me/UniSwapNew")],
            [
                Button.inline("➡️Skip", data=b"f_uni-gr_skip"),
                Button.inline("✅Joined", data=b"f_uni-gr_joined"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/free_uni/task/group/joined": info(
        "/main/free_uni/task/group/joined",
        "✅ Promotion has been completed successfully",
    ),
    "/main/free_uni/task/group/reward": info(
        "/main/free_uni/task/group/reward",
        "✅ Promotion has been completed successfully\nCongratulations! You've earned $cripto_info",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/free_uni/task/bot": info(
        "/main/free_uni/task/bot",
        "Text",
        [
            [Button.url("🤖Start the Bot🤖", "http://t.me/UniSwapNew")],
            [
                Button.inline("➡️Skip", data=b"f_uni-bot_skip"),
                Button.inline("✅Started", data=b"f_uni-bot_joined"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/free_uni/task/bot/verify": info(
        "/main/free_uni/task/bot/verify",
        '🔎 <b>FORWARD a message from that bot to complete this task </b>\n\n1️⃣ Open the bot using <a href="$bot_url">This Link</a>\n\n2️⃣ Select any message from the bot and press "Forward"\n\n3️⃣ Forward it to this bot\n\n👇🏻 <b>Do it now</b>',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/free_uni/task/bot/joined": info(
        "/main/free_uni/task/bot/joined", "✅ Promotion has been completed successfully"
    ),
    "/main/free_uni/task/bot/verify/notjoined": info(
        "/main/free_uni/task/bot/verify/notjoined",
        "The message does not belong to the bot",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/free_uni/task/bot/reward": info(
        "/main/free_uni/task/bot/reward",
        "✅ Promotion has been completed successfully\n⚡ Congratulations! You've earned $cripto_info",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/free_uni/task/sites": info(
        "/main/free_uni/task/sites",
        "Text",
        [
            [
                Button.inline("➡️Skip", data=b"f_uni-sites_skip"),
                Button.url("Open Link", "http://t.me/UniSwapNew"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/unicorn_unauthorized": info(
        "/main/unicorn_unauthorized",
        "🔖 Invite 5 Friends and start earning Free Money. Your 🦄 Unicorn is waiting for you!",
        [
            [
                Button.inline("🔖 Invite friends", data=b"unicorn-friends"),
            ],
            [Button.inline("< Back", data=b"back")],
        ],
    ),
    "/main/unicorn": info(
        "/main/unicorn",
        "🎟️ <b>Name</b> ≈ $name\n\n🔆 <b>Current level</b> ≈  <b>Level</b> $lvl +$diary <b>UNI</b>\n\n🔖 <b>Next level</b> ≈ <b>Level</b> $next_lvl + $next_diary <b>UNI</b>\n\n🍪 <b>Necessary Food</b> ≈ $foot_necesary <b>Weekly Referral</b>\n\n👛 <b>Daily Productivity</b> ≈ $diary <b>UNI</b>",
        [
            [
                Button.inline("🍪 Feed Pet", data=b"unicorn-feed_pet"),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("💡 Tutorial", data=b"unicorn-tutorial"),
            ],
        ],
    ),
    "/main/unicorn/feed_pet": info(
        "/main/unicorn/feed_pet",
        "🔖 <b>Next Level</b> <b>≈</b> <b>Level</b> $next_lvl\n<b>+</b> $next_diary UNI {<b>Diary</b>}\n<b>+</b> $bonus UNI {<b>Level Bonus</b>}\n\n💡 You need to feed your Unicorn with $foot_to_up Referrals to increase its Level:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/unicorn_not_feed": info(
        "/main/unicorn_not_feed",
        "😔 Your Unicorn has not been fed in 20 Days, if you do not feed it soon you will stop receiving profits.",
        [
            [
                Button.inline("🍬 Feed Unicorn!", data=b"unicorn-feed_pet"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/unicorn/feed_pet/ref>": info(
        "/main/unicorn/feed_pet/ref>",
        "💡 You currently have $ref Referrals.\n\n‼️ The number shipped exceeds the quantity available.",
        [[Button.inline("Ok!", data=b"back")]],
    ),
    "/main/unicorn/level_up": info(
        "/main/unicorn/level_up",
        "👏 <b>Congratulations</b>, your Unicorn has reached a <b>New Level</b>.",
        [
            [
                Button.inline("🦄 New Unicorn", data=b"new_unicorn"),
            ],
        ],
    ),
    "/main/unicorn/tutorial": info(
        "/main/unicorn/tutorial",
        "🔘 Click on the question to get it's answer:",
        [
            [
                Button.inline("Q1: How can I win?", data=b"unicorn-Q1"),
            ],
            [
                Button.inline(
                    "Q2: What does 🍪 Necessary Food mean?", data=b"unicorn-Q2"
                ),
            ],
            [
                Button.inline(
                    "Q3: How to increase the level of my Unicorn?", data=b"unicorn-Q3"
                ),
            ],
            [
                Button.inline("Q4: Can I change the name?", data=b"unicorn-Q4"),
            ],
            [
                Button.inline(
                    "Q5: If I feed the unicorn, do I lose my Referrals?",
                    data=b"unicorn-Q5",
                ),
            ],
            [
                Button.inline("< Back", data=b"back"),
                Button.inline("Ask a Question", data=b"unicorn-ask_question"),
            ],
        ],
    ),
    "/main/unicorn/tutorial/ask_question": info(
        "/main/unicorn/tutorial/ask_question",
        "✍️ Please submit your question, no more than 500 characters.",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/unicorn/tutorial/Q1": info(
        "/main/unicorn/tutorial/Q1",
        "<b>Q1:</b> How can I win?\n\n• Each Unicorn is unique and will provide you with rewards as long as you keep it fed. The rewards of each Unicorn improve with each level up.",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/unicorn/tutorial/Q2": info(
        "/main/unicorn/tutorial/Q2",
        "<b>Q2:</b> What does 🍪 Necessary Food mean?\n\n• If your Unicorn remains without feeding for more than 25 Days, it could die, this means that you would stop receiving rewards. Therefore, you need to feed constantly to increase your Level and continue generating benefits. By letting a Unicorn die, it will return with the lowest Level.",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/unicorn/tutorial/Q3": info(
        "/main/unicorn/tutorial/Q3",
        "<b>Q3:</b> How to increase the level of my Unicorn?\n\n• At the moment it is only possible to increase your Unicorn's Level through already known food (Referrals).",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/unicorn/tutorial/Q4": info(
        "/main/unicorn/tutorial/Q4",
        '<b>Q4:</b> Can I change the name?\n\n• Yes, after Level 5 and above your Unicorn will have many functions unlocked including the "Custom Name" function.',
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/unicorn/tutorial/Q5": info(
        "/main/unicorn/tutorial/Q5",
        "<b>Q5:</b> If I feed the unicorn, do I lose my Referrals?\n\n• Yes, in simple answer if you have a total of 10 Referrals and you feed your Unicorn with 5 Referrals you will have a total of 5 Referrals.",
        [[Button.inline("< Back", data=b"back")]],
    ),
    "/main/unicorn/quest_plant": info(
        "/main/unicorn/quest_plant",
        "UID: $uid\n\nQuestions:\n\n$question",
    ),
    "/main/settings": info(
        "/main/settings",
        "<b>ID:</b> <code>$uid</code>\n\n<b> Name: </b> $name\n\n<b> Email: </b> $email\n\n<b> Phone number: </b> $phone\n\n<b> Language: </b> $language\n\n<b> Favorite currency: </b> $currency/USD",
        [
            [
                Button.inline("⚙️ Set up", data=b"setting-set_up"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/settings/set_up": info(
        "/main/settings/set_up",
        "🔆 Configure your profile for better performance.",
        [
            [
                Button.inline("🌏 Language", data=b"set-language"),
            ],
            [
                Button.inline("🎟️ Name", data=b"set-name"),
                Button.inline("📨 Email", data=b"set-email"),
            ],
            [
                Button.inline("📲 Phone", data=b"set-phone"),
                Button.inline("🪙 Currency", data=b"set-currency"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/settings/set_up/language": info(
        "/main/settings/set_up/language",
        "🌏 Select a new language:",
        [
            [
                Button.inline("🇨🇳 普通话", data=b"set_lang{zh-CN>0:0"),
                Button.inline("🇪🇸 Español", data=b"set_lang{es>0:1"),
            ],
            [
                Button.inline("🇺🇸 English", data=b"set_lang{en>1:0"),
                Button.inline("🇮🇳 हिन्दी", data=b"set_lang{hi>1:1"),
            ],
            [
                Button.inline("🇵🇹 Português", data=b"set_lang{pt>2:0"),
                Button.inline("🇷🇺 Русский", data=b"set_lang{ru>2:1"),
            ],
            [
                Button.inline("🇯🇵 日本語", data=b"set_lang{ja>3:0"),
                Button.inline("🇫🇷 Français", data=b"set_lang{fr>3:1"),
            ],
            [
                Button.inline("🇧🇩 বাংলা", data=b"set_lang{bn>4:0"),
                Button.inline("🇸🇦 العربية", data=b"set_lang{ar>4:1"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/settings/set_up/name": info(
        "/main/settings/set_up/name",
        "🎟️ Please send your name:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/settings/set_up/email": info(
        "/main/settings/set_up/email",
        "📨 Send your email here, It will be used only for account recovery in case of loss.",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/settings/set_up/phone": info(
        "/main/settings/set_up/phone",
        "📲 Submit your number, it will be used only for the purpose of recovering your account if necessary.",
        [[Button.request_phone("Share Phone📞")]],
    ),
    "/main/settings/set_up/currency": info(
        "/main/settings/set_up/currency",
        "🪙 Please indicate your favorite currency.",
        [
            [
                Button.inline("USDT", data=b"set_cur{USDT>0:0"),
                Button.inline("ETH", data=b"set_cur{ETH>0:1"),
                Button.inline("TON", data=b"set_cur{TON>0:2"),
            ],
            [
                Button.inline("TRX", data=b"set_cur{TRX>1:0"),
                Button.inline("BNB", data=b"set_cur{BNB>1:1"),
                Button.inline("NOT", data=b"set_cur{NOT>1:2"),
            ],
            [
                Button.inline("BTC", data=b"set_cur{BTC>2:0"),
                Button.inline("UNI", data=b"set_cur{UNI>2:1"),
                Button.inline("LTC", data=b"set_cur{LTC>2:2"),
            ],
            [
                Button.inline("USDC", data=b"set_lang{USDC>3:0"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/settings/set_up/incorrect": info(
        "/main/settings/set_up/incorrect",
        "‼️ Incorrect format, please send the correct format:",
        [[Button.text("🚫 Cancel", resize=True)]],
    ),
    "/main/nft": info(
        "/main/nft",
        "🎨 Manage, create, buy and sell your own NFTs.",
        [
            [
                Button.inline("🎨 My Gallery", data=b"nft-gallery"),
            ],
            [
                Button.inline("📘 Sell Art", data=b"nft-sell_art"),
                Button.inline("📗 Buy Art", data=b"set-buy_art"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/nft/gallery": info(
        "/main/nft/gallery",
        "🎨 In progress, soon...",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/nft/sell_art": info(
        "/main/nft/sell_art",
        "📘 In progress, soon...",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/nft/sell_art": info(
        "/main/nft/buy_art",
        "📗 In progress, soon...",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake": info(
        "/main/stake",
        "🔆 Select the time in Days for which your Staking will be extended.",
        [
            [
                Button.inline("📙 5 Days", data=b"stake-days_5"),
                Button.inline("📗 15 Days", data=b"stake-days_15"),
            ],
            [
                Button.inline("📘 20 Days", data=b"stake-days_20"),
                Button.inline("📕 30 Days", data=b"stake-days_30"),
            ],
            [
                Button.inline("📔 50 Days", data=b"stake-days_50"),
                Button.inline("📓 75 Days", data=b"stake-days_75"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake/currency": info(
        "/main/stake/currency",
        "〽️ Select the Cryptocurrency you wish to Staking.",
        [
            [
                Button.inline("TON", data=b"stake-cr_TON"),
            ],
            [
                Button.inline("USDT", data=b"stake-cr_USDT"),
                Button.inline("NOT", data=b"stake-cr_NOT"),
            ],
            [
                Button.inline("TRX", data=b"stake-cr_TRX"),
                Button.inline("UNI", data=b"stake-cr_UNI"),
            ],
            [
                Button.inline("LTC", data=b"stake-cr_LTC"),
                Button.inline("BTC", data=b"stake-cr_BTC"),
            ],
            [
                Button.inline("ETH", data=b"stake-cr_ETH"),
                Button.inline("BNB", data=b"stake-cr_BNB"),
            ],
            [
                Button.inline("USDC", data=b"stake-cr_USDC"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake/currency/start": info(
        "/main/stake/currency/start",
        "$emoj Staking Days ≈ $days Days + $profit%\n\n👛 Frozen Balance ≈$bal $crypto\n\n🦋 Net Profit ≈ $profit_brute $crypto",
        [
            [
                Button.inline("📈 Start Staking »", data=b"stake-start"),
            ],
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake/currency/info": info(
        "/main/stake/currency/info",
        "🦋 <b>Staking Started</b>!\n\n• Beginning ≈ $start_date\n\n• End ≈ $end_date",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake/completed": info(
        "/main/stake/completed",
        "🦋 <b>Staking Completed</b>!\n\n👛 You just received $profit <b>$crypto</b> directly in your personal wallet!",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
    "/main/stake/currency/not_balance": info(
        "/main/stake/currency/not_balance",
        "Your balance is insuficient!",
        [
            [
                Button.inline("< Back", data=b"back"),
            ],
        ],
    ),
}

my_text_db = Translator_db(menu_system, lenguage, "db/lg_db")
# my_text_db.db_lg()
