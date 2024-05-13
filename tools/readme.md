# Useful tools

## `append_results.py`

将新生成的npy文件与旧的npy文件合并到一个新npy文件中。

```shell
$ python append_results.py --help
usage: append_results.py [-h] --old-npy OLD_NPY --new-npy NEW_NPY [--method-names METHOD_NAMES [METHOD_NAMES ...]]
                         [--dataset-names DATASET_NAMES [DATASET_NAMES ...]] --out-npy OUT_NPY

A simple tool for merging two npy file. Patch the method items corresponding to the `--method-names` and `--dataset-names` of `--new-npy`
into `--old-npy`, and output the whole container to `--out-npy`.

optional arguments:
  -h, --help            show this help message and exit
  --old-npy OLD_NPY
  --new-npy NEW_NPY
  --method-names METHOD_NAMES [METHOD_NAMES ...]
  --dataset-names DATASET_NAMES [DATASET_NAMES ...]
  --out-npy OUT_NPY
```

使用情形：

对于rgb sod数据，我已经生成了包含一批方法的结果的npy文件：`old_rgb_sod_curves.npy`。
对于某个方法重新评估后又获得了一个新的npy文件（文件不重名，所以不会覆盖）：`new_rgb_sod_curves.npy`。
现在我想要将这两个结果整合到一个文件中：`finalnew_rgb_sod_curves.npy`。
可以通过如下指令实现。

```shell
python tools/append_results.py --old-npy output/old_rgb_sod_curves.npy \
                               --new-npy output/new_rgb_sod_curves.npy \
                               --out-npy output/finalnew_rgb_sod_curves.npy
```


## `converter.py`

将生成的 `*_metrics.npy` 文件中的信息导出成latex表格的形式.

可以按照例子文件夹中的 `examples/converter_config.py` 进行手动配置, 从而针对性的生成latex表格代码.

```shell
$ python converter.py --help
usage: converter.py [-h] -i RESULT_FILE [RESULT_FILE ...] -o TEX_FILE [-c CONFIG_FILE] [--contain-table-env] [--transpose]

A useful and convenient tool to convert your .npy results into the table code in latex.

optional arguments:
  -h, --help            show this help message and exit
  -i RESULT_FILE [RESULT_FILE ...], --result-file RESULT_FILE [RESULT_FILE ...]
                        The path of the *_metrics.npy file.
  -o TEX_FILE, --tex-file TEX_FILE
                        The path of the exported tex file.
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        The path of the customized config yaml file.
  --contain-table-env   Whether to containe the table env in the exported code.
  --transpose           Whether to transpose the table.
```

使用案例如下.

```shell
$ python tools/converter.py -i output/your_metrics_1.npy output/your_metrics_2.npy -o output/your_metrics.tex -c ./examples/converter_config.yaml --transpose --contain-table-env
```

该指令从多个npy文件中(如果你仅有一个, 可以紧跟一个npy文件)读取数据, 处理后导出到指定的tex文件中. 并且使用指定的config文件设置了相关的数据集、指标以及模型方法.

另外, 对于输出的表格代码, 使用转置后的竖表, 并且包含table的 `tabular` 环境代码.

## `check_path.py`

通过将json中的信息与实际系统中的路径进行匹配, 检验是否存在异常.

```shell
$ python check_path.py --help
usage: check_path.py [-h] -m METHOD_JSONS [METHOD_JSONS ...] -d DATASET_JSONS [DATASET_JSONS ...]

A simple tool for checking your json config file.

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD_JSONS [METHOD_JSONS ...], --method-jsons METHOD_JSONS [METHOD_JSONS ...]
                        The json file about all methods.
  -d DATASET_JSONS [DATASET_JSONS ...], --dataset-jsons DATASET_JSONS [DATASET_JSONS ...]
```

使用案例如下, 请务必确保, `-m` 和 `-d` 后的文件路径是一一对应的, 在代码中会使用 `zip` 来同步迭代两个列表来确认文件名称的匹配关系.

```shell
$ python check_path.py -m ../configs/methods/json/rgb_sod_methods.json ../configs/methods/json/rgbd_sod_methods.json \
                       -d ../configs/datasets/json/rgb_sod.json ../configs/datasets/json/rgbd_sod.json
```

## `info_py_to_json.py`

将基于python格式的配置文件转化为更便携的json文件.

```shell
$ python info_py_to_json.py --help
usage: info_py_to_json.py [-h] -i SOURCE_PY_ROOT -o TARGET_JSON_ROOT

optional arguments:
  -h, --help            show this help message and exit
  -i SOURCE_PY_ROOT, --source-py-root SOURCE_PY_ROOT
  -o TARGET_JSON_ROOT, --target-json-root TARGET_JSON_ROOT
```

即提供了两个必需提供的配置项, 存放python配置文件的输入目录 `-i` 和将要存放生成的json文件输出目录 `-o` .

通过载入输入目录中各个python文件, 我们默认从中获取内部包含的不使用 `_` 开头的字典对象对应于各个数据集或者方法的配置信息.

最后将这些信息汇总到一个完整的字典中, 直接导出到json文件中, 保存到输出目录下.

## `rename.py`

批量重命名.

使用前建议通读代码, 请小心使用, 防止文件覆盖造成不必要的损失.
