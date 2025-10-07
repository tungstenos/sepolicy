# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

sys_id_user = configure_file(
    input: 'sys.id.in',
    output: 'sys.id',
    configuration: templates_conf_data,
)

install_data(
    sys_id_user,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'users',
    ),
)
