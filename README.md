# Pytest

## Files

- **tests/conftest.py** -> To store all global fixtres which can be reused in all the test modules

- **pytest.ini** -> To store pytest configurations. Must be in root directory

- **pytest.logs** -> Write logs to this file (Optional)


### **Fixtures**:

- mark.slow -> use when we know that features may take too l;ong to process
- mark.skip -> to skip a test case, which could be a broken function at the time of test 
- mark.xfail -> we knew that function will fail (eg:zeroDivisionError)
- mark.parametrize -> to pass on multiple test data to execute and check, 

#### **example**:
```
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (2, 4)])
```

### **Mocking**:
A powerful technique that isolates the system that we are testing, and replace the external dependencies with controlled implementations called **mocks**

- When to use?
    - When fetching data from external APIs using requests. This wont depend or call the API
    - Fetching data from Database

- Use **python Unittest** to achieve mocking

