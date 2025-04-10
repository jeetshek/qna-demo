# test_app.py
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, World!")

app = web.Application()
app.router.add_get('/', handle)

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 8000))  # Changed from 3978 to 8000
    HOST = "0.0.0.0"  # Always use 0.0.0.0 in container environments
    
    print(f"Bot server running on {HOST}:{PORT}")
    web.run_app(app, host=HOST, port=PORT)