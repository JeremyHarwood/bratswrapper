#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import brats

bratsopen = brats.bind("/soft/brats/brats")

bratsopen.execfile("testcommands.txt")
