
# Single Generation

## Structure

`SingleGeneration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `text` | `str` | Required | - |
| `index` | `int` | Optional | Refers to the nth generation. Only present when `num_generations` is greater than zero. |
| `likelihood` | `float` | Optional | - |
| `token_likelihoods` | [`List[TokenLikelihood]`](../../doc/models/token-likelihood.md) | Optional | Only returned if `return_likelihoods` is set to `GENERATION` or `ALL`. The likelihood refers to the average log-likelihood of the entire specified string, which is useful for [evaluating the performance of your model](likelihood-eval), especially if you've created a [custom model](/docs/training-custom-models). Individual token likelihoods provide the log-likelihood of each token. The first token will not have a likelihood. |

## Example (as JSON)

```json
{
  "id": "id0",
  "text": "text0",
  "index": 44,
  "likelihood": 69.76,
  "token_likelihoods": [
    {
      "token": "token3",
      "likelihood": 154.59
    }
  ]
}
```

