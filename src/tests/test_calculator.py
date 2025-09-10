"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from calculator import Calculator

def test_get_hello_message():
    calc = Calculator()
    assert calc.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5
    assert calc.last_result == 5

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(7, 4) == 3
    assert calc.last_result == 3

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(6, 5) == 30
    assert calc.last_result == 30

def test_division():
    calc = Calculator()
    assert calc.division(10, 2) == 5
    assert calc.last_result == 5

def test_division_by_zero():
    calc = Calculator()
    assert calc.division(10, 0) == "Erreur : division par zéro"
    assert calc.last_result == "Error"

def test_fail_addition():
    calc = Calculator()
    # Ce test est faux : 2 + 2 != 5
    assert calc.addition(2, 2) == 5