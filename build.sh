read -p "Run archive script? [y/N] " yn
case $yn in
    [Yy]* ) ./archive.sh;;
    * ) echo "Skipping archive script.";;
esac

rm gen/doc.* gen/texput.log

echo "lang = 'en'
tag = ['resume']" > gen/env.py
python3 gen/build.py
xelatex -interaction=nonstopmode -halt-on-error -output-directory=gen gen/doc.tex
cp gen/doc.pdf build/resume.pdf
rm gen/doc.pdf

echo "lang = 'ja'
tag = ['resume']" > gen/env.py
python3 gen/build.py
xelatex -interaction=nonstopmode -halt-on-error -output-directory=gen gen/doc.tex
cp gen/doc.pdf build/resume-ja.pdf
rm gen/doc.pdf

echo "lang = 'zh'
tag = ['resume', 'resume-zh']" > gen/env.py
python3 gen/build.py
xelatex -interaction=nonstopmode -halt-on-error -output-directory=gen gen/doc.tex
cp gen/doc.pdf build/resume-zh.pdf
rm gen/doc.pdf

rm gen/doc.* gen/texput.log
