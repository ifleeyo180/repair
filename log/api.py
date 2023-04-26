from typing import List, Optional
from ninja import NinjaAPI, Schema
from .models import Tag, LogItem
from django.db.models import Q


api = NinjaAPI()
class TagSchema(Schema):
    subject: str
    Rstyle: str


class LogItemSchema(Schema):
    id:int
    ctime: str
    subject: str
    description: str
    reporter: str
    phone: str
    handler: str
    status: int
    status_class: str
    status_display: str
    utime: str
    comment: str
    picture: Optional[str]
    tags: List[TagSchema]


def logitem_to_schema(logitem: LogItem) -> LogItemSchema:
    return LogItemSchema(
        id=logitem.id,
        ctime=logitem.ctime.strftime('%Y-%m-%d %H:%M:%S'),
        subject=logitem.subject,
        description=logitem.description,
        reporter=logitem.reporter,
        phone=logitem.phone,
        handler=logitem.handler,
        status=logitem.status,
        status_class=logitem.get_status_class(),
        status_display=logitem.get_status_display(),
        utime=logitem.utime.strftime('%Y-%m-%d %H:%M:%S'),
        comment=logitem.comment,
        picture=logitem.picture.url if logitem.picture else None,
        tags=[TagSchema(subject=tag.subject, Rstyle=tag.Rstyle) for tag in logitem.tags.all()],
    )




@api.get("tags", response=List[TagSchema])
def tags(request):
    # tags = Tag.objects.all()
    return [TagSchema(subject=tag.subject, Rstyle=tag.Rstyle) for tag in Tag.objects.all()]


@api.get("logitems", response=List[LogItemSchema])
def logitems(request):
    logitems = LogItem.objects.all()
    return [logitem_to_schema(logitem) for logitem in logitems]


