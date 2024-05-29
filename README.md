# API Test Suite
# automated tests for REST API endpoints. The tests are implemented using `requests` and `pytest`.

## Test Cases

### 1. GET - List Users
- **Why**: Ensures that the endpoint for listing users is functional and returns the expected data.
- **Steps**:
  1. Send a GET request to the endpoint.
  2. Validate the response status code.
  3. Validate the structure and content of the response.
  4. Assert the "total" value in the response.
  5. Assert the "last_name" for the first and second users in the "data" array.
  6. Count the number of received users in the "data" array and compare it with the "total" value.

### 2. POST - Create User
- **Why**: Ensures that the endpoint for creating a new user is functional and correctly creates a user.
- **Steps**:
  1. Send a POST request with user data to the endpoint.
  2. Validate the response status code.
  3. Assert that the response contains an ID and timestamp of `createdAt`.
  4. Make the test data-driven using an external data source.
  5. Assert that the response time was less than a defined limit (e.g., 100 ms).
  
## External Data Source
Create a `user_data.json` file in the `data` directory


## Install dependencies:
1. pip install -r requirements.txt  


## Setup

1. Clone the repository:
 git clone https://github.com/PeterFabianGit/Moxymind_pythonProject2.git

