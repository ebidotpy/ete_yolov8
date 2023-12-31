import sys

from requests import Session
from pydantic import BaseModel
from typing import Optional
from App import models
from App.database import SessionLocal, engine
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "KlgH6AzYDeZeGwD288to79I3vTHT8wp7"
ALGORITHM = "HS256"

sys.path.append("..")

class CreateUser(BaseModel):
    username: str
    password: str
    email: Optional[str]
    first_name: str
    last_name: str

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")



router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authenticated"}}
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, 
                        expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: str = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exception()
        return {"username": username, "id": user_id}
    except JWTError:
        raise get_user_exception()


@router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.username = create_user.username
    create_user_model.email = create_user.email
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.hashed_password = get_password_hash(create_user.password)
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), 
                                 db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, 
                                user.id, 
                                expires_delta=token_expires)
    return {"token": token}
    


def token_exception():
    token_exception_respone = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Incorect username or password", 
        headers={"WWW-Authenticate": "Bearer"}
    )
    return token_exception_respone

def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not validate credentioals", 
        headers={"WWW-Authenticate": "Bearer"}
    )
    return credentials_exception