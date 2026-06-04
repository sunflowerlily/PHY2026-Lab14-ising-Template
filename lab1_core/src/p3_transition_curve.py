import numpy as np
import matplotlib.pyplot as plt
from p1_ising_engine import init_lattice, metropolis_step, get_magnetization

# 解决 macOS 下 Matplotlib 中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def scan_phase_transition(L=24):
    """
    任务 C：扫描温度，测量平均磁性，画出相变曲线
    """
    T_list = np.linspace(1.0, 3.5, 26)
    m_abs_avg = []
    
    T_c_theory = 2.269
    
    print(f"正在扫描温度 (L={L})...")
    for T in T_list:
        beta = 1.0 / T
        spins = init_lattice(L)
        
        # 1. 预热阶段 (丢弃数据)
        # TODO: 跑若干 Sweep 以达到热平衡 (如 500 次)
        
        # 2. 采样阶段 (记录数据)
        m_samples = []
        # TODO: 跑若干 Sweep 采样 (如 500 次)，记录每次的 abs(m)
        
        m_abs_avg.append(np.mean(m_samples) if m_samples else 0.0)
        print(f"T={T:.2f} done", end='\r')

    # 3. 绘图
    plt.figure(figsize=(8, 6))
    plt.plot(T_list, m_abs_avg, 'o-', label=f'Simulation (L={L})')
    plt.axvline(T_c_theory, color='red', linestyle='--', label=f'Theory Tc ≈ {T_c_theory:.3f}')
    plt.xlabel('温度 T', fontsize=12)
    plt.ylabel('平均磁化强度 <|m|>', fontsize=12)
    plt.title('Ising 模型相变曲线', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('ex3_transition.png', dpi=150)
    print("\n✅ 已生成 ex3_transition.png")
    plt.show()

if __name__ == "__main__":
    scan_phase_transition()
