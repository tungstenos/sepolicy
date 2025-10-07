#! /usr/bin/env python3

# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

import argparse
import sys

from pathlib import Path


def generate(directory: Path, recursive: bool = False):
    sources = sorted([f.name for f in directory.glob('*.cil')])

    out = []
    out.append(r"""# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT
""")

    if sources:
        out.append('cil_files = [')
        for f in sources:
            out.append(f"    '{f}',")
        out.append(']')
        out.append('')
        out.append("foreach file : cil_files")
        out.append("    policy_sources += files(file)")
        out.append("endforeach")

    subdirs = sorted([
        d.name for d in directory.iterdir() if d.is_dir() and not d.name.startswith('.')
    ])

    if sources and subdirs:
        out.append('')

    for sub in subdirs:
        out.append(f"subdir('{sub}')")

    file = directory / 'meson.build'
    with file.open('w') as f:
        f.write('\n'.join(out))
        f.write('\n')

    if recursive:
        for sub in subdirs:
            generate(directory / sub, recursive=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Generate meson.build from policy source directories')
    parser.add_argument('-d',
                        '--directory',
                        default='.',
                        help='Directory to operate under (default: current)')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='Operate recursively')
    args = parser.parse_args()

    dir_path = Path(args.directory).resolve()

    if not dir_path.is_dir():
        print(f"Error: '{dir_path}' is not a directory", file=sys.stderr)
        return 1

    generate(dir_path, recursive=args.recursive)

    return 0


if __name__ == '__main__':
    sys.exit(main())
