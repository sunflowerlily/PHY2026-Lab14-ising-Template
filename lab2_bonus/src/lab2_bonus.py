import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 确保能导入 lab1_core 中的辅助函数
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lab1_core/src')))
from p1_ising_engine import init_lattice, get_magnetization

def delta_E_with_field(spins, i, j, J=1.0, h=0.0):
    """
    Lab2 Bonus: 计算包含外场 h 的能量差
    dE = 2 * s_ij * (J * sum(neighbors) + h)
    """
    L = spins.shape[0]
    s = spins[i, j]
    # TODO: 实现包含外磁场的能量差计算
    return 0.0

def metropolis_step_with_field(spins, beta, J=1.0, h=0.0):
    """
    Lab2 Bonus: 包含外场的 Metropolis 演化
    """
    L = spins.shape[0]
    # TODO: 实现包含外磁场的 Metropolis 演化
    return spins

def hysteresis_loop(L=32, T=1.5):
    """
    Lab2 Bonus: 磁滞回线模拟
    磁场 h 从 2.0 -> -2.0 -> 2.0
    """
    h_axis = np.concatenate([np.linspace(2.0, -2.0, 50), np.linspace(-2.0, 2.0, 50)])
    m_history = []
    
    spins = np.ones((L, L)) # 从饱和磁化开始
    
    print(f"开始模拟磁滞回线 (T={T})...")
    # TODO: 循环 h，利用 metropolis_step_with_field 演化并记录平均磁化强度
    
    return h_axis, m_history

if __name__ == "__main__":
    # h, m = hysteresis_loop()
    # plt.plot(h, m)
    # plt.show()
    pass
