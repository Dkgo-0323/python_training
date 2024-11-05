import numpy as np
import matplotlib.pyplot as plt

# 参数设置
g = 9.81  # 重力加速度 (m/s^2)
m = 0.005  # 身份证质量 (kg)
k = 0.01  # 阻力系数 (kg/s)
rho_water = 1000  # 水的密度 (kg/m^3)
V = 0.00001  # 身份证体积 (m^3)

# 时间范围
t_max = 60  # 最大时间 (s)
dt = 0.01  # 时间步长 (s)
time = np.arange(0, t_max, dt)

# 计算速度和位移
effective_weight = (m - rho_water * V) * g
v = (effective_weight / k) * (1 - np.exp(-k * time / m))
s = (effective_weight / k) * (time - (m / k) * (1 - np.exp(-k * time / m)))

# 绘制速度和位移图
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, v, label='速度 (m/s)')
plt.xlabel('时间 (s)')
plt.ylabel('速度 (m/s)')
plt.title('身份证下沉速度随时间变化')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, s, label='位移 (m)', color='orange')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.title('身份证下沉深度随时间变化')
plt.legend()

plt.tight_layout()
plt.show()
