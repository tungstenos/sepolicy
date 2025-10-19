# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

project('sepolicy', meson_version: '>= 1.3.0', version: '0.1')

polvers = get_option('polvers')
selinuxtype = meson.project_name()
mcs = get_option('mcs')
sysadmin = get_option('sysadmin')

policy_sources = []

subdir('src')
subdir('templates')

if get_option('modular')
    # just make sure it exists
    find_program('semodule')

    install_emptydir('/var/lib/selinux', install_mode: 'rwxr-xr-x')
    meson.add_install_script(
        find_program('sh'),
        '-c',
        'semodule --priority=100 -N -vvv -s sepolicy -i "$@" -p "${DESTDIR}"',
        '__argv0_ignore',
        policy_sources,
    )
    # end of build; do not install secilc output directly
    subdir_done()
endif

policy = custom_target(
    'policy',
    output: ['policy.@0@'.format(polvers), 'file_contexts'],
    input: policy_sources,
    command: [
        'secilc',
        '-OM',
        mcs ? ['true'] : ['false'],
        '--policyvers=@0@'.format(polvers),
        '@INPUT@',
    ],
    install: true,
    install_dir: [
        join_paths(get_option('sysconfdir'), 'selinux', selinuxtype, 'policy'),
        join_paths(
            get_option('sysconfdir'),
            'selinux',
            selinuxtype,
            'contexts',
            'files',
        ),
    ],
    install_mode: 'rw-------',
    build_by_default: true,
)

# Hack to work around lack of meson support for different
# install_modes for mutiple outputs in custom_target
meson.add_install_script(
    'chmod',
    '644',
    join_paths(
        get_option('prefix'),
        get_option('sysconfdir'),
        'selinux',
        selinuxtype,
        'contexts',
        'files',
        'file_contexts',
    ),
)
