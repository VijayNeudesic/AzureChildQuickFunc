import logging
import json
import random
from datetime import datetime
from typing import Optional, Dict, Any

import azure.functions as func


def generate_fun_fact() -> str:
    """Generate a random fun fact about Azure or cloud computing"""
    facts = [
        "Azure spans more than 60 regions worldwide, more than any other cloud provider.",
        "Azure Functions can automatically scale from zero to thousands of instances.",
        "Python is one of the most popular languages for serverless computing.",
        "Azure Functions supports multiple trigger types including HTTP, Timer, and Queue.",
        "Serverless computing can reduce costs by up to 90% for certain workloads.",
        "Azure Functions can run for up to 10 minutes by default (or longer with premium plans).",
        "Cold starts in Azure Functions typically last less than a few seconds.",
        "You can deploy Azure Functions using ZIP packages, Docker containers, or from source control."
    ]
    return random.choice(facts)


def get_system_info() -> Dict[str, Any]:
    """Get basic system information"""
    return {
        "python_version": "3.11+",
        "runtime": "Azure Functions Python Worker",
        "timestamp": datetime.now().isoformat(),
        "function_version": "2.0"
    }


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('TestingAnotherFunc: Processing HTTP request')

    try:
        # Extract parameters
        name: Optional[str] = req.params.get('name')
        include_fact: bool = req.params.get('fact', '').lower() == 'true'
        include_system: bool = req.params.get('system', '').lower() == 'true'
        
        # Try to get data from request body if not in query params
        if not name:
            try:
                req_body = req.get_json()
                if req_body:
                    name = req_body.get('name')
                    include_fact = req_body.get('fact', include_fact)
                    include_system = req_body.get('system', include_system)
            except ValueError:
                # No JSON body is acceptable, just continue without name
                pass

        # Build response
        response_data = {
            "function": "TestingAnotherFunc",
            "message": f"Hello, {name}! This function demonstrates enhanced capabilities." if name else "Welcome to the enhanced Azure Functions demo!",
            "timestamp": datetime.now().isoformat()
        }

        # Add optional data based on parameters
        if include_fact:
            response_data["fun_fact"] = generate_fun_fact()
        
        if include_system:
            response_data["system_info"] = get_system_info()

        # Add usage instructions if no name provided
        if not name:
            response_data["usage"] = {
                "parameters": {
                    "name": "Your name for personalized greeting",
                    "fact": "Set to 'true' to include a fun fact about Azure",
                    "system": "Set to 'true' to include system information"
                },
                "example_url": "?name=Alice&fact=true&system=true",
                "example_body": '{"name": "Alice", "fact": true, "system": true}'
            }

        logging.info(f'Successfully processed request for user: {name or "anonymous"}')
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f'Unexpected error in TestingAnotherFunc: {str(e)}')
        error_response = {
            "error": "Internal server error",
            "message": "An unexpected error occurred while processing your request",
            "timestamp": datetime.now().isoformat(),
            "function": "TestingAnotherFunc"
        }
        return func.HttpResponse(
            json.dumps(error_response),
            status_code=500,
            mimetype="application/json"
        )
