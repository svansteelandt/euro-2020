import graphene
from graphene_django import DjangoObjectType

from euro2020.players.models import Team, Player


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "players")


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
        fields = ("id", "name", "notes", "team")


class Query(graphene.ObjectType):
    all_players = graphene.List(PlayerType)
    team_by_name = graphene.Field(TeamType, name=graphene.String(required=True))

    def resolve_all_players(root, info):
        # We can easily optimize query count in the resolve method
        return Player.objects.select_related("team").all()

    def resolve_team_by_name(root, info, name):
        try:
            return Team.objects.get(name=name)
        except Player.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
