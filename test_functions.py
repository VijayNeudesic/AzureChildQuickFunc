#!/usr/bin/env python3
"""
Basic test script for Azure Functions
This script tests the function modules directly without requiring the Azure Functions runtime.
"""

import json
import sys
import os
from datetime import datetime
from unittest.mock import Mock

# Add the project root to the path so we can import the functions
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the function modules
from NewTestChildFunc import main as new_test_child_func
from TestingAnotherFunc import main as testing_another_func


class MockHttpRequest:
    """Mock Azure Functions HttpRequest for testing"""
    
    def __init__(self, query_params=None, json_body=None):
        self.params = query_params or {}
        self._json_body = json_body
        
    def get_json(self):
        if self._json_body is None:
            raise ValueError("No JSON body")
        return self._json_body


def test_new_test_child_func():
    """Test NewTestChildFunc function"""
    print("Testing NewTestChildFunc...")
    
    # Test 1: With name parameter
    req = MockHttpRequest(query_params={'name': 'TestUser'})
    response = new_test_child_func(req)
    
    print(f"Test 1 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 1 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'TestUser' in response_data['message']
    assert 'timestamp' in response_data
    print("✓ Test 1 passed\n")
    
    # Test 2: Without name parameter
    req = MockHttpRequest()
    response = new_test_child_func(req)
    
    print(f"Test 2 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 2 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'instructions' in response_data
    print("✓ Test 2 passed\n")
    
    # Test 3: With JSON body
    req = MockHttpRequest(json_body={'name': 'JSONUser'})
    response = new_test_child_func(req)
    
    print(f"Test 3 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 3 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'JSONUser' in response_data['message']
    print("✓ Test 3 passed\n")


def test_testing_another_func():
    """Test TestingAnotherFunc function"""
    print("Testing TestingAnotherFunc...")
    
    # Test 1: Basic functionality
    req = MockHttpRequest(query_params={'name': 'TestUser'})
    response = testing_another_func(req)
    
    print(f"Test 1 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 1 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'TestUser' in response_data['message']
    print("✓ Test 1 passed\n")
    
    # Test 2: With fact and system info
    req = MockHttpRequest(query_params={
        'name': 'TestUser',
        'fact': 'true',
        'system': 'true'
    })
    response = testing_another_func(req)
    
    print(f"Test 2 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 2 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'fun_fact' in response_data
    assert 'system_info' in response_data
    print("✓ Test 2 passed\n")
    
    # Test 3: Without name (should show usage)
    req = MockHttpRequest()
    response = testing_another_func(req)
    
    print(f"Test 3 - Status Code: {response.status_code}")
    response_data = json.loads(response.get_body().decode())
    print(f"Test 3 - Response: {json.dumps(response_data, indent=2)}")
    
    assert response.status_code == 200
    assert 'usage' in response_data
    print("✓ Test 3 passed\n")


def main():
    """Run all tests"""
    print("Azure Functions Test Suite")
    print("=" * 50)
    
    try:
        test_new_test_child_func()
        test_testing_another_func()
        
        print("🎉 All tests passed successfully!")
        return 0
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())