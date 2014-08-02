<div>
    %if h.user():
        You are signed in ${ h.user().name }
        <a href="${ h.url_for(controller='account', action='signout') }">Sign out</a>
    %else:
        <div>
            You are sooo sleeping on the couch tonight unless you 
            <a href="${ h.url_for(controller='account', action='signin') }">Sign in</a>
        </div>
        <div>
            <a href="${ h.url_for(controller='base', action='signup') }">Sign up</a>
        </div>
    %endif
</div>
<div style="min-height: 100px; background-color: red;">
    %if c.users:
        %for user in c.users:
            <div style="padding: 10px;">
                ${ user.name or 'Nameless!' }
                ${ user.email or "And he doesn't even have an email!" }
            </div>
        %endfor
    %else:
        No database users
        %for user in c.fakes:
            <div style="padding: 10px;">
                ${ user.name or 'Nameless!' }
                ${ user.email or "And he doesn't even have an email!" }
            </div>
        %endfor
    %endif
</div>
