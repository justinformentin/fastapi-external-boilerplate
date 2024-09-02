## Why?

I needed a quick way to create an API that I could deploy on my VPS. Nothing fancy, just a few endpoints that can be exposed publicly. 

Every other boilerplate I found either used specific tools that I didn't want, were set up to be deployed a certain way, or weren't intended to be a public API.

If you have similar needs, this is a good starting place. 

## Development

1. Create and activate a virtualenv 

2. Install the requirements
```bash
pip install -r requirements.txt
```

3. Run the server with uvicorn
```bash
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

## Deployment

If you are using any "one click" installers for platforms like vercel, linode, digitalocean, you will need to include another file outlined by that platform for running the server.

You will need to add a reverse proxy.

For apache, to your `sites-enabled/domain.com.conf` file add:

```bash
    ProxyPreserveHost On
    ProxyPass /v1/ http://localhost:5000/
    ProxyPassReverse /v1/ http://localhost:5000/
```

## Usage

This is a simple example showing the usage of an endpoint, set up using the router, middleware to handle CORS and an API Token check, and a model for the endpoint response.


### main.py
The `main.py` contains the routes, a simple logger, and most importantly, configuration for CORS. 

### CORS Middleware
When editing, it's important to note a few things. Currently, the FastAPI documentation doesn't tell you everything you need for an externally available API. A lot of CORS documentation you'll find is from the point of view of an internal service. 

1. The CORS middleware is *before* the token middleware. It does not work the other way around. If you add other middleware, they might need to go before or after the CORS middleware. You will need to test it.
2. The OPTIONS check in the middleware needs to happen because other servers send a preflight OPTIONS check, and those headers must be set, in addition to returning an ok response.

### API Token Check Middleware
This is assuming your service provides some token, for example `xx_18d903jf093jf93hf8rgh389`. This is *not* related to JWT, and that's a whole separate implementation that this boilerplate does not go into.

The `token.py` middleware file contains the check for the token, which should be in every request's `Authorization` header "Bearer" token.

The `token_service(token)` is a placeholder for your own service that checks the validity of the API token that gets sent in the headers.

### Endpoints
The `api` directory contains the files for each endpoint. You can make multiple files, one for each endpoint, and add them to the router in the `main.py` file.

### Models
The endpoints use pydantic's Models for validation for the request and the response. Create new models for each new route, request, response, exception, etc.
