file_name = "C:/Users/Student/Documents/rename_test/httpswww.youtube.comwatchv=y3p2-xE8lsw&t=891s"

with open(file_name, encoding="utf-8") as f:
    data_lines = f.read()

# 文字列置換
data_lines = data_lines.replace("グーグルマップ", "Google マップ ")

# 同じファイル名で保存
with open(file_name, mode="w", encoding="utf-8") as f:
    f.write(data_lines)