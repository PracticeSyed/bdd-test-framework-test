# 🚀 Quick Start: Context Engineering via Prompts

## ✅ YES! You can run tests by giving me prompts!

---

## 3 Ways to Give Context & Run Tests

### 1️⃣ **Direct Command (Fastest)**
```bash
python ai_test_runner.py "Test guest user browsing products"
```

### 2️⃣ **Ask Me in Chat (Easiest)**
Just say:
- "Run tests for registered user purchase flow"
- "Test guest user browsing"
- "Validate free shipping rules"
- "Check minimum order validation"

I'll execute it for you!

### 3️⃣ **Update Context JSON (Most Powerful)**
Edit `tests/bdd/context/app_context.json` and tell me:
- "Add admin user persona"
- "Add new business rule: Max 10 items per order"
- "Test the new admin flow"

---

## Example Prompts You Can Use Right Now

### Test User Personas
```
"Test guest user browsing products"
"Test registered user purchase flow"
"Validate guest user cannot checkout"
```

### Test Business Rules
```
"Check free shipping rules"
"Validate minimum order value"
"Test cart total calculation"
```

### Test Critical Flows
```
"Test product purchase flow"
"Test user registration flow"
"Validate checkout process"
```

---

## How It Works

1. **You give prompt** → "Test registered user purchase"
2. **AI parses context** → Detects: Persona, Flow, Rules
3. **Generates Gherkin** → Creates feature file
4. **Runs tests** → Executes with Playwright
5. **Shows results** → ✓ Pass/Fail with details

---

## Try It Now!

### Example 1: Test Guest User
```bash
python ai_test_runner.py "Test guest user browsing products"
```

### Example 2: Test Purchase Flow
```bash
python ai_test_runner.py "Validate registered user purchase flow"
```

### Example 3: Test Business Rule
```bash
python ai_test_runner.py "Check free shipping over $50"
```

---

## Add Your Own Context

### Add New Persona
Tell me: **"Add VIP customer persona with priority support"**

I'll update `app_context.json`:
```json
{
  "name": "VIP Customer",
  "goals": ["Priority checkout", "Exclusive deals"],
  "permissions": ["read", "write", "purchase", "vip"]
}
```

### Add New Business Rule
Tell me: **"Add rule: VIP customers get 20% discount"**

I'll add to business_rules and generate tests automatically!

### Add New Flow
Tell me: **"Add return product flow"**

I'll create the flow and test scenarios for all personas!

---

## What Gets Auto-Generated

When you give a prompt, the system:

✓ Detects relevant **personas** from context
✓ Identifies matching **flows** 
✓ Applies **business rules**
✓ Generates **Gherkin scenarios**
✓ Runs **Playwright tests**
✓ Shows **results**

---

## Current Available Context

### Personas
- Guest User
- Registered User

### Flows
- Product Purchase Flow
- User Registration Flow

### Business Rules
- Users must be logged in to purchase
- Cart persists across sessions
- Minimum order value: $10
- Free shipping over $50

---

## Next: Just Ask Me!

Say things like:
- "Run tests for guest user"
- "Add admin persona and test it"
- "Check if shipping rules work"
- "Test the purchase flow"
- "Add new business rule and validate it"

I'll handle the rest! 🚀
