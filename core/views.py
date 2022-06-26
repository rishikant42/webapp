import uuid

from rest_framework.views import APIView
from rest_framework.response import Response


users = []

newsletter = [
    {'id': 1, 'category_id': 1,  'title': 'title1', 'user_id': 1, 'price': 111},
    {'id': 2, 'category_id': 1,  'title': 'title2', 'user_id': 1, 'price': 111},
    {'id': 3, 'category_id': 2,  'title': 'title3', 'user_id': 2, 'price': 111},
]

category = [
    {'id': 1, 'name': 'c1'},
    {'id': 2, 'name': 'c2'},
]

# user: {'id': <id>, 'name': <name>, 'email': <email>}


class UserView(APIView):
    def post(self, request, *args, **kwags):
        name = request.data.get('name')
        email = request.data.get('email')
        if not name or not email:
            return Response({'error': 'missing required fields'}, status=400)

        uid = str(uuid.uuid4())

        users.append(
            {'id': uid, 'name': name, 'email': email},
        )
        print(users)
        return Response({'user_id': uid}, status=201)


class NewsLetterView(APIView):
    def get(self, request, *args, **kwags):
        categories = request.query_params.getlist('categories')
        category_map = {x.get('name'): x.get('id') for x in category}
        resp = []
        for c in categories:
            temp = [x for x in newsletter if x.get('category_id') == category_map.get(c)]
            d = {c: temp}
            resp.append(d)

        result = {'newsletter': resp}

        return Response(result)
