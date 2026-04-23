from rest_framework import serializers
from portfolio.models.about_models import AboutInfo, Skill, Project

class AboutInfoSerializer(serializers.ModelSerializer):
    # We use SerializerMethodField to get the full URL for the CV file
    cv_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutInfo
        fields = ['id', 'title', 'subtitle', 'description', 'professional_summary', 'cv_file', 'cv_url']

    def get_cv_url(self, obj):
        if obj.cv_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cv_file.url)
            return obj.cv_file.url
        return None

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'percent', 'category']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'link', 'order']