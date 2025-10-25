# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'hybridagent.cil',
    'sysagent.cil',
    'useragent.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('hybridagent')
subdir('misc')
subdir('sysagent')
