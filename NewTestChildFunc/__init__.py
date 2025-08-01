import logging
import json
from datetime import datetime
from typing import Optional

import azure.functions as func


def get_greeting_by_time() -> str:
    """Return appropriate greeting based on current time"""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('NewTestChildFunc: Processing HTTP request')

    try:
        # Extract name from query parameters or request body
        name: Optional[str] = req.params.get('name')
        
        if not name:
            try:
                req_body = req.get_json()
                if req_body:
                    name = req_body.get('name')
            except ValueError:
                # No JSON body is acceptable, just continue without name
                pass

        # Generate response
        if name:
            greeting = get_greeting_by_time()
            response_data = {
                "message": f"{greeting}, {name}! Welcome to our Azure Functions demo.",
                "timestamp": datetime.now().isoformat(),
                "function": "NewTestChildFunc",
                "note": "This function demonstrates time-based greetings and JSON responses."
            }
            logging.info(f'Successful greeting generated for user: {name}')
            return func.HttpResponse(
                json.dumps(response_data),
                status_code=200,
                mimetype="application/json"
            )
        else:
            response_data = {
                "message": "This HTTP triggered function executed successfully!",
                "instructions": "Pass a 'name' parameter in the query string or request body for a personalized response.",
                "example_query": "?name=YourName",
                "example_body": '{"name": "YourName"}',
                "timestamp": datetime.now().isoformat(),
                "function": "NewTestChildFunc"
            }
            return func.HttpResponse(
                json.dumps(response_data),
                status_code=200,
                mimetype="application/json"
            )

    except Exception as e:
        logging.error(f'Unexpected error in NewTestChildFunc: {str(e)}')
        error_response = {
            "error": "Internal server error",
            "message": "An unexpected error occurred while processing your request",
            "timestamp": datetime.now().isoformat(),
            "function": "NewTestChildFunc"
        }
        return func.HttpResponse(
            json.dumps(error_response),
            status_code=500,
            mimetype="application/json"
        )
