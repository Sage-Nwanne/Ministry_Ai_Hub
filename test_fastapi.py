#!/usr/bin/env python3

try:
    from fastapi import FastAPI
    print("✅ FastAPI imported successfully")
    
    app = FastAPI()
    print("✅ FastAPI app created successfully")
    
    @app.get("/")
    def read_root():
        return {"message": "FastAPI is working!"}
    
    print("✅ Route defined successfully")
    print("🎯 FastAPI is ready to use!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Other error: {e}")