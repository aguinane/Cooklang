from cooklang.nyum import to_nyum_markdown


def test_nyum_export():
    """Export to NYUM format"""

    example_file = "examples/Easy Pancakes.cook"
    output = to_nyum_markdown(example_file)
    assert "> Serve straightaway with your favourite topping." in output
    assert "* `250 ml` milk" in output
