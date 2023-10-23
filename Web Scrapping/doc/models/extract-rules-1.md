
# Extract Rules 1

## Structure

`ExtractRules1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `all_links` | [`AllLinks`](../../doc/models/all-links.md) | Required | - |

## Example (as JSON)

```json
{
  "all_links": {
    "selector": "a",
    "type": "list",
    "output": {
      "anchor": "a",
      "href": {
        "selector": "a",
        "output": "@href"
      }
    }
  }
}
```

