from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import models
from django.views import View
from django.utils.timezone import now
from datetime import date, timedelta
from core.agent.models import Agent, AgentGrade
from core.agent.forms import AgentForm
from core.grade.models import Grade
from core.pay.models import PayElement, AgentPayElement
from django.http import JsonResponse

class AgentView(View):
    template_name = "agent_list.html"
    form_template_name = "agent_form.html"
    confirm_delete_template_name = "agent_confirm_delete.html"

    def get(self, request, pk=None, action=None):
        if action == "create":
            form = AgentForm()
            return render(request, self.form_template_name, {'form': form})
        
        elif action == "update" and pk:
            agent = get_object_or_404(Agent, pk=pk)
            form = AgentForm(instance=agent)
            return render(request, self.form_template_name, {'form': form})
        
        else:
            agents = Agent.objects.prefetch_related('grades').filter(deleted=False)
            return render(request, self.template_name, {'agents': agents})

    def post(self, request, pk=None, action=None):
        if action in ["create", "update"]:
            agent = get_object_or_404(Agent, pk=pk) if pk else None
            form = AgentForm(request.POST, instance=agent)
            
            if form.is_valid():
                # Vérification de l'âge
                birth_date = form.cleaned_data.get('birth_date')
                if birth_date:
                    age = (date.today() - birth_date) // timedelta(days=365.25)
                    if age < 18 or age > 35:
                        messages.error(request, "L'agent doit avoir entre 18 et 35 ans.")
                        return render(request, self.form_template_name, {'form': form})

                # Vérification du matricule unique
                code_mat = form.cleaned_data.get('code_mat')
                if Agent.objects.filter(code_mat=code_mat).exclude(pk=pk).exists():
                    messages.error(request, "Ce matricule est déjà utilisé.")
                    return render(request, self.form_template_name, {'form': form})

                agent = form.save()

                # Gestion du grade et des dates
                grade = form.cleaned_data.get('grade')
                start_at = form.cleaned_data.get('start')
                end_at = form.cleaned_data.get('end')

                if grade:
                    if start_at and self.check_date_conflict(agent, start_at, end_at):
                        messages.error(request, "Un chevauchement des dates est détecté pour le grade de cet agent.")
                        return render(request, self.form_template_name, {'form': form})

                    # Vérifier s'il existe déjà un AgentGrade actif pour cet agent
                    agent_grade = AgentGrade.objects.filter(agent=agent, end_at__isnull=True).first()

                    if agent_grade:
                        # Mise à jour du grade existant
                        agent_grade.grade = grade
                        agent_grade.start_at = start_at
                        agent_grade.end_at = end_at
                        agent_grade.save()
                    else:
                        # Création d'un nouveau grade
                        AgentGrade.objects.create(agent=agent, grade=grade, start_at=start_at, end_at=end_at)

                    # Gestion du salaire de base
                    self.create_or_update_salary(agent, grade)

                messages.success(request, "Agent enregistré avec succès !")
                return redirect('agent_list')

            messages.error(request, "Erreur dans le formulaire. Veuillez corriger les champs.")
            return render(request, self.form_template_name, {'form': form})

        elif action == "delete" and pk:
            agent = get_object_or_404(Agent, pk=pk)
            agent.delete()
            messages.success(request, "Agent supprimé avec succès !")
            return redirect('agent_list')

    def check_date_conflict(self, agent, start, end):
        """ Vérifie si l'agent a déjà un grade dans cette période """
        if not start:
            return False  # Pas de date de début, pas de conflit à vérifier
        
        # Filtrer uniquement sur start_at si end est None
        filters = models.Q(start_at__lte=start, end_at__gte=start)
        
        if end:  # Vérifier la date de fin uniquement si elle est définie
            filters |= (
                models.Q(start_at__lte=end, end_at__gte=end) |
                models.Q(start_at__gte=start, end_at__lte=end)
            )
        
        return AgentGrade.objects.filter(agent=agent).filter(filters).exists()

    def create_or_update_salary(self, agent, grade):
        """ Crée ou met à jour le salaire de base pour l'agent """
        sb_element = PayElement.objects.filter(code="SB").first()
        if sb_element:
            base_salary = int((grade.index * 3097) / 12)
            AgentPayElement.objects.update_or_create(
                agent=agent,
                element=sb_element,
                defaults={"amount": base_salary, "start_at": date.today(), "end_at": None}
            )

def get_grade_info(request):
    grade_id = request.GET.get("grade_id")
    if grade_id:
        grade = Grade.objects.filter(id=grade_id).first()
        if grade:
            index = grade.index
            base_salary = int((index * 3097) / 12)
            return JsonResponse({"index": index, "base_salary": base_salary})
    return JsonResponse({"error": "Grade not found"}, status=400)

