
# Generation Stream

## Structure

`GenerationStream`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | A segment of text of the generation. |
| `index` | `int` | Optional | Refers to the nth generation. Only present when `num_generations` is greater than zero. |
| `is_finished` | `bool` | Required | - |

## Example (as JSON)

```json
{
  "text": "text0",
  "index": 44,
  "is_finished": false
}
```

