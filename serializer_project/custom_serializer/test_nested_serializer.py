from rest_framework.views import APIView
from .user_serializer import CommentSerializer
from utils.loggers import setup_logger

log = setup_logger(__name__)

class NestedSerializerView(APIView):

    def post(self, request, format=None):

        serializer = CommentSerializer(data={'user': {'email': 'iamtest@gmail.com', 'username': 'admin'}, 'content': 'testing data'})
        serializer.is_valid()
        log.info(serializer.errors)

