import websocket,json
import time
token = "btcusdt"
kline = "kline_1m"
socket = f"wss://stream.binance.com:9443/ws/{token}@{kline}"

def on_error(ws,error):
    print(error)

def on_close(ws,close_status_code,close_msg):
    print("connection closed")

def on_response(ws,message):


