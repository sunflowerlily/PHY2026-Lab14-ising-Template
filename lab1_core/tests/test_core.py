import pytest
import numpy as np
import sys
import os

# 将 src 加入路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from p1_ising_engine import init_lattice, delta_E, get_magnetization, metropolis_step

def test_init_lattice():
    L = 10
    spins = init_lattice(L)
    assert spins.shape == (10, 10)
    assert set(np.unique(spins)).issubset({-1, 1})

def test_delta_E_calculation():
    # 测试能量计算是否正确
    # 全向上的构型，中心翻转
    spins = np.ones((5, 5))
    # 翻转 (2,2) 处的 +1，它的 4 个邻居都是 +1
    # dE = 2 * J * s * sum(nb) = 2 * 1 * 1 * 4 = 8
    de = delta_E(spins, 2, 2, J=1.0)
    assert de == 8.0

def test_magnetization():
    spins = np.array([[1, -1], [1, 1]])
    assert get_magnetization(spins) == 0.5

def test_metropolis_acceptance():
    """
    物理判据测试：
    在极低温度下 (beta -> inf)，如果 dE > 0，不应接受翻转。
    """
    # 创建一个全向上的构型
    spins = np.ones((10, 10))
    # 极低温度
    beta = 1000.0
    # 尝试演化（模板中此时逻辑应为空，故 test 会通过，但学生实现错误时会被拦截）
    new_spins = metropolis_step(spins.copy(), beta)
    
    # 检查：如果是基态且温度极低，不应跳出
    # 注意：如果学生还没写逻辑，new_spins == spins，也会通过。
    # 只有当学生写错了逻辑（如符号写反）时，此项才会失败。
    assert np.all(new_spins == 1.0), "在极低温度下，系统不应从基态自发跳出（Metropolis 判据可能写反了）"
