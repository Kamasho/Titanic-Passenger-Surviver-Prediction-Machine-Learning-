from django.shortcuts import render
import pickle

# Create your views here.


def home(request):
    return render(request, 'home.html')


def getPredictions(pclass, sex, age, sibsp, parch, fare):
    model = pickle.load(open('our_model.sav', 'rb'))
    scaled = pickle.load(open('scaler.sav', 'rb'))
    scaled.clip = False

    prediction = model.predict(scaled.transform([
        [pclass, sex, age, sibsp, parch, fare]
    ]))

    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'


def result(request):

    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibps = int(request.GET['sibps'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])

    result = getPredictions(pclass, sex, age, sibps,
                            parch, fare)
    return render(request, 'result.html', {'result': result})
