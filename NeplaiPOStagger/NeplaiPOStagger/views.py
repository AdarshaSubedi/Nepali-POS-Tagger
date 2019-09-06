from django.shortcuts import render,redirect
import os
from tagger.forms import ParagraphForm
from .import hmmdecode


def paragraph(request):
    if request.method == 'GET':
        context = {
            'form': ParagraphForm(),
        }
        return render(request, 'home.html', context)
    else:
        text = request.POST.get('text')
        file1 = open("writefile.txt","w")
        file1.write(str(text))
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir,'hmmdecode.py')
        hmmdecode.myfunc()
        all_postag = []
        with open('hmmoutput.txt', 'r') as f:
            for line in f:
                postag.append(line)
        file1.close()
        return render(request, 'postag.html', {'postag': all_postag})

def postag(request):
    context = {
        'form': ParagraphForm(),

    }
    return render(request, 'postag.html', context)
