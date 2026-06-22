# 🎭 Mock vs Real Browser Testing

## Current Status: **HYBRID MODE** ✅

The framework now supports **both** mock and real browser testing!

---

## 🔍 How It Works

### Mode 1: **Mock Testing** (Fast)
- Validates business logic only
- No browser launched
- Tests personas, permissions, rules
- **Speed:** ~0.1 seconds

**Example:**
```python
@then('I should not see checkout options')
def step_no_checkout(context):
    permissions = context.current_persona['permissions']
    assert 'purchase' not in permissions  # ✓ Logic check
    print("✓ Checkout hidden (correct for guest)")
```

### Mode 2: **Real Browser Testing** (Accurate)
- Launches Playwright browser
- Tests actual website
- Validates real UI elements
- **Speed:** ~3 seconds

**Example:**
```python
@when('I browse products')
def step_browse_products(context):
    context.page.goto('https://practicesoftwaretesting.com/')
    context.page.wait_for_load_state('networkidle')
    print("✓ Browsing products on real site")
```

---

## 🎯 Which Steps Use Real Browser?

### ✅ Real Browser Steps (Updated)
- `When I navigate to the product catalog` → Opens practice site
- `When I browse products` → Loads real page
- `Then I should see available products` → Checks real content
- `Then I should not see checkout options` → Checks real UI

### 📋 Mock Steps (Fast Validation)
- `Given I am a "Guest User"` → Loads persona from JSON
- `Given business rules are defined` → Loads rules
- `Then shipping cost should be "$0"` → Validates logic
- `Then I should see "message"` → Checks business rules

---

## 🚀 Usage Examples

### Example 1: Real Browser Test
```bash
python ai_test_runner.py "Test guest user browsing products"
```

**What happens:**
1. ✓ Loads context (mock)
2. ✓ Sets persona to Guest (mock)
3. 🌐 **Opens browser** → practicesoftwaretesting.com
4. 🌐 **Checks real page** for products
5. 🌐 **Validates UI** - no checkout button
6. ✓ Closes browser

**Time:** ~3 seconds

### Example 2: Mock Test (No Browser)
```bash
python ai_test_runner.py "Check free shipping rules"
```

**What happens:**
1. ✓ Loads context
2. ✓ Validates: $55 cart > $50 threshold
3. ✓ Asserts: shipping = $0
4. ✓ No browser needed

**Time:** ~0.1 seconds

---

## 📊 Comparison

| Feature | Mock Mode | Real Browser |
|---------|-----------|--------------|
| Speed | ⚡ 0.1s | 🐢 3s |
| Accuracy | Logic only | Full UI |
| Use Case | Business rules | User flows |
| Browser | ❌ No | ✅ Yes |
| Network | ❌ No | ✅ Yes |

---

## 🎨 Architecture

```
User Prompt
    ↓
Parse Context (Mock)
    ↓
Generate Gherkin
    ↓
Run Steps:
    ├─ Context Steps (Mock) ← Fast
    └─ Browser Steps (Real) ← Accurate
    ↓
Results
```

---

## 🔧 How to Control Mode

### Force Real Browser
Add these steps to your prompt:
- "navigate to catalog"
- "browse products"
- "check UI elements"

### Force Mock Mode
Use these steps:
- "validate rules"
- "check permissions"
- "verify business logic"

---

## 💡 Best Practices

### Use Mock When:
✓ Testing business rules
✓ Validating permissions
✓ Checking calculations
✓ Fast feedback needed

### Use Real Browser When:
✓ Testing user flows
✓ Validating UI elements
✓ Checking navigation
✓ End-to-end scenarios

---

## 🎯 Current Implementation

### Steps with Real Browser:
```python
# Opens practicesoftwaretesting.com
@when('I navigate to the product catalog')
@when('I browse products')
@then('I should see available products')
@then('I should not see checkout options')
```

### Steps with Mock:
```python
# No browser, just logic
@given('I am a "{persona}"')
@given('business rules are defined')
@then('shipping cost should be "{cost}"')
@then('I should see "{message}" message')
```

---

## 🚀 Try It Now

### Real Browser Test:
```bash
python ai_test_runner.py "Test guest user browsing products"
# Opens browser, tests real site
```

### Mock Test:
```bash
python ai_test_runner.py "Validate minimum order value"
# No browser, validates logic only
```

---

## 📈 Performance

```
Mock Test:     ⚡⚡⚡⚡⚡ (0.1s)
Hybrid Test:   ⚡⚡⚡⚡   (3s)
Full E2E:      ⚡⚡      (10s+)
```

---

## ✨ Summary

**Current Setup:**
- ✅ Mock testing for business logic
- ✅ Real browser for UI validation
- ✅ Hybrid approach (best of both)
- ✅ Automatic mode selection

**Result:** Fast tests with real validation when needed!
