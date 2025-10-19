# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'hushloginshomefile.cil',
    'inputrchomefile.cil',
    'shellrchomefile.cil',
    'terminfohomefile.cil',
    'userhomecachefile.cil',
    'userhomeconffile.cil',
    'userhomedatafile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('userhomecachefile')
subdir('userhomeconffile')
subdir('userhomedatafile')
