n = int(input())
current_char = ord("A")  # 'A'のASCIIコードを取得

for i in range(n, 0, -1):  # 1からnumまでの数字でループ
    line = ""            # 各行の文字列を初期化
    for j in range(i):   # i回ループして文字を追加
        line = line + chr(current_char)   # ASCIIコードを文字に変換して追加
        current_char = current_char + 1   # 次の文字に移動
    print(line)