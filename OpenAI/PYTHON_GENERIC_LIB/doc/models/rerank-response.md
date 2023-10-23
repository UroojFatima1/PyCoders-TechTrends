
# Rerank Response

## Structure

`RerankResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `results` | [`List[Result2]`](../../doc/models/result-2.md) | Required | An ordered list of ranked documents |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "results": [
    {
      "document": {
        "text": "text7"
      },
      "index": 127,
      "relevance_score": 37.13
    }
  ],
  "id": "id0",
  "meta": {
    "api_version": {
      "version": "version0"
    }
  }
}
```

