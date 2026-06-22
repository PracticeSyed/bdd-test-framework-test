import sys
sys.path.insert(0, 'tests/bdd/utils')
try:
    from test_controller import TestController
    has_controller = True
except ImportError:
    has_controller = False

def before_all(context):
    if has_controller:
        context.controller = TestController()
    context.step_index = 0

def before_scenario(context, scenario):
    context.step_index = 0
    if has_controller:
        state = context.controller.load_state()
        if state and state.get('scenario') == scenario.name:
            context.step_index = state.get('step', 0)
            print(f"▶ Resuming from step {context.step_index}")

def before_step(context, step):
    if has_controller and context.controller.should_skip(context.scenario.name, context.step_index):
        step.skip()
    context.step_index += 1

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
    if has_controller:
        context.controller.clear_state()
