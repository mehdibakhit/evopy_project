from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(label='نام', max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='ایمیل',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="تلفن همراه",max_length=11,widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label="پیام", max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))


class MessageForm(forms.Form):
    name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    last_name = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    phone_number = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))