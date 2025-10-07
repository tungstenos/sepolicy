# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'authfile.cil',
    'bootfile.cil',
    'bootflagfile.cil',
    'certfile.cil',
    'conffile.cil',
    'datafile.cil',
    'devfile.cil',
    'homefile.cil',
    'hugetlbfsfile.cil',
    'mqueuefsfile.cil',
    'runfile.cil',
    'secfile.cil',
    'tmpfile.cil',
    'tmpfsfile.cil',
    'varfile.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('datafile')
subdir('homefile')
subdir('hugetlbfsfile')
subdir('misc')
subdir('mqueuefsfile')
subdir('runfile')
subdir('tmpfile')
subdir('tmpfsfile')
subdir('varfile')
