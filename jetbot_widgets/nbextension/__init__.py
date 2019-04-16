#!/usr/bin/env python
# coding: utf-8

# Copyright (c) John Welsh
# Distributed under the terms of the Modified BSD License.

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'nbextension/static',
        'dest': 'jetbot_widgets',
        'require': 'jetbot_widgets/extension'
    }]
