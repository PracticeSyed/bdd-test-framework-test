# Context Engineering Guide

## ✅ Successfully Implemented!

**Test Results:** 4 scenarios passed, 28 steps passed

---

## What is Context Engineering?

Context Engineering is providing AI/test frameworks with **domain knowledge** to generate intelligent, business-aware tests.

### Key Components:

1. **Application Context** (`context/app_context.json`)
   - Domain information
   - User personas
   - Critical flows
   - Business rules
   - Test data

2. **Context Engine** (`utils/context_engine.py`)
   - Loads and parses context
   - Provides APIs to access domain knowledge
   - Generates test scenarios dynamically

3. **Context-Aware Steps** (`steps/context_steps.py`)
   - Uses personas to drive behavior
   - Validates business rules
   - Adapts to user permissions

---

## Benefits

✓ **Intelligent Tests** - Tests understand business logic
✓ **Persona-Based** - Different user types tested automatically
✓ **Rule Validation** - Business rules enforced in tests
✓ **Maintainable** - Change context, not code
✓ **Scalable** - Add personas/rules without new code

---

## How It Works

### 1. Define Context
```json
{
  "user_personas": [
    {"name": "Guest User", "permissions": ["read_only"]},
    {"name": "Registered User", "permissions": ["purchase"]}
  ],
  "business_rules": [
    "Minimum order value: $10",
    "Free shipping over $50"
  ]
}
```

### 2. Load Context in Tests
```gherkin
Given the application context is loaded
And I am a "Guest User"
Then I should not see checkout options
```

### 3. Engine Validates Rules
```python
permissions = context.current_persona['permissions']
assert 'purchase' not in permissions  # Guest can't checkout
```

---

## Usage Examples

### Run Context-Aware Tests
```bash
cd tests/bdd
behave features/context_aware.feature
```

### Generate Scenarios Programmatically
```python
from context_engine import ContextEngine

engine = ContextEngine()
scenarios = engine.generate_test_scenarios('Product Purchase Flow')
# Returns scenarios for all personas
```

### Add New Persona
Edit `context/app_context.json`:
```json
{
  "name": "Admin User",
  "goals": ["Manage products", "View analytics"],
  "permissions": ["read", "write", "admin"]
}
```

Tests automatically adapt!

---

## Advanced Features

### 1. Dynamic Test Generation
```python
engine.generate_test_scenarios('User Registration Flow')
# Creates tests for each persona automatically
```

### 2. Business Rule Validation
```python
@then('shipping cost should be "{cost}"')
def step_shipping_cost(context, cost):
    cart_value = float(context.cart_total.replace('$', ''))
    expected_free = cart_value > 50  # From business rules
    assert expected_free == (cost == "$0")
```

### 3. Test Data Management
```python
test_data = engine.get_test_data('valid_user')
# Returns: {"email": "test@example.com", "password": "Test123!"}
```

---

## Files Created

```
tests/bdd/
├── context/
│   └── app_context.json          # Domain knowledge
├── utils/
│   └── context_engine.py         # Context loader
├── steps/
│   └── context_steps.py          # Context-aware steps
└── features/
    └── context_aware.feature     # Persona-based tests
```

---

## Next Steps

1. **Expand Context** - Add more personas, flows, rules
2. **AI Integration** - Use context to generate tests with LLMs
3. **Data-Driven** - Load context from APIs/databases
4. **Visual Reports** - Show persona coverage, rule validation

---

## Example Output

```
✓ Loaded context for: Practice Software Testing Site
✓ Loaded 4 business rules
✓ Acting as: Guest User
  Goals: Browse products, View details, Search items
✓ Checkout hidden (correct for guest)

✓ Acting as: Registered User
✓ Logged in as: test@example.com
✓ Added Hammer to cart
✓ Business rules validated
✓ Shipping: $0 (correct)
```

---

## Why This Matters

Traditional tests are **code-centric**. Context engineering makes them **business-centric**.

- Change business rule → Update JSON, not code
- Add user type → Tests auto-generate
- Validate flows → Context ensures correctness

**Result:** Tests that understand your business, not just your UI.
