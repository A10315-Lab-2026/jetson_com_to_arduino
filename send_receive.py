import serial
import time

# Arduinoとのシリアル通信設定
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # 接続初期化の待ち時間（Arduinoリセット待ち）

print("=== 双方向通信テスト ===")
print(" [1] : LED点灯")
print(" [0] : LED消灯")
print(" [b] : LED3回点滅")
print(" [q] : 終了")
print("========================")

try:
    while True:
        # ユーザーのコマンド入力を受け付ける
        cmd = input("コマンドを入力してください > ").strip()

        if cmd == 'q':
            print("通信を終了します")
            break

        if cmd in ['1', '0', 'b']:
            # Arduinoに文字列（バイト列）を送信
            ser.write(cmd.encode('utf-8'))
            
            # Arduinoからの返答を受信して表示
            time.sleep(0.1)  # 応答待ち
            while ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').rstrip()
                print(f"Arduinoからの返答: {response}")
        else:
            print("無効なコマンドです。[1], [0], [b], [q] のいずれかを入力してください。")

except KeyboardInterrupt:
    print("\n強制終了します")
finally:
    ser.close()