
# Result 3

## Structure

`Result3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `input` | `str` | Required | The input text that was classified |
| `prediction` | `str` | Required | The predicted class for the associated query |
| `confidence` | `float` | Optional | The confidence score for the top predicted class |
| `labels` | [`Dict[str, Labels]`](../../doc/models/labels.md) | Required | A map containing each class and its confidence score according to the classifier. The score is computed as follows:<br><br>1. Obtain the likelihood from the back of every generate prompt until the label is formed.<br>2. Divide the sum from Step 1 by the number of tokens in the label.<br>3. Normalize scores with a softmax. |

## Example (as JSON)

```json
{
  "input": "input8",
  "prediction": "prediction6",
  "confidence": 33.06,
  "labels": {
    "key0": {
      "confidence": 94.28
    },
    "key1": {
      "confidence": 94.29
    }
  }
}
```

