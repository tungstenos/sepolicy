# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'noseclabelfs.cil',
    'seclabelfs.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('noseclabelfs')
subdir('seclabelfs')
