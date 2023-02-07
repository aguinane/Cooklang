"""
Export recipe in nyum markdown format
https://github.com/doersino/nyum
"""

from pathlib import Path
from shutil import copy

import frontmatter

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


def from_nyum_markdown(file_path: Path) -> list[str]:
    with open(file_path) as fh:
        metadata, content = frontmatter.parse(fh.read())

    output = []
    desc = metadata.get("description", "")
    if desc:
        output.append(f">> description: {desc}")
    output.append("")
    steps = content.split("---")
    for step in steps:
        step_output = ""
        step = step.replace("> ", "")
        lines = step.split("\n")
        for line in lines:
            if line and line[0] == "*":
                if "`" in line:
                    x = line.split("`")
                    quantity = x[1].strip()
                    if len(x) > 2:
                        ingredient = x[2].strip()
                        cook_ingr = "@" + ingredient + "{" + quantity + "}"
                    else:
                        ingredient = quantity
                        cook_ingr = "@" + ingredient + "{}"
                else:
                    ingredient = line.replace("* ", "").strip()
                    cook_ingr = "@" + ingredient + "{}"
                step_output += cook_ingr + " "
            else:
                if line:
                    step_output += line + " "
        output.append(step_output)
        output.append("")

    return metadata, output


def migrate_nyum_to_cook(nyum_dir: Path, output_dir: Path):
    """Migrate a directory of nyum recipes to cook files"""
    for file_path in nyum_dir.glob("*.md"):
        meta, output = from_nyum_markdown(file_path)
        title = meta["title"]
        category = meta["category"]
        category_dir = output_dir / category
        category_dir.mkdir(exist_ok=True, parents=True)
        cook_path = category_dir / f"{title}.cook"

        img_path = file_path.with_suffix(".jpg")
        if img_path.exists():
            cook_img_path = category_dir / f"{title}.jpg"
            copy(img_path, cook_img_path)

        with open(cook_path, "w") as f:
            f.writelines([x + "\n" for x in output])
