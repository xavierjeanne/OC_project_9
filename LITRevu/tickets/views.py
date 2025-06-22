from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from .forms import TicketForm


@login_required
def home(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    return render(request, 'tickets/home.html', { 
        'tickets': tickets,
        'reviews': reviews,
    })


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('home')  # à ajuster
    else:
        form = TicketForm()
    return render(request,
                  'tickets/ticket_form.html',
                  {'form': form})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, author=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)
    return render(request,
                  'tickets/ticket_form.html',
                  {'form': form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, author=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    return render(request,
                  'tickets/ticket_confirm_delete.html',
                  {'ticket': ticket})
