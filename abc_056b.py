#NarroeRectanglesEasy

#1つ目の長方形は縦[0, 1]を横は[a, a+W]
#2つ目の長方形は縦[1, 2]を横は[b, b+W]

#2つ目の長方形を横に動かして一つ目の長方形と連結にする
#横に動かさないといけない最小値は？

W, a, b = map(int, input().split())


#3, 1, 3の場合

#横をどれだけ移動すればいいかを考える

#a＋Wとbの距離を合わせる

#長方形1の右端
rectangle1_right_end = a

rectangle1_left_end = a + W

rectangle2_right_end = b

rectangle2_left_end = b + W


#すでに重なっている場合は0を出力それ以外は右端と左端の差を出力
if a < b:
    if b <= a + W:
        print(0)
    else:
        print(rectangle2_right_end - rectangle1_left_end)
elif a > b:
    if rectangle1_right_end <= rectangle2_left_end:
        print(0)
    else:
        print(rectangle1_right_end - rectangle2_left_end)
else:
    print(0)



