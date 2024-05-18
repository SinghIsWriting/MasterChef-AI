from django import forms

class RecipeForm1(forms.Form):
    recipe_msg = forms.CharField(max_length=255,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'What are you cooking today?'}
                                    ))
class RecipeForm2(forms.Form):
    recipe_msg = forms.CharField(max_length=255,
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'What ingredients do you have in your kitchen? (e.g., flour, eggs, milk)'}
                                    ))
