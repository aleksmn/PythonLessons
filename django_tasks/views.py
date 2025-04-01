from django.shortcuts import render
from .models import Employee, Team

def search_employees(request):
    # Get the search query and team filter from the request
    query = request.GET.get('q', '').strip()  # Trim whitespace
    team_filter = request.GET.get('team', '')

    # Start with all employees
    employees = Employee.objects.all()

    # Filter employees by name if a query is provided
    if query:
        employees = employees.filter(name__icontains=query)

    # Filter employees by team if a team filter is provided
    if team_filter:
        employees = employees.filter(team__id=team_filter)

    # Get all teams for the dropdown
    teams = Team.objects.all()

    # Render the template with the filtered employees and teams
    return render(request, 'employee_list.html', {
        'employees': employees,
        'teams': teams,
        'selected_team': team_filter
    })
