from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse
from unsplash_cover import generate_cover
#from ai_cover import generate_cover
app=FastAPI()

@app.get("/cover",responses={200:{"content":{"image/png":{}},"description":"Generated collage cover"}},response_class=FileResponse)
async def SPCG(mood:str, genre:str, purpose:str):
    path=generate_cover(mood,genre,purpose)
    if not path:
        raise HTTPException(
            status_code=404,
            detail="Could not generate cover"
        )
    return FileResponse(path,media_type="image/png",headers={"Content-Disposition":"inline"})
 
 
'''
@app.get("/ai_cover",responses={200:{"content":{"image/png":{}},"description":"Generated collage cover"}},response_class=FileResponse)
async def genai(mood:str, genre:str, purpose:str):
    path= await generate_cover(mood,genre,purpose)
    if not path:
        raise HTTPException(
            status_code=404,
            detail="Could not generate cover"
        )
    return FileResponse(path,media_type="image/png",headers={"Content-Disposition":"inline"})
        
    '''