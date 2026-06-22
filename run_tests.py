#!/usr/bin/env python3
"""Main entry point for test framework"""
import sys
import os

# Add framework to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'framework'))

# Import and run
os.chdir('framework')
exec(open('run_tests.py').read())
