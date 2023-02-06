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
    assert "steps" in ast
    assert len(ast["steps"]) > 0
