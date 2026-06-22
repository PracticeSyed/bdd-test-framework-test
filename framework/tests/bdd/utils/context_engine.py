import json
from pathlib import Path

class ContextEngine:
    def __init__(self, context_file='../context/app_context.json'):
        self.context_path = Path(__file__).parent / context_file
        self.context = self._load_context()
    
    def _load_context(self):
        with open(self.context_path, 'r') as f:
            return json.load(f)
    
    def get_critical_flows(self):
        return self.context.get('critical_flows', [])
    
    def get_user_personas(self):
        return self.context.get('user_personas', [])
    
    def get_business_rules(self):
        return self.context.get('business_rules', [])
    
    def generate_test_scenarios(self, flow_name):
        """Generate BDD scenarios based on context"""
        flows = {f['name']: f for f in self.get_critical_flows()}
        if flow_name not in flows:
            return None
        
        flow = flows[flow_name]
        scenarios = []
        
        for persona in self.get_user_personas():
            scenario = {
                'persona': persona['name'],
                'flow': flow_name,
                'steps': flow['steps'],
                'priority': flow['priority']
            }
            scenarios.append(scenario)
        
        return scenarios
    
    def get_test_data(self, key):
        return self.context.get('test_data', {}).get(key)

if __name__ == '__main__':
    engine = ContextEngine()
    print("Critical Flows:", engine.get_critical_flows())
    print("\nGenerated Scenarios:", engine.generate_test_scenarios('Product Purchase Flow'))
