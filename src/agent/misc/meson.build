# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

cil_files = [
    'dbus.cil',
    'nss.cil',
    'pam.cil',
    'systemd.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('pam')
subdir('systemd')
subdir('utillinux')
