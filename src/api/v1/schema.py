"""Scema for Swagger UI."""

from fastapi import FastAPI

app = FastAPI(
    title='ChimichangApp',
    description='lol',
    version='0.0.1',
    terms_of_service='http://example.com/terms/',
    contact={
        'name': 'Deadpoolio the Amazing',
        'url': 'http://x-force.example.com/contact/',
        'email': 'dp@x-force.example.com',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    )


@app.get('/health_check')
async def helth_check() -> bool:
    """Health check API.

    Returns:
        bool: _description_
    """
    return True
