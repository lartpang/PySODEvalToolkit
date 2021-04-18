# -*- coding: utf-8 -*-
import os

import markdown2

html_template = """<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>%s</title>
  <link rel="stylesheet" href="./src/lixiaolai.css" type="text/css" >
  <script src="./src/sort_table.js"></script>
</head>

<body>
%s
</body>

</html>
"""

md_root = "../results"
html_root = "../results/htmls"

md_names = [
    name[:-3]
    for name in os.listdir(md_root)
    if os.path.isfile(os.path.join(md_root, name)) and name.endswith(".md")
]

for md_name in md_names:
    html_body = markdown2.markdown_path(
        os.path.join(md_root, md_name + ".md"),
        extras={"tables": True, "html-classes": {"table": "sortable"}},
    )
    html = html_template % (md_name, html_body)
    with open(os.path.join(html_root, md_name + ".html"), encoding="utf-8", mode="w") as f:
        f.write(html)
