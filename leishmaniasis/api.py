import uuid

from django.http import JsonResponse
from pydantic import ValidationError
from django.conf import settings

from typing import Optional, List
from datetime import datetime
from django.utils import timezone

from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from leishmaniasis.models import Leishmaniasis
from leishmaniasis.schema import LeishmaniasisSchema, NotFoundSchema, ErrorUUIDSchema


api = NinjaAPI()


def is_uuid4(value):
    try:
        # Tenta criar um UUID a partir do valor
        val = uuid.UUID(value, version=4)
        # Verifica se a versão do UUID é 4
        return val.version == 4
    except ValueError:
        # Se houver um erro na criação do UUID, não é um UUID válido
        return False

@api.get('/leishmaniasis', response=List[LeishmaniasisSchema])
def leishmaniasis(request, title: Optional[str] = None):
    if title:
        return Img.objects.filter(title__incontains=title)
    return Img.objects.all()


@api.get('/leishmaniasis/{img_id}', response={200: LeishmaniasisSchema, 404: NotFoundSchema, 500: ErrorUUIDSchema})
def leishmaniasi(request, img_id: str):
    try:
        if is_uuid4(img_id):          
            img = Img.objects.get(pk=img_id)
            return img
        else:
            return 500, {"message": "UUID error"}
    except Img.DoesNotExist as e:
        return 404, {"message": "Image does not exist"}
    

@api.post("/leishmaniasis/", response=LeishmaniasisSchema)
def create_img(request, img: UploadedFile,  title: str):
    # Cria uma instância de Photo com o arquivo recebido
    img_instance = Img.objects.create(
        img=img,
        uploaded_at=timezone.now(),
        title=title
    )
    return LeishmaniasisSchema(
        id=img_instance.id,
        img=img_instance.img.url,
        uploaded_at=img_instance.uploaded_at,
        title=img_instance.title
    )