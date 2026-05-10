from rest_framework import serializers

class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    html_url = serializers.CharField(max_length=256)
    clone_url = serializers.CharField(max_length=256)
    languages = serializers.SerializerMethodField()
    stargazers_count= serializers.IntegerField()
    clone_count = serializers.SerializerMethodField()
    visitor_count= serializers.SerializerMethodField()


    def get_languages(self, obj):
        return obj.get_languages()

    def get_clone_count(self, obj):
        print(obj.name)
        traffic = obj.get_clones_traffic()
        return traffic.count

    def get_visitor_count(self, obj):
        print(obj.name)
        traffic = obj.get_views_traffic()
        return traffic.uniques
