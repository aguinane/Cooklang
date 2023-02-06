"""
Export recipe in Chowdown markdown format
https://github.com/clarklab/chowdown
"""

from pathlib import Path

from cooklang import Recipe


def to_chowdown_markdown(file_path: Path) -> list[str]:
    r = Recipe(file_path)
    ast = r.ast
    title = r.title
    description = r.metadata.get("description", "")
    output = []

    metadata = ast["metadata"]
    steps = ast["steps"]

    output.append("---")
    output.append("layout: recipe")
    output.append(f"title: {title}")
    for key, value in metadata.items():
        output.append(f"{key}: {value}")

    output.append(" ")
    output.append("ingredients:")
    for item in ast["ingredients"]:
        name = item["name"]
        quantity = f"{item['quantity']} {item['units']}".strip()
        ingredient = f"- {quantity} {name}" if quantity else name
        output.append(ingredient)

    output.append(" ")
    output.append("directions:")

    for step in steps:
        method = ""
        for item in step:
            if item["type"] == "text":
                method += item["value"]
            elif item["type"] == "cookware":
                method += item["name"]
            elif item["type"] == "ingredient":
                name = item["name"]
                quantity = f"{item['quantity']} {item['units']}".strip()
                ingredient = f"`{quantity}` {name}" if quantity else name
                method += name
        output.append(f"- {method}")

    output.append("")
    output.append("---")

    output.append("")
    output.append(description)

    return output
