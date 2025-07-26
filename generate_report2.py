def gen_rpt(d):
    s, c = aggr(d)
    avg_s, avg_c = avg(s, c, len(d))
    rpt = rpt_mk(s, c, avg_s, avg_c)
    return rpt

# データの集計
def aggr(d):
    s = 0
    c = 0
    for r in d:
        s += r['sales']
        c += r['customers']
    return s, c

# 平均計算
def avg(s, c, n):
    return s / n, c / n

# レポート生成
def rpt_mk(s, c, avg_s, avg_c):
    rpt = f"Total Sales: {s}\n"
    rpt += f"Total Customers: {c}\n"
    rpt += f"Average Sales per Day: {avg_s:.2f}\n"
    rpt += f"Average Customers per Day: {avg_c:.2f}\n"
    return rpt

# 実行例
d = [
    {"sales": 100, "customers": 10},
    {"sales": 150, "customers": 20},
    {"sales": 200, "customers": 15},
]

print(gen_rpt(d))
