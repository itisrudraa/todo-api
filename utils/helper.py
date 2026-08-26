from fastapi import HTTPException, status, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from db_models import User
import jwt
from jwt.exceptions import InvalidTokenError
import os
from sqlalchemy import select
from dotenv import load_dotenv
from database import get_db

load_dotenv()
security = HTTPBearer()


def is_authenticated(credentials: HTTPAuthorizationCredentials = Depends(security), db=Depends(get_db)):
    try:
        token = credentials.credentials

        data = jwt.decode(
            token, 
            os.getenv("SECRET_KEY"), 
            os.getenv("ALGORITHM")
        )

        user_id = data.get("id")

        user = db.execute(
            select(User).where(User.id == user_id)
        ).scalars().first()


        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorized")

        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are unauthorized")