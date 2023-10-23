# HTMLAPI

```python
htmlapi_controller = client.htmlapi
```

## Class Name

`HTMLAPIController`

## Methods

* [Usage Information](../../doc/controllers/htmlapi.md#usage-information)
* [JSON Response](../../doc/controllers/htmlapi.md#json-response)
* [HTML](../../doc/controllers/htmlapi.md#html)
* [Screenshot Response](../../doc/controllers/htmlapi.md#screenshot-response)


# Usage Information

```python
def usage_information(self)
```

## Response Type

`void`

## Example Usage

```python
result = html_api_controller.usage_information()
print(result)
```


# JSON Response

```python
def json_response(self,
                 url,
                 render_js,
                 json_response)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Query, Required | The URL you want to scrape |
| `render_js` | `bool` | Query, Required | Render the website  in  an headless browser |
| `json_response` | `bool` | Query, Required | Wrap response in JSON. |

## Response Type

`void`

## Example Usage

```python
url = 'https://httpbin-scrapingbee.cleverapps.io/html'

render_js = False

json_response = True

result = html_api_controller.json_response(
    url,
    render_js,
    json_response
)
print(result)
```


# HTML

```python
def html(self,
        url,
        render_js)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Query, Required | The URL you want to scrape |
| `render_js` | `bool` | Query, Required | Render the website  in  an headless browser |

## Response Type

`str`

## Example Usage

```python
url = 'https://httpbin-scrapingbee.cleverapps.io/html'

render_js = False

result = html_api_controller.html(
    url,
    render_js
)
print(result)
```


# Screenshot Response

```python
def screenshot_response(self,
                       url,
                       render_js,
                       screenshot)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Query, Required | The URL you want to scrape |
| `render_js` | `bool` | Query, Required | Render the website  in  an headless browser |
| `screenshot` | `bool` | Query, Required | - |

## Response Type

`binary`

## Example Usage

```python
url = 'https://httpbin-scrapingbee.cleverapps.io'

render_js = True

screenshot = True

result = html_api_controller.screenshot_response(
    url,
    render_js,
    screenshot
)
print(result)
```

