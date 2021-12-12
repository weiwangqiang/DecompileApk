#!/usr/bin/python
# -*- encoding:utf-8 -*-
import os
import sys
import zipfile
from shutil import copyfile

invoke_path = os.path.join(os.getcwd(), "dex-tools-2.1-SNAPSHOT/d2j_invoke.sh")
dex2jar_path = os.path.join(os.getcwd(), "dex-tools-2.1-SNAPSHOT/d2j-dex2jar.sh")
jd_gui_path = os.path.join(os.getcwd(), 'jd-gui-osx-1.6.6')
gui_app = os.path.join(jd_gui_path, 'JD-GUI.app')


def init_permission():
    if not os.path.isfile(invoke_path):
        print('please put dex2jar-2.0 at %s' % os.getcwd())
        exit(1)
    if not os.path.isfile(dex2jar_path):
        print('please put dex2jar-2.0 at %s' % os.getcwd())
        exit(1)
    os.system('chmod a+x %s' % invoke_path)
    os.system('chmod a+x %s' % dex2jar_path)


def un_zip_apk(apk_path):
    if not os.path.isfile(apk_path):
        print('can not find apk by %s' % apk_path)
        exit(1)
    copy_path = str(apk_path).replace('.apk', '.zip')
    copyfile(apk_path, copy_path)
    unzip_path = copy_path.replace('.zip', '')
    if not os.path.isdir(unzip_path):
        os.mkdir(unzip_path)
    zip_file = zipfile.ZipFile(copy_path)
    for names in zip_file.namelist():
        zip_file.extract(names, unzip_path)
    zip_file.close()
    os.remove(copy_path)
    class_dex_path = '%s/classes.dex' % unzip_path
    return class_dex_path, unzip_path


def parse_dex_file(class_dex_path):
    sh = 'sh %s %s' % (dex2jar_path, class_dex_path)
    classes_path = os.path.join(os.getcwd(), 'classes-dex2jar.jar')
    if os.path.isfile(classes_path):
        os.remove(classes_path)
    os.system(sh)


if __name__ == '__main__':
    apk_path = sys.argv[1]
    init_permission()
    dex_path, unzip_path = un_zip_apk(apk_path)
    parse_dex_file(dex_path)
    os.system('rm -r %s' % unzip_path)
    os.system('open %s' % gui_app)
