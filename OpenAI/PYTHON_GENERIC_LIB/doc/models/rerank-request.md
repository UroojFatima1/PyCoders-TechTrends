
# Rerank Request

## Structure

`RerankRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | `str` | Optional | The identifier of the model to use, one of : `rerank-english-v2.0`, `rerank-multilingual-v2.0` |
| `query` | `str` | Required | The search query |
| `documents` | `List[object]` | Required | A list of document objects or strings to rerank.<br>If a document is provided the text fields is required and all other fields will be preserved in the response.<br>The total max chunks (length of documents * max_chunks_per_doc) must be less than 10000. |
| `top_n` | `int` | Optional | The number of most relevant documents or indices to return, defaults to the length of the documents<br>**Constraints**: `>= 1` |
| `return_documents` | `bool` | Optional | - If false, returns results without the doc text - the api will return a list of {index, relevance score} where index is inferred from the list passed into the request.<br>- If true, returns results with the doc text passed in - the api will return an ordered list of {index, text, relevance score} where index + text refers to the list passed into the request.<br>**Default**: `False` |
| `max_chunks_per_doc` | `int` | Optional | The maximum number of chunks to produce internally from a document<br>**Default**: `10` |

## Example (as JSON)

```json
{
  "query": "query0",
  "documents": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "return_documents": false,
  "max_chunks_per_doc": 10,
  "model": "model2",
  "top_n": 136
}
```

