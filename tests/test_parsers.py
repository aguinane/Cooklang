from cooklang.parser import parse_cookware, parse_ingredient, parse_timer
from cooklang.parser import find_cookware, find_ingredients, find_timers


def test_parse_cookware():
    assert parse_cookware("#pot") == {"type": "cookware", "name": "pot", "quantity": ""}
    assert parse_cookware("#potato masher{}") == {
        "type": "cookware",
        "name": "potato masher",
        "quantity": "",
    }


def test_find_cookware():
    assert find_cookware("Blend things in a #blender") == ['#blender']
    assert find_cookware("Mash things with a #potato masher{} for a bit") == ['#potato masher{}']


def test_parse_ingredient():
    assert parse_ingredient("@salt") == {
        "type": "ingredient",
        "name": "salt",
        "quantity": "some",
        "units": "",
    }
    assert parse_ingredient("@milk{4%cup}") == {
        "type": "ingredient",
        "name": "milk",
        "quantity": "4",
        "units": "cup",
    }


def test_find_ingredients():
    assert find_ingredients("Add @salt to the thing") == ['@salt']
    assert find_ingredients("Add @milk{4%cup}") == ['@milk{4%cup}']


def test_parse_timer():
    assert parse_timer("~{25%minutes}") == {
        "type": "timer",
        "name": "",
        "quantity": "25",
        "units": "minutes",
    }
    assert parse_timer("~eggs{3%minutes}") == {
        "type": "timer",
        "name": "eggs",
        "quantity": "3",
        "units": "minutes",
    }

def test_find_timers():
    assert find_timers("Do thing for ~{25%minutes}") == ['~{25%minutes}']
    assert find_timers("Do thing for ~eggs{3%minutes} and stop") == ['~eggs{3%minutes}']


