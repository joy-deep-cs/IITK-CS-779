pip install -r resources/requirement.txt
python -m src.utility.setup.py
rm temp/*
git clone https://github.com/harperco/MeasEval.git temp/masEval/
cp -r temp/masEval/data/* data/
rm -r temp/*
rm temp/*