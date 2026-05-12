import csv
import random
import math
from fractions import Fraction

def generate_csv(filename):
    problems = []

    def rand(min_val, max_val):
        return random.randint(min_val, max_val)

    def to_tex_prob(num, den):
        if den == 1:
            return str(num)
        return f"\\dfrac{{{num}}}{{{den}}}"

    def to_tex_ans(f):
        if f.denominator == 1:
            return str(f.numerator)
        return f"\\dfrac{{{f.numerator}}}{{{f.denominator}}}"

    # --- 足し算 (8問) ---
    # 1: 分母同じ、約分なし
    while True:
        d = rand(3, 9)
        n1 = rand(1, d-2)
        n2 = rand(1, d - 1 - n1)
        if Fraction(n1+n2, d).denominator == d:
            problems.append([f"{to_tex_prob(n1,d)}+{to_tex_prob(n2,d)} =", to_tex_ans(Fraction(n1+n2,d))])
            break

    # 2: 分母同じ、約分あり
    while True:
        d = rand(4, 12)
        n1 = rand(1, d-1)
        n2 = rand(1, d-1)
        if Fraction(n1+n2, d).denominator != d and (n1+n2) != d:
            problems.append([f"{to_tex_prob(n1,d)}+{to_tex_prob(n2,d)} =", to_tex_ans(Fraction(n1+n2,d))])
            break

    # 3: 分母異なる（倍数）
    while True:
        d1 = rand(2, 6)
        d2 = d1 * rand(2, 3)
        n1 = rand(1, d1-1); n2 = rand(1, d2-1)
        if math.gcd(n1, d1) == 1 and math.gcd(n2, d2) == 1:
            problems.append([f"{to_tex_prob(n1,d1)}+{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)+Fraction(n2,d2))])
            break

    # 4: 分母異なる（互いに素、小さめ）
    while True:
        d1 = rand(2, 5); d2 = rand(2, 5)
        if math.gcd(d1, d2) == 1 and d1 != d2:
            n1 = rand(1, d1-1); n2 = rand(1, d2-1)
            problems.append([f"{to_tex_prob(n1,d1)}+{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)+Fraction(n2,d2))])
            break

    # 5: 分母異なる（互いに素、大きめ）
    while True:
        d1 = rand(5, 9); d2 = rand(5, 9)
        if math.gcd(d1, d2) == 1 and d1 != d2:
            n1 = rand(1, d1-1); n2 = rand(1, d2-1)
            if math.gcd(n1, d1) == 1 and math.gcd(n2, d2) == 1:
                problems.append([f"{to_tex_prob(n1,d1)}+{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)+Fraction(n2,d2))])
                break

    # 6: 分母異なる（最小公倍数）
    while True:
        d1 = rand(4, 10); d2 = rand(4, 10)
        g = math.gcd(d1, d2)
        if g > 1 and d1 != d2 and d1 != g and d2 != g:
            n1 = rand(1, d1-1); n2 = rand(1, d2-1)
            if math.gcd(n1, d1) == 1 and math.gcd(n2, d2) == 1:
                problems.append([f"{to_tex_prob(n1,d1)}+{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)+Fraction(n2,d2))])
                break

    # 7: 分数 + 整数
    while True:
        d = rand(2, 5); n = rand(1, d*2)
        if math.gcd(n, d) == 1 and n % d != 0:
            i = rand(1, 3)
            problems.append([f"{to_tex_prob(n,d)}+{i} =", to_tex_ans(Fraction(n,d)+i)])
            break

    # 8: 整数 + 分数
    while True:
        d = rand(2, 5); n = rand(1, d*2)
        if math.gcd(n, d) == 1 and n % d != 0:
            i = rand(1, 3)
            problems.append([f"{i}+{to_tex_prob(n,d)} =", to_tex_ans(i+Fraction(n,d))])
            break

    # --- 引き算 (8問) ---
    # 9: 分母同じ、約分なし
    while True:
        d = rand(3, 9)
        n1 = rand(2, d+3); n2 = rand(1, n1-1)
        if Fraction(n1-n2, d).denominator == d and math.gcd(n1,d)==1 and math.gcd(n2,d)==1:
            problems.append([f"{to_tex_prob(n1,d)}-{to_tex_prob(n2,d)} =", to_tex_ans(Fraction(n1-n2,d))])
            break

    # 10: 分母同じ、約分あり
    while True:
        d = rand(4, 12)
        n1 = rand(2, d+5); n2 = rand(1, n1-1)
        if Fraction(n1-n2, d).denominator != d and (n1-n2) != d and math.gcd(n1,d)==1 and math.gcd(n2,d)==1:
            problems.append([f"{to_tex_prob(n1,d)}-{to_tex_prob(n2,d)} =", to_tex_ans(Fraction(n1-n2,d))])
            break

    # 11: 分母異なる（倍数）
    while True:
        d1 = rand(2, 6); d2 = d1 * rand(2, 3)
        n1 = rand(1, d1*2); n2 = rand(1, d2*2)
        if Fraction(n1,d1) > Fraction(n2,d2) and math.gcd(n1,d1)==1 and math.gcd(n2,d2)==1:
            problems.append([f"{to_tex_prob(n1,d1)}-{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)-Fraction(n2,d2))])
            break

    # 12: 分母異なる（互いに素）
    while True:
        d1 = rand(2, 6); d2 = rand(2, 6)
        if math.gcd(d1, d2) == 1 and d1 != d2:
            n1 = rand(1, d1*2); n2 = rand(1, d2*2)
            if Fraction(n1,d1) > Fraction(n2,d2) and math.gcd(n1,d1)==1 and math.gcd(n2,d2)==1:
                problems.append([f"{to_tex_prob(n1,d1)}-{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)-Fraction(n2,d2))])
                break

    # 13: 分母異なる（最小公倍数）
    while True:
        d1 = rand(4, 10); d2 = rand(4, 10)
        g = math.gcd(d1, d2)
        if g > 1 and d1 != d2 and d1 != g and d2 != g:
            n1 = rand(1, d1*2); n2 = rand(1, d2*2)
            if Fraction(n1,d1) > Fraction(n2,d2) and math.gcd(n1,d1)==1 and math.gcd(n2,d2)==1:
                problems.append([f"{to_tex_prob(n1,d1)}-{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)-Fraction(n2,d2))])
                break

    # 14: 分母異なる（最小公倍数・大きめ）
    while True:
        d1 = rand(6, 15); d2 = rand(6, 15)
        g = math.gcd(d1, d2)
        if g > 1 and d1 != d2 and d1 != g and d2 != g:
            n1 = rand(1, d1*2); n2 = rand(1, d2*2)
            if Fraction(n1,d1) > Fraction(n2,d2) and math.gcd(n1,d1)==1 and math.gcd(n2,d2)==1:
                problems.append([f"{to_tex_prob(n1,d1)}-{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)-Fraction(n2,d2))])
                break

    # 15: 分数 - 整数
    while True:
        d = rand(2, 5); n = rand(d+1, d*4)
        i = rand(1, 3)
        if Fraction(n,d) > i and math.gcd(n,d)==1:
            problems.append([f"{to_tex_prob(n,d)}-{i} =", to_tex_ans(Fraction(n,d)-i)])
            break

    # 16: 整数 - 分数
    while True:
        i = rand(1, 4)
        d = rand(2, 5); n = rand(1, d*3)
        if i > Fraction(n,d) and math.gcd(n,d)==1:
            problems.append([f"{i}-{to_tex_prob(n,d)} =", to_tex_ans(i-Fraction(n,d))])
            break

    # --- 掛け算 (8問) ---
    # 17: 約分なし
    while True:
        d1 = rand(2, 5); n1 = rand(1, d1-1)
        d2 = rand(2, 5); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1 and math.gcd(n1, d2)==1 and math.gcd(n2, d1)==1:
            problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
            break

    # 18: 1箇所約分
    while True:
        d1 = rand(2, 6); n1 = rand(1, d1-1)
        d2 = rand(2, 6); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            g1 = math.gcd(n1, d2); g2 = math.gcd(n2, d1)
            if (g1 > 1 and g2 == 1) or (g1 == 1 and g2 > 1):
                problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
                break

    # 19: 2箇所約分
    while True:
        d1 = rand(2, 9); n1 = rand(1, d1-1)
        d2 = rand(2, 9); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, d2) > 1 and math.gcd(n2, d1) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
                break

    # 20: 2箇所約分（大きめ）
    while True:
        d1 = rand(6, 15); n1 = rand(1, d1-1)
        d2 = rand(6, 15); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, d2) > 1 and math.gcd(n2, d1) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
                break

    # 21: 仮分数での約分
    while True:
        d1 = rand(2, 8); n1 = rand(d1+1, d1*3)
        d2 = rand(2, 8); n2 = rand(d2+1, d2*3)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, d2) > 1 and math.gcd(n2, d1) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
                break

    # 22: 仮分数での約分（大きめ）
    while True:
        d1 = rand(5, 15); n1 = rand(d1+1, d1*3)
        d2 = rand(5, 15); n2 = rand(d2+1, d2*3)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, d2) > 1 and math.gcd(n2, d1) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\times{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)*Fraction(n2,d2))])
                break

    # 23: 分数 × 整数
    while True:
        d = rand(2, 9); n = rand(1, d*2)
        i = rand(2, 9)
        if math.gcd(n, d)==1 and math.gcd(d, i) > 1:
            problems.append([f"{to_tex_prob(n,d)}\\times{i} =", to_tex_ans(Fraction(n,d)*i)])
            break

    # 24: 整数 × 分数
    while True:
        i = rand(2, 9)
        d = rand(2, 9); n = rand(1, d*2)
        if math.gcd(n, d)==1 and math.gcd(i, d) > 1:
            problems.append([f"{i}\\times{to_tex_prob(n,d)} =", to_tex_ans(i*Fraction(n,d))])
            break

    # --- 割り算 (8問) ---
    # 25: 約分なし
    while True:
        d1 = rand(2, 6); n1 = rand(1, d1-1)
        d2 = rand(2, 6); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, n2)==1 and math.gcd(d1, d2)==1:
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 26: 1箇所約分
    while True:
        d1 = rand(2, 8); n1 = rand(1, d1-1)
        d2 = rand(2, 8); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            g1 = math.gcd(n1, n2); g2 = math.gcd(d1, d2)
            if (g1 > 1 and g2 == 1) or (g1 == 1 and g2 > 1):
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 27: 2箇所約分
    while True:
        d1 = rand(3, 10); n1 = rand(1, d1-1)
        d2 = rand(3, 10); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, n2) > 1 and math.gcd(d1, d2) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 28: 2箇所約分（大きめ）
    while True:
        d1 = rand(6, 15); n1 = rand(1, d1-1)
        d2 = rand(6, 15); n2 = rand(1, d2-1)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, n2) > 1 and math.gcd(d1, d2) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 29: 仮分数での約分
    while True:
        d1 = rand(3, 12); n1 = rand(d1+1, d1*3)
        d2 = rand(3, 12); n2 = rand(d2+1, d2*3)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, n2) > 1 and math.gcd(d1, d2) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 30: 仮分数での約分（大きめ）
    while True:
        d1 = rand(8, 20); n1 = rand(d1+1, d1*3)
        d2 = rand(8, 20); n2 = rand(d2+1, d2*3)
        if math.gcd(n1, d1)==1 and math.gcd(n2, d2)==1:
            if math.gcd(n1, n2) > 1 and math.gcd(d1, d2) > 1:
                problems.append([f"{to_tex_prob(n1,d1)}\\div{to_tex_prob(n2,d2)} =", to_tex_ans(Fraction(n1,d1)/Fraction(n2,d2))])
                break

    # 31: 分数 ÷ 整数
    while True:
        d = rand(2, 9); n = rand(1, d*3)
        i = rand(2, 9)
        if math.gcd(n, d)==1 and math.gcd(n, i) > 1:
            problems.append([f"{to_tex_prob(n,d)}\\div{i} =", to_tex_ans(Fraction(n,d)/i)])
            break

    # 32: 整数 ÷ 分数
    while True:
        i = rand(2, 9)
        d = rand(2, 9); n = rand(1, d*3)
        if math.gcd(n, d)==1 and math.gcd(i, n) > 1:
            problems.append([f"{i}\\div{to_tex_prob(n,d)} =", to_tex_ans(i/Fraction(n,d))])
            break

    # CSVに出力
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["problem", "answer"])
        writer.writerows(problems)
        
    print(f"Generated {len(problems)} problems and saved to {filename}.")

if __name__ == "__main__":
    generate_csv("master_fraction.csv")
