This package contains translation of man-pages from http://www.kernel.org/doc/man-pages/.
English version of files can be refreshed from git.


The project's structure:

Original repo of English pages on kernel.org:
 man-pages-git/man1
 man-pages-git/man2
 ...

Patches for English pages:
 page_name.patch
 ...

Man-pages in English after patching
(which are used to create .pot files):
 man-pages/man1
 man-pages/man2
 ...

Translated pages:
 man/LANGUAGE/man1
 man/LANGUAGE/man2
 ...

.po-files of translatable pages:
 po/man1/LANGUAGE/LC_MESSAGES/
 po/man2/LANGUAGE/LC_MESSAGES/
 ...

Packages for work:
 subversion - works with svn
 jam or ftjam - build system
 po4a - converts man-files into po-files and conversely
 gettext - creates compendium-file
 git-core - helps to get fresh original pages
 patch -  patching of original pages

For translation and coordination we use an open service Transifex:
https://www.transifex.com/projects/p/man-pages/

Generation of translated pages:

cd man-pages-ru
jam make-man

or (if there are several processores/cores):

jam -j 4 make-man


