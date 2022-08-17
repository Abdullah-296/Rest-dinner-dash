from django import forms
from maindisplay.models import Item, Restaurant, Category
import os
import re

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg', '.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Only accept images.')


class AddItemform(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                             validators=[validate_file_extension])
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.filter(id=1), widget=forms.CheckboxSelectMultiple(attrs={'id': 'restaurantcategory'}))

    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'restaurant', 'category', 'available', 'images')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Zinger Burger', 'onchange': "myFunction(this.value);"}),
            'description': forms.Textarea(
                attrs={'cols': 2, 'rows': 4, 'class': 'form-control', 'placeholder': ' crispy'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'min': "1", 'type': 'number'}),
            'restaurant': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Restaurant',
                                              'onchange': "Changerestaurantcategory(this.value);"}),
            # 'category': forms.CheckboxSelectMultiple(attrs={'id': 'restaurantcategory'})
        }

    def __init__(self, *args, **kwargs):
        super(AddItemform, self).__init__(*args, **kwargs)
        self.fields['images'].required = False
        self.fields['category'].empty_label = None

    def clean_title(self):
        title = self.cleaned_data.get("title")
        match = re.fullmatch('[A-Za-z0-9_.]{2,32}( [A-Za-z]{2,32})?', title)
        if match is None:
            raise forms.ValidationError("This field only accept character , Numbers, _ and . ")

        return title

    # def clean_category(self):
    #     categoryUser = self.cleaned_data.get("category")
    #     restaurant = self.cleaned_data.get("restaurant")
    #
    #     restaurantinstance = Restaurant.objects.get(Name=restaurant)
    #     restaurantcategory = restaurantinstance.category_set.all()
    #
    #     if len(restaurantcategory & categoryUser) != len(categoryUser):
    #         raise forms.ValidationError(
    #             "Restaurant does have category which you select, kindly select category which specific restaurant have")
    #
    #     return categoryUser


class AddRestaurantform(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('Name', 'Address', 'Owner', 'description', 'photo')
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KFC'}),
            'Address': forms.Textarea(
                attrs={'cols': 2, 'rows': 3, 'class': 'form-control', 'placeholder': ' I-10 Islamabad'}),
            'Owner': forms.Select(attrs={'class': 'form-control', 'placeholder': 'David'}),
            'description': forms.Textarea(
                attrs={'cols': 2, 'rows': 3, 'class': 'form-control', 'placeholder': 'Provide good tast food'}),
        }

    def clean_Name(self):
        Name = self.cleaned_data.get("Name")
        match = re.fullmatch('[A-Za-z0-9_.]{2,32}( [A-Za-z]{2,32})?', Name)
        if match is None:
            raise forms.ValidationError("This field only accept character , Numbers, _ and . ")

        return Name


class AddCategoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('Name', 'RestaurantCategory')
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KFC'}),
        }

    def clean_Name(self):
        Name = self.cleaned_data.get("Name")
        match = re.fullmatch('[A-Za-z0-9_.]{2,32}( [A-Za-z]{2,32})?', Name)
        if match is None:
            raise forms.ValidationError("This field only accept character , Numbers, _ and . ")

        return Name
