from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Division, Agent, Face, AgentAgreements


@admin.register(Division)
class DivisionAdmin(ModelAdmin):

    list_display = ['name']


@admin.register(Agent)
class AgentAdmin(ModelAdmin):

    list_display = ['face', 'status']


@admin.register(Face)
class FaceAdmin(ModelAdmin):

    list_display = ['counterparty_type', 'first_name', 'second_name', 'last_name']


@admin.register(AgentAgreements)
class AgentAgreementsAdmin(ModelAdmin):

    list_display = ['agent', 'lob']