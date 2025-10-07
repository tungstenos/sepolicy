# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'ibnet.cil',
    'netifnet.cil',
    'nodenet.cil',
    'packetnet.cil',
    'peernet.cil',
    'portnet.cil',
    'spdnet.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('ibnet')
subdir('portnet')
