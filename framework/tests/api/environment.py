def before_all(context):
    context.api_results = []

def after_scenario(context, scenario):
    context.api_results.append({
        'name': scenario.name,
        'status': scenario.status.name
    })
