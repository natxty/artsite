import json
from datetime import datetime
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django import template
from .models import Resume
from sorl.thumbnail import get_thumbnail


def resume_main(request):
    resume = get_object_or_404(Resume)
    return render(request, "resume/index.html",{
        'resume': resume
    })


from io import StringIO
# import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()
#
#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), mimetype='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def resume_pdf(request):
    resume = get_object_or_404(Resume)

    return render_to_pdf(
            'resume/resume_pdf.html',
            {
                'pagesize':'letter',
                'resume': resume,
            }
        )