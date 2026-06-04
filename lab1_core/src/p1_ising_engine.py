import numpy as np
import matplotlib.pyplot as plt

# 解决 macOS 下 Matplotlib 中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def init_lattice(L):
    """
    任务 A：初始化 L x L 的随机自旋矩阵，取值为 +1 或 -1
    """
    return np.random.choice([-1, 1], size=(L, L))

def delta_E(spins, i, j, J=1.0):
    """
    任务 A：计算翻转 (i, j) 处自旋引起的能量变化 dE
    使用周期性边界条件
    dE = 2 * J * s_ij * sum(neighbors)
    """
    L = spins.shape[0]
    s = spins[i, j]
    # TODO: 获取上下左右四个邻居 (注意取模实现周期性)
    # neighbors = ...
    # return 2 * J * s * neighbors
    return 0.0

def metropolis_step(spins, beta, J=1.0):
    """
    任务 A：执行一个完整 Sweep（尝试翻转 L*L 次）
    """
    L = spins.shape[0]
    for _ in range(L * L):
        # 1. 随机挑选一个格点
        i, j = np.random.randint(0, L, size=2)
        
        # 2. 计算翻转该点所需的能量代价 dE
        de = delta_E(spins, i, j, J)
        
        # 3. Metropolis 判据：接受或拒绝翻转
        # TODO: 补全判据
        # if ...
        pass
    return spins

def get_magnetization(spins):
    """计算平均磁化强度 m"""
    return np.mean(spins)

if __name__ == "__main__":
    L = 20
    T_low, T_high = 1.0, 4.0
    
    print(f"--- 练习 1 验证 (L={L}) ---")
    for T in [T_low, T_high]:
        beta = 1.0 / T
        spins = init_lattice(L)
        # 演化 500 个 sweep
        for _ in range(500):
            spins = metropolis_step(spins, beta)
        m = get_magnetization(spins)
        print(f"温度 T={T:.1f}: 平均磁化强度 m = {m:.4f}, |m| = {abs(m):.4f}")
