# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'bpffile.cil',
    'cgroupfile.cil',
    'debugfile.cil',
    'procfile.cil',
    'pstorefile.cil',
    'securityfile.cil',
    'sysfile.cil',
    'tracefile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('procfile')
subdir('sysfile')
