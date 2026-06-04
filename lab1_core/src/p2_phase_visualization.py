import numpy as np
import matplotlib.pyplot as plt
from p1_ising_engine import init_lattice, metropolis_step

# 解决 macOS 下 Matplotlib 中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def plot_melting_comparison(L=50, temps=[1.5, 2.27, 3.5]):
    """
    任务 B：可视化三个典型温度下的棋盘“融化”过程
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    titles = [f"有序 (T={temps[0]})", f"临界 (T={temps[1]})", f"混乱 (T={temps[2]})"]
    
    for i, T in enumerate(temps):
        beta = 1.0 / T
        spins = init_lattice(L)
        
        # TODO: 演化足够多的 Sweep (建议 1000+)
        # for _ in range(1000):
        #     spins = metropolis_step(spins, beta)
            
        axes[i].imshow(spins, cmap='bwr')
        axes[i].set_title(titles[i], fontsize=14)
        axes[i].axis('off')
        
    plt.tight_layout()
    plt.savefig('ex2_melting.png', dpi=150)
    print("✅ 已生成 ex2_melting.png")
    plt.show()

if __name__ == "__main__":
    plot_melting_comparison()
