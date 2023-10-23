
# Email Addresses

## Structure

`EmailAddresses`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `selector` | `str` | Required | - |
| `output` | `str` | Required | - |
| `mtype` | `str` | Required | - |

## Example (as JSON)

```json
{
  "selector": "a[href^='mailto']",
  "output": "@href",
  "type": "list"
}
```

