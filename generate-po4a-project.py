#!/usr/bin/env python

import sys
import os.path

categories = ['man1', 'man2', 'man3', 'man4', 'man5', 'man6', 'man7', 'man8']

languages = ['ru']
po_root_dir = 'po'
source_root_dir = 'man-pages'
translated_root_dir = 'translated'

option_bug_address = "https://github.com/linux-kernel-man-pages-l10n/linux-kernel-man-pages-l10n"
option_copyright_holder = "Linux Kernel Man Pages l10n"
option_package_name = "linux_kernel_man_pages_l10n"
option_package_version = "5.03"
option_common = "-M UTF-8 -o generated -o groff_code=verbatim -o untranslated=if,q,de1,.,INDENT,UNINDENT,ft"

for cat in categories:
    with open(cat + ".cfg", "w") as out_file:
        source_dir = os.path.join(source_root_dir, cat)
        if not os.path.exists(source_dir):
            print("Source dir '{}' does not exists, exiting".format(source_dir))
            exit(1)

        out_file.write("[po4a_langs] {}\n".format(' '.join(languages)))
        out_file.write(
            "[options] "
            "--msgid-bugs-address {0} --copyright-holder {1} --package-name {2} --package-version {3} {4}\n"
                .format(option_bug_address, option_copyright_holder, option_package_name, option_package_version,
                        option_common))
        out_file.write("[po4a_paths] {0}/{1}/template.pot $lang:{0}/{1}/$lang.po\n\n".format(po_root_dir, cat))

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                out_file.write("[type: man] {0}/{1} $lang:{2}/{3}/$lang/{1}\n"
                               .format(source_dir, file, translated_root_dir, cat))
