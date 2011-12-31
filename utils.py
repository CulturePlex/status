import jinja2

from settings import CONTEXT, TEMPLATES_PATH

jinja_loader = jinja2.FileSystemLoader(TEMPLATES_PATH)
jinja_environment = jinja2.Environment(loader=jinja_loader)


def render_to_response(cls, template_file, dic={}, headers={}):
    context_dic = CONTEXT.copy()
    context_dic.update(dic)
    cls.response.headers.update(headers)
    template = jinja_environment.get_template(template_file)
    cls.response.out.write(template.render(context_dic))
