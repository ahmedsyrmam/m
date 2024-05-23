import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
p = dict(root='plugins')
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')
if not db.exists("admin_list"):
    db.set('admin_list', [5108562302,6379161238])
if not db.exists("sessions"):
    db.set('sessions', [])
if not db.exists("ban_list"):
    db.set("ban_list", [])
x = Client(name='lossclhos', api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', bot_token='7046489169:AAGCpPKOpvLZ1yedn4RW3kWuMqtPPRswAoI', workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
