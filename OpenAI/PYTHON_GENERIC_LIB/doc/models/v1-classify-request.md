
# V1 Classify Request

## Structure

`V1ClassifyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | `str` | Optional | The size of the model. Currently available models are `small` and `large` (default). Smaller models are faster, while larger models will perform better. [Custom models](/docs/training-custom-models) can also be supplied with their full ID. |
| `inputs` | `List[str]` | Required | Represents a list of queries to be classified, each entry must not be empty. The maximum is 32 inputs.<br>**Constraints**: *Maximum Items*: `32` |
| `examples` | [`List[Example]`](../../doc/models/example.md) | Required | An array of examples to provide context to the model. Each example is a text string and its label/class. Each unique label/class requires at least 5 examples associated with it, there is a maximum of 50 total examples.<br>**Constraints**: *Maximum Items*: `50` |
| `truncate` | [`TruncateEnum`](../../doc/models/truncate-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "inputs": [
    "inputs8"
  ],
  "examples": [
    {
      "text": "text5",
      "label": "label5"
    }
  ],
  "model": "model2",
  "truncate": "END"
}
```

