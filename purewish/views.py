from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime, date, time
from django.views.generic import ListView
from postman.models import Message
from .models import Posts, Donor, Messages, Volunteer, Stuff, Gallery, MailManager, ProjectManager
from .forms import AddPostForm, DonorForm, MessageForm, StuffForm, VolunteerForm, GalleryForm, MailForm, ProjectForm, UserUpdateForm, ProfileUpdateForm


class UserPostListView(ListView):
    model = Posts
    template_name = 'purewish/user_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


@login_required(login_url='login')
def index(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        donors = Donor.objects.filter(
            Q(username__username__icontains=q) |
            Q(organisation__icontains=q) |
            Q(country__icontains=q)
        )
    else:
        q = ''
        donors = Donor.objects.filter(
            Q(username__icontains=q) |
            Q(organisation__icontains=q) |
            Q(country__icontains=q)
        )

    t_user = User.objects.all()
    total_user = int(t_user.count()) / 100
    donor = Donor.objects.all()
    timenow = datetime.now().strftime("%d %b %H:%M")
    room_name = "purewish"
    images = Gallery.objects.all()
    stuffs = Stuff.objects.all()
    total_stuff = stuffs.count()

    count = donor.count()
    message = Messages.objects.filter(room=room_name)[0:25]

    message_count = message.count()
    context = {'donors': donors, 'count': count, 'message': message, 'donor': donor, 'message_count': message_count, 'images': images,
               'room_name': room_name, 'timenow': timenow, 'total_user': total_user, 'total_stuff': total_stuff}
    return render(request, 'purewish/index.html', context)


def direct_chat(request):
    if request.method == 'POST':
        Messages.objects.create(
            user=request.user,
            message=request.POST.get('message'),
        )


@login_required(login_url='login')
def all_post(request):
    page = 'post'
    post = Posts.objects.all()
    context = {'post': post, 'page': page}
    return render(request, 'purewish/all_post.html', context)


@login_required(login_url='login')
def add_post(request):
    form = AddPostForm(request.POST)
    form.instance.author = request.user

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('all-post')
        else:
            messages.error(request, 'Please check your post.')

    context = {'form': form}
    return render(request, 'purewish/add_post.html', context)


@login_required(login_url='login')
def update_post(request, id):
    post = Posts.objects.get(id=id)
    form = AddPostForm(instance=post)

    if request.method == 'POST':
        form = AddPostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()

            return redirect('all-post')

        else:
            messages.error(request, 'Please check yoyr post.')

    context = {'form': form}
    return render(request, 'purewish/update_post.html', context)


def delete_post(request, id):
    post = Posts.objects.get(id=id)
    post.delete()

    return redirect('all-post')


@login_required(login_url='login')
def view_donor(request):
    page = 'donor_page'
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        donor = Donor.objects.filter(
            Q(username__icontains=q) |
            Q(organisation__icontains=q) |
            Q(country__icontains=q)
        )
    else:
        q = ''
        donor = Donor.objects.filter(
            Q(username_username__icontains=q) |
            Q(organisation__icontains=q) |
            Q(country__icontains=q)
        )
    donor_count = donor.count()
    form = DonorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            donor = form.save(commit=False)
            donor.save()

            return redirect('view-donor')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'donor': donor, 'donor_count': donor_count,
               'form': form, 'page': page}
    return render(request, 'purewish/view_donors.html', context)


@login_required(login_url='login')
def add_donor(request):
    form = DonorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            donor = form.save(commit=False)
            donor.save()

            return redirect('view-donor')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'form': form}
    return render(request, 'purewish/add_donors.html', context)


def update_donor(request, id):
    donor = Donor.objects.get(id=id)
    form = DonorForm(instance=donor)

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)

        if form.is_valid():
            form.save()

            return redirect('view-donor')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'form': form}
    return render(request, 'purewish/update_donor.html', context)


def delete_donor(request, id):
    post = Donor.objects.get(id=id)
    post.delete()

    return redirect('view-donor')


@login_required(login_url='login')
def donor_contact(request):
    page = 'donor_contact'
    contacts = Donor.objects.all()
    context = {'contacts': contacts, 'page': page}
    return render(request, 'purewish/donor_contacts.html', context)


@login_required(login_url='login')
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error ocurred during registration.')

    context = {'form': form}
    return render(request, 'purewish/login_register.html', context)


def userLogin(request):
    pager = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Username or Password does not exist.')

    context = {'pager': pager}
    return render(request, 'purewish/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def all_messages(request):
    page = 'message_page'
    message = Messages.objects.all()
    msg_count = message.count()
    context = {'message': message, 'msg_count': msg_count}
    return render(request, 'purewish/msg_view.html', context)


@login_required(login_url='login')
def message_staff(request):
    post = Posts.objects.all()
    context = {'post': post}
    return render(request, 'purewish/msg_stuff.html', context)


@login_required(login_url='login')
def message_donor(request):
    post = Posts.objects.all()
    context = {'post': post}
    return render(request, 'purewish/msg_donor.html', context)


@login_required(login_url='login')
def user_messages(request, id):
    message = Messages.objects.get(id=id)
    message.donor.username.upper()
    context = {'message': message}
    return render(request, 'purewish/msg_donor.html', context)


@login_required(login_url='login')
def available_staff(request):
    page = 'stuff_page'
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        stuff = Stuff.objects.filter(
            Q(stuff__icontains=q) |
            Q(first_name__icontains=q)
        )
    else:
        q = ''
        stuff = Stuff.objects.filter(
            Q(stuff__icontains=q) |
            Q(first_name__icontains=q)
        )
    form = StuffForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            stuff = form.save(commit=False)
            stuff.save()

            return redirect('all-staffs')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'stuff': stuff, 'form': form, 'page': page}
    return render(request, 'purewish/all_stuff.html', context)


