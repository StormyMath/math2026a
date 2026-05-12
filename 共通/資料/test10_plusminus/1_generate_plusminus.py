import csv
import random

def generate_csv(filename):
    problems = []

    def rand(min_val, max_val):
        return random.randint(min_val, max_val)

    # 1: -A+B -> originally -3+5
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}+{B} =", str(-A + B)])

    # 2: A-(-B) -> originally 7-(-2)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}-(-{B}) =", str(A - (-B))])

    # 3: -A*B -> originally -4*2
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}\\times{B} =", str(-A * B)])

    # 4: A/(-B) -> originally 35/(-5)
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"{A}\\div(-{B}) =", str(A // (-B))])

    # 5: -A+(-B) -> originally -6+(-1)
    A = rand(2, 9); B = rand(1, 9)
    problems.append([f"-{A}+(-{B}) =", str(-A + (-B))])

    # 6: A*(-B) -> originally 9*(-4)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}\\times(-{B}) =", str(A * (-B))])

    # 7: (-A)*(-B) -> originally (-3)*(-3)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"(-{A})\\times(-{B}) =", str((-A) * (-B))])

    # 8: (-A)/B -> originally (-8)/2
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"(-{A})\\div{B} =", str((-A) // B)])

    # 9: A+(-B) -> originally 5+(-7)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}+(-{B}) =", str(A + (-B))])

    # 10: -A-B -> originally -2-6
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}-{B} =", str(-A - B)])

    # 11: A*(-B) -> originally 4*(-6)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}\\times(-{B}) =", str(A * (-B))])

    # 12: -A/(-B) -> originally -9/(-3)
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"-{A}\\div(-{B}) =", str((-A) // (-B))])

    # 13: -A+B -> originally -11+8
    A = rand(11, 19); B = rand(2, 9)
    problems.append([f"-{A}+{B} =", str(-A + B)])

    # 14: -A*(-B) -> originally -7*(-5)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}\\times(-{B}) =", str(-A * (-B))])

    # 15: -A-B -> originally -5-3
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}-{B} =", str(-A - B)])

    # 16: A/(-B) -> originally 21/(-3)
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"{A}\\div(-{B}) =", str(A // (-B))])

    # 17: -A*B -> originally -8*7
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-{A}\\times{B} =", str(-A * B)])

    # 18: A/(-B) -> originally 28/(-4)
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"{A}\\div(-{B}) =", str(A // (-B))])

    # 19: -A-(-B) -> originally -12-(-4)
    A = rand(11, 19); B = rand(2, 9)
    problems.append([f"-{A}-(-{B}) =", str(-A - (-B))])

    # 20: -A/B -> originally -6/3
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"-{A}\\div{B} =", str((-A) // B)])

    # 21: A+(-B) -> originally 7+(-3)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}+(-{B}) =", str(A + (-B))])

    # 22: -A+B -> originally -5+12
    A = rand(2, 9); B = rand(11, 19)
    problems.append([f"-{A}+{B} =", str(-A + B)])

    # 23: A*(-B) -> originally 9*(-3)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"{A}\\times(-{B}) =", str(A * (-B))])

    # 24: -A/(-B) -> originally -56/(-8)
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"-{A}\\div(-{B}) =", str((-A) // (-B))])

    # 25: -A/B -> originally -42/6
    ans = rand(2, 9); B = rand(2, 9); A = ans * B
    problems.append([f"-{A}\\div{B} =", str((-A) // B)])

    # 26: A*(-B) -> originally 4*(-11)
    A = rand(2, 9); B = rand(11, 19)
    problems.append([f"{A}\\times(-{B}) =", str(A * (-B))])

    # 27: -A*0 -> originally -7*0
    A = rand(2, 9)
    problems.append([f"-{A}\\times0 =", str(-A * 0)])

    # 28: 0+A -> originally -0+13
    A = rand(11, 19)
    problems.append([f"0+{A} =", str(0 + A)])

    # 29: A+(-B) -> originally 14+(-18)
    A = rand(11, 19); B = rand(11, 19)
    problems.append([f"{A}+(-{B}) =", str(A + (-B))])

    # 30: -A/(-B) -> originally -60/(-12)
    ans = rand(2, 9); B = rand(11, 19); A = ans * B
    problems.append([f"-{A}\\div(-{B}) =", str((-A) // (-B))])

    # 31: -A+B*(-C) -> originally -3+7*(-2)
    A = rand(2, 9); B = rand(2, 9); C = rand(2, 9)
    problems.append([f"-{A}+{B}\\times(-{C}) =", str(-A + B * (-C))])

    # 32: A/(-B)-C -> originally 8/(-4)-5
    ans1 = rand(2, 9); B = rand(2, 9); A = ans1 * B; C = rand(2, 9)
    problems.append([f"{A}\\div(-{B})-{C} =", str(A // (-B) - C)])

    # 33: (-A)*(-B)/(-C) -> originally (-8)*(-3)/(-2)
    A = rand(2, 9); B = rand(2, 9)
    ans = rand(2, 9)
    C = rand(2, 9); B_mult = rand(1, 5); B = C * B_mult
    problems.append([f"(-{A})\\times(-{B})\\div(-{C}) =", str((-A) * (-B) // (-C))])

    # 34: A-(-B)*C -> originally 9-(-5)*4
    A = rand(2, 9); B = rand(2, 9); C = rand(2, 9)
    problems.append([f"{A}-(-{B})\\times{C} =", str(A - (-B) * C)])

    # 35: A+(-B)-(+C) -> originally 4+(-9)-(+3)
    A = rand(2, 9); B = rand(2, 9); C = rand(2, 9)
    problems.append([f"{A}+(-{B})-(+{C}) =", str(A + (-B) - C)])

    # 36: A*(-B)+(-C) -> originally 7*(-3)+(-8)
    A = rand(2, 9); B = rand(2, 9); C = rand(2, 9)
    problems.append([f"{A}\\times(-{B})+(-{C}) =", str(A * (-B) + (-C))])

    # 37: -(-A)*(-B) -> originally -(-6)*(-7)
    A = rand(2, 9); B = rand(2, 9)
    problems.append([f"-(-{A})\\times(-{B}) =", str(-(-A) * (-B))])

    # 38: (-A)*B/(-C) -> originally (-7)*6/(-3)
    C = rand(2, 9); B_mult = rand(1, 5); B = C * B_mult; A = rand(2, 9)
    problems.append([f"(-{A})\\times{B}\\div(-{C}) =", str((-A) * B // (-C))])

    # 39: A/(-B)-C -> originally 45/(-9)-2
    ans1 = rand(2, 9); B = rand(2, 9); A = ans1 * B; C = rand(2, 9)
    problems.append([f"{A}\\div(-{B})-{C} =", str(A // (-B) - C)])

    # 40: (-A)*B/C -> originally (-6)*15/9
    C = rand(2, 9); B_mult = rand(1, 5); B = C * B_mult; A = rand(2, 9)
    problems.append([f"(-{A})\\times{B}\\div{C} =", str((-A) * B // C)])

    # CSVに出力
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["problem", "answer"])
        writer.writerows(problems)
        
    print(f"Generated {len(problems)} problems and saved to {filename}.")

if __name__ == "__main__":
    generate_csv("master_plusminus.csv")
