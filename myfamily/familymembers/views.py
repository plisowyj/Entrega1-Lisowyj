from operator import truediv
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from familymembers.forms import PeopleF, PeoplePhone, PeopleAddress
from .models import People, People_phones, People_address


def findex(request):
  myfamily = People.objects.all().values()
  familyphones = People_phones.objects.all().values()
  familyaddress = People_address.objects.all().values()
  show = "true"

  template = loader.get_template('index.html')
  context = {
      'myfamily': myfamily,
      'familyphones':familyphones,
      'familyaddress': familyaddress,
      'show':show
  }
  return HttpResponse(template.render(context, request))


def faddmember(request):
  show = "false"

  if request.method == 'POST':
      miFormulario = PeopleF(request.POST)

      print(miFormulario)

      if miFormulario.is_valid:
        informacion = miFormulario.cleaned_data

        people = People(lastname=informacion['lastname'],
                        firstname=informacion['firstname'],
                        identity=informacion['identity'],
                        datebirth=informacion['datebirth'])
        people.save()

        return HttpResponseRedirect(reverse('findex'))

  else:
    miFormulario = PeopleF()

    return render(request, "add_member.html", {'miFormulario': miFormulario,
                                            'show': show})


def faddPhones(request):
  show = "false"

  if request.method == 'POST':
      miFormulario = PeoplePhone(request.POST)

      print(miFormulario)

      if miFormulario.is_valid:
        informacion = miFormulario.cleaned_data

        phone = People_phones(
            id_people=informacion['id_people'], phonenumber=informacion['phonenumber'])
        phone.save()

        return HttpResponseRedirect(reverse('findex'))

  else:
    miFormulario = PeoplePhone()
      
    return render(request, "add_phone.html", {'miFormulario': miFormulario,
                                            'show': show})
        

def faddAddress(request):
  show = "false"

  if request.method == 'POST':
      miFormulario = PeopleAddress(request.POST)

      print(miFormulario)

      if miFormulario.is_valid:
        informacion = miFormulario.cleaned_data

        address = People_address(
            id_people=informacion['id_people'], address=informacion['address'], type=informacion['type'])
        address.save()

        return HttpResponseRedirect(reverse('findex'))

  else:
    miFormulario = PeopleAddress()

    return render(request, "add_address.html", {'miFormulario': miFormulario,
                                              'show': show})


def fFinder(request):
  show = "false"
  p = ''
  t = ''
  d = ''

  if request.method == 'POST':
    criterio=request.POST.get('pCriterio')

    opcion= request.POST.get(
        'pFind')
    
    if opcion=='1':
      mydata = People.objects.filter(firstname__startswith=criterio).values()
      p='*'
    elif opcion=='2':
      mydata = People_phones.objects.filter(
            phonenumber__startswith=criterio).values()
      t = '*'
    elif opcion=='3':
      mydata = People_address.objects.filter(
            address__startswith=criterio).values()
      d = '*'
    else:
      mydata = ""

    return render(request, "finder.html", {'miFormulario': mydata,
                                                'show': show,
                                                'label': 'true',
                                                'p': p,
                                                't': t, 
                                                'd': d })

  else:
    return render(request, "finder.html", {'show': show,
                                          'label':'',
                                           'p': p,
                                           't': t,
                                           'd': d})
