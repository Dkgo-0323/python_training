import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用SimHei字体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 参数设置
g = 9.81  # 重力加速度 (m/s^2)
m = 0.2  # 手机质量 (kg)
k = 0.1  # 阻力系数 (kg/s)

# 时间范围
t_max = 60  # 最大时间 (s)
dt = 0.01  # 时间步长 (s)
time = np.arange(0, t_max, dt)

# 计算速度和位移
alpha = k / m
v = (m * g / k) * (1 - np.exp(-alpha * time))
s = (m * g / k) * (time - (m / k) * (1 - np.exp(-alpha * time)))

# 绘制速度和位移图
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, v, label='速度 (m/s)')
plt.xlabel('时间 (s)')
plt.ylabel('速度 (m/s)')
plt.title('手机下沉速度随时间变化')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, s, label='位移 (m)', color='orange')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.title('手机下沉深度随时间变化')
plt.legend()

plt.tight_layout()
plt.show()
