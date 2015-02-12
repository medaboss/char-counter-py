
from django.shortcuts import render

import string
import re

def index(request):
        return render(request, 'index.html')

def result(request):
        passed_parameter = request.POST['content']

        alphabets_upper = list(string.ascii_uppercase)
        alphabets_lower = list(string.ascii_lowercase)
        alphabets = alphabets_upper + alphabets_lower
        character_count = []
        for character in alphabets:
            output = len(re.findall(character, passed_parameter))
            if output == 0:
                pass
            else:
                character_count.append([character, output])
        context = {
            'output': character_count
        }
        return render(request, 'result.html', context)



