# SPDX-FileCopyrightText: 2025 Rahul Sandhu <nvraxn@gmail.com>
# SPDX-License-Identifier: MIT

mcs_suffix = mcs ? ':s0' : ''
mcs_range_suffix = mcs ? ':s0-s0' : ''
sysadmin_user_entry = sysadmin ? 'sys.role:sys.user.subj' + mcs_suffix : ''

templates_conf_data = configuration_data()
templates_conf_data.set('MCS_SUFFIX', mcs_suffix)
templates_conf_data.set('MCS_RANGE_SUFFIX', mcs_range_suffix)
templates_conf_data.set('SYSADMIN_USER_ENTRY', sysadmin_user_entry)

subdir('contexts')
subdir('logins')
