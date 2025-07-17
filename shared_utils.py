"""
Shared utility functions for Azure Functions
"""
import logging
from typing import Optional


def validate_name(name: Optional[str]) -> str:
    """
    Validates and sanitizes the name parameter.
    
    Args:
        name: The name to validate
        
    Returns:
        Sanitized name string
        
    Raises:
        ValueError: If name is invalid
    """
    if not name:
        raise ValueError("Name parameter is required")
    
    # Basic sanitization - remove extra whitespace
    sanitized_name = name.strip()
    
    if not sanitized_name:
        raise ValueError("Name cannot be empty or whitespace only")
    
    # Basic validation - ensure reasonable length
    if len(sanitized_name) > 100:
        raise ValueError("Name is too long (max 100 characters)")
    
    return sanitized_name


def format_greeting(name: str, include_lastname: bool = False) -> str:
    """
    Formats a greeting message.
    
    Args:
        name: The name to greet
        include_lastname: Whether to include a last name in the greeting
        
    Returns:
        Formatted greeting message
    """
    # For demonstration purposes, we'll add a mock last name
    if include_lastname:
        return f"Hello, {name} Copilot. This greeting includes your full name!"
    else:
        return f"Hello, {name}. This HTTP triggered function executed successfully."


def log_function_call(function_name: str, name: Optional[str] = None):
    """
    Logs function call details.
    
    Args:
        function_name: Name of the function being called
        name: Optional name parameter passed to the function
    """
    if name:
        logging.info(f'{function_name} called with name parameter: {name}')
    else:
        logging.info(f'{function_name} called without name parameter')