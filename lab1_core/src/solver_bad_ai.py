import numpy as np

"""
AI 辅助生成的 Metropolis 核心逻辑 (含有隐蔽的物理毒药)
提示：这段代码语法完全正确，甚至能跑出“有序”和“混乱”的区别。
但在处理关键的 Metropolis 判据时，AI 犯了一个计算物理的“常识性”错误。
"""

def bad_ai_metropolis(spins, beta, J=1.0):
    L = spins.shape[0]
    for _ in range(L * L):
        i, j = np.random.randint(0, L, size=2)
        
        # 计算能量差 dE
        nb = (spins[(i+1)%L, j] + spins[(i-1)%L, j] + 
              spins[i, (j+1)%L] + spins[i, (j-1)%L])
        dE = 2 * J * spins[i, j] * nb
        
        # AI 漏洞点：判断逻辑
        # 正确逻辑是：如果 dE <= 0，接受；否则以 exp(-beta*dE) 概率接受。
        # 此处 AI “自作聪明”地将判断改成了：
        if dE <= 0:
            spins[i, j] *= -1
        elif np.random.random() < np.exp(beta * dE): # 错误：指数符号写反了
            spins[i, j] *= -1
            
    return spins

if __name__ == "__main__":
    # 如果运行这段代码，你会发现系统在高温下也会“强行磁化”，
    # 或者在低温下无法稳定。请分析为什么。
    pass
