from watersnake.models import *

from django.utils import unittest



class TestVotesWithoutDelegation(unittest.TestCase):
    def setUp(self):
        self.yea_voters = [Voter.objects.create_voter_and_user('yea_%d' % i) for i in range(11)]
        self.nay_voters = [Voter.objects.create_voter_and_user('nay_%d' % i) for i in range(12)]

        self.topic = Topic.objects.create(title='Test topic')
        self.proposal = Proposal.objects.create(proposer=self.yea_voters[0], topic=self.topic, text='Test proposal text')

        for voter in self.yea_voters:
            Vote.objects.create(proposal=self.proposal, voter=voter, vote='yea')

        for voter in self.nay_voters:
            Vote.objects.create(proposal=self.proposal, voter=voter, vote='nay')

    def test_result(self):
        result = self.proposal.resolve_votes()

        self.assertEqual(result, -1)

    def tearDown(self):
        Voter.objects.all().delete()
        Topic.objects.all().delete()
        Proposal.objects.all().delete()
        Vote.objects.all().delete()

        User.objects.all().delete()



class TestVotesWithDelegation(unittest.TestCase):
    def setUp(self):
        self.yea_voters = [Voter.objects.create_voter_and_user('yea_%d' % i) for i in range(11)]
        self.nay_voters = [Voter.objects.create_voter_and_user('nay_%d' % i) for i in range(12)]

        self.topic = Topic.objects.create(title='Test topic')
        self.proposal = Proposal.objects.create(proposer=self.yea_voters[0], topic=self.topic, text='Test proposal text')

        # These two people delaget their votes to the yea side
        self.delegators = [Voter.objects.create_voter_and_user('delegator_%d' % i) for i in range(2)]

        for delegator in self.delegators:
            Delegation.objects.create(delegator=delegator, topic=self.topic, delegate=self.yea_voters[0])

        for voter in self.yea_voters:
            Vote.objects.create(proposal=self.proposal, voter=voter, vote='yea')

        for voter in self.nay_voters:
            Vote.objects.create(proposal=self.proposal, voter=voter, vote='nay')

    def test_result(self):
        result = self.proposal.resolve_votes()

        self.assertEquals(result, 1)

    def tearDown(self):
        Voter.objects.all().delete()
        Topic.objects.all().delete()
        Proposal.objects.all().delete()
        Vote.objects.all().delete()

        User.objects.all().delete()

        Delegation.objects.all().delete()
