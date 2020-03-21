# coding: utf-8
"""Photometric stereo algorithms

"""

import sys

import numpy as np


def diffuse_ps(imgs, l_dirs):
    """input should be grayscale images
    
    Returns:
        [tuple]: (albedo_img, normal_img)
    """

    img_size = imgs[0].shape
    I = np.vstack([img.reshape(-1) for img in imgs])

    S = np.vstack([l for l in l_dirs])
    
    S_inv = np.linalg.pinv(S)

    p_normals = S_inv @ I
    
    albedo = np.linalg.norm(p_normals, axis=0)

    normals = np.zeros(p_normals.shape)
    normals[:, albedo!=0] = p_normals[:, albedo!=0] / albedo[albedo!=0]

    return albedo.reshape(img_size), normals.reshape(3, *img_size)

