# -*- coding: utf-8 -*-
import os

import markdown2

index_template = """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>{html_title}</title>
    <link rel="stylesheet" href="./src/lixiaolai.css" type="text/css" >
</head>

<body>
    <p>{html_urls}</p>
    {html_body}
</body>

</html>
"""

html_template = """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>{html_title}</title>
    <link rel="stylesheet" href="./src/lixiaolai.css" type="text/css" >
    <script src="./src/sort_table.js"></script>
</head>

<body>
    <p>{html_urls}</p>
    {html_body}
</body>

</html>
"""
list_item_template = "<li><a href='./{html_name}.html'>{item_name}</a></li>"


def save_html(html_text, html_path):
    with open(html_path, encoding="utf-8", mode="w") as f:
        f.write(html_text)


md_root = "../results"
html_root = "../results/htmls"

md_names = [
    name[:-3]
    for name in os.listdir(md_root)
    if os.path.isfile(os.path.join(md_root, name)) and name.endswith(".md")
]

url_list = "\n".join(
    ["<ul>"]
    + [list_item_template.format(html_name=name, item_name=name.upper()) for name in md_names]
    + ["</ul>"]
)

index_html = index_template.format(html_title="Index", html_urls=url_list, html_body="Updating...")
save_html(html_text=index_html, html_path=os.path.join(html_root, "index.html"))

for md_name in md_names:
    html_body = markdown2.markdown_path(
        os.path.join(md_root, md_name + ".md"),
        extras={"tables": True, "html-classes": {"table": "sortable"}},
    )
    html = html_template.format(html_title=md_name, html_urls=url_list, html_body=html_body)
    save_html(html_text=html, html_path=os.path.join(html_root, md_name + ".html"))
