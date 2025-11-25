import pytest
from sys import stderr
from q2 import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

q2_testcases = [
    {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}
]   

# @pytest.mark.parametrize("result", question2_testcases)
# def test_question2(capsys, result):
#     q2()
#     captured, _ = capsys.readouterr()
#     assert captured[:-1] == result

@pytest.mark.parametrize("result", q2_testcases)
def test_q2(result):
    assert q_2() == result