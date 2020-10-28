# 2019F問題
# 文字列Sが与えられる。これは、1つ以上の単語を (間に空白などを挟まずに) 連結したものである。
# ここで、各単語は2文字以上であり、最初の文字と最後の文字のみが英大文字、それ以外の文字は全て英小文字である。
# これらの単語を辞書順に並べ (大文字小文字の違いは無視する)、同様に連結して出力するプログラムを作成せよ。
# 例えば、S=FisHDoGCaTAAAaAAbCACとする。これは FisH, DoG, CaT, AA, AaA, AbC, ACの7つの単語を連結したものである。
# これらを辞書順に並べると AA, AaA, AbC, AC, CaT, DoG, FisH となるため、AAAaAAbCACCaTDoGFisH と出力すればよい。

S1 = input("文字列を入力してください >>> ")
S2 = []
checker = 0

for i in range(len(S1)):
    S2.append(S1[i])
    if S1[i].isupper():
        checker += 1
    if checker%2==0:
        S2.append(',')

S2 = "".join(S2)
S2 = S2.split(',')
del S2[-1]
S2 = sorted(S2,key = str.lower)
print(''.join(S2))
