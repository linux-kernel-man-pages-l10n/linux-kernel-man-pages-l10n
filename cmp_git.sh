#/bin/sh
cd /srv/repo/svn/man-pages-ru/man-pages-git
for f in `find . -print`
do
  if ! [ -f /srv/repo/svn/man-pages-ru/man/ru/$f ]; then
    echo 'Потерялся' $f
  fi
done
