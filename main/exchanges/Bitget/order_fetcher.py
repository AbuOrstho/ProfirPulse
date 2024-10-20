import asyncio
import websockets
import datetime
import json

# WebSocket URL Bitget
BITGET_WS_URL = "wss://ws.bitget.com/v2/ws/public"


async def subscribe_to_order_book(websocket):
    # Формируем запрос для подписки на ордербук BTCUSDT
    subscribe_message = {
        "op": "subscribe",
        "args": [
            {
                "instType": "SPOT",
                "channel": "books15",
                "instId": "BTCUSDT"
            }
        ]
    }
    await websocket.send(json.dumps(subscribe_message))
    print(f"Subscribed to order book for BTCUSDT")


async def handle_message(websocket):
    async for message in websocket:
        data = json.loads(message)
        time = datetime.datetime.now().strftime('%H:%M:%S')
        if data != 'Ошибка':
            print(f"{time} {data}")
            # Преобразование в JSON-формат
            json_data = json.dumps(data, indent=4)
            # Сохранение в файл
            with open('data.json', 'w') as json_file:
                json_file.write(json_data)



async def main():
    async with websockets.connect(BITGET_WS_URL) as websocket:
        await subscribe_to_order_book(websocket)
        await handle_message(websocket)


# Запуск программы
asyncio.get_event_loop().run_until_complete(main())
