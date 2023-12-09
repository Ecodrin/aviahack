#cloning WaveRange
git clone https://github.com/pseudospectators/WaveRange.git
cd WaveRange

#specifying the version
git checkout 3336bdd

#build
cp ../config.mk ./ && make generic

#creating symlinks in src/ directory
cp ./bin/generic/wrenc ../src/wrenc
cp ./bin/generic/wrdec ../src/wrdec

#autoremove self
rm ./wrbuild.sh
