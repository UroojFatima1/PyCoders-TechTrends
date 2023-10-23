
# Tokenize Response

## Structure

`TokenizeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tokens` | `List[int]` | Required | An array of tokens, where each token is an integer. |
| `token_strings` | `List[str]` | Required | - |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "tokens": [
    219,
    220,
    221
  ],
  "token_strings": [
    "token_strings9"
  ],
  "meta": {
    "api_version": {
      "version": "version0"
    }
  }
}
```

