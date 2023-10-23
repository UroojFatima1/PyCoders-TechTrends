# API

```python
client_controller = client.client
```

## Class Name

`APIController`

## Methods

* [Detokenize](../../doc/controllers/api.md#detokenize)
* [Generate](../../doc/controllers/api.md#generate)
* [Detect-Language](../../doc/controllers/api.md#detect-language)
* [Tokenize](../../doc/controllers/api.md#tokenize)
* [Classify](../../doc/controllers/api.md#classify)
* [Summarize](../../doc/controllers/api.md#summarize)
* [Rerank](../../doc/controllers/api.md#rerank)


# Detokenize

This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page.

```python
def detokenize(self,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DetokenizeRequest`](../../doc/models/detokenize-request.md) | Body, Optional | - |

## Response Type

[`DetokenizeResponse`](../../doc/models/detokenize-response.md)

## Example Usage

```python
body = DetokenizeRequest(
    tokens=[
        10104,
        12221,
        1315,
        34,
        1420,
        69
    ]
)

result = client_controller.detokenize(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "text": " Anton Mun",
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```


# Generate

This endpoint generates realistic text conditioned on a given input.

```python
def generate(self,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GenerateRequest`](../../doc/models/generate-request.md) | Body, Optional | - |

## Response Type

[`Generation`](../../doc/models/generation.md)

## Example Usage

```python
body = GenerateRequest(
    prompt='Please explain to me how LLMs work'
)

result = client_controller.generate(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "8c88b6dd-a818-493d-9960-103a85359625",
  "generations": [
    {
      "id": "e4ce17ca-f705-4740-a34e-e6f0d17d5c16",
      "text": " LLMs are large language models trained on massive amounts of text data, which enable them to generate human"
    }
  ],
  "prompt": "Please explain to me how LLMs work",
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 498 | Blocked Input or Output | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Detect-Language

This endpoint identifies which language each of the provided texts is written in.

```python
def detect_language(self,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DetectLanguageRequest`](../../doc/models/detect-language-request.md) | Body, Optional | - |

## Response Type

[`DetectLanguageResponse`](../../doc/models/detect-language-response.md)

## Example Usage

```python
body = DetectLanguageRequest(
    texts=[
        'Hello world',
        'Здравствуй, Мир'
    ]
)

result = client_controller.detect_language(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "e649e08d-f798-48e8-8e8f-1160852705f9",
  "results": [
    {
      "language_code": "en",
      "language_name": "English"
    },
    {
      "language_code": "ru",
      "language_name": "Russian"
    }
  ],
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```


# Tokenize

This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page.

```python
def tokenize(self,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TokenizeRequest`](../../doc/models/tokenize-request.md) | Body, Optional | - |

## Response Type

[`TokenizeResponse`](../../doc/models/tokenize-response.md)

## Example Usage

```python
body = TokenizeRequest(
    text='tokenize me! :D',
    model='command'
)

result = client_controller.tokenize(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "tokens": [
    10002,
    2261,
    2012,
    8,
    2792,
    43
  ],
  "token_strings": [
    "token",
    "ize",
    " me",
    "!",
    " :",
    "D"
  ],
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Classify

This endpoint makes a prediction about which label fits the specified text inputs best. To make a prediction, Classify uses the provided `examples` of text + label pairs as a reference.

Note: [Custom Models](/training-representation-models) trained on classification examples don't require the `examples` parameter to be passed in explicitly.

```python
def classify(self,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ClassifyRequest`](../../doc/models/classify-request.md) | Body, Optional | - |

## Response Type

[`ClassifyResponse`](../../doc/models/classify-response.md)

## Example Usage

```python
body = ClassifyRequest(
    inputs=[
        'Confirm your email address',
        'hey i need u to send some $'
    ],
    examples=[
        Example(
            text='Dermatologists don\'t like her!',
            label='Spam'
        ),
        Example(
            text='Hello, open to this?',
            label='Spam'
        ),
        Example(
            text='I need help please wire me $1000 right now',
            label='Spam'
        ),
        Example(
            text='Nice to know you ;)',
            label='Spam'
        ),
        Example(
            text='Please help me?',
            label='Spam'
        ),
        Example(
            text='Your parcel will be delivered today',
            label='Not spam'
        ),
        Example(
            text='Review changes to our Terms and Conditions',
            label='Not spam'
        ),
        Example(
            text='Weekly sync notes',
            label='Not spam'
        ),
        Example(
            text='Re: Follow up from today’s meeting',
            label='Not spam'
        ),
        Example(
            text='Pre-read for tomorrow',
            label='Not spam'
        )
    ]
)

result = client_controller.classify(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "5374ccb0-9b88-4647-b23c-f6166f8a5c46",
  "classifications": [
    {
      "id": "083f55cb-f37d-4400-b779-236d28bcfd81",
      "input": "Confirm your email address",
      "prediction": "Not spam",
      "confidence": 0.8082329,
      "labels": {
        "Not spam": {
          "confidence": 0.8082329
        },
        "Spam": {
          "confidence": 0.19176713
        }
      }
    },
    {
      "id": "28b62557-2777-485f-bb05-6bb3e7361074",
      "input": "hey i need u to send some $",
      "prediction": "Spam",
      "confidence": 0.9893421,
      "labels": {
        "Not spam": {
          "confidence": 0.01065793
        },
        "Spam": {
          "confidence": 0.9893421
        }
      }
    }
  ],
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 500 | Internal Server Error | `APIException` |


# Summarize

This endpoint generates a summary in English for a given text.

```python
def summarize(self,
             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SummarizeRequest`](../../doc/models/summarize-request.md) | Body, Optional | - |

## Response Type

[`SummarizeResponse`](../../doc/models/summarize-response.md)

## Example Usage

```python
body = SummarizeRequest(
    text='Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.\n\nThe meaning of the name "ice cream" varies from one country to another. In some countries, such as the United States, "ice cream" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled "frozen dairy dessert" instead. In other countries, such as Italy and Argentina, one word is used fo all variants. Analogues made from dairy alternatives, such as goat\'s or sheep\'s milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan.'
)

result = client_controller.summarize(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "64d38a49-f241-4158-b4b2-04ce7f7489bf",
  "summary": "Ice cream is a frozen dessert made from milk or cream and flavoured with a sweetener and a spice or fruit. It can also be made by whisking a flavoured cream base and liquid nitrogen together. It is cooled below the freezing point of water and stirred to incorporate air spaces and prevent ice crystals from forming. It is a smooth, semi-solid foam that is solid at very low temperatures. It can be made from dairy alternatives for those who are lactose intolerant, allergic to dairy protein or vegan. The meaning of the name \"ice cream\" varies from one country to another.",
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```


# Rerank

This endpoint takes in a query and a list of texts and produces an ordered array with each text assigned a relevance score.

```python
def rerank(self,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RerankRequest`](../../doc/models/rerank-request.md) | Body, Optional | - |

## Response Type

[`RerankResponse`](../../doc/models/rerank-response.md)

## Example Usage

```python
body = RerankRequest(
    query='What is the capital of the United States?',
    documents=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    model='rerank-english-v2.0'
)

result = client_controller.rerank(
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "d02f0979-e59c-4b19-9e0e-542ced2fd3b3",
  "results": [
    {
      "document": {
        "text": "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.\",     \"The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.\",     \"Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.\",     \"Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.\",     \"Capital punishment (the death penalty) has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment."
      },
      "index": 0,
      "relevance_score": 0.87059724
    }
  ],
  "meta": {
    "api_version": {
      "version": "1"
    }
  }
}
```

