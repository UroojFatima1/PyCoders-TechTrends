
# Embed Response

## Structure

`EmbedResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `embeddings` | `List[object]` | Required | An array of embeddings, where each embedding is an array of floats. The length of the `embeddings` array will be the same as the length of the original `texts` array. The `small` embeddings have length `1024` and the large embeddings have length `4096`. |
| `texts` | `List[str]` | Required | The text entries for which embeddings were returned. |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "embeddings": [
    [
      {
        "key1": "val1",
        "key2": "val2"
      }
    ]
  ],
  "texts": [
    "texts6"
  ],
  "meta": {
    "api_version": {
      "version": "version0"
    }
  }
}
```

