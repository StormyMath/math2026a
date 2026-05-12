import os
import csv
import json
import sys

# 共通モジュールをインポート
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from _shared.tex_builder import load_settings, build_and_save_tex

def generate_tex(settings, is_answer_key=False):
    rows_per_page = settings["rows_per_page"]
    input_csv = settings["input_csv"]

    try:
        with open(input_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            problems = list(reader)
    except FileNotFoundError:
        print(f"エラー: {input_csv} が見つかりません。")
        return

    problem_lines = []
    for i, row in enumerate(problems, 1):
        problem_str = row['problem']
        answer_str = row['answer']
        
        # LaTeXの数式モード（$）で囲み、解答部分は太字（\mathbf）にする。
        # 分数の場合、\mathbf が効きづらいことがあるので、場合によっては \bm 等が必要ですが、
        # ここでは \mathbf に \dfrac を入れています。
        if is_answer_key:
            content_str = f"({i}) \\quad ${problem_str} \\mathbf{{{answer_str}}}$"
        else:
            content_str = f"({i}) \\quad ${problem_str}$"
        
        problem_lines.append(f"\\noindent {content_str}")
        problem_lines.append(r"\vspace*{\fill}")
        
        # 指定された行数に達するごとに \columnbreak を挿入する
        if i % rows_per_page == 0 and i < len(problems):
            problem_lines.append(r"\columnbreak")
            
        problem_lines.append("")

    content = "\n".join(problem_lines)
    
    # 共通モジュールでテンプレート当てはめと保存
    build_and_save_tex(settings, content, preamble_macros="", is_answer_key=is_answer_key)

if __name__ == "__main__":
    if not os.path.exists("settings.json"):
        default_settings = {
            "print_title": "次の計算をしなさい。",
            "columns": 2,
            "rows_per_page": 8,
            "show_name_field": True,
            "name_field_format": "\\rightline{　年\\quad 　組\\quad 　番 \\quad 氏名\\underline{\\hspace{25ex}}}",
            "template_file": "../_templates/base_layout.tex",
            "input_csv": "master_fraction.csv",
            "output_tex": "calctest-11_prob.tex",
            "output_ans_tex": "calctest-11_ans.tex"
        }
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(default_settings, f, ensure_ascii=False, indent=4)
        print("settings.json が無かったため作成しました。")

    settings = load_settings("settings.json")
    generate_tex(settings, is_answer_key=False)
    generate_tex(settings, is_answer_key=True)
