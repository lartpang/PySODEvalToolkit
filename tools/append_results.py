# -*- coding: utf-8 -*-
import argparse

import numpy as np


def get_args():
    parser = argparse.ArgumentParser(
        description="""A simple tool for merging two npy file.
    Patch the method items corresponding to the `--method-names` and `--dataset-names` of `--new-npy` into `--old-npy`,
    and output the whole container to `--out-npy`.
    """
    )
    parser.add_argument("--old-npy", type=str, required=True)
    parser.add_argument("--new-npy", type=str, required=True)
    parser.add_argument("--method-names", type=str, nargs="+")
    parser.add_argument("--dataset-names", type=str, nargs="+")
    parser.add_argument("--out-npy", type=str, required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    new_npy: dict = np.load(args.new_npy, allow_pickle=True).item()
    old_npy: dict = np.load(args.old_npy, allow_pickle=True).item()

    for dataset_name, methods_info in new_npy.items():
        if args.dataset_names and dataset_name not in args.dataset_names:
            continue

        print(f"[PROCESSING INFORMATION ABOUT DATASET {dataset_name}...]")
        old_methods_info = old_npy.get(dataset_name)
        if not old_methods_info:
            raise KeyError(f"{old_npy} doesn't contain the information about {dataset_name}.")

        print(f"OLD_NPY: {list(old_methods_info.keys())}")
        print(f"NEW_NPY: {list(methods_info.keys())}")

        for method_name, method_info in methods_info.items():
            if args.method_names and method_name not in args.method_names:
                continue

            if method_name not in old_npy[dataset_name]:
                old_methods_info[method_name] = method_info
        print(f"MERGED_NPY: {list(old_methods_info.keys())}")

    np.save(file=args.out_npy, arr=old_npy)
    print(f"THE MERGED_NPY IS SAVED INTO {args.out_npy}")


if __name__ == "__main__":
    main()
