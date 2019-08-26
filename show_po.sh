#/bin/sh

for f in `find translations -name ru.po`
do
  msgfmt --statistics -o /dev/null $f;
done
