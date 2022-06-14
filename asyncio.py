import aiohttp
import asyncio

async def test():

    async with aiohttp.ClientSession() as session:
        async with session.get url as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

  asyncio.run(main())
