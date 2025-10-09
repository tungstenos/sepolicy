# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'blocksysfile.cil',
    'bussysfile.cil',
    'classsysfile.cil',
    'devicessysfile.cil',
    'devsysfile.cil',
    'firmwaresysfile.cil',
    'fssysfile.cil',
    'hypervisorsysfile.cil',
    'kernelsysfile.cil',
    'modulesysfile.cil',
    'powersysfile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('classsysfile')
subdir('devicessysfile')
subdir('fssysfile')
subdir('kernelsysfile')
