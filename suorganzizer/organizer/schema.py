import graphene
from graphene_django.types import DjangoObjectType

from organizer.models import Tag as TagModel
from organizer.models import Startup as StartupModel
from organizer.models import NewsLink as NewsLinkModel

class Tag(DjangoObjectType):
    class Meta:
        model = TagModel
Tag.Connection = connection_for_type(Tag)

class Startup(DjangoObjectType):
    class Meta:
        model = StartupModel
Startup.Connection = connection_for_type(Startup)

class NewsLink(DjangoObjectType):
    class Meta:
        model = NewsLinkModel
Newslink.Connection = connection_for_type(Newslink)

class Query(graphene.AbstractType):
    
    all_tags = graphene.List(Tag)
    all_startups = graphene.List(Startup)
    all_newslinks = graphene.List(NewsLink)

    def connection_for_type(_type):
        
    def resolve_all_tags(self, args, context, info):
        return TagModel.objects.all()

    def resolve_all_startups(self, args, context, info):
        return StartupModel.objects.all()

    def resolve_all_newslinks(self, args, context, info):
        return NewsLinkModel.objects.all()
 

class Connection(graphene.Connection):
       total_count = graphene.Int()

       class Meta:
           name = _type._meta.name + 'Connection'
           node = _type

       def resolve_total_count(self, args, context, info):
           return self.length

   return Connection   
