
# Extract Rules 3

## Structure

`ExtractRules3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email_addresses` | [`EmailAddresses`](../../doc/models/email-addresses.md) | Required | - |

## Example (as JSON)

```json
{
  "email_addresses": {
    "selector": "a[href^='mailto']",
    "output": "@href",
    "type": "list"
  }
}
```

