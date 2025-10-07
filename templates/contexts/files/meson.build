# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

media = configure_file(
    input: 'media.in',
    output: 'media',
    configuration: templates_conf_data,
)

install_data(
    'file_contexts.subs_dist',
    media,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'files',
    ),
)
