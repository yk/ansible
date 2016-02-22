#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess


def get_file_name(name, directory):
    fn = '{}.hdf5'.format(name)
    if name == 'svhn 1':
        fn = 'svhn_format_1.hdf5'
    if name == 'svhn 2':
        fn = 'svhn_format_2.hdf5'
    return "{}/{}".format(directory, fn)


def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, universal_newlines=True)
    out, err = process.communicate()
    rc = process.returncode
    return out, err, rc


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            directory=dict(default='data', type='str'),
        ),
        supports_check_mode=True
    )

    name = module.params['name']
    state = module.params['state']
    directory = module.params['directory']

    fn = get_file_name(name, directory)

    if module.check_mode:
        module.exit_json(changed=(os.path.exists(fn) == (state == 'absent')))

    if state == 'present' and os.path.exists(fn):
        module.exit_json(changed=False)

    if state == 'absent' and not os.path.exists(fn):
        module.exit_json(changed=False)

    if not os.path.exists(directory):
        os.makedirs(directory)

    fuel_download_cmd = "fuel-download {} -d {}".format(name, directory)

    if state == 'absent':
        fuel_download_cmd += " --clear"

    out1, err1, rc1 = run_command(fuel_download_cmd)
    if rc1 != 0:
        module.fail_json(msg="Error while running downloader")

    fuel_convert_cmd = "fuel-convert {} -d {} -o {}".format(name, directory, directory)

    if state != 'absent':
        out2, err2, rc2 = run_command(fuel_convert_cmd)
        if rc2 != 0:
            module.fail_json(msg="Error while running converter")

    module.exit_json(changed=True)


from ansible.module_utils.basic import *  # noqa
if __name__ == '__main__':
    main()
