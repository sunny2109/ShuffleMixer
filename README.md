# ShuffleMixer
[![LICENSE](https://img.shields.io/badge/license-MIT-green)](https://github.com/sunny2109/ShuffleMixer/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/pytorch-1.11-%237732a8)](https://pytorch.org/)

#### [Paper](https://arxiv.org/pdf/2205.15175.pdf) | [Discussion](https://github.com/sunny2109/ShuffleMixer/issues)
### ShuffleMixer: An Efficient ConvNet for Image Super-Resolution
By [Long Sun](https://github.com/sunny2109), [Jinshan Pan](https://jspan.github.io/), and Jinhui Tang


## Network Architecture

## Dependencies
- Linux (Tested on Ubuntu 18.04)
- Python 3.8.5 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux))
- [PyTorch 1.11.0](https://pytorch.org/): `pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113` 
- Install [BasicSR](https://github.com/XPixelGroup/BasicSR) toolbox, please see the [INSTALL.md](https://github.com/XPixelGroup/BasicSR/blob/master/docs/INSTALL.md) file.


### Training
- Our model.
- Run the following commands:
```
python basicsr/train.py -opt options/train/ShuffleMixer/train_base_DF2K_x4.yml
```

### Testing
- Download the pretrained models.
- Download the testing dataset.
- Run the following commands:
```
python basicsr/test.py -opt options/test/ShuffleMixer/test_base_benchmark_x4.yml
```
- The test results will be in './results'.


### Results
- Pretrained models and benchmark results can be downloaded [[Here]]().

## Citation
```
@InProceedings{Pan_2020_CVPR,
	author = {Sun, Long and Pan, Jinshan and Tang, Jinhui},
	title = {ShuffleMixer: An Efficient ConvNet for Image Super-Resolution},
	booktitle = {arXiv preprint arXiv:2205.15175},
	year = {2022}
}
```
