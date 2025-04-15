from .serializers import ExperienceSerializer, ProjectSerializer, CertificationSerializer, EducationSerializer, SkillSerializer, ContactMessageSerializer
from .models import Experience, Project, Certification, Education, Skills, ContactMessage
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import request

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
