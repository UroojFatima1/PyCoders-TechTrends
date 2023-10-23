
# Knowledge Graph

## Structure

`KnowledgeGraph`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `title` | `str` | Required | - |
| `images` | `List[object]` | Required | - |
| `website` | `str` | Required | - |
| `source` | [`Search`](../../doc/models/search.md) | Required | - |
| `description` | `str` | Required | - |
| `known_attributes` | [`List[KnownAttribute]`](../../doc/models/known-attribute.md) | Required | - |
| `block_position` | `int` | Required | - |
| `people_also_search_for` | [`List[Search]`](../../doc/models/search.md) | Required | - |
| `people_also_search_for_view_more_link` | `str` | Required | - |

## Example (as JSON)

```json
{
  "id": "id8",
  "title": "title4",
  "images": [
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
  "website": "website4",
  "source": {
    "name": "name4",
    "link": "link4"
  },
  "description": "description8",
  "known_attributes": [
    {
      "attribute": "attribute4",
      "value": "value8",
      "name": "name6"
    }
  ],
  "block_position": 204,
  "people_also_search_for": [
    {
      "name": "name8",
      "link": "link8"
    }
  ],
  "people_also_search_for_view_more_link": "people_also_search_for_view_more_link0"
}
```

