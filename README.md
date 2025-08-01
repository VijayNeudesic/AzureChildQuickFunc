# Azure Functions Demo Project

This project demonstrates Azure Functions capabilities with Python, featuring enhanced HTTP trigger functions that showcase various serverless computing concepts.

## Functions Overview

### 1. NewTestChildFunc
A time-aware greeting function that provides personalized responses based on the current time of day.

**Features:**
- Time-based greetings (Good morning/afternoon/evening)
- JSON responses with structured data
- Comprehensive error handling
- Detailed logging

**Usage:**
```bash
# Query parameter
GET /api/NewTestChildFunc?name=Alice

# JSON body
POST /api/NewTestChildFunc
{
  "name": "Alice"
}
```

**Response Example:**
```json
{
  "message": "Good morning, Alice! Welcome to our Azure Functions demo.",
  "timestamp": "2025-08-01T10:30:00.123456",
  "function": "NewTestChildFunc",
  "note": "This function demonstrates time-based greetings and JSON responses."
}
```

### 2. TestingAnotherFunc
An enhanced function that provides optional additional information including Azure fun facts and system details.

**Features:**
- Conditional response data based on parameters
- Random Azure/cloud computing fun facts
- System information display
- Interactive parameter documentation

**Parameters:**
- `name`: Your name for personalized greeting
- `fact`: Set to 'true' to include a fun fact about Azure
- `system`: Set to 'true' to include system information

**Usage:**
```bash
# Basic usage
GET /api/TestingAnotherFunc?name=Bob

# With additional features
GET /api/TestingAnotherFunc?name=Bob&fact=true&system=true

# JSON body
POST /api/TestingAnotherFunc
{
  "name": "Bob",
  "fact": true,
  "system": true
}
```

**Response Example:**
```json
{
  "function": "TestingAnotherFunc",
  "message": "Hello, Bob! This function demonstrates enhanced capabilities.",
  "timestamp": "2025-08-01T10:30:00.123456",
  "fun_fact": "Azure spans more than 60 regions worldwide, more than any other cloud provider.",
  "system_info": {
    "python_version": "3.11+",
    "runtime": "Azure Functions Python Worker",
    "timestamp": "2025-08-01T10:30:00.123456",
    "function_version": "2.0"
  }
}
```

## Local Development

### Prerequisites
- Python 3.11 or higher
- Azure Functions Core Tools (for local testing)
- Azure CLI (for deployment)

### Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally (if you have Azure Functions Core Tools installed):
   ```bash
   func start
   ```

### Project Structure
```
├── .github/workflows/     # CI/CD pipeline
├── .vscode/              # VS Code configuration
├── NewTestChildFunc/     # Time-aware greeting function
│   ├── __init__.py
│   ├── function.json
│   └── sample.dat
├── TestingAnotherFunc/   # Enhanced demo function
│   ├── __init__.py
│   ├── function.json
│   └── sample.dat
├── host.json            # Functions runtime configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Deployment

This project includes a GitHub Actions workflow for automated deployment to Azure Functions. The workflow is triggered manually and requires:

- Azure service principal credentials
- Target Function App name

### Manual Deployment
1. Ensure you have Azure CLI installed and logged in
2. Create a Function App in Azure
3. Deploy using Azure Functions Core Tools:
   ```bash
   func azure functionapp publish <your-function-app-name>
   ```

## Features Demonstrated

- **HTTP Triggers**: Both functions respond to HTTP requests
- **JSON Processing**: Handle JSON request bodies and return structured JSON responses
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Logging**: Structured logging for monitoring and debugging
- **Parameter Handling**: Support for both query parameters and JSON body data
- **Time-based Logic**: Dynamic responses based on current time
- **Random Data Generation**: Fun facts with random selection
- **System Information**: Runtime and environment details
- **Documentation**: Self-documenting APIs with usage examples

## API Testing

### Test NewTestChildFunc
```bash
# Basic test
curl "https://your-function-app.azurewebsites.net/api/NewTestChildFunc?name=TestUser"

# Test without name parameter
curl "https://your-function-app.azurewebsites.net/api/NewTestChildFunc"

# Test with JSON body
curl -X POST "https://your-function-app.azurewebsites.net/api/NewTestChildFunc" \
  -H "Content-Type: application/json" \
  -d '{"name": "TestUser"}'
```

### Test TestingAnotherFunc
```bash
# Basic test
curl "https://your-function-app.azurewebsites.net/api/TestingAnotherFunc?name=TestUser"

# Test with all features
curl "https://your-function-app.azurewebsites.net/api/TestingAnotherFunc?name=TestUser&fact=true&system=true"

# Test with JSON body
curl -X POST "https://your-function-app.azurewebsites.net/api/TestingAnotherFunc" \
  -H "Content-Type: application/json" \
  -d '{"name": "TestUser", "fact": true, "system": true}'
```

## Contributing

This is a demo project showcasing Azure Functions capabilities. Feel free to extend the functions with additional features or create new functions to demonstrate other Azure services integration.

## License

This project is for demonstration purposes.