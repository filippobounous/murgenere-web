from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

try:
    from fball import inventory, investments
except ImportError:  # fball package not installed
    inventory = None
    investments = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/inventory')
@app.post('/api/inventory')
async def inventory_endpoint():
    if inventory and hasattr(inventory, 'run_inventory_analysis'):
        result = inventory.run_inventory_analysis()
    else:
        result = {"message": "Inventory analysis placeholder"}
    return JSONResponse(content=result)

@app.get('/api/investments')
@app.post('/api/investments')
async def investments_endpoint():
    if investments and hasattr(investments, 'run_investment_analysis'):
        result = investments.run_investment_analysis()
    else:
        result = {"message": "Investments analysis placeholder"}
    return JSONResponse(content=result)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
