import pytest
from sys import stderr
from q1 import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

res_1a = [{'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}]
res_1b = [True] 
res_1c = [False]
res_1d = [{'value': 4, 'left': {}, 'right': {}}]
res_1e = [{'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}]
res_1f = [{'value': 94, 'left': {}, 'right': {}}]
res_1g = [{'value': 66, 'left': {}, 'right': {}}]
res_1h = [[4, 50, 61, 66, 68, 76, 82, 88, 89, 94]]
res_1i = [[68, 61, 50, 4, 66, 88, 76, 82, 89, 94]]
res_1j = [[4, 50, 66, 61, 82, 76, 94, 89, 88, 68]]
res_1k = [82]

bst = res_1a[0]

@pytest.mark.parametrize("result", res_1a)
def test_q1a(result):
    assert q_1a() == result

@pytest.mark.parametrize("result", res_1b)
def test_q1b(result):
    assert q_1b(bst) == result

@pytest.mark.parametrize("result", res_1c)
def test_q1c(result):
    assert q_1c(bst) == result

@pytest.mark.parametrize("result", res_1d)
def test_q1d(result):
    assert q_1d(bst) == result

@pytest.mark.parametrize("result", res_1e)
def test_q1e(result):
    assert q_1e(bst) == result

@pytest.mark.parametrize("result", res_1f)
def test_q1f(result):
    assert q_1f(bst) == result

@pytest.mark.parametrize("result", res_1g)
def test_q1g(result):
    assert q_1g(bst) == result

@pytest.mark.parametrize("result", res_1h)
def test_q1h(result):
    assert q_1h(bst) == result

@pytest.mark.parametrize("result", res_1i)
def test_q1i(result):
    assert q_1i(bst) == result

@pytest.mark.parametrize("result", res_1j)
def test_q1j(result):
    assert q_1j(bst) == result

@pytest.mark.parametrize("result", res_1k)
def test_q1k(result):
    assert q_1k(bst) == result