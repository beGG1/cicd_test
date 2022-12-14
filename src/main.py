"""main."""
import uvicorn

from api.v1.schema import app

if __name__ == '__main__':
    port = 8000
    uvicorn.run('main:app', host='127.0.0.1', port=port, reload=True)
