import hashlib
import time

from pylons import url, session, request, response, config
from pylons.controllers.util import redirect

from paypertrade import model
from paypertrade.lib.helpers import superhelpers as sh

COOKIE_SALT = "WE'RE SAILORS ON THE MOON, WE CARRY A HARPOON!"


def user():
    user_id = session.get('user_id')
    if user_id and not request.environ.get('REMOTE_USER'):
        request.environ['REMOTE_USER'] = user_id
    if not user_id:
        user_id = get_cookie_user()
        if user_id:
            save_user(user_id)
    return model.User.get(user_id) if user_id else None

def save_user(user_id, remember=False):
    session['user_id'] = user_id
    session.save()
    request.environ['REMOTE_USER'] = user_id
    if remember:
        set_cookie_user(user_id)

def clear_user():
    session['user_id'] = None
    session.save()
    response.set_cookie('user_id', '')
    request.environ['REMOTE_USER'] = ''

def set_cookie_user(user_id):
    thyme = time.time()
    secret_str = '%s:%d:%d' % (get_cookie_secret(user_id, thyme), thyme, user_id)
    user = model.User.get(user_id)
    user.token = secret_str
    model.Session.add(user)
    model.Session.commit()
    # expires in 15 days
    response.set_cookie('user_id', secret_str, max_age=1296000)

def get_cookie_secret(user_id, thyme):
    return hashlib.md5(str(user_id) + COOKIE_SALT + str(thyme)).hexdigest()

def get_cookie_user():
    from paypertrade import model
    user = None
    try:
        cookie_str = request.cookies.get('user_id')
        if cookie_str:
            cookie_tuple = cookie_str.split(':')
            if len(cookie_tuple) == 3:
                user_id = sh.safe_int(cookie_tuple[2])
                session = sh.safe_int(cookie_tuple[1])
                obj = model.User.get(user_id)
                if obj.token:
                    obj_tuple = obj.token.split(':')
                    last_session = sh.safe_int(obj_tuple[1])
                    if session == last_session:
                        if cookie_tuple[0] == obj_tuple[0]:
                            user = obj
                        else:
                            obj.token = None
                            model.Session.add(obj)
                            model.Session.commit()
    except:
        log.error('Error getting user cookie')
    return user.id if user else None

def redirect_to(**kw):
    redirect(url_for(**kw), code=302)

def url_for(*arg, **kw):
    if not kw.get('action'):
        kw['action'] = 'index'

    if not kw.get('controller'):
        kw['controller'] = current_route('controller')

    if request.environ.get('HTTP_X_URL_SCHEME', '').lower() == 'https':
        prefix = 'https'
    elif kw.get('secure'):
        prefix = 'https'
    else:
        prefix = 'http'

    if 'secure' in kw:
        del(kw['secure'])

    hashtag = ''
    if kw.get('hashtag'):
        hashtag = '#%s' % kw.get('hashtag')
        del(kw['hashtag'])

    app_host = config.get('app_host')
    if kw.get('shorten'):
        if app_host.startswith('www.'):
            app_host = app_host[4:]
        del(kw['shorten'])

    path = url(*arg, **kw)

    if path.startswith('http'):
        return path

    return '%s://%s%s%s' % (prefix, app_host, path, hashtag)

