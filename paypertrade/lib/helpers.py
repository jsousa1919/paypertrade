from pylons import url, session, request

"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

def user():
    user = session.get('user')
    if user and not request.environ.get('REMOTE_USER'):
        request.environ['REMOTE_USER'] = user.id
    if not user:
        user = get_cookie_user()
        if user:
            save_user(user)
    return user

def save_user(user, remember=False):
    session['user'] = user
    session.save()
    request.environ['REMOTE_USER'] = user.id
    if remember:
        set_cookie_user(user)

def set_cookie_user(user):
    thyme = time.time()
    secret_str = '%s:%d:%d' % (get_cookie_secret(user.id, thyme), thyme, user.id)
    user.token = secret_str
    model.Session.add(user)
    model.Session.commit()
    # expires in 15 days
    response.set_cookie('user', secret_str, max_age=1296000)

def get_cookie_secret(user_id, thyme):
    return hashlib.md5(str(user_id) + COOKIE_SALT + str(thyme)).hexdigest()

def get_cookie_user():
    user = None
    try:
        cookie_str = request.cookies.get('user')
        if cookie_str:
            cookie_tuple = cookie_str.split(':')
            if len(cookie_tuple) == 3:
                user_id = safe_int(cookie_tuple[2])
                session = safe_int(cookie_tuple[1])
                obj = model.User.get(user_id)
                if obj.token:
                    obj_tuple = obj.token.split(':')
                    last_session = safe_int(obj_tuple[1])
                    if session == last_session:
                        if cookie_tuple[0] == obj_tuple[0]:
                            user = obj
                        else:
                            obj.token = None
                            model.Session.add(obj)
                            model.Session.commit()
    except:
        log.error('Error getting user cookie')
    return user

def redirect_to(**kw):
    redirect(url(**kw), code=302)
