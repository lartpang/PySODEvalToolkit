# Useful tools

## `check_path.py`

通过将json中的信息与实际系统中的路径进行匹配，检验是否存在异常。

## `info_py_to_json.py`

将基于python格式的配置文件转化为更便携的json文件。

```shell
$ python info_py_to_json.py --help
usage: info_py_to_json.py [-h] -i SOURCE_PY_ROOT -o TARGET_JSON_ROOT

optional arguments:
  -h, --help            show this help message and exit
  -i SOURCE_PY_ROOT, --source-py-root SOURCE_PY_ROOT
  -o TARGET_JSON_ROOT, --target-json-root TARGET_JSON_ROOT
```

即提供了两个必需提供的配置项，存放python配置文件的输入目录`-i`和将要存放生成的json文件输出目录`-o`。

通过载入输入目录中各个python文件，我们默认从中获取内部包含的不使用`_`开头的字典对象对应于各个数据集或者方法的配置信息。

最后将这些信息汇总到一个完整的字典中，直接导出到json文件中，保存到输出目录下。

## `markdown2html.py`

该文件用于将results中存放结果信息的markdown文件转化为html文件，便于在基于github page的静态站点上进行展示。

## `rename.py`

批量重命名。

使用前建议通读代码，请小心使用，防止文件覆盖造成不必要的损失。
