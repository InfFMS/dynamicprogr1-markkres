PRICE = [0, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
INF=10**9
min_score=[INF]*16
min_score[0]=0
for i in range(1, 16):
    f1=min_score[i - 1] if i-1>=0 else INF
    f2=min_score[i - 2] if i-2>=0 else INF
    f4=min_score[i - 4] if i-4>=0 else INF
    prev_min = min(f1, f2, f4)
    if prev_min<INF:
        min_score[i] = prev_min + PRICE[i]
print(min_score[15])
