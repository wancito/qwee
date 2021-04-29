import pyupbit

access = "1nxxGjJVAzUcgo163ybKSQ7mixbHxBYPiPYt2uZr"          # 본인 값으로 변경
secret = "McFi6A0PhlbAf8Q7aRF2DpwHQ2JLZuB1EP1GxDwQ"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-CVC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회