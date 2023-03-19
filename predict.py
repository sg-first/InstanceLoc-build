import torch
import torchsummary
from mmdet.models import build_detector
from mmcv import Config

model_dict = torch.load('epoch_30.pth')
# print(model)

cfg = Config.fromfile('configs/FPN/insloc_fpn_200ep.py')
model = build_detector(
        cfg.model, train_cfg=cfg.train_cfg, test_cfg=cfg.test_cfg)
model.load_state_dict(model_dict)

torchsummary.summary(model, input_size=(3,224,224))
