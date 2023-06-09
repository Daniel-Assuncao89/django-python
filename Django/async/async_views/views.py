import asyncio
import httpx


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
        async with httpx.AsyncClient() as cliente:
            r = await cliente.get("https://httpbin.org/")
            print(r)