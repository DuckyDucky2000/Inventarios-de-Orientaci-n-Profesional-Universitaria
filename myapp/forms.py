from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200)
    description = forms.CharField(label="Descripcion", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre de Proyecto:", max_length=200)

class FormTest(forms.Form):
    CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),        
    ]
    num1 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    num2 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    num3 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    #total = num1 + num2 + num3
