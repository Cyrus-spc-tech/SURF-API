from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate, PostResponse
app = FastAPI()


text_post={1:{"title":"New Post","content":"cool test post"},
2:{"title":"Python tips ","content":"use list comprehension for cleaner loop"},
3:{"title":"Daily Motivation", "content":"low freq beats and song "},
4:{"title":"Python secrets ","content":"use map function for cleaner loop"},
5:{"title":"Daily Meditation", "content":"low freq beats and song "},
6:{"title":"Code Hacks ","content":"use list comprehension for cleaner loop"},
7:{"title":"Daily Goals", "content":"low freq beats and song "},
8:{"title":"Python tips ","content":"use filter function for cleaner loop"},
9:{"title":"Daily Gratitude", "content":"low freq beats and song "},
10:{"title":"Code Structure ","content":"use for loop for cleaner loop"},
}

@app.get("/posts")
def get_all_posts(limit : int):
    if limit:
        return list(text_post.values())[:limit]
    return text_post


@app.get("/posts/{id}")
def get_post(id:int) -> PostResponse:

    if id not in text_post:
        raise HTTPException(status_code=404,detail="post not found")

    return id , text_post.get(id)


@app.post("/posts")
def create_post( post: PostCreate ) -> PostResponse:
    new_post={"title": post.title, "content":  post.content}
    text_post[max(text_post.keys())+1]=new_post

    return {}


# @app.delete()