from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Dict

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

@router.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = form.username
    
    if user:
        return {'ok': 'todo ok'}
    
    return {'error': 'se presento un error'}