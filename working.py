from re import U
from fastapi import FastAPI,Path
import uvicorn  ## ASGI
app=FastAPI()

# @app.get("/")
# def home():
#     return {"Data":"Testing"}
     
# @app.get("/about")
# def about():
#     return {"About":"OKOK"}


# ## for setting up path parameter
# inventory={
#     1:{
#         "name":"Apple",
#         "price":3.66
#     }
# }
# @app.get("/get-item/{item_id}")
# def get_item(item_id:int =Path(None,description="THis is an item")):
#     return inventory[item_id]




## INdex route, opens automatically on http://127.0.0.1:8000

@app.get('/')
def index():
    return {'message':'Hello, AAAA'}

@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome to Krish Youtube Channel ':f'{name}'}


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port='127.0.0.0:8000')