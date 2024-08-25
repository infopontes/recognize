from ninja import ModelSchema, Schema

from pydantic import BaseModel


from leishmaniasis.models import Leishmaniasis

class LeishmaniasisSchema(ModelSchema):
    class Config:
        model = Leishmaniasis
        model_fields = ['id','img', 'uploaded_at', 'title']
   
        
class NotFoundSchema(Schema):
    message: str
    
class ErrorUUIDSchema(Schema):
    message: str