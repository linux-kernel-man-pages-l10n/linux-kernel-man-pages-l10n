#/bin/sh
#
# старый без tar.gz
#
tar -jxf ${1}.tar.bz2 -C /tmp/
cd /tmp/${1}
for f in `find . -print`
do
  if ! [ -f /srv/repo/svn/man-pages-ru/man/ru/$f ]; then
    echo 'Потерялся' /tmp/${1}/$f
  fi
done
