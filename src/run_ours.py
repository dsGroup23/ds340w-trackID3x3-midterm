import os
import json
import argparse
import numpy as np

# ---- cv2 可选：demo 模式不需要；real 模式/可选 TTA 才需要 ----
try:
    import cv2  # optional
    _cv2_ok = True
except Exception:
    cv2 = None
    _cv2_ok = False

# TTA：如果没有 cv2，就退化为“只跑一遍”的安全版本
if _cv2_ok:
    from .tta_runner import tta_average_mask
else:
    def tta_average_mask(predict_fn, image_bgr):
        return predict_fn(image_bgr)

from .postproc_ours import refine_ball_center_from_mask
