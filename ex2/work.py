from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    if m <= 0:
        return None
    
    #初乗りの距離までの料金
    min_kyori = 1700
    min_sum = 610

    #初乗りの距離を超える場合
    if m <= min_kyori:
        return min_sum
    else:
        #追加料金
        add_kyori=m - min_kyori
        add_sum=ceil(add_kyori/315)*80
        total_min=min_sum + add_sum
        return total_min

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


