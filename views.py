





import json
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView, View





class consecutivenumber(CreateView):
    def get(self, request):
        return render(request,'kmd/consecutivenumber.html')

    def post(self,request):
        numbers = str(request.POST['numbers'])
        print('number',numbers)
        lst = json.loads(numbers)
        print ('List',lst)

        print(groupconsecnumbers(lst))

        return redirect('consecutivenumbers')

def groupconsecnumbers(nlist):
    pnumber = min(nlist) if nlist else None
    pagelist = list()

    for number in sorted(nlist):
        if number != pnumber+1:
            pagelist.append([number])
        elif len(pagelist[-1]) > 1:
            pagelist[-1][-1] = number
        else:
            pagelist[-1].append(number)
        pnumber = number

    return ','.join(['-'.join(map(str,page)) for page in pagelist])
