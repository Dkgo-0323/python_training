import numpy as np
import matplotlib.pyplot as plt

# 参数设置
g = 9.81  # 重力加速度 (m/s^2)
m = 0.2  # 手机质量 (kg)
k = 0.1  # 阻力系数 (kg/s)
v_flow = 1.0  # 运河流速 (m/s)

# 时间范围
t_max = 60  # 最大时间 (s)
dt = 0.01  # 时间步长 (s)
time = np.arange(0, t_max, dt)

# 计算垂直方向速度和位移
alpha = k / m
v_y = (m * g / k) * (1 - np.exp(-alpha * time))
s_y = (m * g / k) * (time - (m / k) * (1 - np.exp(-alpha * time)))

# 计算水平方向位移
v_x = v_flow * time
s_x = v_flow * time

# 绘制水平和垂直位移图
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, v_y, label='垂直速度 (m/s)')
plt.xlabel('时间 (s)')
plt.ylabel('速度 (m/s)')
plt.title('手机垂直下沉速度随时间变化')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, s_y, label='垂直位移 (m)', color='orange')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.title('手机垂直下沉深度随时间变化')
plt.legend()

plt.tight_layout()
plt.show()

# 绘制手机在水中的运动轨迹
plt.figure(figsize=(12, 6))
plt.plot(s_x, s_y, label='手机运动轨迹')
plt.xlabel('水平位移 (m)')
plt.ylabel('垂直位移 (m)')
plt.title('手机在水中的运动轨迹')
plt.legend()
plt.grid(True)
plt.show()
