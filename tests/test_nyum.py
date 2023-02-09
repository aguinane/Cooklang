from cooklang.nyum import from_nyum_markdown, to_nyum_markdown


def test_nyum_export():
    """Export to NYUM format"""

    example_file = "examples/Easy Pancakes.cook"
    output = to_nyum_markdown(example_file)
    assert "> Serve straightaway with your favourite topping." in output
    assert "* `250 ml` milk" in output


def test_nyum_import():
    """Import to NYUM format"""
    example_file = "examples/cheesebuldak.md"
    metadata, output = from_nyum_markdown(example_file)
    assert "description" in metadata
    assert "Garnish with the spring onion slices and serve. " in output
