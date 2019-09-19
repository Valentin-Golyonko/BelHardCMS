from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .models import Client, Sex, Citizenship, Family_state, Children, City, Telephone, State, Skills, Experience


def client_main_page(request):
    response = csrf(request)

    response['client_img'] = 'client/img/user_1.png'

    return render(request, 'client/client_main_page.html', response)


def client_profile(request):
    response = csrf(request)

    response['client_img'] = 'client/img/user_1.png'

    return render(request, 'client/client_profile.html', response)


def client_edit_main(request):
    response = csrf(request)

    response['client_img'] = 'client/img/user_1.png'

    return render(request, 'client/client_edit_main.html', response)


def save_client_edit_main(request):
    if request.POST:
        print("save_client_edit_main - request POST")

        client = Client(
            name=request.POST['client_first_name'],
            lastname=request.POST['client_last_name'],
            patronymic=request.POST['client_middle_name'],
            sex=Sex(sex_word=request.POST['sex']),
            date_born=None,
            citizenship=Citizenship(country_word=request.POST['citizenship']),
            family_state=Family_state(state_word=request.POST['family_state']),
            children=Children(children_word=request.POST['children']),
            country=Citizenship(country_word=request.POST['country']),
            city=City(city_word=request.POST['city']),
            street=request.POST['street'],
            house=request.POST['house'],
            flat=request.POST['flat'],
            telegram_link=request.POST['telegram_link'],
            skills_id=request.POST['skills_id'],
            email=request.POST['email'],
            link_linkedin=request.POST['link_linkedin'],
            state=State(state_word=request.POST['state']),
        )
        # client.save()

        Telephone(telephone_number=request.POST['phone'])  # .save()

        print(
            request.POST['client_first_name'],
            request.POST['client_last_name'],
            request.POST['client_middle_name'],
            request.POST['sex'],
            request.POST['date_born'],
            request.POST['citizenship'],
            request.POST['family_state'],
            request.POST['children'],
            request.POST['country'],
            request.POST['city'],
            request.POST['street'],
            request.POST['house'],
            request.POST['flat'],
            request.POST['phone'],
            request.POST['telegram_link'],
            request.POST['skills_id'],
            request.POST['email'],
            request.POST['link_linkedin'],
            request.POST['state'],
        )

    return redirect('/client/profile')


def client_edit_skills(request):
    response = csrf(request)

    response['client_img'] = 'client/img/user_1.png'

    return render(request, 'client/client_edit_skills.html', response)


def save_client_edit_skills(request):
    if request.POST:
        print("save_client_edit_skills - request POST")

        skill = Skills(skills=request.POST['skill_1'])
        # skill.save()

        print("skill: %s" % request.POST['skill_1'])

    return redirect('/client/edit')

def client_edit_experience(request):
    response = csrf(request)

    response['client_img'] = 'client/img/user_1.png'

    return render(request, 'client/client_edit_experience.html', response)

def save_client_edit_experience(request):
    if request.POST:
        print("save_client_edit_experience - request POST")

        experiences = Experience(experience=request.POST)


        print("experience: %s" % request.POST['experience_1'])

    return redirect('/client/edit')