pip install -r resources/requirement.txt
pipenv install
pipenv run python -m src.utility.setup
rm temp/*
git clone https://github.com/harperco/MeasEval.git temp/masEval/
cp -r temp/masEval/data/* data/
rm -r temp/*
rm temp/*
wget -P temp/ https://github.com/kermitt2/grobid/archive/0.6.1.zip
unzip temp/0.6.1.zip -d resources/
rm temp/0.6.1.zip
cd resources/grobid-0.6.1
./gradlew clean install
cd ..
cd ..
wget -P temp/ https://github.com/kermitt2/grobid-quantities/archive/master.zip
unzip temp/master.zip -d resources/grobid-0.6.1/
rm temp/master.zip
cd resources/grobid-0.6.1/grobid-quantities-master
./gradlew copyModels
./gradlew clean install