
# Detokenize Request

## Structure

`DetokenizeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tokens` | `List[int]` | Required | The list of tokens to be detokenized.<br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `65536` |
| `model` | `str` | Optional | An optional parameter to provide the model name. This will ensure that the detokenization is done by the tokenizer used by that model. |

## Example (as JSON)

```json
{
  "tokens": [
    219,
    220,
    221
  ],
  "model": "model2"
}
```

