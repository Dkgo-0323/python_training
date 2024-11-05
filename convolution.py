import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return  np.where((t >= 0) & (t <= 3), 1, 0)


# 定义信号 x(t) 和冲激响应 h(t)
t = np.linspace(0, 10, 100)  # 时间向量
x = x(t)  # 输入信号
h = np.exp(-t) * (t >= 0)  # 冲激响应，单位阶跃函数乘以指数衰减

# 计算卷积
y = np.convolve(x, h, mode='full')  # mode='full' 表示返回完整卷积结果
# 计算对应的时间向量
t_conv = np.linspace(0, 20, len(y))

# 绘制结果
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x, label='x(t) - Input Signal')
plt.title('Input Signal x(t)')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, h, label='h(t) - Impulse Response', color='orange')
plt.title('Impulse Response h(t)')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_conv, y, label='y(t) - Convolution Result', color='green')
plt.title('Convolution y(t) = x(t) * h(t)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
