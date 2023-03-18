InstanceLoc-build
===========
build for `	Ubuntu Server 20.04 LTS 64bit` / `NVIDIA T4`

Install Package
----------
``` bash
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install mmcv==0.6.1
```

Free Build Run
----------
``` bash
./tools/dist_train.sh configs/FPN/insloc_fpn_200ep.py 1
```

Rebuild
------------
``` bash
python setup.py build_ext
```
编译完成后需要手动把so复制到对应目录

训练数据
------------
图片放置于`data_path/imagenet/train`，标注放置于`annotation_path/train.txt`（具体参考一下例子，和imagenet数据格式一样的）