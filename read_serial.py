import serial
import time

# Arduinoが接続されているポート名とボーレートを指定
# アクセス権限エラーが出る場合は sudo python3 read_serial.py で実行してください
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # 接続初期化の待ち時間

print("通信を開始します...")

try:
    while True:
        if ser.in_waiting > 0:
            # 送信されてきた文字列をデコードして表示
            line = ser.readline().decode('utf-8').rstrip()
            print(f"受信: {line}")
except KeyboardInterrupt:
    print("通信を終了します")
    ser.close()