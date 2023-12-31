# -*- coding: utf-8 -*-

"""
cohereapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from cohereapi.api_helper import APIHelper
from cohereapi.models.detokenize_request import DetokenizeRequest
from cohereapi.models.generate_request import GenerateRequest
from cohereapi.models.detect_language_request import DetectLanguageRequest
from cohereapi.models.tokenize_request import TokenizeRequest
from cohereapi.models.classify_request import ClassifyRequest
from cohereapi.models.summarize_request import SummarizeRequest
from cohereapi.models.rerank_request import RerankRequest


class APIControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(APIControllerTests, cls).setUpClass()
        cls.controller = cls.client.client
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page.
    def test_detokenize(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"tokens":[10104,12221,1315,34,1420,69]}', DetokenizeRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.detokenize(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"text":" Anton Mun","meta":{"api_version":{"version":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint generates realistic text conditioned on a given input.
    def test_generate(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"prompt":"Please explain to me how LLMs work"}', GenerateRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.generate(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"8c88b6dd-a818-493d-9960-103a85359625","generations":[{"id":'
            '"e4ce17ca-f705-4740-a34e-e6f0d17d5c16","text":" LLMs are large lan'
            'guage models trained on massive amounts of text data, which enable'
            ' them to generate human"}],"prompt":"Please explain to me how LLMs'
            ' work","meta":{"api_version":{"version":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint generates realistic text conditioned on a given input.
    def test_generate_1(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"prompt":"Please explain to me how LLMs work"}', GenerateRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.generate(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/stream+json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # This endpoint identifies which language each of the provided texts is written in.
    def test_detect_language(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"texts":["Hello world","Здравствуй, Мир"]}', DetectLanguageRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.detect_language(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"e649e08d-f798-48e8-8e8f-1160852705f9","results":[{"language'
            '_code":"en","language_name":"English"},{"language_code":"ru","lang'
            'uage_name":"Russian"}],"meta":{"api_version":{"version":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page.
    def test_tokenize(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"text":"tokenize me! :D","model":"command"}', TokenizeRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.tokenize(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"tokens":[10002,2261,2012,8,2792,43],"token_strings":["token","iz'
            'e"," me","!"," :","D"],"meta":{"api_version":{"version":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint makes a prediction about which label fits the specified text inputs best. To make a prediction, Classify uses the provided `examples` of text + label pairs as a reference.
    #
    #Note: [Custom Models](/training-representation-models) trained on classification examples don't require the `examples` parameter to be passed in explicitly.
    def test_classify(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"inputs":["Confirm your email address","hey i need u to send some'
            ' $"],"examples":[{"text":"Dermatologists don\'t like her!","label"'
            ':"Spam"},{"text":"Hello, open to this?","label":"Spam"},{"text":"I'
            ' need help please wire me $1000 right now","label":"Spam"},{"text"'
            ':"Nice to know you ;)","label":"Spam"},{"text":"Please help me?","'
            'label":"Spam"},{"text":"Your parcel will be delivered today","labe'
            'l":"Not spam"},{"text":"Review changes to our Terms and Conditions'
            '","label":"Not spam"},{"text":"Weekly sync notes","label":"Not spa'
            'm"},{"text":"Re: Follow up from today’s meeting","label":"Not spam'
            '"},{"text":"Pre-read for tomorrow","label":"Not spam"}]}', ClassifyRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.classify(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"5374ccb0-9b88-4647-b23c-f6166f8a5c46","classifications":[{"'
            'id":"083f55cb-f37d-4400-b779-236d28bcfd81","input":"Confirm your e'
            'mail address","prediction":"Not spam","confidence":0.8082329,"labe'
            'ls":{"Not spam":{"confidence":0.8082329},"Spam":{"confidence":0.19'
            '176713}}},{"id":"28b62557-2777-485f-bb05-6bb3e7361074","input":"he'
            'y i need u to send some $","prediction":"Spam","confidence":0.9893'
            '421,"labels":{"Not spam":{"confidence":0.01065793},"Spam":{"confid'
            'ence":0.9893421}}}],"meta":{"api_version":{"version":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This endpoint generates a summary in English for a given text.
    def test_summarize(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"text":"Ice cream is a sweetened frozen food typically eaten as a'
            ' snack or dessert. It may be made from milk or cream and is flavou'
            'red with a sweetener, either sugar or an alternative, and a spice,'
            ' such as cocoa or vanilla, or with fruit such as strawberries or p'
            'eaches. It can also be made by whisking a flavored cream base and '
            'liquid nitrogen together. Food coloring is sometimes added, in add'
            'ition to stabilizers. The mixture is cooled below the freezing poi'
            'nt of water and stirred to incorporate air spaces and to prevent d'
            'etectable ice crystals from forming. The result is a smooth, semi-'
            'solid foam that is solid at very low temperatures (below 2 °C or 3'
            '5 °F). It becomes more malleable as its temperature increases.\\n'
            '\\nThe meaning of the name \"ice cream\" varies from one country t'
            'o another. In some countries, such as the United States, \"ice cre'
            'am\" applies only to a specific variety, and most governments regu'
            'late the commercial use of the various terms according to the rela'
            'tive quantities of the main ingredients, notably the amount of cre'
            'am. Products that do not meet the criteria to be called ice cream '
            'are sometimes labelled \"frozen dairy dessert\" instead. In other '
            'countries, such as Italy and Argentina, one word is used fo\\r all'
            ' variants. Analogues made from dairy alternatives, such as goat\'s'
            ' or sheep\'s milk, or milk substitutes (e.g., soy, cashew, coconut'
            ', almond milk or tofu), are available for those who are lactose in'
            'tolerant, allergic to dairy protein or vegan."}', SummarizeRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.summarize(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['x-api-warning'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"64d38a49-f241-4158-b4b2-04ce7f7489bf","summary":"Ice cream '
            'is a frozen dessert made from milk or cream and flavoured with a s'
            'weetener and a spice or fruit. It can also be made by whisking a f'
            'lavoured cream base and liquid nitrogen together. It is cooled bel'
            'ow the freezing point of water and stirred to incorporate air spac'
            'es and prevent ice crystals from forming. It is a smooth, semi-sol'
            'id foam that is solid at very low temperatures. It can be made fro'
            'm dairy alternatives for those who are lactose intolerant, allergi'
            'c to dairy protein or vegan. The meaning of the name \"ice cream\"'
            ' varies from one country to another.","meta":{"api_version":{"vers'
            'ion":"1"}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

