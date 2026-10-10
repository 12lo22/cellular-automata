import matplotlib
matplotlib.use("Agg")   # 只保存文件不弹窗，避免窗口卡住流程
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# —— Rule 30 规则表 ——
RULE = {
    "111": 0, "110": 0, "101": 0, "100": 1,
    "011": 1, "010": 1, "001": 1, "000": 0
}

def next_row(row):
    """输入一代，输出下一代"""
    extended = [0] + row + [0]
    nxt = []
    for i in range(1, len(extended) - 1):
        key = f"{extended[i-1]}{extended[i]}{extended[i+1]}"
        nxt.append(RULE[key])
    return nxt

# —— 第一步：预生成 30 代 ——
history = []
row = [0] * 60
row[30] = 1
for _ in range(30):
    history.append(list(row))
    row = next_row(row)

grid = np.array(history)   # 关键：升成二维 (30行 × 60列)，imshow 要的是"面"不是"线"

# —— 第二步：逐帧动画 ——
fig, ax = plt.subplots()
ax.set_axis_off()
img = ax.imshow(np.zeros_like(grid), cmap="Greys", vmin=0, vmax=1, animated=True)

def update(frame):
    canvas = np.zeros_like(grid)          # 全零画布，和图片同形状
    canvas[:frame + 1] = grid[:frame + 1] # 前 frame+1 行填真实数据 → 图案逐行往下长
    img.set_data(canvas)
    return [img]

ani = animation.FuncAnimation(fig, update, frames=len(history), interval=100, blit=True)
ani.save("rule30.gif", writer="pillow")
print("saved!")