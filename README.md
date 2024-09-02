### **IP Geolocation Tool**
### **Overview**
The IP Geolocation Tool is a Python-based application designed to geocode a list of IP addresses using the ipgeolocation.io API. The application reads IP addresses from a CSV file, processes them in batches, and outputs the geocoded data to a JSON file. The tool includes robust error handling and supports retry mechanisms for transient errors.

### **Features**

- Batch Processing: Efficiently processes IP addresses in batches to optimize API usage and minimize request times.
- Error Handling: Handles various exceptions such as HTTP errors, connection errors, and timeouts.
- Logging: Provides detailed logging for tracking and debugging.

### **Prerequisites**

Before running the project, ensure you have the following installed:

- Python 3.8+
- Pip (Python package installer)
- Git (optional, for cloning the repository)

### **Project Structure**

project/
│
├── data/
│   ├── ip_addresses.csv          # Input file containing IP addresses
│   └── geocoded_ips.json         # Output file containing geocoded data
│
├── geocode_function.py           # Contains the geocoding and batch processing functions
├── main.py                       # Main script to execute the application
├── tests/
│ │   └── test_geocode.py           # Unit tests for the geocoding functions
│
├── .env                          # Environment file for storing API keys
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
### **Installation**

1. **Clone the Repository**

If you haven't cloned the repository yet, do so with:


git clone https://github.com/yourusername/ip-geolocation-tool.git
cd ip-geolocation-tool

2. **Install Dependencies**

Use pip to install the required Python packages:


pip install -r requirements.txt

3. **Set Up Environment Variables**

Create a .env file in the root directory and add your IP_GEOLOCATION_API_KEY:

makefile
Copy code
IP_GEOLOCATION_API_KEY=your_api_key_here
Replace your_api_key_here with your actual API key from ipgeolocation.io.

### **Usage**
1. **Prepare Your IP Address File**
Place your IP addresses in a CSV file named ip_addresses.csv within the data/ directory. The file should have a single column named ip_address, like this:

Copy code
ip_address
8.8.8.8
8.8.4.4
192.168.1.1
2. ** Run the Main Script**
Execute the main.py script to start processing the IP addresses:

bash
Copy code
python main.py
This script will read the IP addresses, geocode them, and save the results in data/geocoded_ips.json.

3. **Output**
The geocoded results will be saved as a JSON file in the data/ directory:

json
Copy code
[
    {
        "ip": "8.8.8.8",
        "country_name": "United States",
        "city": "Mountain View",
        "latitude": "37.4056",
        "longitude": "-122.0775"
    },
    ...
]
###** Error Handling and Retries**

- HTTP Errors: The tool gracefully handles HTTP errors like 404, 500, and specifically 423 (resource locked).

- Retry Mechanism: When a 423 error occurs, the tool retries the request with an exponential backoff strategy.

- Logging: All activities, including errors and retries, are logged for better monitoring.

###** Testing**
The project includes unit tests to validate the functionality of the geocoding functions.

**Running the Tests**
Navigate to the project root and execute:


python -m unittest discover -s tests
This command will discover and run all tests within the tests/ directory.

**Test Structure**

- test_geocode.py: Contains tests for the geocode_ip and batch_ips_processing functions, including handling of successful responses, HTTP errors, and batch processing scenarios.

### **Future** Improvements

- Rate Limiting: Implement dynamic rate limiting to avoid hitting the API's request limits.

- Parallel Processing: Enhance the tool to process IPs in parallel to further reduce processing time.

- Extended Error Handling: Handle additional HTTP status codes and edge cases.

### **Contributing**
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or improvements.

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.
