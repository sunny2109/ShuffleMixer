import cv2
import torch
import torch.nn.functional as F

def get_gaussian_kernel(size=21):
    kernel = cv2.getGaussianKernel(size, 0).dot(cv2.getGaussianKernel(size, 0).T)
    kernel = torch.from_numpy(kernel).unsqueeze(0).unsqueeze(0)
    kernel = torch.nn.Parameter(kernel, requires_grad=False)
    return kernel

def get_gaussian_blur(x, kernel):
    pad = (kernel.size(-1) - 1) // 2
    kernel = kernel.repeat(x.size(1), 1, 1, 1).type_as(x)
    return F.conv2d(x, kernel, stride=1, padding=pad, groups=x.size(1))

def get_high_freq(img, size):
    kernel = get_gaussian_kernel(size)
    low_freq = get_gaussian_blur(img, kernel)
    return img - low_freq

if __name__ == '__main__':
    x = torch.randn(1, 3, 15, 19)
    high_freq = get_high_freq(x, size=3)
    print(f'high_freq:{high_freq}; shape:{high_freq.shape}')

