from typing import List
from ninja import NinjaAPI, Schema
from .models import Tag

api = NinjaAPI()

class TagSchema(Schema):
    subject: str
    Rstyle: str


@api.get("tags", response=List[TagSchema])
def tags(request):
    # tags = Tag.objects.all()
    return [TagSchema(subject=tag.subject, Rstyle=tag.Rstyle) for tag in Tag.objects.all()]
