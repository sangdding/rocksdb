rm -rf /root/lsm2/rocksdb/plugin/zenfs/log
mkdir /root/lsm2/rocksdb/plugin/zenfs/log
./plugin/zenfs/util/zenfs mkfs --zbd=nvme0n2 --aux_path=/root/lsm2/rocksdb/plugin/zenfs/log --force=true --enable_gc=true
