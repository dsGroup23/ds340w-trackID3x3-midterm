
from typing import Optional, Tuple
import numpy as np
import cv2


def refine_ball_center_from_mask(prob_mask: np.ndarray,
                                 min_r: int = 2,
                                 max_r: int = 12) -> Optional[Tuple[float, float]]:
    assert prob_mask.ndim == 2, "prob_mask must be HxW in [0,1]"
    m = (np.clip(prob_mask, 0.0, 1.0) * 255).astype(np.uint8)
    m = cv2.GaussianBlur(m, (5, 5), 0)
    _, bw = cv2.threshold(m, 0, 255, cv2.THRESH_OTSU)
    bw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))

    circles = cv2.HoughCircles(
        bw, cv2.HOUGH_GRADIENT, dp=1.2, minDist=8,
        param1=60, param2=10, minRadius=min_r, maxRadius=max_r
    )
    if circles is None:
        ys, xs = np.where(bw > 0)
        if len(xs) == 0:
            return None
        return (float(xs.mean()), float(ys.mean()))

    x, y, r = np.squeeze(circles, axis=0)[0]
    return (float(x), float(y))
