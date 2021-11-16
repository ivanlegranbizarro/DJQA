from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Answer
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionRegistrationForm, AnswerRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def question_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            questions = Question.objects.filter(
                title__icontains=q).order_by('-created_at')
            return render(request, 'questions/question_list.html', {'questions': questions})
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/question_list.html', {'questions': questions})


def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerRegistrationForm(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.author = request.user
            new_answer.save()
            return redirect('question_detail', slug=slug)
    else:
        form = AnswerRegistrationForm()
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers, 'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'questions/register_success.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'questions/register.html', {'form': form})


@login_required
def register_question(request):
    if request.method == 'POST':
        form = QuestionRegistrationForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()
            return redirect('question_list')
    else:
        form = QuestionRegistrationForm()
    return render(request, 'questions/question_register.html', {'form': form})


@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == 'POST':
        form = QuestionRegistrationForm(request.POST, instance=question)
        if form.is_valid():
            updated_question = form.save(commit=False)
            updated_question.author = request.user
            updated_question.save()
            return redirect('question_detail', slug=slug)
    else:
        form = QuestionRegistrationForm(instance=question)
    return render(request, 'questions/question_update.html', {'form': form})


@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


@login_required
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()
    return redirect('question_detail', slug=answer.question.slug)


@login_required
def update_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == 'POST':
        form = AnswerRegistrationForm(request.POST, instance=answer)
        if form.is_valid():
            updated_answer = form.save(commit=False)
            updated_answer.author = request.user
            updated_answer.save()
            return redirect('question_detail', slug=answer.question.slug)
    else:
        form = AnswerRegistrationForm(instance=answer)
    return render(request, 'questions/answer_update.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            updated_user.save()
            messages.success(
                request, 'Your profile has been updated succesfully')
            return redirect('question_list')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'questions/edit_profile.html', {'form': form})


@login_required
def list_questions_and_answers_by_author(request):
    questions = Question.objects.filter(
        author=request.user).order_by('-created_at')
    answers = Answer.objects.filter(
        author=request.user).order_by('-created_at')
    return render(request, 'questions/list_questions_and_answers_by_author.html', {'questions': questions, 'answers': answers})
