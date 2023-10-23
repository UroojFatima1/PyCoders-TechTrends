
# Embed Request

## Structure

`EmbedRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `texts` | `List[str]` | Required | An array of strings for the model to embed. Maximum number of texts per call is `96`. We recommend reducing the length of each text to be under `512` tokens for optimal quality.<br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `96` |
| `model` | `str` | Optional | The identifier of the model. Currently available models are `embed-english-light-v2.0`, `embed-multilingual-v2.0` and `embed-english-v2.0` (default). Smaller "light" models are faster, while larger models will perform better. [Custom models](/docs/training-custom-models) can also be supplied with their full ID.<br><br>Models Embedding Names:<br><br>* `embed-english-light-v2.0` 1024<br>* `embed-english-v2.0` 4096<br>* `embed-multilingual-v2.0` 768 |
| `truncate` | [`TruncateEnum`](../../doc/models/truncate-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "texts": [
    "texts6"
  ],
  "model": "model2",
  "truncate": "END"
}
```

