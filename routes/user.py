from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.user import UserServices
from decouple import config

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

@router.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends()):    
    if not UserServices().get_user(form.username, form.password):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={
                'error': {
                    'message': 'invalid authorization data'
                }
            }
        )

    token = {
        'exp': datetime.utcnow() - timedelta(minutes=config('TIME_OUT_TOKEN')),
        'usr': form.username
    }

    return 