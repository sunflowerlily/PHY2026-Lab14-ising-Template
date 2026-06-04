import pytest
import sys
import os

class GraderPlugin:
    def __init__(self):
        self.results = {}

    def pytest_runtest_logreport(self, report):
        if report.when == 'call':
            self.results[report.nodeid] = report.passed

def main():
    plugin = GraderPlugin()
    pytest.main(['lab1_core/tests/test_core.py', '-q'], plugins=[plugin])
    
    # 评分权重
    weights = {
        'test_init_lattice': 10,
        'test_delta_E_calculation': 20,
        'test_magnetization': 10,
        'test_metropolis_acceptance': 30
    }
    
    total = 0
    for test, passed in plugin.results.items():
        for key, weight in weights.items():
            if key in test and passed:
                total += weight
                
    print(f"\n--- 自动评分结果 ---")
    print(f"基础功能得分: {total} / 70")
    print(f"Bonus 与 报告得分由人工复核。")

if __name__ == "__main__":
    main()
