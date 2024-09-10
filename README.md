## Overview

This script extracts candidate data from a remote URL, filters it based on 3 filtering funcions: industry, skills, and years of experience, a and then inserts the filtered data into a MongoDB collection.

## Requirements

- Python 3.7 or higher
- MongoDB with a collection named filtered_candidates
- Required Python libraries: `pymongo`, `requests`

## Setup

1. **Clone Repository**

2. **Set Mongo Enviroment variables**:
    export MONGO_USER="user"
    export MONGO_PASSWORD="password"
    export MONGO_CLUSTER="cluster"
    export MONGO_DB_NAME="db_name"

2. **Run the Python Script**:
    Navigate to the Directory
    Than run
    python main.py
