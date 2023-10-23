
# Search Response

## Structure

`SearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `meta_data` | [`MetaData`](../../doc/models/meta-data.md) | Required | - |
| `organic_results` | [`List[OrganicResults]`](../../doc/models/organic-results.md) | Required | - |
| `local_results` | [`List[LocalResults]`](../../doc/models/local-results.md) | Required | - |
| `top_ads` | `List[str]` | Required | - |
| `bottom_ads` | `List[str]` | Required | - |
| `related_queries` | [`List[RelatedQueries]`](../../doc/models/related-queries.md) | Required | - |
| `questions` | [`List[Questions]`](../../doc/models/questions.md) | Required | - |
| `top_stories` | [`List[TopStories]`](../../doc/models/top-stories.md) | Required | - |
| `news_results` | `str` | Required | - |
| `knowledge_graph` | [`KnowledgeGraph`](../../doc/models/knowledge-graph.md) | Required | - |
| `related_searches` | [`RelatedSearches`](../../doc/models/related-searches.md) | Required | - |

## Example (as JSON)

```json
{
  "meta_data": {
    "url": "url2",
    "number_of_results": 86,
    "location": {
      "key1": "val1",
      "key2": "val2"
    },
    "number_of_organic_results": 22,
    "number_of_ads": 18,
    "number_of_page": 150
  },
  "organic_results": [
    {
      "url": "url8",
      "displayed_url": "displayed_url6",
      "description": {
        "key1": "val1",
        "key2": "val2"
      },
      "position": 20,
      "title": "title0",
      "domain": "domain0",
      "sitelinks": {
        "key1": "val1",
        "key2": "val2"
      },
      "rich_snippet": {
        "key1": "val1",
        "key2": "val2"
      },
      "date": "date0",
      "date_utc": "date_utc0"
    }
  ],
  "local_results": [
    {
      "title": "title8",
      "review": 194.64,
      "review_count": 38,
      "position": 94
    }
  ],
  "top_ads": [
    "top_ads8"
  ],
  "bottom_ads": [
    "bottom_ads8"
  ],
  "related_queries": [
    {
      "title": "title6",
      "url": "url4",
      "position": 34
    }
  ],
  "questions": [
    {
      "text": "text2",
      "position": 0,
      "answer": "answer6"
    }
  ],
  "top_stories": [
    {
      "title": "title6",
      "link": "link0",
      "source": "source6",
      "data": "data0",
      "position": 216
    }
  ],
  "news_results": "news_results6",
  "knowledge_graph": {
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
  },
  "related_searches": {
    "query": "query4",
    "link": "link4",
    "type": "type6",
    "position": 0
  }
}
```

