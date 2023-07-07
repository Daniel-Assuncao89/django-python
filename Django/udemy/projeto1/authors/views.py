from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import RegisterForm, LoginForm, AuthorRecipeForm
from recipes.models import Recipe

# Create your views here.


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create')
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Your user is created, please log in.')

        del (request.session['register_form_data'])

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logged in')
            login(request, authenticated_user)
            return redirect('authors:dashboard')

        messages.error(request, 'Invalid credentials')
        return redirect(login_url)

    messages.error(request, 'Error to validate form data')
    return redirect(login_url)


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        print('Invalid user name', request.POST, request.user)
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )

    page_obj = make_pagination(request, recipes, 3)

    return render(request, 'authors/pages/dashboard.html', {
        'recipes': page_obj
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_edit(request, recipe_id):
    recipe = Recipe.objects.filter(
        pk=recipe_id,
        is_published=False,
        author=request.user,
    ).first()

    if not recipe:
        raise Http404('Invalid recipe')

    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )

    if form.is_valid():
        recipe = form.save(commit=False)

        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_published = False

        recipe.save()

        messages.success(request, 'Recipe updated')
        return redirect(reverse('authors:dashboard_recipe_edit',
                                args=(recipe_id,)
                                )
                        )

    return render(request, 'authors/pages/dashboard_recipe.html',  {
        'form': form,
    })


def make_pagination(request, queryset, per_page):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page', 1)
    print(request.GET)
    page_obj = paginator.get_page(page_number)
    return page_obj
