# Usage

## Running Locally

1. Install dependencies:
    ```bash
    pip install flask
    ```
2. Run the app:
    ```bash
    python app.py
    ```
3. Access endpoints:
    - [http://localhost:5000/api/v1/details](http://localhost:5000/api/v1/details)
    - [http://localhost:5000/api/v1/healthz](http://localhost:5000/api/v1/healthz)

## Environment Variables

- `INFRA_DATA`: Optional. Used to inject infrastructure-related data into the `/api/v1/details` response.