wget -P temp/ https://github.com/kermitt2/grobid/archive/0.6.1.zip
unzip temp/0.6.1.zip -d resources/grobid/
rm temp/0.6.1.zip
cd resources/grobid/grobid-0.6.1
./gradlew clean install
cd ..
cd ..
cd ..
wget -P temp/ https://github.com/kermitt2/grobid-quantities/archive/master.zip
unzip temp/master.zip -d resources/grobid/grobid-0.6.1/
rm temp/master.zip
cp resources/gradle-wrapper.properties resources/grobid/grobid-0.6.1/grobid-quantities-master/gradle/wrapper/
cd resources/grobid/grobid-0.6.1/grobid-quantities-master
./gradlew copyModels
./gradlew clean install
java -jar build/libs/grobid-quantities-0.6.1-SNAPSHOT-onejar.jar server resources/config/config.yml
# java -jar build/libs/grobid-quantities-0.6.1-SNAPSHOT-onejar.jar trainingGeneration resources/config/config.yml -dIn ../../../../data/train/text/ -dOut ../../../../output/