from rest_framework.response import Response
from rest_framework.views import APIView
from course import serializers, models

class LevelViews(APIView):
    serializers_classes = serializers.LevelSerializers

    def get(self, request):
        levels = models.Level.objects.all()
        serializer_elem = self.serializers_classes(levels, many=True)
        return Response(serializer_elem.data)


    # def post(self, request):
    #     element = request.data
    #     serializer_elem = self.serializers_classes(data=element)
        
    #     if serializer_elem.is_valid():
    #         serializer_elem.save()
    #         return Response(serializer_elem.data)
        
    #     return Response({"status": "faild", "message": serializer_elem.errors})
