#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf

def version():
    return '1.0'


def main():
    a = tf.Variable(1)

print(version())