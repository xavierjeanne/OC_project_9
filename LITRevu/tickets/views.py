from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, TicketForm, UserFollowsForm
from django.db import models
from django.db.models import Value
from django.db.models.functions import Now
from .models import Ticket, Review, UserFollows


@login_required
def home(request):
    user = request.user
    followed_users = UserFollows.objects.filter(follower=user).values_list('followed', flat=True)

    tickets = Ticket.objects.filter(
        models.Q(author__in=followed_users) | models.Q(author=user)
    ).annotate(content_type=Value('TICKET', output_field=models.CharField()))

    reviews = Review.objects.filter(
        models.Q(author__in=followed_users) |
        models.Q(author=user) |
        models.Q(ticket__author=user)
    ).annotate(content_type=Value('REVIEW', output_field=models.CharField()))

    posts = sorted(
        list(tickets) + list(reviews),
        key=lambda post: post.created_at,
        reverse=True
    )
    return render(request, "tickets/home.html", {"posts": posts})


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})


@login_required
def create_review_for_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'tickets/create_review_for_ticket.html', {
        'ticket': ticket,
        'form': form
    })


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, author=request.user)

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)
    
    return render(request, 'tickets/ticket_form.html', {'form': form, 'ticket': ticket})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, author=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    return render(request,
                  'tickets/ticket_confirm_delete.html',
                  {'ticket': ticket})


@login_required
def create_ticket_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    return render(request, 'tickets/create_ticket_review.html', {
        'ticket_form': ticket_form,
        'review_form': review_form
    })


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'tickets/review_form.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('home')
    return render(request, 'tickets/review_confirm_delete.html', {'review': review})


@login_required
def follow_user(request):
    message = ''
    if request.method == 'POST':
        form = UserFollowsForm(request.POST)
        if form.is_valid():
            user_to_follow = form.cleaned_data["followed"]
            if user_to_follow == request.user:
                message = "Vous ne pouvez pas vous suivre vous-même."
            elif UserFollows.objects.filter(follower=request.user, followed=user_to_follow).exists():
                message = "Vous suivez déjà cet utilisateur."
            else:
                UserFollows.objects.create(follower=request.user, followed=user_to_follow)
                return redirect("follows")
    else:
        form = UserFollowsForm()
        
    following = UserFollows.objects.filter(follower=request.user)
    followers = UserFollows.objects.filter(followed=request.user)

    return render(request, "tickets/follows_view.html", {
        "form": form,
        "following": following,
        "followers": followers,
        "message": message
    })
    
    
@login_required
def unfollow_view(request, followed_id):
    relation = UserFollows.objects.filter(follower=request.user, followed__id=followed_id).first()
    if request.method == "POST" and relation:
        relation.delete()
    return redirect("follows")
