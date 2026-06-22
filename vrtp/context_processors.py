from .translations import get_translations
from users.models import User
from jobs.models import Application


def language_context(request):
    """
    Inject translation strings and current language into every template.
    Reads the user's preferred language from their profile (session-based).
    """
    lang = 'en'  # default

    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            if user.language in ('en', 'hi', 'te'):
                lang = user.language
        except User.DoesNotExist:
            pass

    # Also allow override via query param: ?lang=hi
    qs_lang = request.GET.get('lang')
    if qs_lang in ('en', 'hi', 'te'):
        lang = qs_lang

    translations = get_translations(lang)

    nav_hired_count = 0
    if user_id and request.session.get('role') == 'worker':
        try:
            nav_hired_count = Application.objects.filter(
                worker_id=user_id, status='hired'
            ).count()
        except Exception:
            pass

    return {
        'T': translations,
        'current_lang': lang,
        'nav_hired_count': nav_hired_count,
    }
