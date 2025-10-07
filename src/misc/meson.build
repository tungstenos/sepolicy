# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

mcs_enabled = mcs ? 'true' : 'false'

cil_conf_data = configuration_data()
cil_conf_data.set('MCS_ENABLED', mcs_enabled)

conf_cil = configure_file(
    input: 'conf.cil.in',
    output: 'conf.cil',
    configuration: cil_conf_data
)

policy_sources += conf_cil

cil_files = [
    'av.cil',
    'default.cil',
    'isid.cil',
    'map.cil',
    'mls.cil',
    'modular.cil',
    'obj.cil',
    'perm.cil',
    'silenced.cil',
    'unconfined.cil',
]

foreach file : cil_files
    policy_sources += files(file)
endforeach

subdir('av')
subdir('constrain')
subdir('xperm')
