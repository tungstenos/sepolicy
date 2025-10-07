# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

mcs_suffix = mcs ? ':s0' : ''
mcs_range_suffix = mcs ? ':s0-s0' : ''

templates_conf_data = configuration_data()
templates_conf_data.set('MCS_SUFFIX', mcs_suffix)
templates_conf_data.set('MCS_RANGE_SUFFIX', mcs_range_suffix)

seusers = configure_file(
    input: 'seusers.in',
    output: 'seusers',
    configuration: templates_conf_data,
)

install_data(
    seusers,
    install_dir: join_paths(get_option('sysconfdir'), 'selinux', selinuxtype),
)

subdir('contexts')
subdir('logins')
