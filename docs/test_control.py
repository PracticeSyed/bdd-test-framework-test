#!/usr/bin/env python3
"""Pause/Resume Test Control"""
import sys
sys.path.insert(0, 'tests/bdd/utils')
from test_controller import TestController

def main():
    controller = TestController()
    
    if len(sys.argv) < 2:
        print("Usage: python test_control.py [pause|resume|status]")
        return
    
    cmd = sys.argv[1]
    
    if cmd == 'pause':
        scenario = input("Scenario name: ")
        step = int(input("Step index: "))
        controller.save_state(scenario, step)
        print(f"⏸ Paused at {scenario}, step {step}")
    
    elif cmd == 'resume':
        controller.clear_state()
        print("▶ Resumed - state cleared")
    
    elif cmd == 'status':
        state = controller.load_state()
        if state:
            print(f"⏸ Paused: {state['scenario']}, step {state['step']}")
        else:
            print("▶ Running")

if __name__ == '__main__':
    main()
