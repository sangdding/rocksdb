rm -rf ./plugin/zenfs/log
mkdir ./plugin/zenfs/log
./plugin/zenfs/util/zenfs mkfs --zbd=nvme0n2 --aux_path=./plugin/zenfs/log --force=true --enable_gc=true
