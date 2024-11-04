export PYTHONDONTWRITEBYTECODE=1

rm gen/doc.* gen/texput.log

echo "lang = 'en'
tag = ['resume']" > gen/env.py
python3 -B gen/build.py
xelatex -interaction=nonstopmode -halt-on-error -output-directory=gen gen/doc.tex
