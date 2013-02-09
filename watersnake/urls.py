from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'watersnake.views.index', name='index'),

    # url(r'^colofon/$', 'django.views.generic.simple.direct_to_template', {'template': 'boogie/colofon.html'}, name='colofon'),
    # url(r'^faq/$', 'django.views.generic.simple.direct_to_template', {'template': 'boogie/faq.html'}, name='faq'),
    # url(r'^help/$', 'django.views.generic.simple.direct_to_template', {'template': 'boogie/help.html'}, name='help'),

    # url(r'^pre/launch/$', 'boogie.views.pre_launch', name='pre_launch'),
    # url(r'^pre/launch/thanks/$', 'django.views.generic.simple.direct_to_template', {'template': 'boogie/pre_launch_thanks.html'}, name='pre_launch_thanks'),
    
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    # url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    # url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    # url(r'^password/reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    # url(r'^editors/$', 'django.views.generic.simple.direct_to_template', {'template': 'boogie/editors.html'}, name='editors'),
    # url(r'^summary/$', 'boogie.views.summary', name='summary'),

    # url(r'^topics/$', 'boogie.views.topic_list', name='topic_list'),
    # url(r'^topics/(\d+)/(\S+?)/$', 'boogie.views.topic_detail', name="topic_detail"),

    # url(r'^pieces/$', 'boogie.views.piece_list', name='pieces_list'),
    # url(r'^pieces/week/(\d+)/$', 'boogie.views.pieces_per_week', name='pieces_per_week'),
    # url(r'^pieces/queue/', 'boogie.views.piece_queue', name='piece_queue'),
    
    # url(r'^pieces/(\d+)/$', 'boogie.views.piece_detail'),
    # url(r'^pieces/submit/$', 'boogie.views.piece_submit', name='piece_submit'),
    # url(r'^pieces/assign/$', 'boogie.views.pieces_assign', name='pieces_assign'),
    # url(r'^pieces/(\d+)/validate/', 'boogie.views.piece_validate', name='piece_validate'),
    # url(r'^pieces/(\d+)/vote/up/', 'boogie.views.piece_vote_up', name='piece_vote_up'),

    # # TODO for now these two URLs point to the same view
    # url(r'^users/(?P<name>\w+?)/$', 'django.views.generic.simple.redirect_to', {'url': '/players/%(name)s/'}),

    # url(r'^writers/$', 'boogie.views.writers', name='writers'),
    # url(r'^writers/(\w+?)/$', 'boogie.views.writer_profile', name='writer_profile'),

    # url(r'^players/(\w+?)/$', 'boogie.views.player_profile', name='player_profile'),
    # url(r'^players/(\w+?)/edit/$', 'boogie.views.player_profile_edit', name='player_profile_edit'),
)
