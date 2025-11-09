
from typing import Callable
import numpy as np
import cv2


def tta_average_mask(predict_fn: Callable[[np.ndarray], np.ndarray],
                     image_bgr: np.ndarray) -> np.ndarray:
    m1 = predict_fn(image_bgr)
    m2 = predict_fn(cv2.flip(image_bgr, 1))[:, ::-1]
    m = 0.5 * (m1 + m2)
    return np.clip(m, 0.0, 1.0)
