# rule30.py
# 规则表：键是三元组拼成的字符串，值是下一代中心格
RULE = {"111": 0, "110": 0, "101": 0, "100": 1,
        "011": 1, "010": 1, "001": 1, "000": 0}

def next_row(row):
    """输入一代（如 [0,1,0,1,0]），输出下一代"""
    extended = [0] + row + [0]          # 两端各补一个0，处理边界
    nxt = []
    for i in range(1, len(extended) - 1):
        # 坑1：把 extended[i-1], extended[i], extended[i+1] 拼成 "101" 这样的字符串
        key = f"{extended[i-1]}{extended[i]}{extended[i+1]}"  # 提示：f"{a}{b}{c}" 是Python的拼接写法
        # 坑2：用 key 查 RULE，把结果 append 进 nxt
        nxt.append(RULE[key])
    return nxt

# 主程序：从"只有一颗黑子"开始，演化 30 代，每代打印成一行（1 画成 #，0 画成 .）
row = [0]*60
row[30] = 1
for _ in range(30):
    # 坑3：打印当前行（提示："".join(("#" if c else ".") for c in row)）
    print("".join(("#" if c else ".") for c in row))
    row = next_row(row)