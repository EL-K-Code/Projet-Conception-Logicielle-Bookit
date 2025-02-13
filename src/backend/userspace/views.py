# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions
# from .models import Event
# from .serializers import EventSerializer
# from .permissions import IsEventAdmin

# class CreateEventView(APIView):
#     """
#     Vue pour créer un événement. Seuls les utilisateurs du groupe 'event_admin'
#     peuvent accéder à cette vue.
#     """
#     permission_classes = [IsEventAdmin]

#     def post(self, request, *args, **kwargs):
#         # Crée un nouvel événement à partir des données envoyées
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
