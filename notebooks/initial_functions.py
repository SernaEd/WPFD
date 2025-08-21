
from math import exp, pi, sqrt

import numpy as np


def gaussian_component_1d(x_array, xi, sigma, x0, k0):
    result_array = np.zeros_like(x_array, dtype=complex)
    amplitude = xi / (sigma ** 2 * pi) ** (1 / 4)
    
    for i in range(len(x_array)):
        real_part = exp(-(x_array[i]-x0)**2/(2*sigma**2))
        imag_part = exp(1j * x_array[i] * k0)
        result_array[i] = amplitude * real_part * imag_part
        
    return result_array

def gaussian_wp_init(box_width, delta_x, xi_a, xi_b, sigma, x0, k0):
    x_array = np.arange(0, box_width, delta_x, dtype=float)
    coefficient = 1 / sqrt(xi_a^2 + xi_b^2)
    
    psi_1 = gaussian_component_1d(x_array, xi_a, sigma, x0, k0)
    psi_2 = gaussian_component_1d(x_array, xi_b, sigma, x0, k0)
    
    psi_1 = psi_1 * coefficient
    psi_2 = psi_2 * coefficient
    
    psi_1[0] = 0 + 0j
    psi_2[0] = 0 + 0j
    
    psi_1[-1] = 0 + 0j
    psi_2[-1] = 0 + 0j
    
    gaussian_wp = [psi_1, psi_2]

    return gaussian_wp

def discrete_potential():
    n_elements = int(box_size / step_x)
    v = np.zeros(n_elements, dtype=float)
    
    for i in range(n_elements):
        if b_position <= i <= b_position + b_width:
            v[i] = b_height
