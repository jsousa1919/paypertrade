<div style="min-height: 100px; background-color: red;">
    %for user in c.users:
        <div style="padding: 10px;">
            ${ user.name or 'Nameless!' }
            ${ user.email or "And he doesn't even have an email!" }
            <div>
                ${ user.username }
            </div>
        </div>
    %endfor
</div>
