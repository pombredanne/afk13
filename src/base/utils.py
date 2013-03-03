from django.template import loader


def render_to_template(*args, **kwargs):
    return loader.render_to_string(*args, **kwargs)
