import numpy as np
from PIL import Image, ImageEnhance


def l3enhance(
    rgb,
    scale=0.01,
    vmin=0.01,
    vmax=1.02,
    gamma=0.95,
    contrast=1.5,
    brightness=1.02,
    sharpness=2,
    saturation=1.1,
):
    """Enhance a RGB data array for visualization.

    Parameters
    ----------
    rgb
        the input data array with shape (M, N, 3)
    scale
    vmin
    vmax
    gamma
    contrast
    brightness
    sharpness
    saturation

    Returns
    -------
        the input data array with modified data
    """
    rgb = rgb.where(rgb > 0)
    rgb = np.log(rgb / scale) / np.log(1 / scale)
    rgb = (rgb - rgb.min()) / (rgb.max() - rgb.min())
    rgb = rgb * gamma
    img = rgb * 255
    img = img.where(img.notnull(), 0).astype("uint8")
    img = Image.fromarray(img.data)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation)
    rgb[:] = np.array(img) / 255
    return rgb