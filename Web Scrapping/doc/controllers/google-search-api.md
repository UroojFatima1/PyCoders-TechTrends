# Google Search API

```python
google_search_api_controller = client.google_search_api
```

## Class Name

`GoogleSearchAPIController`


# Simple Search

```python
def simple_search(self,
                 search)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `search` | `str` | Query, Required | The text you would put in the Google search bar. |

## Response Type

[`SearchResponse`](../../doc/models/search-response.md)

## Example Usage

```python
search = 'pizza new york'

result = google_search_api_controller.simple_search(search)
print(result)
```

