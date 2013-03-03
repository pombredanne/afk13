from django import template

register = template.Library()


@register.filter(takes_context=True)
def debug(context, value):
    import debug


@register.simple_tag(takes_context=True)
def regroup_per_rows(context, bricks):
    span = 0
    rows = list()
    rows.append(list())
    print rows
    for brick in bricks:
        if brick.span + brick.span > 12:
            rows.append(list())
            span = 0
        span += brick.span if brick.span else 0
        rows[-1].append(brick)
    context['rows'] = rows
    return ''
