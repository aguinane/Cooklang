from cooklang.chowdown import to_chowdown_markdown


def test_chowdown_export():
    """Export to Chowdown format"""

    example_file = "examples/Easy Pancakes.cook"
    output = to_chowdown_markdown(example_file)
    assert "layout: recipe" in output
    assert "- Serve straightaway with your favourite topping." in output
    assert "- 250 ml milk" in output
