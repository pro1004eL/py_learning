import pytest

from lesson_16.homework_16_1 import TeamLead

def test_teamlead_department_and_programming_language():
    team_lead = TeamLead(name='Denis', salary=195000, department='AQA', programming_language='Python', team_size=20)

    assert team_lead.department == "AQA"
    assert team_lead.programming_language == "Python"

def test_teamlead_name_and_salary():
    team_lead = TeamLead("Anton", 120000, "Development", "Python", 3)

    assert team_lead.name == "Anton"
    assert team_lead.salary == 120000


def test_teamlead_team_size():
    team_lead = TeamLead("Daisy", 100000, "Support", "Ruby", 6)
    assert team_lead.team_size == 6

