import json

import pytest

from cooklang import Recipe

TEST_FILES = [
    "examples/Easy Pancakes.cook",
    "examples/Mixed Berry Smoothie.cook",
]


@pytest.mark.parametrize("example_file", TEST_FILES)
def test_import_recipe(example_file):
    """Read in recipe files and generate AST"""

    r = Recipe(example_file)
    ast = r.ast
    assert "metadata" in ast
    assert "ingredients" in ast
    assert "cookware" in ast
    assert "steps" in ast
    assert len(ast["steps"]) > 0


def test_smoothie_recipe():
    """Read in recipe files and generate AST"""

    r = Recipe("examples/Mixed Berry Smoothie.cook")

    with open("examples/smoothie.json") as fh:
        example_ast = json.load(fh)

    assert r.ast["metadata"] == example_ast["metadata"]
    assert r.ast["ingredients"] == example_ast["ingredients"]
    assert r.ast["cookware"] == example_ast["cookware"]
