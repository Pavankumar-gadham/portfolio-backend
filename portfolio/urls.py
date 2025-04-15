from django.urls import path, include
from .views import ExperienceViewSet, ProjectViewSet, CertificationViewSet, EducationViewSet, SkillViewSet, ContactViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact', ContactViewSet)



urlpatterns = [
    path("", include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
