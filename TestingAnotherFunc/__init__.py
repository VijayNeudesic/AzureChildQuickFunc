import logging
import azure.functions as func
import sys
import os

# Add the parent directory to the Python path to import shared_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_utils import validate_name, format_greeting, log_function_call


def main(req: func.HttpRequest) -> func.HttpResponse:
    function_name = "TestingAnotherFunc"
    log_function_call(function_name)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        try:
            # Validate and sanitize the name
            validated_name = validate_name(name)
            log_function_call(function_name, validated_name)
            
            # Format greeting without last name
            greeting = format_greeting(validated_name, include_lastname=False)
            return func.HttpResponse(greeting, status_code=200)
            
        except ValueError as e:
            logging.warning(f"Invalid name parameter: {e}")
            return func.HttpResponse(
                f"Error: {str(e)}",
                status_code=400
            )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
