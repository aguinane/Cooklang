from cooklang.chowdown import to_chowdown_markdown
from cooklang.nyum import to_nyum_markdown

output = to_nyum_markdown("examples/Easy Pancakes.cook")
with open("examples/nyum.md", "w") as f:
    f.writelines([x + "\n" for x in output])

output = to_chowdown_markdown("examples/Easy Pancakes.cook")
with open("examples/chowdown.md", "w") as f:
    f.writelines([x + "\n" for x in output])
