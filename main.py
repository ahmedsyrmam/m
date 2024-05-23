import pyrogram , pyromod
from keep import alive
from pyromod import listen

from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '7046489169:AAGCpPKOpvLZ1yedn4RW3kWuMqtPPRswAoI' ## توكنك 
id = 6379161238
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id, 5108562302])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['trprogram'])
x = Client(name='loclhosst', api_id=25453029, api_hash='ed66bc9eba4e8d21d0041b257a1e525a', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
