#/bin/sh

for f in `find translations -name ru.po`
do
  echo -n $f " "
  msgfmt --statistics -o /dev/null $f
  echo -n $f " "
  msgfmt --statistics -o /dev/null ../man-pages-ru-copy/$f
#  if ! [ -f /srv/repo/svn/man-pages-ru/man/ru/$f ]; then
#    echo $f
#  fi
done
