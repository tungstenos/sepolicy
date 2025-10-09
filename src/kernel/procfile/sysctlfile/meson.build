# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'abisysctlfile.cil',
    'cryptosysctlfile.cil',
    'debugsysctlfile.cil',
    'devsysctlfile.cil',
    'fssysctlfile.cil',
    'kernelsysctlfile.cil',
    'netsysctlfile.cil',
    'sunrpcsysctlfile.cil',
    'usersysctlfile.cil',
    'vmsysctlfile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('kernelsysctlfile')
subdir('netsysctlfile')
subdir('vmsysctlfile')
