from django import forms

class ApprovalForm(forms.Form):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not_Graduated', 'Not_Graduated')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )

    firstname = forms.CharField(max_length = 15, widget=forms.TextInput(attrs={'placeholder':'Enter Firstname'}))
    lastname = forms.CharField(max_length = 15, widget=forms.TextInput(attrs={'placeholder':'Enter Lastname'}))
    Dependents = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Number of Dependents'}))
    ApplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Applicant Monthly Income'}))
    CoapplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter CoApplicant Monthly Income'}))
    LoanAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Requested Loan Amount'}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Loan Term in Months'}))
    Credit_History = forms.ChoiceField(choices=[('0',0), ('1',1), ('2',2),('3',3)])
    Gender = forms.ChoiceField(choices = GENDER_CHOICES)
    Married = forms.ChoiceField(choices = MARRIED_CHOICES)
    Education = forms.ChoiceField(choices = GRADUATED_CHOICES)
    Self_Employed = forms.ChoiceField(choices = SELFEMPLOYED_CHOICES)
    Property_Area = forms.ChoiceField(choices = PROPERTY_CHOICES)