from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .forms import SubmitForm
from .models import Attempt

from PIL import Image, ImageDraw, ImageFont


def home_view(request):  # *args, **kwargs
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            num_results = Attempt.objects.filter(student_id = student_id).count()
            attempts = 1
            # process the data in form.cleaned_data as requir
            if num_results == 0:
                submitform = Attempt(student_id=student_id)
                submitform.save()
                attempts = 0
            form = SubmitForm()
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            result = get_object_or_404(Attempt, student_id=student_id)
            
            ####
            #Create an Image Object from an Image
            im = Image.open('static/'+str(result.random_id)+'.jpg')
            width, height = im.size

            draw = ImageDraw.Draw(im)
            text = str(result.id)

            font = ImageFont.truetype('arial.ttf', 36)
            textwidth, textheight = draw.textsize(text, font)

            # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height /2

            # draw watermark in the bottom right corner
            draw.text((x, y), text, (128, 128, 128), font=font)

            #Save watermarked image
            im.save('static/watermark/'+ str(result.id) +'.jpg')
            ####
            context = {'result': result,'attempts': attempts,'form': form}
            return render(request, 'result.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmitForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def result_view(request):
    return render(request, 'result.html')