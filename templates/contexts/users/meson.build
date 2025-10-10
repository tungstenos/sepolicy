# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

user_id_user = configure_file(
    input: 'user.id.in',
    output: 'user.id',
    configuration: templates_conf_data,
)

user_contexts_install_data = [user_id_user]

if sysadmin
    sys_id_user = configure_file(
        input: 'sys.id.in',
        output: 'sys.id',
        configuration: templates_conf_data,
    )
    user_contexts_install_data += sys_id_user
endif

install_data(
    user_contexts_install_data,
    install_dir: join_paths(
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'users',
    ),
)
