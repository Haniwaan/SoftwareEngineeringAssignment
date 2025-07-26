# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。
def cal_avg(grades):
    total = sum(grades)
    avg = total / len(grades)
    return total, avg

def top_std(stu):
    top_n = ""
    top_s = 0
    rep = []

    for name, grades in stu.items():
        total, avg = cal_avg(grades)
        rep.append((name, total, avg))
        if total > top_s:
            top_s = total
            top_n = name

    return top_n, top_s, rep

def print_rep(rep):
    for name, total, avg in rep:
        print(f"Student: {name}, Total: {total}, Average: {avg:.2f}")

def main():
    stu = {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 84],
        "Charlie": [70, 75, 80],
        "David": [95, 85, 90]
    }

    top_n, top_s, rep = top_std(stu)
    print_rep(rep)
    print(f"Best student: {top_n} with total score: {top_s}")

main()