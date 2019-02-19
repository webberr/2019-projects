# 24hour_stats.py

import asyncio

from copra.rest import Client

loop = asyncio.get_event_loop()

client = Client(loop)

async def get_stats():
    btc_stats = await client.get_24hour_stats('LTC-USD')
    print(btc_stats)

loop.run_until_complete(get_stats())
loop.run_until_complete(client.close())