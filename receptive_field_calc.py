#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: receptive_field_calc.py

@time: 2019/5/18 16:25

@desc:

'''


def receptive_field_calc(image_size, layers, layer_names, print_flag):   # assume width and height are equal
    input = (image_size, 1, 1)
    print_layer(input, 'input image')
    for layer, name, flag in zip(layers, layer_names, print_flag):
        isDeConv = 'deConv' in name
        input = out_from_in(input, layer, isDeConv)
        if flag:
            print_layer(input, name)

def out_from_in(inLayer, Conv, isDeConv=False):
    k, s, p = Conv       # kernel size, stride, padding
    n, r, j = inLayer    # number of features, receptive field size, distance between two adjacent features

    if isDeConv:
        n_out = s * (n - 1) + k - 2 * p
        j_out = j // s
        r_out = r + (k - 1) * j_out
    else:
        n_out = (n + 2 * p - k) // s + 1
        j_out = j * s
        r_out = r + (k - 1) * j

    return n_out, r_out, j_out

def print_layer(layer, layer_name):
    n, r, j = layer
    print(layer_name + ':')
    print(f'\t number of features: {n} \t distance: {j} \t receptive field: {r}')


if __name__ == '__main__':
    # V-Net example
    layer_names = ['L-Stage 1', 'downConv 1', 'Conv 2', 'L-Stage 2', 'downConv 2', 'Conv 4', 'Conv 5',
                   'L-Stage 3', 'downConv 3', 'Conv 7', 'Conv 8', 'L-Stage 4', 'downConv 4', 'Conv 10',
                   'Conv 11', 'L-Stage 5', 'deConv 1', 'Conv 13', 'Conv 14', 'R-Stage 4', 'deConv 2',
                   'Conv 16', 'Conv 17', 'R-Stage 3', 'deConv 3', 'Conv 19', 'R-Stage 2', 'deConv 4',
                   'R-Stage 1', 'output']
    # kernel size, stride, padding
    layers = [(5, 1, 2), (2, 2, 0), (5, 1, 2), (5, 1, 2), (2, 2, 0), (5, 1, 2), (5, 1, 2), (5, 1, 2),
              (2, 2, 0), (5, 1, 2), (5, 1, 2), (5, 1, 2), (2, 2, 0), (5, 1, 2), (5, 1, 2), (5, 1, 2),
              (2, 2, 0), (5, 1, 2), (5, 1, 2), (5, 1, 2), (2, 2, 0), (5, 1, 2), (5, 1, 2), (5, 1, 2),
              (2, 2, 0), (5, 1, 2), (5, 1, 2), (2, 2, 0), (5, 1, 2), (1, 1, 0)]

    print_flag = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]

    assert(len(layer_names) == len(layers))
    assert(len(layer_names) == len(print_flag))

    receptive_field_calc(128, layers, layer_names, print_flag)


