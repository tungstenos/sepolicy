# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'nodedev.cil',
    'stordev.cil',
    'termdev.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('nodedev')
subdir('stordev')
subdir('termdev')
