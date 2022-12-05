from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import ContactForm,PostForm
from django.views import View
from  django.views.generic import FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib import messages
from django.db.models import Q

def search(request):
    query=request.POST.get('search','')
    if query:
        queryset = (Q(title__icontains=query)) | (
            Q(details__icontains=query)) | (Q(medium__icontains=query)) |(Q(category__icontains=query)) | (Q(subject__name__icontains=query)) | (Q(class_in__name__icontains=query))
        results=Post.objects.filter(queryset).distinct()
    else:
        results=[]
    context={
        'results':results
    }
    return render (request,'tuition/search.html',context)

def filter(request):
    if request.method=='POST':
        subject=request.POST['subject']
        class_in = request.POST['class_in']
        salary_from = request.POST['salary_from']
        salary_to = request.POST['salary_to']
        available = request.POST['available']
        if subject or class_in:
            queryset =(Q(subject__name__icontains=subject)) & (Q(class_in__name__icontains=class_in))
            results = Post.objects.filter(queryset).distinct()
            if available:
                results=results.filter(available=True)
            if salary_from:
                results = results.filter(salary__gte=salary_from)
            if salary_to:
                results = results.filter(salary__lte=salary_to)
        else:
            results = []
        context = {
            'results': results
        }
        return render(request, 'tuition/search.html', context)

def home(request):
    return render(request,'home.html')


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    # success_url='/'
    def form_valid(self,form):
        form.save()
        messages.success(self.request,'From successfully submitted')
        return super().form_valid(form)

    def form_invalid(self,form):

        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('HomeView')
# class ContactView(View):
#     form_class =ContactForm
#     template_name='contact.html'
#     def get(self,request,*args,**kwargs):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})
    
#     def post(self, request, *args, **kwargs):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Success")
#         return render(request, self.template_name, {'form': form})



def contact(request):
    initials={
        'name':'My name is ',
        'phone':'+8801',
        'content':'My problem is '
    }
    if request.method=='POST':
        form=ContactForm(request.POST,initial=initials)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']
            obj=Contact(name=name,phone=phone,content=content)
            obj.save()
    else:
        form = ContactForm(initial=initials)
        
    return render(request,'contact.html',{'form':form})

class PostListView(ListView):
    # queryset=Post.objects.filter(user=1)\
    model=Post
    template_name='tuition/postList.html'
    context_object_name='posts'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['posts']=context.get('object_list')
        context['subjects']=Subject.objects.all()
        context['classes'] = Class_in.objects.all()
        return context

class PostDetailView(DetailView):
    model=Post
    template_name='tuition/postDetail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post'] = context.get('object')
        context['msg'] = 'This is post Detail'
        return context

    
def postView(request):
    post=Post.objects.all()
    return render(request,'tuition/postView.html',{'post':post})


def subjectView(request):
    sub = Subject.objects.get(name='Bangla')
    post=sub.subject_set .all()
    return render(request, 'tuition/subjectView.html', {'sub': sub,'post':post})

class PostCreateView(CreateView):
    model=Post
    form_class= PostForm
    template_name = 'tuition/postCreate.html'
    # success_url='/'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('tuition:subject')


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postCreate.html'
    # success_url='/'

    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('tuition:postdetail', kwargs={'pk': id})
    
class PostDeleteView(DeleteView):
    model=Post
    template_name='tuition/delete.html'
    success_url=reverse_lazy('tuition:postlist')
    
    
# def postCreate(request):
#     if request.method=='POST':
#         form=PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.user=request.user
#             obj.save()
#             sub=form.cleaned_data['subject']
#             for i in sub:
#                 obj.subject.add(i)
#                 obj.save()
#             class_in = form.cleaned_data['class_in']
#             for i in class_in:
#                 obj.class_in.add(i)
#                 obj.save()
#             return HttpResponse('Success')
#     else:
#         form=PostForm()
#         return render(request,'tuition/postCreate.html',{'form':form})