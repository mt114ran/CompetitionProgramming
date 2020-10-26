# 2019E問題
# あなたは、N人のユーザが参加する SNS を運営している。彼らはユーザ1,…,Nと呼ばれ、別のユーザを何人でもフォローすることができる。
# しかし、あるトラブルにより、どのユーザがどのユーザをフォローしているかの情報がすべて失われてしまった。
# 幸い、ユーザがこの SNS で行ったすべての操作のログが残っており、あなたは操作ログをもとにフォロー状況を復元しようとしている。
# 操作ログはQ行からなり、そのi行目(1≦i≦Q)は文字列Siである。各ユーザは以下の3種類の操作を行うことができ、
# SiはSNS全体で i番目に行われた操作に対応する。
# フォロー: ユーザaがユーザb(a≠b)をフォローする。
# ログには 1 a b という行が記載される。
# フォロー全返し: ユーザ aが、その時点でユーザaをフォローしているユーザ全員をフォローする。
# ログには 2 a という行が記載される。
# フォローフォロー: その時点でユーザaがフォローしている各ユーザxに対し、ユーザ aが次を行う
# 「その時点でユーザxがフォローしているすべてのユーザ (ユーザa自身を除く) をフォローする」。
# ログには 3 a という行が記載される。
# なお、この SNS が開設された時点では、どのユーザも誰もフォローしていなかった。
# また、ユーザaがユーザbを既にフォローしているとき、ユーザaがユーザbを再びフォローしても何も起こらない。
# フォロー状況を復元せよ。
# 各i,j(1≤i,j≤N)に対し、ユーザiがユーザjをフォローしているときfij='Y',そうでないときfij='N'として、以下の形式で出力せよ。

Num,Q = (int(x) for x in input().split())

follow_list = [['N'] * Num for i in range(Num)]
# follow_list = [['N'] * Num] * Num
# 変更前の宣言だとアドレスが一緒になってしまう

for i in range(Q):
    log = [0,0,0]
    log = input().split()
    if log[0] == '1':
        follow_list[int(log[1])-1][int(log[2])-1] = 'Y'
    if log[0] == '2':
        for s in range(Num):
            if not s+1 == int(log[1]):
                if follow_list[s][int(log[1])-1] == 'Y':
                    follow_list[int(log[1])-1][s] = 'Y'
    if log[0] == '3':
        for l in range(Num):
            if follow_list[int(log[1])-1][l] == 'Y':
                for m in range(Num):
                    if follow_list[l][m] == 'Y':
                        follow_list[int(log[1])-1][m] = 'Y'

for  i in range(Num):
    follows = " ".join(follow_list[i])
    print(follows)