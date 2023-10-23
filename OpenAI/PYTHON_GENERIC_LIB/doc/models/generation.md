
# Generation

## Structure

`Generation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `prompt` | `str` | Optional | Prompt used for generations. |
| `generations` | [`List[SingleGeneration]`](../../doc/models/single-generation.md) | Required | List of generated results |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "generations": [
    {
      "id": "id9",
      "text": "text9",
      "index": 117,
      "likelihood": 74.15,
      "token_likelihoods": [
        {
          "token": "token6",
          "likelihood": 158.98
        }
      ]
    }
  ],
  "prompt": "prompt0",
  "meta": {
    "api_version": {
      "version": "version0"
    }
  }
}
```

