from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
import json


# Create your views here.
class PlayView(View):
    def get(self, request):
        # Stuff to do in GET request
        context = {
            'categories': [
                {'name': 'animal 1', 'questions': [{'points': 100, 'question': 'Q1-animal 1'},{'points': 200, 'question': 'Q2-animal 1'},{'points': 300, 'question': 'Q3-animal 1'}]},
                {'name': 'animal 2', 'questions': [{'points': 100, 'question': 'Q1-animal 2'},{'points': 200, 'question': 'Q2-animal 2'},{'points': 300, 'question': 'Q3-animal 2'}]},
                {'name': 'animal 3', 'questions': [{'points': 100, 'question': 'Q1-animal 3'},{'points': 200, 'question': 'Q2-animal 3'},{'points': 300, 'question': 'Q3-animal 3'}]},
                {'name': 'animal 4', 'questions': [{'points': 100, 'question': 'Q1-animal 4'},{'points': 200, 'question': 'Q2-animal 4'},{'points': 300, 'question': 'Q3-animal 4'}]},
                {'name': 'animal 5', 'questions': [{'points': 100, 'question': 'Q1-animal 5'},{'points': 200, 'question': 'Q2-animal 5'},{'points': 300, 'question': 'Q3-animal 5'}]}            
            ]
        }
        
        return render(request, 'jeopardy/play.html', context=context)

    def post(self, request):
        # Stuff to do in POST request
        return "POST"

@method_decorator(csrf_exempt, name='dispatch')
class SaveView(View):
    def get(self, request):
        # Send the user back to the play page caus they should not send a get here      
        return redirect("play")

    def post(self, request):
        # Stuff to do in POST request
        data = request.POST
        collums = int(data['categories'])
        rows = int(data['rows'])
        
        # For all of the quesitons and points, make a 2d array and store all of the info in them on a per lign basis (just reading throught the list given in)
        # Then write them all in
        questions = [[]]
        questions = [[x for x in range(rows)] for y in range(collums)]
        # print(questions)
        for i in range(rows):
            for x in range(collums):
                questions[x][i]= {'points': data[str(i) + '_' + str(x) + '_value'], 'question':data[str(i) + '_' + str(x) + '_question']}

        # print(questions)

        # Link the catgories and the questions
        board = []
        for i in range(collums):
            board.append({"name":data[str(i) + "_catergory_name"], "questions": questions[i]})

        # Add the final quesiton, category and the isFinal=True
        
        board.append({"name":data["final_category"], "question":data["final_question"], "isFinal":True})

        # print(board)
        
        return render(request, 'jeopardy/save.html', context={'json': json.dumps(board)})


@method_decorator(csrf_exempt, name='dispatch')
class BuildView(View):
    def get(self, request):
        # Stuff to do in GET request
        return render(request, 'jeopardy/build.html')

    def post(self, request):
        # Make the load feature
        return render(request, 'jeopardy/build.html')


