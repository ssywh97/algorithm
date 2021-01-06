n = 1260 #거슬러줘야하는 돈
count = 0 #거슬러준 동전의 갯수

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10] #500원 100원 50원 10원

for coin in coin_types:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(coint)