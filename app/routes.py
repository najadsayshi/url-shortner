from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import URL
from app.schemas import URLCreate
from app.utils import encode_base62

router = APIRouter()

BASE_URL = "http://localhost:8000"

@router.get("/")
def root():
    return {"message": "Welcome to the URL Shortener API!"}

@router.post("/shorten")
def shorten_url(data: URLCreate, session: Session = Depends(get_session)):
    long_url = str(data.original_url)

    # 🔹 Check existing URL
    statement = select(URL).where(URL.original_url == long_url)
    existing = session.exec(statement).first()

    if existing:
        return {"short_url": f"{BASE_URL}/{existing.short_code}"}

    # 🔹 Custom alias logic
    if data.custom_alias:
        statement = select(URL).where(URL.short_code == data.custom_alias)
        alias_exists = session.exec(statement).first()

        if alias_exists:
            raise HTTPException(status_code=409, detail="Alias already taken")

        new_url = URL(
            original_url=long_url,
            short_code=data.custom_alias
        )
        session.add(new_url)
        session.commit()

        return {"short_url": f"{BASE_URL}/{data.custom_alias}"}

    # 🔹 Normal flow
    new_url = URL(original_url=long_url)
    session.add(new_url)
    session.commit()
    session.refresh(new_url)

    short_code = encode_base62(new_url.id)

    new_url.short_code = short_code
    session.add(new_url)
    session.commit()

    return {"short_url": f"{BASE_URL}/{short_code}"}




#redirect endpoint
from fastapi.responses import RedirectResponse
from datetime import datetime

@router.get("/{short_code}")
def redirect_url(short_code: str, session: Session = Depends(get_session)):
    statement = select(URL).where(URL.short_code == short_code)
    url = session.exec(statement).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    if url.expiry_at and url.expiry_at < datetime.utcnow():
        raise HTTPException(status_code=410, detail="URL expired")

    url.click_count += 1
    session.add(url)
    session.commit()

    return RedirectResponse(url.original_url)

#analytics endpoint

@router.get("/analytics/{short_code}")
def get_analytics(short_code: str, session: Session = Depends(get_session)):
    statement = select(URL).where(URL.short_code == short_code)
    url = session.exec(statement).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "original_url": url.original_url,
        "click_count": url.click_count,
        "created_at": url.created_at,
        "expiry_at": url.expiry_at
    }