import pytest

from postikasittely import kasittely


def test_kasittely_yksi():
    assert len(kasittely('korvatunturi')) == 1


def test_kasittely_yhtaan():
    assert len(kasittely('Los Angeles')) == 0


def test_kasittely_monta():
    assert len(kasittely('järvenpää')) == 7


def test_kasittely_vali():
    assert len(kasittely('smart post')) == len(kasittely('smartpost'))
