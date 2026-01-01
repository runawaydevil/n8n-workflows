#!/usr/bin/env python3
"""
Script rápido para testar se todas as dependências estão instaladas corretamente.
"""

def test_imports():
    """Testa se todas as dependências principais podem ser importadas."""
    errors = []
    
    try:
        import fastapi
        print(f"✅ FastAPI {fastapi.__version__}")
    except ImportError as e:
        errors.append(f"❌ FastAPI: {e}")
    
    try:
        import pydantic
        print(f"✅ Pydantic {pydantic.__version__}")
    except ImportError as e:
        errors.append(f"❌ Pydantic: {e}")
    
    try:
        import uvicorn
        print(f"✅ Uvicorn {uvicorn.__version__}")
    except ImportError as e:
        errors.append(f"❌ Uvicorn: {e}")
    
    try:
        import sqlite3
        print(f"✅ SQLite3 (built-in)")
    except ImportError as e:
        errors.append(f"❌ SQLite3: {e}")
    
    try:
        import jwt
        print(f"✅ PyJWT")
    except ImportError as e:
        errors.append(f"❌ PyJWT: {e}")
    
    try:
        from workflow_db import WorkflowDatabase
        print(f"✅ workflow_db module")
    except ImportError as e:
        errors.append(f"⚠️  workflow_db: {e} (normal se ainda não indexou)")
    
    if errors:
        print("\n❌ Erros encontrados:")
        for error in errors:
            print(f"  {error}")
        return False
    else:
        print("\n🎉 Todas as dependências principais estão instaladas!")
        print("\n💡 Você pode rodar o servidor com: python run.py")
        return True

if __name__ == "__main__":
    test_imports()

