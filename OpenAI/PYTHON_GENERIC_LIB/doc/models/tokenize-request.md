
# Tokenize Request

## Structure

`TokenizeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | The string to be tokenized, the minimum text length is 1 character, and the maximum text length is 65536 characters.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `65536` |
| `model` | `str` | Optional | An optional parameter to provide the model name. This will ensure that the tokenization uses the tokenizer used by that model. |

## Example (as JSON)

```json
{
  "text": "text0",
  "model": "model2"
}
```

