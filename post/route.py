from fastapi import APIRouter, Depends, HTTPException, status
from beanie import PydanticObjectId

from auth.utilties import authenticate
from database import Database
from .model import Post

router = APIRouter()

post_database = Database(Post)


@router.get("/all", response_model=list[Post])
async def get_all_post(user: str = Depends(authenticate)) -> list[Post]:
    posts = await post_database.get_all()
    return posts


@router.get("/{id}", response_model=Post)
async def retrieve_post(id: PydanticObjectId, user: str = Depends(authenticate)) -> Post:
    post = await post_database.get(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post Supplied ID Doesn't Exist."
        )
    return post


@router.post("/new")
async def create_post(body: Post, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await post_database.save(body)
    return {
        "message": "Post created Successfully."
    }


@router.put("/{id}", response_model=Post)
async def update_event(id: PydanticObjectId, body: Post, user: str = Depends(authenticate)) -> Post:
    post = await post_database.get(id)
    if post.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed."
        )
    updated_post = await post_database.update(id, body)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post with supplied ID does not exist"
        )
    return updated_post


@router.delete("/{id}")
async def delete_post(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    post = await post_database.get(id)
    if post.creator != user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post with supplied ID does not exist"
        )
    await post_database.delete(id)

    return {
        "message": "Post deleted successfully."
    }
