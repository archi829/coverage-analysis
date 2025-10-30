# 🧪 Test Coverage Trade-Offs

## 📘 Overview

This repository explores the trade-offs between writing **many tests for high coverage** and writing **fewer, high-quality tests**.  
It discusses how teams can balance **coverage goals**, **testing effort**, and **long-term maintainability**.

---

## ⚖️ Trade-Off Summary

| Approach                     | ✅ Pros                                                                               | ⚠️ Cons                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **More Tests for Coverage**  | • Achieves high coverage (100% looks impressive)<br>• Catches many small/simple bugs | • Time-consuming to write, run, and maintain<br>• Can include redundant or low-value tests |
| **Fewer High-Quality Tests** | • Easier to maintain<br>• Focuses effort on critical or complex code areas           | • Lower coverage percentage<br>• May miss bugs in simpler, untested lines                  |

---

## 💡 Key Insight

High coverage doesn’t always mean high quality.  
The best testing strategy gives **confidence in correctness** with **minimal redundancy**.

---

## 🧭 Best Practices

* Focus on **critical paths** and **complex logic** first.  
* Treat coverage as a **guideline**, not a strict target.  
* Continuously refactor or remove unnecessary tests.  
* Automate testing and reporting where possible.

---

## 📂 Repository Contents

* `tradeoff_summary.md` — Summary table and explanation  
* `examples/` — Illustrations of both testing approaches  
* `README.md` — This file  

---

## 🧩 Example Code

Below are two sample test styles showing the difference between **high coverage** and **high-value** testing approaches.

### 🔹 Example 1 — High Coverage Style

```python
# test_calculator_high_coverage.py
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
def test_subtract():
    assert subtract(5, 3) == 2
def test_multiply():
    assert multiply(2, 3) == 6
def test_divide():
    assert divide(10, 2) == 5
