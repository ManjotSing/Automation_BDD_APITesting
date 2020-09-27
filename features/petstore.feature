Feature: REST API testing framework using BDD framework in Python for Petstore API Collection.

Background:
	Given Set basic web application url is "https://petstore.swagger.io/v2/pet/"

Scenario:GET list of pets based on their status
	Given Set GET api endpoint as "findByStatus"
    When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
    And Set Query param as "empty"
	And Raise "GET" HTTP request
    Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty
	And Response BODY parsing for "GET__PET" should be successful

Scenario: POST request to Add new pet.
	  Given Set POST api endpoint as " "
	  When Set HEADER param request content type as "application/json"
	  And Set HEADER param response accept type as "application/json"
	  And Set BODY form param using basic pet name as "fluffy" and status as "available"
	  And Raise "POST" HTTP request
	  Then Valid HTTP response should be received
	  And Response http code should be 200
	  And Response HEADER content type should be "application/json"
	  And Response BODY should not be null or empty
	  And Response BODY parsing for "POST__PET" should be successful

Scenario: PUT request to update pet information.
  	Given Set PUT api endpoint as " "
	When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Modify BODY form pet name as "Shadow" and status as "sold"
	And Raise "PUT" HTTP request
  	Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty
	And Response BODY parsing for "PUT__MODIFY__PET" should be successful

Scenario: DELETE request to delete pet with pet id.
  	Given  Set DELETE api endpoint with id as 15435006002149
 	When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json"
	And Set Query param as "based on user details"
	And Raise "DELETE" HTTP request
  	Then Valid HTTP response should be received
	And Response http code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty
	And Response BODY parsing for "DELETE__PET" should be successful

