
# Classify Request

## Structure

`ClassifyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `inputs` | `List[str]` | Required | Represents a list of queries to be classified, each entry must not be empty. The maximum is 96 inputs.<br>**Constraints**: *Maximum Items*: `96` |
| `examples` | [`List[Example]`](../../doc/models/example.md) | Required | An array of examples to provide context to the model. Each example is a text string and its associated label/class. Each unique label requires at least 2 examples associated with it; the maximum number of examples is 2500, and each example has a maximum length of 512 tokens. The values should be structured as `{text: "...",label: "..."}`.<br><br>Note: [Custom Models](/training-representation-models) trained on classification examples don't require the `examples` parameter to be passed in explicitly.<br>**Constraints**: *Maximum Items*: `2500` |
| `model` | `str` | Optional | The identifier of the model. Currently available models are `embed-multilingual-v2.0`, `embed-english-light-v2.0`, and `embed-english-v2.0` (default). Smaller "light" models are faster, while larger models will perform better. [Custom models](/docs/training-custom-models) can also be supplied with their full ID. |
| `preset` | `str` | Optional | The ID of a custom playground preset. You can create presets in the [playground](https://dashboard.cohere.ai/playground/classify?model=large). If you use a preset, all other parameters become optional, and any included parameters will override the preset's parameters. |
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
  "preset": "my-preset-a58sbd",
  "model": "model2",
  "truncate": "END"
}
```

