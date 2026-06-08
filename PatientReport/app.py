from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import patients, predictions

app = FastAPI(
    title="SURF API - Unified Application",
    description="Combined Patient Management and Insurance Prediction System",
    version="1.0.0"
)

# Include routers
app.include_router(patients.router)
app.include_router(predictions.router)


@app.get("/", summary="Home", tags=["General"])
def home():
    return {"message": "Patient Management System & Insurance Prediction API"}


@app.get("/about", summary="About", tags=["General"])
def about():
    return {
        "message": "A fully functional unified system combining Patient management and Insurance prediction capabilities",
        "endpoints": {
            "patients": "/api/patients",
            "predictions": "/api/predictions",
            "docs": "/docs"
        }
    }


@app.get("/health", summary="Health Check", tags=["General"])
def health_check():
    return {"status": "healthy", "message": "API is running"}
