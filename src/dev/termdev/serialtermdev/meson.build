# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'acmserialtermdev.cil',
    'consoleserialtermdev.cil',
    'loginserialtermdev.cil',
    'msmserialtermdev.cil',
    'sysserialtermdev.cil',
    'usbserialtermdev.cil',
    'vcsserialtermdev.cil',
    'vportserialtermdev.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('loginserialtermdev')
