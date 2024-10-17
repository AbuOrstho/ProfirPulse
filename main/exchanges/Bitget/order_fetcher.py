import json
import websocket

# Список торговых пар
symbols = [
    "BTCUSDT",  # Bitcoin
    "ETHUSDT",  # Ethereum
    "BNBUSDT",  # BNB
    "SOLUSDT",  # Solana
    "XRPUSDT",  # XRP
    "DOGEUSDT",  # Dogecoin
    "TRXUSDT",  # TRON
    "TONUSDT",  # Toncoin
    "ADAUSDT",  # Cardano
]

# URL для подключения к WebSocket
url = "wss://ws.bitget.com/mix/v1/stream"

# Функция для обработки сообщений
def on_message(ws, message):
    data = json.loads(message)
    if 'data' in data:
        order_book = data['data']
        symbol = data['arg']['instId']
        print(f"Order book for {symbol}:")
        print(f"Bids: {order_book['bids'][:50]}")
        print(f"Asks: {order_book['asks'][:50]}")
        print("-" * 50)

# Функция для обработки ошибок
def on_error(ws, error):
    print(f"Error: {error}")

# Функция для обработки закрытия соединения (принимает 3 аргумента)
def on_close(ws, close_status_code, close_msg):
    print(f"### Connection closed with status code {close_status_code} and message: {close_msg} ###")

# Функция для инициализации подключения
def on_open(ws):
    # Подписка на order book для каждой валютной пары
    for symbol in symbols:
        subscribe_message = {
            "op": "subscribe",
            "args": [
                {
                    "channel": "depth",
                    "instId": symbol
                }
            ]
        }
        ws.send(json.dumps(subscribe_message))

# Основная функция для подключения к WebSocket
def start_socket():
    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    start_socket()
