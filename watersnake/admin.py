from django.contrib import admin
from watersnake.models import *

class VoterAdmin(admin.ModelAdmin):
    list_display = ('user', )
admin.site.register(Voter, VoterAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', )
admin.site.register(Topic, TopicAdmin)

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('proposer', 'text', 'topic')
admin.site.register(Proposal, ProposalAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter', 'proposal', 'vote')
admin.site.register(Vote, VoteAdmin)

class DelegationAdmin(admin.ModelAdmin):
    list_display = ('delegator', 'topic', 'delegate')
admin.site.register(Delegation, DelegationAdmin)
