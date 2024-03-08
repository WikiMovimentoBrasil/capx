from django.http import HttpResponseServerError
from django.shortcuts import render
from opensearchpy.exceptions import ConnectionError
from users.documents import ProfileDocument
from skills.documents import SkillDocument


def search(request):
    query = request.GET.get('query', '')
    try:
        users_results = ProfileDocument.search().query({
            "fuzzy": {
                "user__username": {
                    "value": query,
                    "fuzziness": 2,
                    "prefix_length": 1
                }
            }}).execute()
        skills_results = SkillDocument.search().query({
            "fuzzy": {
                "skill_name": {
                    "value": query,
                    "fuzziness": 2,
                    "prefix_length": 1
                }
            }}).execute()
        return render(request, 'search.html', {
            'users_results': users_results,
            'skills_results': skills_results,
            'query': query
        })
    except ConnectionError as e:
        error_message = f"Error connecting to Elasticsearch: {str(e)}"
        return render(request, 'search.html', {
            'error_message': error_message,
            'query': query
        })
