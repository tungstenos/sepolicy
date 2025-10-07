# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

default_contexts = configure_file(
    input: 'default_contexts.in',
    output: 'default_contexts',
    configuration: templates_conf_data,
)

failsafe_context = configure_file(
    input: 'failsafe_context.in',
    output: 'failsafe_context',
    configuration: templates_conf_data,
)

removable_context = configure_file(
    input: 'removable_context.in',
    output: 'removable_context',
    configuration: templates_conf_data,
)

install_data(
    'customizable_types',
    'dbus_contexts',
    default_contexts,
    'default_type',
    failsafe_context,
    removable_context,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
    ),
)

subdir('files')
subdir('users')
