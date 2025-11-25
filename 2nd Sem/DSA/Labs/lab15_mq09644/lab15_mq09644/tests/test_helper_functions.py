import pytest
from helper_functions import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

insert_testcases = [
    ({}, 5, {"value": 5, "left": {}, "right": {}}),
    ({"value": 10, "left": {}, "right": {}}, 5, {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}),
    ({"value": 5, "left": {}, "right": {}}, 10, {"value": 5, "left": {}, "right": {"value": 10, "left": {}, "right": {}}}),
    ({"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}, 2, {"value": 10, "left": {"value": 5, "left": {"value": 2, "left": {}, "right": {}}, "right": {}}, "right": {}})
    ]

exist_testcases = [
    ({}, 5, False),
    ({"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}, 5, True),
    ({"value": 5, "left": {}, "right": {}}, 10, False),
    ({"value": 10, "left": {"value": 5, "left": {"value": 2, "left": {}, "right": {}}, "right": {}}, "right": {}}, 2, True)
    ]

G = {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}

minimum_testcases = [
    (G, 89, {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}),
    (G, 50, {'value': 4, 'left': {}, 'right': {}}),
    (G, 76, {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}),
    (G, 68, {'value': 4, 'left': {}, 'right': {}})
]

mimaximum_testcases = [
    (G, 61, {'value': 66, 'left': {}, 'right': {}}),
    (G, 68, {'value': 94, 'left': {}, 'right': {}}),
    (G, 89, {'value': 94, 'left': {}, 'right': {}}),
    (G, 50, {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}})
]

G1 = {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {"value": 15, "left": {}, "right": {}}}
G2 = {"value": 20, "left": {"value": 10, "left": {"value": 5, "left": {}, "right": {}}, "right": {}}, "right": {"value": 30, "left": {}, "right": {}}}
G3 = {"value": 5, "left": {}, "right": {"value": 10, "left": {"value": 8, "left": {}, "right": {}}, "right": {"value": 15, "left": {}, "right": {}}}}
G4 = {"value": 10, "left": {"value": 5, "left": {"value": 2, "left": {}, "right": {}}, "right": {"value": 8, "left": {}, "right": {}}}, "right": {"value": 15, "left": {"value": 12, "left": {}, "right": {}}, "right": {"value": 18, "left": {}, "right": {}}}}
G5 = {'value': 68, 'left': {'value': 61, 'left': {'value': 50, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {}}, 'right': {'value': 66, 'left': {}, 'right': {}}}, 'right': {'value': 88, 'left': {'value': 76, 'left': {}, 'right': {'value': 82, 'left': {}, 'right': {}}}, 'right': {'value': 89, 'left': {}, 'right': {'value': 94, 'left': {}, 'right': {}}}}}
G6 = {}

inorder_testcases = [
    (G1,  [5, 10, 15]),
    (G2,  [5, 10, 20, 30]),
    (G3,  [5, 8, 10, 15]),
    (G4,  [2, 5, 8, 10, 12, 15, 18]),
    (G5,  [4, 50, 61, 66, 68, 76, 82, 88, 89, 94]), 
    (G6,  []), 
]

preorder_testcases = [
    (G1,  [10, 5, 15]),
    (G2,  [20, 10, 5, 30]),
    (G3,  [5, 10, 8, 15]),
    (G4,  [10, 5, 2, 8, 15, 12, 18]),
    (G5,  [68, 61, 50, 4, 66, 88, 76, 82, 89, 94]), 
    (G6,  []), 
]

postorder_testcases = [
    (G1,  [5, 15, 10]),
    (G2,  [5, 10, 30, 20]),
    (G3,  [8, 15, 10, 5]),
    (G4,  [2, 8, 5, 12, 18, 15, 10]),
    (G5,  [4, 50, 66, 61, 82, 76, 94, 89, 88, 68]), 
    (G6,  []), 
]

successor_testcases = [
    (G1, 5, 10),
    (G1, 10, 15),
    (G2, 20, 30),
    (G2, 10, 20),
    (G2, 5, 10),
    (G3, 5, 8),
    (G3, 8, 10),
    (G3, 10, 15),
    (G4, 2, 5),
    (G4, 5, 8),
    (G5, 61, 66),
    (G5, 66, 68),
    (G5, 94, None),
    (G5, 4, 50),
]

@pytest.mark.parametrize("BST,key,result", insert_testcases)
def test_insert(BST, key, result):
    insert(BST, key)
    assert BST == result

@pytest.mark.parametrize("BST,key,result", exist_testcases)
def test_exist(BST, key, result):
    assert exist(BST, key) == result

@pytest.mark.parametrize("BST,root,result", minimum_testcases)
def test_minimum(BST, root, result):
    assert minimum(BST, root) == result

@pytest.mark.parametrize("BST,root,result", mimaximum_testcases)
def test_maximum(BST, root, result):
    assert maximum(BST, root) == result

@pytest.mark.parametrize("BST,result", inorder_testcases)
def test_inorder(BST, result):
    x = []
    inorder_traversal(BST, x)
    assert x == result

@pytest.mark.parametrize("BST,result", preorder_testcases)
def test_preorder(BST, result):
    x = []
    preorder_traversal(BST, x)
    assert x == result

@pytest.mark.parametrize("BST,result", postorder_testcases)
def test_postorder(BST, result):
    x = []
    postorder_traversal(BST, x)
    assert x == result

@pytest.mark.parametrize("BST,key,result", successor_testcases)
def test_successor(BST, key, result):
    x = successor(BST, key)
    assert x == result