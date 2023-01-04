from django import forms
from .models import PreferenceSnippet
class SnippetForm(forms.ModelForm):

	class Meta:
		model = PreferenceSnippet
		fields = ('ABV_value','Style_Key','Ave_Rating','Min_IBU','Max_IBU','Astringency','Body','Alcohol','Bitter','Sweet','Sour','Salty','Fruits','Hoppy','Spices','Malty','Average_IBU')

