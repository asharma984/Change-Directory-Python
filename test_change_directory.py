import pytest
from change_directory import ChangeDirectory

def test_change_directory():
    current6 = "/"
    change6 = "abc"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc"

def test_change_directory_2():
    current6 = "/abc/def"
    change6 = "ghi"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc/def/ghi"

def test_change_directory_3():
    current6 = "/abc/def"
    change6 = ".."
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc"

def test_change_directory_4():
    current6 = "/abc/def"
    change6 = "/abc"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc"

def test_change_directory_5():
    current6 = "/abc/def"
    change6 = "/abc/klm"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc/klm"

def test_change_directory_6():
    current6 = "/abc/def"
    change6 = "../.."
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/"

def test_change_directory_7():
    current6 = "/abc/def"
    change6 = "../../.."
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/"

def test_change_directory_8():
    current6 = "/abc/def"
    change6 = "."
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc/def"

def test_change_directory_9():
    current6 = "/abc/def"
    change6 = "..klm"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "No Such Directory Exist."

def test_change_directory_10():
    current6 = "/abc/def"
    change6 = "//////"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/"  

def test_change_directory_11():
    current6 = "/abc/def"
    change6 = "......"
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "No Such Directory Exist."  

def test_change_directory_12():
    current6 = "/abc/def"
    change6 = "../gh///../klm/."
    cd = ChangeDirectory()
    output = cd.change_directory(current6, change6)
    assert output == "/abc/klm"      

