from django import forms
from .models import Contact,Post
# class ContactFrom(forms.Form):
#     name=forms.CharField(max_length=100,label="Your Name",widget=form.TextInput(attrs={'class':form-control}))
#     phone = forms.CharField(max_length=150,label="Your Phone")
#     content = forms.CharField(max_length=150,label="Your Details")

# MOdel Forms 

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label='My name'
        self.fields['name'].initial='My name'
        self.fields['phone'].initial = '+880'
        self.fields['content'].initial = 'My problem is'
    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w=value.split(' ')
        if len(num_of_w) > 3:
            self.add_error('name','Name can have maximum of 3 words')
        else:
            return value
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
        #     'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Phone'}),
        #     'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Say something','rows':'5'}),
        # }
        # labels={
        #     'name':'Your name',
        #     'phone':'Phone number',
        #     'content':'Your words'
        # }
        # help_texts={
        #     'name': 'Your name',
        #     'phone': 'Phone number',
        #     'content': 'Your words'
        # }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ['user', 'id', 'created_at','slug']
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={'multiple':True}),
            'subject': forms.CheckboxSelectMultiple(attrs={'multiple': True})
        }