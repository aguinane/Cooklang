"""
Export recipe in nyum markdown format
https://github.com/doersino/nyum
"""

from pathlib import Path

from cooklang import Recipe


def to_nyum_markdown(file_path: Path) -> list[str]:
    r = Recipe(file_path)
    ast = r.ast
    title = r.title
    output = []

    metadata = ast["metadata"]
    steps = ast["steps"]

    output.append("---")
    output.append(f"title: {title}")
    for key, value in metadata.items():
        output.append(f"{key}: {value}")

    output.append("---")
    output.append("")

    for step in steps:
        output.append("")
        method = ""
        ingredients = []
        for item in step:
            if item["type"] == "text":
                method += item["value"]
            elif item["type"] == "cookware":
                method += item["name"]
            elif item["type"] == "ingredient":
                name = item["name"]
                quantity = f"{item['quantity']} {item['units']}".strip()
                ingredient = f"`{quantity}` {name}" if quantity else name
                ingredients.append(ingredient)
                method += name

        if ingredients:
            for x in ingredients:
                output.append(f"* {x}")
            output.append("")

        output.append(f"> {method}")
        output.append("")
        output.append("---")

    del output[-1]  # remove last line break

    return output
