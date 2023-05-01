from typing import List, Optional
from ninja import NinjaAPI, Schema
from .models import Tag, LogItem
from django.db.models import Q
from ninja.security import django_auth

api = NinjaAPI(csrf=True)


class TagSchema(Schema):
    subject: str
    Rstyle: str


class LogItemSchema(Schema):
    id: int
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
        tags=[TagSchema(subject=tag.subject, Rstyle=tag.Rstyle)
              for tag in logitem.tags.all()],
    )


@api.get("tags", response=List[TagSchema])
def tags(request):
    # tags = Tag.objects.all()
    return [TagSchema(subject=tag.subject, Rstyle=tag.Rstyle) for tag in Tag.objects.all()]


@api.get("logitems", response=List[LogItemSchema], auth=django_auth)
def logitems(request):
    logitems = LogItem.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        # Check if the search query can be converted to an integer
        try:
            search_query_int = int(search_query)
            int_filter = Q(id=search_query_int)
        except ValueError:
            int_filter = Q()

        # Apply the filter to the queryset using the Q object
        logitems = logitems.filter(
            Q(subject__icontains=search_query) |
            Q(reporter__icontains=search_query) |
            Q(handler__icontains=search_query) |
            Q(tags__subject__icontains=search_query) |
            int_filter
        ).distinct()
    return [logitem_to_schema(logitem) for logitem in logitems]
