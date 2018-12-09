from django import template
import datetime

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)


@register.filter
def dict_status(bound_field):
    status_dict= {'n':'Не розпочата','i':'Незавершена','c':'Завершена'}
    return status_dict[bound_field]
    
@register.filter
def make_human(bound_field):
    import datetime, re, math
    bound_field = bound_field.replace(re.findall("^.+(\:\d{2}Z)$",bound_field)[0],"")
    re_pattern = re.findall( '^(\d{4}\-\d{2}\-\d{2}).*$',bound_field)[0]
    word = bound_field.replace(re_pattern+"T", "")
    date_article = [int(_) for _ in re_pattern.split('-')]
    date_current = (lambda _: [_.year, _.month, _.day])(datetime.datetime.now().date())
    if date_article == date_current:
        return "Сьогодні "+ word
    elif date_article[0] == date_current[0] and date_article[1] == date_current[1] and math.fabs((date_current[2] - date_article[2])) == 1:
        return "Вчора " + word
    elif date_article[0] == date_current[0] and date_article[1] == date_current[1] and math.fabs(date_current[2] - date_article[2]) == 2:
        return "Позавчора " + word
    else:
        return re_pattern+" "+word
        
