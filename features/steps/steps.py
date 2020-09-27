from behave import given, when, then, step
import requests
import json

global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}

@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url

@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] =get_api_endpoint

@given(u'Set POST api endpoint as "{post_api_endpoint}"')
def step_impl(context, post_api_endpoint):
    global_general_variables['POST_api_endpoint'] = post_api_endpoint

@given(u'Set DELETE api endpoint with id as {petId}')
def step_impl(context, petId):
    global_general_variables['DELETE_api_endpoint'] = petId
    global_general_variables['basic_application_URL']+=petId;


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type

@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type

@when(u'Set Query param as "{query_param}"')
def step_impl(context, query_param):
    if 'empty' in query_param:
        http_request_url_query_param.clear()
    else:
        http_request_url_query_param.clear()
        http_request_url_query_param['status'] = query_param;

@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,headers=http_request_header,params=http_request_url_query_param,data=http_request_body)
    elif 'POST' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] =requests.post(url_temp,headers=http_request_header,params=http_request_url_query_param,data=json.dumps(http_request_body))
    elif 'PUT' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] =requests.put(url_temp,headers=http_request_header,params=http_request_url_query_param,data=json.dumps(http_request_body))
    elif 'DELETE' == http_request_type:
        http_request_url_query_param.clear()
        global_general_variables['response_full'] =requests.delete(url_temp,headers=http_request_header,params=http_request_url_query_param,data=http_request_body)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'

@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)

@when(u'Set BODY form param using basic pet name as {petname} and status as {status}')
def step_impl(context,petname,status):
    http_request_body["name"] = petname;
    http_request_body["status"] = status;


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type

@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'

@given(u'Set PUT api endpoint as "{put_api_endpoint}"')
def step_impl(context, put_api_endpoint):
    global_general_variables['POST_api_endpoint'] = put_api_endpoint

@when(u'Modify BODY form pet name as {name} and status as {status}')
def step_impl(context, name,status):
    http_request_body["name"] = name;
    http_request_body["status"] = status;

@then(u'Response BODY parsing for "{body_parsing_for}" should be successful')
def step_impl(context, body_parsing_for):
    current_json = global_general_variables['response_full'].context()
    data = json.loads(current_json);
    if 'GET__PET' == body_parsing_for:
        for key, value in data.items():
            print(key, value);
    elif 'POST__PET' == body_parsing_for:
       print('ID: ' + data['id'])
       print('Name: ' + data['name'])
       print('Status: ' + data['status'])
    elif 'PUT__MODIFY__PET' == body_parsing_for:
        print('ID: ' + current_json['id'])
        print('Name: ' + current_json['name'])
        print('Status: ' + current_json['status'])
    elif 'DELETE__PET' == body_parsing_for:
        print('Code: ' + current_json['code'])
        print('Id: ' + current_json['message'])
