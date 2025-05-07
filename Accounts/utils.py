from user_agents import parse

def is_mobile(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    parsed = parse(user_agent)
    return parsed.is_mobile
