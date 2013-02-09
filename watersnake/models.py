# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class VoterManager(models.Manager):
    def create_voter_and_user(self, name):
        user = User.objects.create_user(name, 'none@devnull.com', name)

        return Voter.objects.create(user=user)

class Voter(models.Model):
    datecreated = models.DateTimeField(auto_now_add=True)
    datechanged = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(User)

    objects = VoterManager()

    def __unicode__(self):
        return self.user.username

class Topic(models.Model):
    datecreated = models.DateTimeField(auto_now_add=True)
    datechanged = models.DateTimeField(auto_now=True)    

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title


class Proposal(models.Model):
    datecreated = models.DateTimeField(auto_now_add=True)
    datechanged = models.DateTimeField(auto_now=True)

    # TODO add fields for open/closed
    # resolved or not
    # resolution field

    proposer = models.ForeignKey(Voter)

    text = models.TextField()

    topic = models.ForeignKey(Topic)

    def resolve_votes(self):
        yea_votes = Vote.objects.filter(vote='yea', proposal=self).count()
        nay_votes = Vote.objects.filter(vote='nay', proposal=self).count()
        abstains = Vote.objects.filter(vote='nay', proposal=self).count()

        # Process the delegations

        # Find the people who haven't voted on this proposal 
        # Who do have a delegate for this topic
        # Turned out not to be necessary
        # Voter.objects.exclude(vote__proposal=p).filter(delegations__topic=p.topic)

        # Find the Delegations of people who haven't voted on this proposal
        # The delegate must have voted on the proposal otherwise we don't count it
        # Count the yea and nay votes of the delegates on this proposal

        yea_delegations = Delegation.objects.exclude(delegator__vote__proposal=self).filter(delegate__vote__proposal=self, delegate__vote__vote='yea').count()
        nay_delegations = Delegation.objects.exclude(delegator__vote__proposal=self).filter(delegate__vote__proposal=self, delegate__vote__vote='nay').count()

        yea_votes += yea_delegations
        nay_votes += nay_delegations

        if yea_votes > nay_votes:
            return 1
        elif nay_votes > yea_votes:
            return -1
        else:
            return 0

    def __unicode__(self):
        return self.text

class Vote(models.Model):
    datecreated = models.DateTimeField(auto_now_add=True)
    datechanged = models.DateTimeField(auto_now=True)

    voter = models.ForeignKey(Voter)
    proposal = models.ForeignKey(Proposal)

    vote = models.CharField(max_length=255, choices=(('yea', 'yea'), ('nay', 'nay'), ('abstain', 'abstain')))

class Delegation(models.Model):
    datecreated = models.DateTimeField(auto_now_add=True)
    datechanged = models.DateTimeField(auto_now=True)

    # The person delegating their vote on a certain topic
    delegator = models.ForeignKey(Voter, related_name='delegations')
    topic = models.ForeignKey(Topic)

    # The person whose vote will be counted if the delegator does not vote on a proposal
    delegate = models.ForeignKey(Voter, related_name='delegateds')

    def __unicode__(self):
        return "%s delegates to %s on %s" % (self.delegator, self.delegate, self.topic)
