congratulations!
%if h.user():
    Oh hey look who signed in, that shithead ${ h.user().name }
%else:
    Why are you here? we don't like your kind around these parts
%endif
<a href="${ h.url_for(controller="base", action="index") }">Index</a>
