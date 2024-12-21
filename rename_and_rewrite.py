import glob
import os
import re
import sys

# ディレクトリのパスを指定
path = 'C:/Users/Student/Documents/rename_test'
folder = glob.glob(path + '/*')

# 編集対象のファイル
target_files = []

# 変更対象のファイル内容を表示する
def view_file():
    for i in range(len(target_files)):
        with open(target_files[i], encoding="utf-8") as f:
            file_read = f.read()
            print(target_files[i][len(path)+1:] + ':' + file_read)

# 編集対象のファイルの存在チェック
def get_target_files():
    print('【フォルダパス：】' + path[:-1])
    for i in range(len(folder)):
        if old_name in folder[i][len(path)+1:]:
            target_files.append(folder[i])
        else:
            continue
    if len(target_files) == 0:
        print('「' + old_name + '」'  + 'を含むファイルが見つかりませんでした。')
        sys.exit()
    else:
        for j in range(len(target_files)):
            print('temp.編集対象：', target_files[j])

# 引数の定義
def get_args(var1, var2):
    global old_name
    old_name = var1
    global new_name
    new_name = var2

    get_target_files()

# 末尾に「-renamed」を追加する
# 新規保存用
# save_as_new():
#     with open(rename[i] + '-renamed', mode="w", encoding="utf-8") as f:
#         f.write(data_lines)

# 新しいファイル名の一時保存先
rename = []

def save_as_new():
    print('変更前：' + old_name, '変更後：' + new_name)
    try:
        for i in range(len(target_files)):
            # print('ファイル一覧', folder[i][len(path)-1:])
            """
            # 変更したいファイル名の"一部分"を入力、変更後のファイル名の"一部分"を入力
            # ↓ ↓
            # 設定しているフォルダ内（path）に上記があれば処理続行
            # ↓ ↓
            # ファイル内容の編集
            # ↓ ↓
            # 変更後の"一部分"を元のファイル名から置換し、それを一時保存する（rename）
            # ↓ ↓
            # 変更後のファイル名を別に保存（新規保存）
            
            """
            # ファイルを開く
            with open(target_files[i], encoding="utf-8") as f:
                data_lines = f.read()
                
            # ファイル中身の文字列置換（2か所）
            data_lines = data_lines.replace("06-31", "06-29")
            data_lines = data_lines.replace("0606", "0609")
            
            print('【変換前】', target_files[i][len(path)-1:])
            # 1：変換前文字列、2：変換後文字列、3：対象ファイル
            rename.append(re.sub(old_name, new_name, target_files[i]))
            
            # ↓ ↓ そもそもファイル名を変更しない ↓ ↓
            # # with open(target_files[j], mode="w", encoding="utf-8") as f:
            
            # 変更後の名前が既に存在している場合は末尾に「_renamed」を追加する
            if os.path.exists(rename[i]):
                with open(rename[i] + '_renamed', mode="w", encoding="utf-8") as f:
                        f.write(data_lines)
                
            
            # ファイル編集適用
            with open(rename[i], mode="w", encoding="utf-8") as f:
                f.write(data_lines)
                
                
        renamed_files = []
        renamed_folder = glob.glob(path)
        for i in range(len(renamed_folder)):
            if new_name in renamed_folder[i]:
                renamed_files.append(renamed_folder[i])
            else:
                continue
        for j in range(len(renamed_files)):
            print('【変換後】', renamed_files[j][len(path)-1:])



    except FileNotFoundError as e:
        # print('変更前ファイル：' + old_name + 'を含むファイルが見つかりませんでした。')
        print(e)
    except OSError as e:
        # print('ファイルパスを確認下さい。')
        print(e)


def overwrite():
    print('変更前：' + old_name, '変更後：' + new_name)
    try:
        for i in range(len(target_files)):
            # print('ファイル一覧', folder[i][len(path)-1:])
            """
            # 変更したいファイル名の"一部分"を入力、変更後のファイル名の"一部分"を入力
            # ↓ ↓
            # 設定しているフォルダ内（path）に上記があれば処理続行
            # ↓ ↓
            # ファイル内容の編集
            # ↓ ↓
            # 変更後の"一部分"を元のファイル名から置換し、それを一時保存する（rename）
            # ↓ ↓
            # 変更後のファイル名に変更して保存（上書き保存）
        
            """

            print('【変換前】', target_files[i][len(path)-1:])
        
            # ファイルを開く
            with open(target_files[i], encoding="utf-8") as f:
                data_lines = f.read()

            # ファイル中身の文字列置換（2か所）
            data_lines = data_lines.replace("06-06", "06-30")
            data_lines = data_lines.replace("0606", "0609")
            
            # ファイル編集適用
            with open(target_files[i], mode="w", encoding="utf-8") as f:
                f.write(data_lines)
            
            # 新しいファイル名を一時保存　1：変更前ファイル名、2：変更後ファイル名、3：対象ファイル
            rename.append(re.sub(old_name, new_name, target_files[i]))
            # rename.append(re.sub(r'8[0-9][0-9]s', '0606', target_files[i]))
            
            # ここを試験的に追加（変更後の名前が既に存在し、重複している場合）
            if os.path.exists(rename[i]):
                # 末尾に「_renamed」を追加する
                os.rename(target_files[i] + '_renamed', rename[i])
            
            # ファイル名変更を適用
            os.rename(target_files[i], rename[i])
        
            # リネーム後を確認
            renamed_files = []
            renamed_folder = glob.glob(path)
            for i in range(len(renamed_folder)):
                if new_name in renamed_folder[i]:
                    renamed_files.append(renamed_folder[i])
                else:
                    continue
            for j in range(len(renamed_files)):
                print('【変換後】', renamed_files[j][len(path)-1:])


    except FileNotFoundError as e:
        # print('変更前ファイル：' + old_name + 'を含むファイルが見つかりませんでした。')
        print(e)
    except OSError as e:
        # print('ファイルパスを確認下さい。')
        print(e)

    
# # 変換後のファイルの名前が既に存在する場合
# # ->末尾に(001)など付ける
# if os.path.exists(rename[i]):
#     
#     save_as_new():
#         with open(rename[i] + '-renamed', mode="w", encoding="utf-8") as f:
#                 f.write(data_lines)
        
#     overwrite():
#         os.rename(target_files[i] + '-renamed', rename[i])

def select_action():
    print('次を選択し操作を選択してください。上書き：1  新規保存：2  ファイルを開く：3  何もせず終了：9')
    sel = input()
    if sel == '1':
        overwrite()
    elif sel == '2':
        save_as_new()
    elif sel == '3':
        view_file()
    elif sel == '9':
        sys.exit()
    else:
        print('入力は"1"又は"2"若しくは"9"のみ有効です。')
        select_action()
        
if __name__ == '__main__':
    print('変更前ファイル名を入力して下さい。')
    var1 = input()
    print('変更後ファイル名を入力して下さい。')
    var2 = input()
    get_args(var1, var2)

    select_action()