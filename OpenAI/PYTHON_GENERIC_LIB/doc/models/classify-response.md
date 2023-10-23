
# Classify Response

## Structure

`ClassifyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `classifications` | [`List[Classification]`](../../doc/models/classification.md) | Required | - |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "classifications": [
    {
      "id": "id7",
      "input": "input5",
      "prediction": "prediction3",
      "confidence": 151.01,
      "labels": {
        "key0": {
          "confidence": 23.67
        },
        "key1": {
          "confidence": 23.66
        },
        "key2": {
          "confidence": 23.65
        }
      },
      "confidences": [
        {
          "key1": "val1",
          "key2": "val2"
        }
      ]
    }
  ],
  "meta": {
    "api_version": {
      "version": "version0"
    }
  }
}
```

