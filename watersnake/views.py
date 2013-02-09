# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.template import RequestContext, loader
from django.template.defaultfilters import slugify
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# from boogie.models import *

# from boogie import tasks


def index(request):
    t = loader.get_template('boogie/index.html')
    
    c = RequestContext(request, {
    })

    return HttpResponse(t.render(c))

# class PreLaunchEmailForm(ModelForm):
#     class Meta:
#         model = PreLaunchEmail
#         fields = ('email', )

# def pre_launch(request):
#     t = loader.get_template('boogie/pre_launch.html')
    
#     if request.method == 'POST':
#         form = PreLaunchEmailForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('pre_launch_thanks'))
#     else:
#         form = PreLaunchEmailForm()

#     c = RequestContext(request, {
#         'form': form
#     })
#     return HttpResponse(t.render(c))

# @login_required
# def summary(request):
#     t = loader.get_template('boogie/summary.html')

#     c = RequestContext(request, {
#         'summary': Summary.objects.all().order_by('-datecreated')
#     })

#     return HttpResponse(t.render(c))

# @login_required
# def topic_list(request):
#     t = loader.get_template('boogie/topic_list.html')
    
#     c = RequestContext(request, {
#             'writer_topics': Topic.objects.filter(pool='WRITER'),
#             'player_topics': Topic.objects.filter(pool='PLAYER')
#     })
#     return HttpResponse(t.render(c))
    
# @login_required
# def topic_detail(request, topicid, slug):
#     t = loader.get_template('boogie/topic_detail.html')
    
#     order = request.GET.get('order', '-rating')

#     topic = Topic.objects.get(id=topicid)

#     c = RequestContext(request, {
#             'topic': topic,
#             'pieces': topic.approved_pieces().order_by(order),
#             'order': order
#     })
#     return HttpResponse(t.render(c))
    
# @login_required
# def piece_list(request):
#     t = loader.get_template('boogie/piece_list.html')
    
#     c = RequestContext(request, {
#             'pieces': Piece.objects.filter(status='APPROVED').order_by('-score_cache')
#     })
#     return HttpResponse(t.render(c))

# @login_required
# def pieces_per_week(request, week):
#     week = int(week)
#     datestart = Game.objects.get_latest_game().start_date

#     weekStart = datestart + datetime.timedelta(week * 7)
#     weekEnd = datestart + datetime.timedelta((week + 1) * 7)

#     order_crit = request.GET.get('order', '-score_cache')

#     t = loader.get_template('boogie/pieces_per_week.html')

#     c = RequestContext(request, {
#         'pieces': Piece.objects.filter(datepublished__gte=weekStart).filter(datepublished__lte=weekEnd).order_by(order_crit),
#         'week': week,
#         'order': order_crit
#     })

#     return HttpResponse(t.render(c))

# @login_required
# def piece_detail(request, id):
#     t = loader.get_template('boogie/piece_detail.html')

#     c = RequestContext(request, {
#             'piece': Piece.objects.get(id=id)
#     })
#     return HttpResponse(t.render(c))

# class PieceSubmitForm(ModelForm):
#     class Meta:
#         model = Piece
#         fields = ('genre', 'title', 'text', 'new_topic')

# class WriterPieceSubmitForm(ModelForm):
#     class Meta:
#         model = Piece
#         fields = ('topic', 'title', 'genre', 'text')

# @login_required
# def piece_submit(request):
#     t = loader.get_template('boogie/piece_submit.html')
    
#     player = Player.objects.get(user=request.user)

#     if player.role == 'WRITER':
#         if request.method == 'POST':
#             form = WriterPieceSubmitForm(request.POST)
#             if form.is_valid():
#                 # We don't need a special status, we can figure out if a piece was written by a writer by querying JOIN on the author
#                 form.instance.status = 'APPROVED'
                
#                 # These fields already be filled in with a Piece stub for a player
#                 form.instance.writer = player
#                 form.instance.deadline = datetime.datetime.now() # We don't actually use this
#                 form.save()

#                 form.instance.topic.pool = 'PLAYER'
#                 form.instance.topic.piece_threshold += 1
#                 form.instance.topic.save()

#                 # TODO figure out where the piece of the writer would be going to 
#                 return HttpResponseRedirect(reverse('boogie.views.piece_detail', args=[form.instance.id]))
#         else:
#             form = WriterPieceSubmitForm()

#         form.fields['topic'].queryset = Topic.objects.all().filter(pool='WRITER')
#     else:
#         assignments = Piece.objects.filter(Q(status='ASSIGNED') | Q(status='NEEDSWORK')).filter(writer__user=request.user)
#         if assignments:
#             # TODO this doesn't go too well if we have more than one assignment
#             # TODO make sure that never happens
#             piece = assignments[0]

#             if request.method == 'POST':
#                 form = PieceSubmitForm(request.POST, instance=piece)
#                 if form.is_valid():
#                     # The piece has been submitted into the bowels of the system
#                     form.instance.status = 'SUBMITTED'
#                     form.save()

