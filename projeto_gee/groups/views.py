from django.shortcuts import render
from groups.model.groups import Group


# Create your views here.

def index(request):
    groups = Group.objects.all()
    return render(request, 'groups/index.html',{
        'groups': groups
    })


def group_details(request, group_slug):
    try:
        selected_group = Group.objects.get(slug=group_slug)
        return render(request, 'groups/group-details.html', {
            'group_found' : True,
            'group_name': selected_group.title,
            'group_description': selected_group.description,
            'group_date': selected_group.date,
            'group_organizer_email': selected_group.organizer_email
        })
    except Exception as exc:
        return render(request, 'groups/group-details.html',{
            'group_found' : False
        })


#Admin - senha: BRUH