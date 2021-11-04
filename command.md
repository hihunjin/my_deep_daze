# install

```
!apt update;apt install wget -y
pip install regex siren-pytorch torch_optimizer imageio ftfy deep-daze
```

# wget an image
```
wget http://www.blakearchive.org/images/bb85.a.6.ps.100.jpg -O image.jpg
```

# docker run

```
docker run -it --gpus=all --shm-size=64gb --cpus=12 -p 8886:8888 -v $(pwd):/workspace pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime /bin/bash
```