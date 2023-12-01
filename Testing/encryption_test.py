from Encryption import *
import pytest

def test_empty_string_encrypt():
    test = encrypt("")
    assert test == ""

def test_positive_case_encrypt():
    test = encrypt("admin")
    assert test == "ckakn"

def test_negative_case_encrypt():
    with pytest.raises(ValueError):
        encrypt("Adm1n")

def test_empty_string_decrypt():
    test = decrypt("")
    assert test == ""

def test_positive_case_decrypt():
    test = decrypt("ckakn")
    assert test == "admin"

def test_negative_case_decrypt():
    with pytest.raises(ValueError):
        encrypt("Adm1n")