import json
from pathlib import Path

class TestController:
    def __init__(self, state_file='tests/bdd/config/test_state.json'):
        self.state_file = state_file
    
    def save_state(self, scenario_name, step_index):
        state = {'scenario': scenario_name, 'step': step_index, 'paused': True}
        Path(self.state_file).parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(state, f)
    
    def load_state(self):
        if Path(self.state_file).exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return None
    
    def clear_state(self):
        if Path(self.state_file).exists():
            Path(self.state_file).unlink()
    
    def should_skip(self, scenario_name, step_index):
        state = self.load_state()
        if state and state.get('paused'):
            return scenario_name != state['scenario'] or step_index < state['step']
        return False
