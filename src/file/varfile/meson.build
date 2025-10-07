# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'cachefile.cil',
    'dbfile.cil',
    'logfile.cil',
    'spoolfile.cil',
    'statefile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('spoolfile')
