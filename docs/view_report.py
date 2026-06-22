#!/usr/bin/env python3
import os
from IPython.display import IFrame, display

report_path = 'tests/bdd/reports/report_20260619_100333.html'
display(IFrame(src=report_path, width=1000, height=600))