#                     return HttpResponseRedirect(reverse('boogie.views.piece_detail', args=[piece.id]))
#             else:
#                 form = PieceSubmitForm(instance=piece)
#         else:
#             form = None
    
#     c = RequestContext(request, {
#             'form': form
#     })
#     return HttpResponse(t.render(c))

# # TODO proper access controls
# @require_POST
# @login_required
# def piece_validate(request, piece_id):
#     piece = Piece.objects.get(id=piece_id)
    
#     valid = request.POST.get('ok', '')
    
#     if valid == 'yes':
#         piece.status = 'APPROVED'
#         piece.datepublished = datetime.datetime.now()
        
#         piece.topic.piece_count += 1
#         piece.topic.save()

#         # Check whether this topic should switch pools back to writers
#         tasks.check_topic_pool.delay(piece.topic)

#         # Don't give this player a new assignment
#         # tasks.get_new_assignment.delay(piece.writer)

#         # Also we need to create a new topic based on this approved piece
#         if piece.new_topic:
#             t = Topic.objects.create(pool="PLAYER", title=piece.new_topic, slug=slugify(piece.new_topic))
#             t.save()
#     elif valid == 'retry':
#         # The piece needs more work
#         piece.rejection_reason = request.POST.get('reason', '')
#         piece.status = 'NEEDSWORK'
#     elif valid == 'no':
#         piece.status = 'REJECTED'

#         # Don't give this player a new assignment
#         # tasks.get_new_assignment.delay(piece.writer)

#     piece.save()
        
#     return HttpResponseRedirect(reverse('piece_queue'))

# @user_passes_test(lambda u: u.is_superuser)
# def pieces_assign(request):
#     players_without = Player.objects.exclude(piece__status='ASSIGNED').exclude(piece__status='NEEDSWORK')

#     counter = 0
#     for player in players_without:
#         player.get_new_assignment()
#         counter += 1

#     return HttpResponse('Spelers met een nieuwe opdracht: %d' % counter)

# @login_required
# @require_POST
# def piece_vote_up(request, piece_id):
#     piece = Piece.objects.get(id=piece_id)

#     player = Player.objects.get(user=request.user)

#     piece.vote_up(player)
#     piece.update_score_cache()

#     return HttpResponseRedirect(reverse('boogie.views.piece_detail', args=[piece.id]))
    

# @login_required    
# def piece_queue(request):
#     t = loader.get_template('boogie/piece_queue.html')

#     c = RequestContext(request, {
#         'pieces': Piece.objects.filter(status='SUBMITTED').order_by('-datecreated')
#     })
#     return HttpResponse(t.render(c))

# @login_required
# def player_profile(request, name):
#     player = Player.objects.get(user__username=name)

#     c = RequestContext(request, {
#         'player': player
#     })
    
#     if player.role == 'PLAYER':
#         t = loader.get_template('boogie/player_profile.html')

#         # Show the approved pieces in any case
#         c['approved_pieces'] = player.pieces().filter(status="APPROVED")

#         if request.user.username == name:
#             c['assigned_pieces'] = player.pieces().filter(status="ASSIGNED")
#             c['submitted_pieces'] = player.pieces().filter(status="SUBMITTED")

#             c['needswork_pieces'] = player.pieces().filter(status="NEEDSWORK")
#             c['rejected_pieces'] = player.pieces().filter(status="REJECTED")
        
#         return HttpResponse(t.render(c))


# class UserProfileForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')

# class PlayerProfileForm(ModelForm):
#     class Meta:
#         model = Player
#         fields = ('pseudonym', 'biography', 'avatar')

# @login_required
# def player_profile_edit(request, name):
#     t = loader.get_template('boogie/player_profile_edit.html')

#     # TODO check if you can edit your profile
#     player = Player.objects.get(user__username=name)

#     if request.method == 'POST':
#         userform = UserProfileForm(request.POST, instance=player.user)
#         profileform = PlayerProfileForm(request.POST, request.FILES, instance=player)

#         if userform.is_valid() and profileform.is_valid():
#             userform.save()
#             profileform.save()

#             return HttpResponseRedirect(reverse('boogie.views.player_profile', args=[name]))
#     else:
#         userform = UserProfileForm(instance=player.user)
#         playerform = PlayerProfileForm(instance=player)

#     c = RequestContext(request, {
#         'userform': userform,
#         'playerform': playerform
#     })

#     return HttpResponse(t.render(c))

# @login_required
# def writers(request):
#     writers = Player.objects.filter(role='WRITER')

#     t = loader.get_template('boogie/writers.html')
#     c = RequestContext(request, {
#         'writers': writers
#     })

#     return HttpResponse(t.render(c))

# @login_required
# def writer_profile(request, name):
#     player = Player.objects.get(user__username=name)

#     if player.role == 'WRITER':
#         t = loader.get_template('boogie/writer_profile.html')

#         c = RequestContext(request, {
#             'writer': player
#         })

#         return HttpResponse(t.render(c))