@login_required(login_url='login')
def add_staff(request):
    form = StuffForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            stuff = form.save(commit=False)
            stuff.save()

            return redirect('all-staffs')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')
    context = {'form': form}
    return render(request, 'purewish/add_stuff.html', context)


@login_required(login_url='login')
def update_stuff(request, id):
    stuff = Stuff.objects.get(id=id)
    form = StuffForm(instance=stuff)

    if request.method == 'POST':
        form = StuffForm(request.POST, instance=stuff)

        if form.is_valid():
            form.save()

            return redirect('all-staffs')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'form': form}
    return render(request, 'purewish/update_stuff.html', context)


def delete_stuff(request, id):
    stuff = Stuff.objects.get(id=id)
    stuff.delete()

    return redirect('all-staffs')


@login_required(login_url='login')
def staffs_contact(request):
    page = 'stuff_contacts'
    contacts = Stuff.objects.all()
    context = {'contacts': contacts, 'page': page}
    return render(request, 'purewish/stuff_contacts.html', context)


@login_required(login_url='login')
def all_volunteers(request):
    page = 'volunteer_page'
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        volunteer = Volunteer.objects.filter(
            Q(volunteer__icontains=q) |
            Q(first_name__icontains=q)
        )
    else:
        q = ''
        volunteer = Volunteer.objects.filter(
            Q(volunteer__icontains=q) |
            Q(first_name__icontains=q)
        )
    volunteer_count = volunteer.count()
    form = VolunteerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.save()

            return redirect('all-volunteers')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')
    context = {'volunteer': volunteer,
               'volunteer_count': volunteer_count, 'form': form, 'page': page}
    return render(request, 'purewish/all_volunteers.html', context)


@login_required(login_url='login')
def add_volunteers(request):
    form = VolunteerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.save()

            return redirect('all-volunteers')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')
    context = {'form': form}
    return render(request, 'purewish/add_volunteers.html', context)


def update_volunteer(request, id):
    volunteer = Volunteer.objects.get(id=id)
    form = VolunteerForm(instance=volunteer)

    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)

        if form.is_valid():
            form.save()
            messages.success(request, 'Volunteer details updated.')

            return redirect('all-volunteers')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'form': form}
    return render(request, 'purewish/update_volunteer.html', context)


def delete_volunteer(request, id):
    volunteer = Volunteer.objects.get(id=id)
    volunteer.delete()

    return redirect('all-volunteers')


@login_required(login_url='login')
def volunteers_contact(request):
    page = 'volunteers_contact'
    contacts = Volunteer.objects.all()
    context = {'contacts': contacts, 'page': page}
    return render(request, 'purewish/volunteers_contacts.html', context)


@login_required(login_url='login')
def calender(request):
    images = Gallery.objects.all()
    context = {'images': images}
    return render(request, 'purewish/calendar.html', context)


@login_required(login_url='login')
def gallery(request):
    images = Gallery.objects.all()
    form = GalleryForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()

            return redirect('gallery')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')
    context = {'images': images, 'form': form}
    return render(request, 'purewish/gallery.html', context)


@login_required(login_url='login')
def mail_inbox(request):
    page = 'mail_page'
    mail = MailManager.objects.all()
    context = {'mail': mail, 'page': page}
    return render(request, 'purewish/inbox.html', context)


@login_required(login_url='login')
def compose_mail(request):
    form = MailForm()
    if request.method == 'POST':
        MailManager.objects.create(
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            receiver=request.POST.get('receiver')
        )
        try:
            send_mail(
                request.POST.get('subject'),
                request.POST.get('message'),
                settings.EMAIL_HOST_USER,
                [request.POST.get('receiver')],
                fail_silently=False
            )

        except Exception as e:
            messages.error(request, f'Sorry...{e} occured, Try Again Later.')
            print(f'sorry this error {e} ocured.')

        return redirect('compose-mail')
    context = {'form': form}
    return render(request, 'purewish/compose.html', context)


@login_required(login_url='login')
def read_mail(request):
    images = Gallery.objects.all()
    context = {'images': images}
    return render(request, 'purewish/read.html', context)


def view_projects(request):
    page = 'project_page'
    project = ProjectManager.objects.all()
    context = {'project': project, 'page': page}
    return render(request, 'purewish/view_project.html', context)


@login_required(login_url='login')
def add_project(request):
    form = ProjectForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            project = form.save(commit=False)
            project.save()

            return redirect('view-project')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')
    context = {'form': form}
    return render(request, 'purewish/add_project.html', context)


@login_required(login_url='login')
def project_detail(request, id):
    project = ProjectManager.objects.get(id=id)
    context = {'project': project}
    return render(request, 'purewish/project_detail.html', context)


def delete_project(request, id):
    project = ProjectManager.objects.get(id=id)
    project.delete()

    return redirect('view-project')


@login_required(login_url='login')
def update_project(request, id):
    project = ProjectManager.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()

            return redirect('view-project')

        else:
            messages.error(request, 'Please enter a vaild info for the form.')

    context = {'form': form}
    return render(request, 'purewish/update_project.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'purewish/profile.html', context)
