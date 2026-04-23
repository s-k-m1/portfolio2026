from rest_framework.views import APIView
from rest_framework.response import Response
from portfolio.models.about_models import AboutInfo, Skill, Project
from portfolio.Serializer.about_serializers import AboutInfoSerializer, SkillSerializer, ProjectSerializer

class AboutDataView(APIView):
    def get(self, request):
        about = AboutInfo.objects.first()
        skills = Skill.objects.all()
        projects = Project.objects.all().order_by('order')

        # Pass context={'request': request} to ensure full URLs for CV/Images
        about_data = AboutInfoSerializer(about, context={'request': request}).data if about else {}
        
        return Response({
            "about": about_data,
            "skills": {
                "frontend": SkillSerializer(skills.filter(category='frontend'), many=True).data,
                "backend": SkillSerializer(skills.filter(category='backend'), many=True).data,
            },
            "projects": ProjectSerializer(projects, many=True).data
        })