
# All Links

## Structure

`AllLinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `selector` | `str` | Required | - |
| `mtype` | `str` | Required | - |
| `output` | [`Output`](../../doc/models/output.md) | Required | - |

## Example (as JSON)

```json
{
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
```

