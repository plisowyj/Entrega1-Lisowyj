from django.http import HttpResponse
from django.template import loader
from .models import People, People_phones


def findex(request):
  myfamily = People.objects.all().values()
  familyphones = People_phones.objects.all().values()

  template = loader.get_template('index.html')
  context = {
      'myfamily': myfamily,
      'familyphones':familyphones
  }
  return HttpResponse(template.render(context, request))

